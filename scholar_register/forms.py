from django import forms
from accounts.models import User
from .models import StudentProfile


class StudentUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','phone_number','role')
        
        def clean_Password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("password don't match")
            return password2
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.role = '3'
            if commit:
                user.save()
            return user
        
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = "__all__"            