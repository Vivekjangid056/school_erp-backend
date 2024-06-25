from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import *
from .models import *
from django.views.generic import UpdateView, CreateView, DeleteView, FormView, ListView


def temp(request):
    data = Institute.objects.all()
    print(data)


class InstituteList(ListView):
    model = Institute
    context_object_name = 'institutes'
    template_name = 'institute_list.html'


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    context_object_name = "form"
    template_name = 'update_form.html'
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)
    

class InstituteRegisterView(CreateView):
    template_name = 'institute_register.html'
    form_class = CustomUserRegisterForm
    second_form_class = InstituteForm
    success_url = reverse_lazy('institute:institute_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        profile_form = self.second_form_class(request.POST, request.FILES)
        
        print(f"User Form Errors: {form.errors}")
        print(f"Profile Form Errors: {profile_form.errors}")

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Handle password setting
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(form=form, profile_form=profile_form)
        )
    

class InstituteDeleteView(DeleteView):
    model = Institute
    success_url = reverse_lazy('institute:institute_list')


#                                        signature CRUD Starts
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
    
class AddHouse(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = HouseForm
    success_url = reverse_lazy('institute:list_of_hoouse')

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

    
class AddPaymentMode(FormView):
    template_name = "list_of_masters/lom_form.html"
    form_class = PaymentModeForm
    success_url = reverse_lazy('institute:institute_list')

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



# working on role Element

# class RoleCreate(CreateView):
#     template_name = 'role/create_role.html'
#     form_class = RoleForm
#     success_url = reverse_lazy('institute:list_of_roles')

# class RoleView(ListView):
#     template_name = 'role/list_of_roles.html'
#     model = InstituteRole
#     context_object_name = 'list_of_roles'

# class UpdateRole(UpdateView):
#     model = InstituteRole
#     form_class = RoleForm
#     context_object_name = "form"
#     template_name = 'role/create_role.html'
#     success_url = reverse_lazy('institute:list_of_roles')

#     def form_valid(self, form):
#         messages.success(self.request, "Institute role updated successfully!")
#         return super().form_valid(form)

# class DeleteRole(DeleteView):
#     model = InstituteRole
#     template_name = 'role/role_confirm_delete.html'
#     success_url = reverse_lazy('institute:list_of_roles')

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, "Institute role deleted successfully!")
#         return super().delete(request, *args, **kwargs)



def role_list(request):
    roles = InstituteRole.objects.all()
    return render(request, 'role/list_of_roles.html', {'roles': roles})

# def role_create(request):
#     if request.method == 'POST':
#         form = RoleForm(request.POST)
#         if form.is_valid():
#             role = form.save()
#             return redirect('institute:update_role', role_id=role.id)
#     else:
#         form = RoleForm()
#     return render(request, 'role/role_form.html', {'form': form})

# def role_update(request, pk):
#     role = get_object_or_404(InstituteRole, id=pk)
#     if request.method == 'POST':
#         form = RoleForm(request.POST, instance=role)
#         if form.is_valid():
#             form.save()
#             return redirect('role_list')
#     else:
#         form = RoleForm(instance=role)
#     permissions = Permission.objects.filter(role=role)
#     permission_form = PermissionForm()
#     return render(request, 'role/role_form.html', {
#         'form': form,
#         'role': role,
#         'permissions': permissions,
#         'permission_form': permission_form,
#     })

# def permission_create(request, role_id):
#     role = get_object_or_404(InstituteRole, id=role_id)
#     if request.method == 'POST':
#         form = PermissionForm(request.POST)
#         if form.is_valid():
#             permission = form.save(commit=False)
#             permission.role = role
#             permission.save()
#             return redirect('update_role', role_id=role.id)
#     return redirect('role_update', role_id=role.id)

class RoleDeleteView(DeleteView):
    model = InstituteRole
    success_url = reverse_lazy('institute:list_of_roles')



def role_create(request):
    if request.method == 'POST':
        form = InstituteRoleForm(request.POST)
        if form.is_valid():
            role = form.save()
            # Process permissions
            for key, value in request.POST.items():
                if key.startswith('permissions'):
                    # permissions[<supersubmenu_id>][<permission_type>]
                    parts = key.split('[')
                    supersubmenu_id = parts[1][:-1]
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
            return redirect('institute:list_of_roles')  # Redirect to a list view or detail view
    else:
        form = InstituteRoleForm()

    menus = MainMenu.objects.all()
    structured_data = []

    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        menu_data = {
            'menu': menu,
            'submenus': []
        }
        for submenu in submenus:
            supersubmenus = SuperSubMenu.objects.filter(submenu=submenu)
            submenu_data = {
                'submenu': submenu,
                'supersubmenus': supersubmenus
            }
            menu_data['submenus'].append(submenu_data)
        structured_data.append(menu_data)

    context = {
        'form': form,
        'structured_data': structured_data,
    }
    return render(request, 'role/create_role.html', context)







def role_update(request, pk):
    role = get_object_or_404(InstituteRole, id=pk)
    menus = MainMenu.objects.all()
    
    permissions = Permission.objects.filter(role=role)

    structured_data = []

    for menu in menus:
        submenus = SubMenu.objects.filter(menu=menu)
        menu_data = {
            'menu': menu,
            'submenus': []
        }
        for submenu in submenus:
            supersubmenus = SuperSubMenu.objects.filter(submenu=submenu)
            submenu_data = {
                'submenu': submenu,
                'supersubmenus': []
            }
            for supersubmenu in supersubmenus:
                submenu_permissions = permissions.filter(menu=menu, submenu=submenu, supersubmenu=supersubmenu).first()
                submenu_data['supersubmenus'].append({
                    'supersubmenu': supersubmenu,
                    'permissions': submenu_permissions
                })
            menu_data['submenus'].append(submenu_data)
        structured_data.append(menu_data)

    context = {
        'role': role,
        'structured_data': structured_data,
    }

    return render(request, 'role/role_form.html', context)