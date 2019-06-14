from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def clean_email(self):
        currentEmail = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=currentEmail)
        except User.DoesNotExist:
            return currentEmail

        raise forms.ValidationError('This email address is already in use.')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # commit=False tells Django that "Don't send this to database yet.
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text",)