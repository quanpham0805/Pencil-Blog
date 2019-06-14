# import needed stuffs
# here we will have our custom forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Comment

# form for registration
class RegisterForm(UserCreationForm):
    # additional fields
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        # user can change username, email, password1 and 2, first name and last name
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    # function to check if email exist
    def clean_email(self):
        # get the cleaned current email
        currentEmail = self.cleaned_data.get('email')
        try:
            # try to match it.
            match = User.objects.get(email=currentEmail)
        except User.DoesNotExist:
            # if it doesn't exist, then it's good to go
            return currentEmail
        # otherwise user must use another.
        raise forms.ValidationError('This email address is already in use.')

    # overide save function
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # commit=False tells Django that "Don't send this to database yet.
        user.email = self.cleaned_data["email"]
        # then assign value using clean data.
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            # then save to the database
        return user

# the form to comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # only allow user to change the comment text.
        fields = ("comment_text",)