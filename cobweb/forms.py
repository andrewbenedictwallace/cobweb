from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms 
from django.contrib import auth
from django.contrib.auth import forms as authforms
from . import models

class UserForm(authforms.UserCreationForm):
    email = forms.EmailField(required=True)
    # first_name
    # last_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    class Meta:
        model = auth.models.User
        fields = ("username", "email", "password1", "password2")

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = models.Project
        fields = ['name', 'description']

class NominationForm(forms.ModelForm):

    class Meta:
        model = models.Nomination
        fields = ['resource', 'description']

    resource = forms.CharField(widget=forms.TextInput) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean_resource(self):
        root_url = self.cleaned_data.get("resource")
        if not root_url:
            raise forms.ValidationError("Please enter a URL.")
        else:
            return models.Resource.objects.get_or_create(root_url = root_url)[0]

