from django import forms
from models import UserModel        #, Review

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['firstname', 'lastname', 'username', 'email' ,'gender', 'password']

class LogInForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['service','product_quality','delivery_time','app_website','innovate']

"""

"""
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = UserModel.objects.filter(username= username).exists()
        if user:
            raise forms.ValidationError('UserName Already Exists')

"""


