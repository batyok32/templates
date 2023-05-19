from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# class UserCreationForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username',)

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Repeat Password', widget=forms.PasswordInput)

#     class Meta:
#         fields = ('username',)
#         model = User

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords don\'t match')
#         return password2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password2'])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ('username', 'password',  'type', 'is_active',
#                   'is_staff', 'date_joined')

#     def clean_password(self):
#         return self.initial['password']
