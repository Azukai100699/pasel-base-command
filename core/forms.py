from django import forms
from django.contrib.auth.models import User
from .models import AccessCode

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    access_code = forms.CharField(
        max_length=50, 
        help_text="Enter the secure code provided in your invitation."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_access_code(self):
        code = self.cleaned_data.get('access_code')
        # Check if the code exists and is active
        if not AccessCode.objects.filter(code=code, is_active=True).exists():
            raise forms.ValidationError("Invalid or inactive access code. Please contact an administrator.")
        return code

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user