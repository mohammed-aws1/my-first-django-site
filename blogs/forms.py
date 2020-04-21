from django import forms
from django.contrib.auth.models import User
from .models import Posts


class contact(forms.Form):
    first_name= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
        ,required=True)
    last_name= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
        ,required=True)
    email= forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control'})
        ,required=True)
    subject =forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
        ,required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','cols':'30','rows':'7','placeholder':'اكتب رسالتك هنا ...'})
        ,required=True)
class Create_User(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'الأسم'})
        ,required=True,max_length=20)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'البريد الألكتروني'})
        ,required=True,max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'كلمة السر'})
        ,required=True)
    class Meta():
        model = User
        fields =['username','email','password']
    def clean_username(self):
        name = self.cleaned_data.get('username')
        if name.count(' ') == 1:
            firstname, lastname = name.split(' ')
            name = firstname + '_' + lastname
        elif name.count(' ') > 1:
            raise forms.ValidationError("لايمكن ان يحتوي الاسم على اكثر من مسافة")
        elif len(name) <= 3:
            raise forms.ValidationError('هذا الاسم قصير جدا حاول مرة اخرى')
        else:
            for usern in User.objects.all():
                if usern.username == name:
                    raise forms.ValidationError('هذا الاسم مستخدم ')
        return name
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for Emails in User.objects.all():
            if email == Emails.email:
                raise forms.ValidationError('هذا البريد مستخدم')
        return email
    def clean_password(self):
        pass1 = self.cleaned_data.get('password')
        if len(pass1) < 8 and len(pass1) >= 1 :
            raise forms.ValidationError('كلمة السر قصيرة جدا حاول مرة اخرى')
        elif pass1.isdigit():
            raise forms.ValidationError('يجب ان تحتوي كلمة السر على حرف واحد على الاقل')
        return pass1

class Add_post(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input--style-6', 'placeholder': 'اكتب العنوان هنا ...'})
        , required=True)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'textarea--style-6', 'placeholder': 'اكتب المحتوى هنا ...'})
        )
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input--style-6', 'placeholder': 'مكان ابرز التغريدات فقط اجب ب (نعم) او اتركه فارغاَ ...'})
        ,required=False)

    class Meta():
        model  = Posts
        fields = ['title','content','img','tags']