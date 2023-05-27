from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProfitCenterForm(ModelForm):
    class Meta:
        model = ProfitCenter
        fields = ('profitCenterName', 'description')


class BussinessObjectiveForm(ModelForm):
    class Meta:
        model = BusinessObjective
        fields = '__all__'


class BizNeedForm(ModelForm):
    class Meta:
        model = BizNeed
        fields = '__all__'