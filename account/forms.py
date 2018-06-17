from django import forms
from account.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'帳號'}) )
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'密碼','class':"form-control"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'確認密碼','class':"form-control"}))
    fullName = forms.CharField(label='', max_length=128, widget=forms.TextInput(attrs={'placeholder':'姓名','class':"form-control"}))
    # website = forms.URLField(label='個人網址', max_length=128)
    address = forms.CharField(label='', max_length=128, widget=forms.TextInput(attrs={'placeholder':'住址','class':"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'fullName', 'address']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user