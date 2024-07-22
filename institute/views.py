from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views import View
from django.views.decorators.http import require_POST

from scholar_register.models import StudentProfile
from .forms import *
from .models import *
from django.views.generic import UpdateView, CreateView, DeleteView, FormView, ListView
from .utils import send_sms


def institute_profile(request):
    user = request.user
    print(user)
    user_id = user.id
    print(user_id)
    institute = Institute.objects.filter(user_id = user_id).first()
    print(institute)
    return render(request, 'institute_profile.html', {'institute': institute, 'user':user})



# ===================================== signature CRUD Starts ===========================================
class AddSignature(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = SignatureForm
    success_url = reverse_lazy('institute:list_of_signatures')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofSignatures(ListView):
    model = LomSignature
    template_name = "list_of_masters/signature_list.html"
    context_object_name = 'signature_list'

class UpdateSignature(UpdateView):
    model = LomSignature
    form_class = SignatureForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_signatures')

    def form_valid(self, form):
        messages.success(self.request, "signature updated successfully!")
        return super().form_valid(form)

class SignatureDeleteView(DeleteView):
    model = LomSignature
    success_url = reverse_lazy('institute:list_of_signatures')

# ====================================== caste CRUD system ==============================================
class AddCaste(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = CasteForm
    success_url = reverse_lazy('institute:list_of_caste')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofCaste(ListView):
    model = Caste
    template_name = "list_of_masters/caste_list.html"
    context_object_name = 'caste_list'

class UpdateCaste(UpdateView):
    model = Caste
    form_class = CasteForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_caste')

    def form_valid(self, form):
        messages.success(self.request, "Caste updated successfully!")
        return super().form_valid(form)

class CasteDeleteView(DeleteView):
    model = Caste
    success_url = reverse_lazy('institute:list_of_caste')

# ==================================== category crud ====================================================
class AddCategory(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy('institute:list_of_category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofCategory(ListView):
    model = Category
    template_name = "list_of_masters/category_list.html"
    context_object_name = 'category_list'

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_category')

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully!")
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('institute:list_of_category')
    
# ========================================= House CRUD ==================================================
class AddHouse(FormView):
    template_name = "list_of_masters/lom_house_add.html"
    form_class = HouseForm
    success_url = reverse_lazy('institute:list_of_house')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofHouse(ListView):
    model = House
    template_name = "list_of_masters/house_list.html"
    context_object_name = 'house_list'

class UpdateHouse(UpdateView):
    model = House
    form_class = HouseForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_house')

    def form_valid(self, form):
        messages.success(self.request, "House updated successfully!")
        return super().form_valid(form)

class HouseDeleteView(DeleteView):
    model = House
    success_url = reverse_lazy('institute:list_of_house')

    
# ========================================= medium CRUD =================================================
class AddMedium(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = MediumForm
    success_url = reverse_lazy('institute:list_of_medium')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofMedium(ListView):
    model = Medium
    template_name = "list_of_masters/medium_list.html"
    context_object_name = 'medium_list'

class UpdateMedium(UpdateView):
    model = Medium
    form_class = MediumForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_medium')

    def form_valid(self, form):
        messages.success(self.request, "Medium updated successfully!")
        return super().form_valid(form)

class MediumDeleteView(DeleteView):
    model = Medium
    success_url = reverse_lazy('institute:list_of_medium')

# =========================================== religion CRUD =============================================
class AddReligion(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = ReligionForm
    success_url = reverse_lazy('institute:list_of_religion')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofReligion(ListView):
    model = Religion
    template_name = "list_of_masters/religion_list.html"
    context_object_name = 'religion_list'

class UpdateReligion(UpdateView):
    model = Religion
    form_class = ReligionForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_religion')

    def form_valid(self, form):
        messages.success(self.request, "Religion updated successfully!")
        return super().form_valid(form)

class RelligionDeleteView(DeleteView):
    model = Religion
    success_url = reverse_lazy('institute:list_of_religion')

# ======================================== reference CRUD ===============================================
class AddReference(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = ReferenceForm
    success_url = reverse_lazy('institute:list_of_reference')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofReference(ListView):
    model = Reference
    template_name = "list_of_masters/reference_list.html"
    context_object_name = 'reference_list'

class UpdateReference(UpdateView):
    model = Reference
    form_class = ReferenceForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_reference')

    def form_valid(self, form):
        messages.success(self.request, "Reference updated successfully!")
        return super().form_valid(form)

class ReferenceDeleteView(DeleteView):
    model = Reference
    success_url = reverse_lazy('institute:list_of_reference')

# =========================================nationality CRUD =============================================
class AddNationality(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = NationalityForm
    success_url = reverse_lazy('institute:list_of_nationality')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofNationality(ListView):
    model = Nationality
    template_name = "list_of_masters/nationality_list.html"
    context_object_name = 'nationality_list'

class UpdateNationality(UpdateView):
    model = Nationality
    form_class = NationalityForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_nationality')

    def form_valid(self, form):
        messages.success(self.request, "Nationality updated successfully!")
        return super().form_valid(form)

class NationalityDeleteView(DeleteView):
    model = Nationality
    success_url = reverse_lazy('institute:list_of_nationality')

# ======================================== mother tongue CRUD ===========================================
class AddMotherTongue(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = MotherTongueForm
    success_url = reverse_lazy('institute:list_of_mother_tongue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofMotherToungue(ListView):
    model = MotherToungue
    template_name = "list_of_masters/mother_tongue_list.html"
    context_object_name = 'mother_tongue_list'

class UpdateMotherTongue(UpdateView):
    model = MotherToungue
    form_class = MotherTongueForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_mother_tongue')

    def form_valid(self, form):
        messages.success(self.request, "Mother Tongue updated successfully!")
        return super().form_valid(form)

class MotherTongueDeleteView(DeleteView):
    model = MotherToungue
    success_url = reverse_lazy('institute:list_of_mother_tongue')

# ========================================= family relation CRUD ========================================
class AddFamilyRelation(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = FamilyRelationForm
    success_url = reverse_lazy('institute:list_of_family_relation')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofFamilyRelation(ListView):
    model = FamiliRelation
    template_name = "list_of_masters/family_relation_list.html"
    context_object_name = 'family_relation_list'

class UpdateFamilyRelation(UpdateView):
    model = FamiliRelation
    form_class = FamilyRelationForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_family_relation')

    def form_valid(self, form):
        messages.success(self.request, "Family Relation updated successfully!")
        return super().form_valid(form)

class FamilyRelationDeleteView(DeleteView):
    model = FamiliRelation
    success_url = reverse_lazy('institute:list_of_family_relation')

# ======================================= enquiryType CRUD ==============================================
class AddEnquiryType(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = EnquiryTypeForm
    success_url = reverse_lazy('institute:list_of_enquiry_type')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofEnquiryType(ListView):
    model = EnquiryType
    template_name = "list_of_masters/enquiry_type_list.html"
    context_object_name = 'enquiry_type_list'

class UpdateEnquiryType(UpdateView):
    model = EnquiryType
    form_class = EnquiryTypeForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_enquiry_type')

    def form_valid(self, form):
        messages.success(self.request, "Enquiry Type updated successfully!")
        return super().form_valid(form)

class EnquiryTypeDeleteView(DeleteView):
    model = EnquiryType
    success_url = reverse_lazy('institute:list_of_enquiry_type')

# ========================================= payment CRUD ================================================
class AddPaymentMode(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = PaymentModeForm
    success_url = reverse_lazy('institute:list_of_payment_mode')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofPaymentMode(ListView):
    model = PaymentMode
    template_name = "list_of_masters/payment_mode_list.html"
    context_object_name = 'payment_mode_list'

class UpdatePaymentMode(UpdateView):
    model = PaymentMode
    form_class = PaymentModeForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_payment_mode')

    def form_valid(self, form):
        messages.success(self.request, "Payment mode updated successfully!")
        return super().form_valid(form)

class PaymentModeDeleteView(DeleteView):
    model = PaymentMode
    success_url = reverse_lazy('institute:list_of_payment_mode')

# ================================== class group CRUD ===================================================
class AddClassGroups(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = ClassGroupsForm
    success_url = reverse_lazy('institute:list_of_class_groups')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofClassGroups(ListView):
    model = ClassGroups
    template_name = "list_of_masters/class_groups_list.html"
    context_object_name = 'class_group_list'

class UpdateClassGroups(UpdateView):
    model = ClassGroups
    form_class = ClassGroupsForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_class_groups')

    def form_valid(self, form):
        messages.success(self.request, "Class Group updated successfully!")
        return super().form_valid(form)

class ClassGroupsDeleteView(DeleteView):
    model = ClassGroups
    success_url = reverse_lazy('institute:list_of_class_groups')

# =========================================== standard CRUD =============================================
class AddStandard(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = StandardForm
    success_url = reverse_lazy('institute:list_of_standard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofStandard(ListView):
    model = Standard
    template_name = "list_of_masters/standard_list.html"
    context_object_name = 'standard_list'

class UpdateStandard(UpdateView):
    model = Standard
    form_class = StandardForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_standard')

    def form_valid(self, form):
        messages.success(self.request, "Standard updated successfully!")
        return super().form_valid(form)

class StandardDeleteView(DeleteView):
    model = Standard
    success_url = reverse_lazy('institute:list_of_standard')

# ============================================ subject CRUD =============================================
class AddSubject(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = SubjectsForm
    success_url = reverse_lazy('institute:list_of_subjects')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofSubjects(ListView):
    model = Subjects
    template_name = "list_of_masters/subject_list.html"
    context_object_name = 'subjects_list'

class UpdateSubjects(UpdateView):
    model = Subjects
    form_class = SubjectsForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_subjects')

    def form_valid(self, form):
        messages.success(self.request, "Subject updated successfully!")
        return super().form_valid(form)

class SubjectDeleteView(DeleteView):
    model = Subjects
    success_url = reverse_lazy('institute:list_of_subjects')
    
    


# ======================================= document CRUD =================================================
class AddDocuments(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = DocumnetsForm
    success_url = reverse_lazy('institute:list_of_documents')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofDocuments(ListView):
    model = Documents
    template_name = "list_of_masters/document_list.html"
    context_object_name = 'documents_list'

class UpdateDocument(UpdateView):
    model = Documents
    form_class = DocumnetsForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_documents')

    def form_valid(self, form):
        messages.success(self.request, "Documant updated successfully!")
        return super().form_valid(form)

class DocumentDeleteView(DeleteView):
    model = Documents
    success_url = reverse_lazy('institute:list_of_documents')

# =================================== fee heads CRUD ====================================================
class AddFeeHeads(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = FeeHeadsForm
    success_url = reverse_lazy('institute:list_of_fee_heads')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofFeeHeads(ListView):
    model = FeeHeads
    template_name = "list_of_masters/fee_heads_list.html"
    context_object_name = 'fee_heads_list'

class UpdateFeeHeads(UpdateView):
    model = FeeHeads
    form_class = FeeHeadsForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_fee_heads')

    def form_valid(self, form):
        messages.success(self.request, "Fee head updated successfully!")
        return super().form_valid(form)

class FeeHeadDeleteView(DeleteView):
    model = FeeHeads
    success_url = reverse_lazy('institute:list_of_fee_heads')

# ======================================== fee installments CRUD ========================================
class AddFeeInstallments(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = FeeInstallmentForm
    success_url = reverse_lazy('institute:list_of_fee_installments')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofFeeInstallments(ListView):
    model = FeeInstallments
    template_name = "list_of_masters/fee_installments_list.html"
    context_object_name = 'fee_installments_list'

class UpdateFeeInstallment(UpdateView):
    model = FeeInstallments
    form_class = FeeInstallmentForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_fee_installments')

    def form_valid(self, form):
        messages.success(self.request, "Fee Installment updated successfully!")
        return super().form_valid(form)

class FeeInstallmentDeleteView(DeleteView):
    model = FeeInstallments
    success_url = reverse_lazy('institute:list_of_fee_installments')

# ===================================== leaving reason CRUD =============================================
class AddLeavingReason(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = LeavingReasonForm
    success_url = reverse_lazy('institute:list_of_leaving_reason')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofLeavingReasonTC(ListView):
    model = LeavingReasonTC
    template_name = "list_of_masters/leaving_reason_list.html"
    context_object_name = 'leaving_reason_list'

class UpdateLeavingReason(UpdateView):
    model = LeavingReasonTC
    form_class = LeavingReasonForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_leaving_reason')

    def form_valid(self, form):
        messages.success(self.request, "Leaving Reason updated successfully!")
        return super().form_valid(form)

class LeavingReasonDeleteView(DeleteView):
    model = LeavingReasonTC
    success_url = reverse_lazy('institute:list_of_leaving_reason')
    
# ========================================= sainik school CRUD ==========================================
class AddNameOfSainikSchool(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = NameOfSainikSchoolForm
    success_url = reverse_lazy('institute:list_of_sainik_school')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofNameOfSainikSchool(ListView):
    model = NameOfSainikSchool
    template_name = "list_of_masters/sainik_school_list.html"
    context_object_name = 'sainik_school_list'

class UpdateSainikSchool(UpdateView):
    model = NameOfSainikSchool
    form_class = NameOfSainikSchoolForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_sainik_school')

    def form_valid(self, form):
        messages.success(self.request, "Name of Sainik School updated successfully!")
        return super().form_valid(form)

class SainikSchoolDeleteView(DeleteView):
    model = NameOfSainikSchool
    success_url = reverse_lazy('institute:list_of_sainik_school')

# ===================================== Bank CRUD =======================================================
class AddNameOfBank(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = NameOfBankForm
    success_url = reverse_lazy('institute:list_of_name_of_bank')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofNameOfTheBank(ListView):
    model = NameOfTheBank
    template_name = "list_of_masters/name_of_bank_list.html"
    context_object_name = 'name_of_bank_list'

class UpdateNameOfBank(UpdateView):
    model = NameOfTheBank
    form_class = NameOfBankForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_name_of_bank')

    def form_valid(self, form):
        messages.success(self.request, "Name of Bank updated successfully!")
        return super().form_valid(form)

class NameOfBankDeleteView(DeleteView):
    model = NameOfTheBank
    success_url = reverse_lazy('institute:list_of_name_of_bank')

# ================================= student type CRUD ===================================================
class AddStudentType(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = StudentTypeForm
    success_url = reverse_lazy('institute:list_of_student_type')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofStudentType(ListView):
    model = StudentType
    template_name = "list_of_masters/student_type_list.html"
    context_object_name = 'student_type_list'

class UpdateStudentType(UpdateView):
    model = StudentType
    form_class = StudentTypeForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_student_type')

    def form_valid(self, form):
        messages.success(self.request, "Student Type updated successfully!")
        return super().form_valid(form)

class StudentTypeDeleteView(DeleteView):
    model = StudentType
    success_url = reverse_lazy('institute:list_of_student_type')

# ========================================== child status CRUD ==========================================
class AddChildStatus(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = ChildStatusForm
    success_url = reverse_lazy('institute:list_of_child_status')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListofChildStatus(ListView):
    model = ChildStatus
    template_name = "list_of_masters/child_status_list.html"
    context_object_name = 'child_status_list'

class UpdateChildStatus(UpdateView):
    model = ChildStatus
    form_class = ChildStatusForm
    context_object_name = "form"
    template_name = 'list_of_masters/lom_form.html'
    success_url = reverse_lazy('institute:list_of_child_status')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)

class ChildStatusDeleteView(DeleteView):
    model = ChildStatus
    success_url = reverse_lazy('institute:list_of_child_status')


# ============================================ working on role Element ==================================
def permission_create(request, role_id):
    role = get_object_or_404(InstituteRole, id=role_id)
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            permission = form.save(commit=False)
            permission.role = role
            permission.save()
            return redirect('update_role', role_id=role.id)
    return redirect('role_update', role_id=role.id)

# ========================================== menu data crud =============================================

def get_menu_data(request):
    main_menu_id = request.GET.get('main_menu_id')
    if main_menu_id:
        submenus = SubMenu.objects.filter(menu_id=main_menu_id)
        structured_data = []
        for submenu in submenus:
            supersubmenus = SuperSubMenu.objects.filter(submenu=submenu)
            # print(supersubmenus)
            submenu_data = {
                'submenu': {
                    'id': submenu.id,
                    'name': submenu.name
                },
                'supersubmenus': []
            }
            for supersubmenu in supersubmenus:
                submenu_data['supersubmenus'].append({
                    'id': supersubmenu.id,
                    'name': supersubmenu.name
                })
            structured_data.append(submenu_data)
        # print(structured_data)
        return JsonResponse(structured_data, safe=False)
    return JsonResponse({'error': 'Invalid Main Menu ID'}, status=400)


# ================== Create The Role and assign the permission at the same time =====================
def role_create(request):
    if request.method == 'POST':
        form = InstituteRoleForm(request.POST)
        if not form.is_valid():
            errors = form.errors
            for field, error_list in errors.items():
                for error in error_list:
                    print(f"Error in field '{field}': {error}")
        if form.is_valid():
            role = form.save()
            for key, value in request.POST.items():
                if key.startswith('permissions'):
                    parts = key.split('[')
                    supersubmenu_id = parts[1][:-1]
                    if supersubmenu_id.startswith("supersubmenu_"):
                        supersubmenu_id = supersubmenu_id[13:]
                    print("supersubmenu_id :", supersubmenu_id)
                    permission_type = parts[2][:-1]

                    supersubmenu = SuperSubMenu.objects.get(id=supersubmenu_id)
                    submenu = supersubmenu.submenu
                    menu = submenu.menu

                    permission, created = Permission.objects.get_or_create(
                        role=role,
                        menu=menu,
                        submenu=submenu,
                        supersubmenu=supersubmenu
                    )
                    setattr(permission, f'can_{permission_type}', value == 'on')
                    permission.save()
            return redirect('institute:list_of_roles')
    else:
        form = InstituteRoleForm()

    main_menus = MainMenu.objects.all()
    context = {
        'form': form,
        'main_menus': main_menus,
    }
    return render(request, 'role/create_role.html', context)

# List of Role Created
def role_list(request):
    roles = InstituteRole.objects.all()
    return render(request, 'role/list_of_roles.html', {'roles': roles})

# Update The Role
def role_update(request, pk):
    role = get_object_or_404(InstituteRole, pk=pk)
    if request.method == 'POST':
        form = InstituteRoleForm(request.POST, instance=role)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            form.save_m2m()  # Save the many-to-many relationships

            # Clear existing permissions and re-add them
            Permission.objects.filter(role=role).delete()
            for key, value in request.POST.items():
                if key.startswith('permissions'):
                    parts = key.split('[')
                    supersubmenu_id = parts[1][:-1]
                    if supersubmenu_id.startswith("supersubmenu_"):
                        supersubmenu_id = supersubmenu_id[13:]
                    permission_type = parts[2][:-1]

                    supersubmenu = SuperSubMenu.objects.get(id=supersubmenu_id)
                    submenu = supersubmenu.submenu
                    menu = submenu.menu

                    permission, created = Permission.objects.get_or_create(
                        role=role,
                        menu=menu,
                        submenu=submenu,
                        supersubmenu=supersubmenu
                    )
                    setattr(permission, f'can_{permission_type}', value == 'on')
                    permission.save()
            return redirect('institute:list_of_roles')
    else:
        form = InstituteRoleForm(instance=role)

    main_menus = MainMenu.objects.all()
    context = {
        'form': form,
        'main_menus': main_menus,
        'role': role,
    }
    return render(request, 'role/update_role.html', context)

# Delete The role
class RoleDeleteView(DeleteView):
    model = InstituteRole
    success_url = reverse_lazy('institute:list_of_roles')

# ================================== create users section started ====================================

# list of Employees
class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee/employee_list.html'

# creating the Employee
def create_employee(request):
    if request.method == 'POST':
        user_form = EmployeeRegistrationForm(request.POST)
        profile_form = EmployeeProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data["password1"])
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                return redirect('institute:list_of_employees')
            except Exception as e:
                print(f"Error saving user or profile: {e}")
        else:
            print(f"User form errors: {user_form.errors}")
            print(f"Profile form errors: {profile_form.errors}")

    else:
        user_form = EmployeeRegistrationForm()
        profile_form = EmployeeProfileForm()
        return render(request, 'employee/create_employee.html', {'user_form': user_form, 'profile_form': profile_form})


# Update the employee
def update_employee(request, pk):
    profile = get_object_or_404(Employee, pk=pk)
    user = get_object_or_404(User, pk= profile.user.id)
    if request.method == 'POST':
        user_form = EmployeeRegistrationForm(request.POST, instance=user)
        profile_form = EmployeeProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data["password1"])
                user.save()
            except Exception as e:
                print(e)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('institute:list_of_employees')
        else:
            return render(request, 'employee/update_employee.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = EmployeeRegistrationForm(instance=user)
        profile_form = EmployeeProfileForm(instance=profile)
        return render(request, 'employee/update_employee.html', {'user_form': user_form, 'profile_form': profile_form})

# Delete Employee data
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('institute:list_of_employees')

# ===================================== Notification CRUD ============================================
def notification_create_view(request):
    if request.method == 'POST':
        form = NotificationModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('institute:list_of_notifications')  # Redirect to a list view or another appropriate view
    else:
        form = NotificationModelForm()
    return render(request, 'notification_form.html', {'form': form})

#<------------------------ for SubFOrClassGroup in session settings ---------------------------------->

def notification_update_view(request, pk):
    notification = get_object_or_404(NotificationModel, pk=pk)
    if request.method == 'POST':
        form = NotificationModelForm(request.POST, request.FILES, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('institute:list_of_notifications')  # Redirect to the detail view or another appropriate view
    else:
        form = NotificationModelForm(instance=notification)
    return render(request, 'notification_form.html', {'form': form})


class NotificationsListView(ListView):
    model = NotificationModel
    template_name = "notification_list.html"
    context_object_name = 'notifications_list' 

class NotificationDeleteView(DeleteView):
    model = NotificationModel
    success_url = reverse_lazy('institute:list_of_notifications')


# ================================= subject for class groups data crud ================================
class AddSubForClassGroup(CreateView):
    template_name = "session_settings/ss_sub_for_groups_form.html"
    form_class = SubjectsForClassGroupForm
    success_url = reverse_lazy('institute:list_of_sub_for_class_groups')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class listSubForClassGroup(ListView):
    template_name = "session_settings/ss_sub_for_groups_list.html"
    model = SubjectsForClassGroup
    context_object_name = 'subject_for_class_group_list'
class UpdateSubForClassGroup(UpdateView):
    model = SubjectsForClassGroup
    form_class = SubjectsForClassGroupForm
    context_object_name = "form"
    template_name = 'session_settings/ss_sub_for_groups_form.html'
    success_url = reverse_lazy('institute:list_of_sub_for_class_groups')
    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)


class DeleteSubForClassGroup(DeleteView):
    model = SubjectsForClassGroup
    success_url = reverse_lazy('institute:list_of_sub_for_class_groups')

class AddSubForClassGroup(CreateView):
    template_name = "session_settings/ss_sub_for_groups_form.html"
    form_class = SubjectsForClassGroupForm
    success_url = reverse_lazy('institute:list_of_sub_for_class_groups')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# =============================== for section in session settings ===================================
class AddSection(CreateView):
    template_name = "session_settings/section_form.html"
    form_class = SectionForm
    success_url = reverse_lazy('institute:list_of_section')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class listOfSection(ListView):
    template_name = "session_settings/section_list.html"
    model = Section
    context_object_name = 'section_list'

class UpdateSection(UpdateView):
    model = Section
    form_class = SectionForm
    context_object_name = "form"
    template_name = 'session_settings/section_form.html'
    success_url = reverse_lazy('institute:list_of_section')
    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)


class DeleteSection(DeleteView):
    model = Section
    success_url = reverse_lazy('institute:list_of_section')

#  =============================== for discount scheme in session settings ===========================
class AddDiscountScheme(CreateView):
    template_name = "session_settings/discount_form.html"
    form_class = DiscountSchemeForm
    success_url = reverse_lazy('institute:list_of_discount')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class listOfDiscountScheme(ListView):
    template_name = "session_settings/discount_list.html"
    model = DiscountScheme
    context_object_name = 'discount_list'

class UpdateDiscountScheme(UpdateView):
    model = DiscountScheme
    form_class = DiscountSchemeForm
    context_object_name = "form"
    template_name = 'session_settings/discount_form.html'
    success_url = reverse_lazy('institute:list_of_discount')
    def form_valid(self, form):
        messages.success(self.request, "discount updated successfully!")
        return super().form_valid(form)

class DeleteDiscountScheme(DeleteView):
    model = DiscountScheme
    success_url = reverse_lazy('institute:list_of_discount')
    
    
#<------------------------ for Attendance ---------------------------------->

def attendance_view(request):
    standards = Standard.objects.all()
    if request.method == 'POST':
        data = request.POST
        date = data.get('date')
        standard_id = data.get('standard')
        subject_id = data.get('subjects')

        students = StudentProfile.objects.filter(standard_id=standard_id)

        for student in students:
            student_id = student.id
            attendance_status = data.get(f'attendance_status_{student_id}')
            present = attendance_status == 'present'
            absent = attendance_status == 'absent'

            Attendance.objects.update_or_create(
                student_id=student_id,
                subject_id=subject_id,
                standard_id = standard_id,
                date=date,
                defaults={'present': present, 'absent': absent}
            )

        return redirect('institute:attendance_list')  # redirecting to list of students
    form = AttendanceForm
    context = {
        'standards': standards,
        'form': form,
    }
    return render(request, 'attendance.html', context)
    
def load_subjects(request):
    standard_id = request.GET.get('standard_id')
    subjects = Subjects.objects.filter(standard_id=standard_id).all()
    return JsonResponse(list(subjects.values('id', 'name')), safe=False)




def fetch_students_attendance(request):
    if request.method == 'GET':
        standard_id = request.GET.get('standard_id')
        subject_id = request.GET.get('subject_id')
        date = request.GET.get('date')

        # Fetch students based on the selected standard
        students = StudentProfile.objects.filter(
            standard_id=standard_id
        ).values('id', 'user__first_name', 'user__last_name', 'enroll_no')

        # Prepare attendance data
        attendance_data = []
        for student in students:
            attendance_status = Attendance.objects.filter(
                student_id=student['id'],
                subject_id=subject_id,
                date=date
            ).first()

            attendance_data.append({
                'id': student['id'],
                'name': f"{student['user__first_name']} {student['user__last_name']}",
                'roll_no': student['enroll_no'],
                'present': attendance_status.present if attendance_status else False,
                'absent': attendance_status.absent if attendance_status else False
            })

        return JsonResponse({'students': attendance_data})

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def attendance_list(request):
    standards = Standard.objects.all()
    subjects = Subjects.objects.all()
    return render(request, 'attendance_list.html', {'standards': standards, 'subjects': subjects})


def fetch_attendance_data(request):
    if request.method == 'GET':
        standard_id = request.GET.get('standard_id')
        subject_id = request.GET.get('subject_id')

        attendance_records = Attendance.objects.filter(
            standard_id=standard_id,
            subject_id=subject_id
        ).select_related('student')

        attendance_data = []
        for record in attendance_records:
            attendance_data.append({
                'name': f"{record.student.user.first_name} {record.student.user.last_name}",
                'enroll_no': record.student.enroll_no,
                'present': record.present,
                'absent': record.absent,
                'date': record.date.strftime('%Y-%m-%d'),
            })

        return JsonResponse({'attendance_data': attendance_data})

    return JsonResponse({'error': 'Method not allowed'}, status=405)