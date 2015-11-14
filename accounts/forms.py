from django import forms
from django.forms import ModelForm
# from django.core.exceptions import ValidationError
from models import MyUser, UserInfo

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

class UserProfile(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(UserProfile, self).__init__(*args, **kwargs)
    #     # assign a (computed, I assume) default value to the choice field
    #     self.fields['owner'] = forms.ModelChoiceField(queryset=MyUser.objects.all(),initial=3)

    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # address = forms.CharField()
    # city = forms.CharField()
    # zipcode = forms.CharField()
    # title = forms.CharField()
    # phone_number = forms.CharField()
    # wechat_number = forms.CharField()
    # introduction = forms.CharField()
    # owner = forms.ModelChoiceField(queryset=Speed.objects.all())

    # def __init__(self, user, *args, **kwargs):
    #     super(UserProfile, self).__init__(*args, **kwargs)
    #     UserInfo.objects.filter(owner=user.pk)
    #     self.fields['owner'].queryset = UserInfo.objects.filter(owner=user.pk)
    #     print 'Owner    '+`self.fields['owner'].queryset`

    class Meta:
        model = UserInfo
        exclude = ("owner",)

    # def save(self, commit=True):
    #     userprofile = super(UserProfile, self).save(commit=False)
    #     userprofile.set_user(self.cleaned_data["password"])

    #     if commit:
    #         userprofile.save()




class SignUpTestForm(forms.Form):


    # <input id="textinput" name="textinput" type="text" placeholder="Email" class="form-control input-md" required="">

    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'id':"email",'class': "form-control input-md",'required':"",'placeholder':"Email"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'id':"password",'class': "form-control input-md",'required':"",'placeholder':"Password"}))
    error_css_class = 'error'
    class Meta:
        model = MyUser
        fields = '__all__'

    # def clean(self):
        # raise forms.ValidationError(u'That domain is already taken.  Please choose another')

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



