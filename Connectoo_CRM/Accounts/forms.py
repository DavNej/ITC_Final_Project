from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from CRM.models import Users



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # check user exists
            user = authenticate(username=username, password=password)
            # check_user = Users.objects.filter(username=email) 
            # if check_user.count() == 1:
                # user = check_user.first()
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
                
        # return data from the form
        return super(UserLoginForm, self).clean()