from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Todo
from django.forms import ModelForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="hộp thư của ban:")
    username = forms.CharField(label="tên đangq nhập")
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['Ho_ten','sdt','khoa_phong','dia_chi','MSBN','cd_benh','lich_hen_kham']




class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['sot', 'ho', 'kho_tho','tiepxuc_f0','tiepxuc_f1','vung_dich','tt_banthan']