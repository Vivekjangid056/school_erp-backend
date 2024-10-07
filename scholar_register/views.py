from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from accounts.models import User
from fees_module.models import PaymentSchedule
from scholar_register.models import StudentProfile
from .forms import *
from django.contrib import messages
from django.db import transaction
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def student_list(request):
    # user_institute = request.user.institute_id.first() #or
    institute = Institute.objects.get(user_id = request.user)
# for fetching the data from a table which is not directly connected with the current table but its f
# oreignkey table has a reference in the table then we user __
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return StudentProfile.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        StudentProfile.objects.none()
    students = StudentProfile.objects.filter(parent__institute = institute, branch=active_branch, session=active_session)
    context = {
        'students':students
    }
    return render(request, 'students_list.html',context=context)

@transaction.atomic
def student_register(request):

    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)
    
    parents = StudentParents.objects.filter(institute = request.user.institute_id.first())
    user_form = ParentUserCreationForm()
    parent_form = ParentProfileForm(user = user)
    profile_form = StudentProfileForm(user = user, session=request.session)
    fees_form = StudentFeesForm(user = user, session=request.session)

    context={
        'user_form': user_form,
        'parent_form': parent_form,
        'profile_form': profile_form,
        'parents': parents,
        'fees_form': fees_form,
    }

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return render(request, 'student_form.html', context=context)

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return render(request, 'student_form.html', context=context)

    if request.method == 'POST':
        parent_registered = request.POST.get('parent_registered')
        profile_form = StudentProfileForm(request.POST, request.FILES)
        fees_form = StudentFeesForm(request.POST)
        paying_amount = float(request.POST.get('paying_amount'))
        installment_frequency=request.POST.get('installment_frequency')
        initial_payment = float(request.POST.get('initial_fees_deposit'))
        due_amount = float(paying_amount) - float(initial_payment)

        if parent_registered == 'yes':
            existing_parent_id = request.POST.get('existing_parent')
            if not existing_parent_id:
                messages.error(request, "Please select an existing parent.")
                parents = StudentParents.objects.filter(institute = request.user.institute_id.first())
                context = {
                    'profile_form': profile_form,
                    'parent_form': parent_form,
                    'fees_form': fees_form,
                    'parents':parents
                }
                return render(request, 'students_form.html', context)
            try:
                parents = StudentParents.objects.get(id=existing_parent_id)
            except StudentParents.DoesNotExist:
                messages.error(request, "Selected parent not found.")
                parents = StudentParents.objects.filter(institute = request.user.institute_id.first())
                context = {
                    'profile_form': profile_form,
                    'fees_form': fees_form,
                    'parents': parents,
                }
                return render(request, 'students_form.html', context)
            
            if profile_form.is_valid() and fees_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.parent = parents
                profile.branch = active_branch
                profile.session =active_session
                profile_form.save()

                fees = fees_form.save(commit=False)
                fees.student = profile  # Set the student here
                fees.branch= active_branch
                fees.session=active_session
                fees_form.save()

                if installment_frequency == 'No Installement':
                    paid_status = True if due_amount == 0 else False

                    if paid_status:
                        # If fully paid, set the payment schedule with no due date since it's fully paid
                        due_payment_schedule_data = {
                            'institute': institute,
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': initial_payment,
                            'due_amount': due_amount,
                            'payment_date': datetime.today().date(),
                            'payment_due_date': "",  # No due date since fully paid
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)
                    else:
                        # Calculate monthly installment for remaining amount
                        installment = float(paying_amount / 12)  # Assuming paying_amount is the total amount
                        advance_amount = initial_payment
                        remaining_due_amount = 0
                        last_payment_month = 0

                        for i in range(1, 13):
                            if advance_amount >= installment:
                                # Deduct installment from advance amount
                                advance_amount -= installment
                                last_payment_month = i  # Track the month of last payment made
                            else:
                                # If advance payment is less than installment, calculate remaining due
                                remaining_due_amount = (installment * (12 - last_payment_month)) - advance_amount  # Remaining installments
                                break
                        
                        # Create payment schedule for partially paid situation
                        due_payment_schedule_data = {
                            'institute': institute,
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': initial_payment if initial_payment else 0,
                            'due_amount': round(remaining_due_amount),
                            'payment_date': datetime.today().date() if initial_payment else "",  # Payment made today
                            'payment_due_date': datetime.today().date() + relativedelta(months=last_payment_month),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)


                if installment_frequency == 'Monthly':
                    # Monthly installment: 12 payments
                    installment = float(paying_amount) / 12
                    advance_amount = initial_payment

                    for i in range(1, 13):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                # Fully cover the installment
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                # Partially cover the installment
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0  # No more advance left
                                paid_status = False
                        else:
                            # No advance left, no payment made
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                elif installment_frequency == 'Quarterly':
                    # Quarterly installment: 4 payments (every 3 months)
                    installment = float(paying_amount) / 4
                    advance_amount = initial_payment

                    for i in range(1, 5):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0
                                paid_status = False
                        else:
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i*3),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                elif installment_frequency == 'Half-Yearly':
                    # Half-Yearly installment: 2 payments (every 6 months)
                    installment = float(paying_amount) / 2
                    advance_amount = initial_payment

                    for i in range(1, 3):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0
                                paid_status = False
                        else:
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i*6),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)
                messages.success(request, "Student registered successfully.")
                return redirect('students:list_of_students')
            else:
                print("Profile form errors:", profile_form.errors)
        else:
            user_form = ParentUserCreationForm(request.POST)
            parent_form = ParentProfileForm(request.POST, user=request.user)
            profile_form = StudentProfileForm(request.POST, request.FILES)
            fees_form = StudentFeesForm(request.POST)

            if user_form.is_valid() and parent_form.is_valid() and profile_form.is_valid() and fees_form.is_valid():
                user = user_form.save()
                parent = parent_form.save(commit=False)
                parent.user = user
                parent.save()

                profile = profile_form.save(commit=False)
                profile.parent = parent
                profile.branch = active_branch
                profile.session =active_session
                profile.save()

                fees = fees_form.save(commit=False)
                fees.student = profile  # Set the student here
                fees.branch = active_branch
                fees.session=active_session
                fees.save()

                if installment_frequency == 'No Installement':
                    paid_status = True if due_amount == 0 else False

                    if paid_status:
                        # If fully paid, set the payment schedule with no due date since it's fully paid
                        due_payment_schedule_data = {
                            'institute': institute,
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': initial_payment,
                            'due_amount': due_amount,
                            'payment_date': datetime.today().date(),
                            'payment_due_date': "",  # No due date since fully paid
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)
                    else:
                        # Calculate monthly installment for remaining amount
                        installment = float(paying_amount / 12)  # Assuming paying_amount is the total amount
                        advance_amount = initial_payment
                        remaining_due_amount = 0
                        last_payment_month = 0

                        for i in range(1, 13):
                            if advance_amount >= installment:
                                # Deduct installment from advance amount
                                advance_amount -= installment
                                last_payment_month = i  # Track the month of last payment made
                            else:
                                # If advance payment is less than installment, calculate remaining due
                                remaining_due_amount = (installment * (12 - last_payment_month)) - advance_amount  # Remaining installments
                                break
                        print(remaining_due_amount)
                        # Create payment schedule for partially paid situation
                        due_payment_schedule_data = {
                            'institute': institute,
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': initial_payment if initial_payment else 0,
                            'due_amount': round(remaining_due_amount),
                            'payment_date': datetime.today().date() if initial_payment else 0,  # Payment made today
                            'payment_due_date': datetime.today().date() + relativedelta(months=last_payment_month),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                if installment_frequency == 'Monthly':
                    # Monthly installment: 12 payments
                    installment = float(initial_payment) / 12
                    advance_amount = initial_payment

                    for i in range(1, 13):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                # Fully cover the installment
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                # Partially cover the installment
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0  # No more advance left
                                paid_status = False
                        else:
                            # No advance left, no payment made
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                elif installment_frequency == 'Quarterly':
                    # Quarterly installment: 4 payments (every 3 months)
                    installment = float(initial_payment) / 4
                    advance_amount = initial_payment

                    for i in range(1, 5):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0
                                paid_status = False
                        else:
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i*3),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                elif installment_frequency == 'Half-Yearly':
                    # Half-Yearly installment: 2 payments (every 6 months)
                    installment = float(initial_payment) / 2
                    advance_amount = initial_payment

                    for i in range(1, 3):
                        if advance_amount > 0:
                            if advance_amount >= installment:
                                amount_paid = installment
                                advance_amount -= installment
                                due_amount_adjusted = 0
                                paid_status = True
                            else:
                                amount_paid = advance_amount
                                due_amount_adjusted = installment - advance_amount
                                advance_amount = 0
                                paid_status = False
                        else:
                            amount_paid = None
                            due_amount_adjusted = installment
                            paid_status = False

                        due_payment_schedule_data = {
                            'institute': institute, 
                            'session': active_session,
                            'branch': active_branch,
                            'student_fee_payment': fees,
                            'amount_paid': amount_paid if amount_paid else 0,
                            'due_amount': due_amount_adjusted,
                            'payment_date': datetime.today().date() if paid_status else "",
                            'payment_due_date': datetime.today().date() + relativedelta(months=i*6),
                            'paid': paid_status
                        }
                        PaymentSchedule.objects.create(**due_payment_schedule_data)

                messages.success(request, "Student and parent registered successfully.")
                return redirect('students:list_of_students')
            else:
                print("User form errors:", user_form.errors)
                print("Parent form errors:", parent_form.errors)
                print("Profile form errors:", profile_form.errors)
                print("fees form errors:", fees_form.errors)
        
                messages.error(request, "There were errors in the form. Please correct them and try again.")
        
                # Prepare context for invalid POST
        parents = StudentParents.objects.filter(institute = request.user.institute_id.first())
        context = {
            'user_form': user_form if parent_registered == 'no' else ParentUserCreationForm(),
            'parent_form': parent_form if parent_registered == 'no' else ParentProfileForm(),
            'profile_form': profile_form,
            'parents': parents,
            'fees_form': fees_form,
        }
        return render(request, 'students_form.html', context)
    else:
        # GET request
        user = request.user
        user_form = ParentUserCreationForm()
        parent_form = ParentProfileForm(user = user)
        profile_form = StudentProfileForm(user = user)
        fees_form = StudentFeesForm(user = user)

    # Prepare context for GET
    parents = StudentParents.objects.filter(institute = request.user.institute_id.first())
    context = {
        'user_form': user_form,
        'parent_form': parent_form,
        'profile_form': profile_form,
        'parents': parents,
        'fees_form': fees_form,
    }
    
    return render(request, 'students_form.html', context)


def student_update(request, pk):
    student_profile = get_object_or_404(StudentProfile, pk=pk)
    
    if request.method == 'POST':
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=student_profile, user=request.user, session=request.session)
        print("jhgDHFBASMFASDFSGDHJF::::::::::::::::::::")
        
        if profile_form.is_valid():
            print("form is valid :::::::::::::::::::::::::::;")
            try:
                profile_form.save()
                messages.success(request, "Student profile updated successfully.")
                return redirect('students:list_of_students')
            except Exception as e:
                messages.error(request, f"Error saving form: {e}")
        else:
            print(messages.error(request, "Please correct the errors in the form.", profile_form.errors))
            print(profile_form.errors)
    
    else:
        profile_form = StudentProfileForm(instance=student_profile, user=request.user)

    return render(request, 'students_update.html', {
        'profile_form': profile_form
    })

def student_delete(request, pk):
    student_profile = get_object_or_404(StudentProfile, pk=pk)
    parent = student_profile.parent
    user = student_profile.parent.user
    student_profile.delete()
    parent.delete()
    user.delete()
    return redirect('students:list_of_students')


def student_suggestion_complaint(request, student_id, institute_id, branch_id, session_id):
    if request.method == 'POST':
        student = get_object_or_404(StudentProfile, id=student_id)
        institute = get_object_or_404(Institute, registration_number=institute_id)
        branch = get_object_or_404(InstituteBranch, id=branch_id)
        session = get_object_or_404(AcademicSession, id=session_id)

        request_type = request.POST.get('request_type')
        suggestion_type = request.POST.get('suggestion_type')
        query = request.POST.get('query')

        if request_type and suggestion_type and query:
            suggestion_complaint = StudentComplaintsOrSuggestions(
                student=student,
                institute=institute,
                branch=branch,
                session=session,
                request_type=request_type,
                suggestion_type=suggestion_type,
                query=query
            )
            suggestion_complaint.save()
            messages.success(request, 'Suggestion or complaint submitted successfully')
            return render(request, 'create_complaint.html')  # Assuming you have a complaint list page
        else:
            messages.error(request, 'Please fill all the required fields')

    return render(request, 'create_complaint.html')



def update_suggestion_complaint(request, student_id, complaint_id):
    complaint = get_object_or_404(StudentComplaintsOrSuggestions, id=complaint_id, student_id=student_id)

    if request.method == 'POST':
        complaint.request_type = request.POST.get('request_type', complaint.request_type)
        complaint.suggestion_type = request.POST.get('suggestion_type', complaint.suggestion_type)
        complaint.query = request.POST.get('query', complaint.query)

        complaint.save()
        messages.success(request, 'Complaint or suggestion updated successfully')
        return render(request, 'create_complaint.html')

    return render(request, 'update_complaint.html', {'complaint': complaint})


def delete_suggestion_complaint(request, student_id, complaint_id):
    complaint = get_object_or_404(StudentComplaintsOrSuggestions, id=complaint_id, student_id=student_id)
    
    if request.method == 'POST':
        complaint.delete()
        messages.success(request, 'Complaint or suggestion deleted successfully')
        return render(request, 'create_complaint.html')

    return render(request, 'delete_complaint.html', {'complaint': complaint})
