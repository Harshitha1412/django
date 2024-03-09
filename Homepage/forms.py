from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError

from django import forms
from .models import UserProfile

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'gender', 'password', 'profile_image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)



class ProfilePictureForm(forms.Form):
    profile_image = forms.ImageField()

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if profile_image:
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if not any(profile_image.name.lower().endswith(ext) for ext in allowed_extensions):
                raise ValidationError('Unsupported file extension. Please upload a valid image.')
        return profile_image