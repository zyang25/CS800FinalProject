from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from models import MyUser

class SignUpForm(ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email','password']
    
    def clean_email(self):
        model = MyUser
        form_email = self.cleaned_data['email']
        try:
            model.objects.get(email__exact=form_email)
        except model.DoesNotExist:
            return form_email
        raise forms.ValidationError("The email has already existed.")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        user.is_admin = False
        if commit:
            user.save()
        # return user

class LoginForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
    )
    
    # def clean(self):       
    #     user = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')

    #     if User.objects.filter(email=user).exists():
    #         password = self.cleaned_data.get('password')
    #         user = authenticate(username=user.username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    #         return self.cleaned_data

    # def login(self, request):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     return user




