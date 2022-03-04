from datetime import datetime
from django import forms
from homework.models import Homework
STATUS_CHOICE = (
    (0, "Yes"),
    (1, "No"),
)


class TaskForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'field-style field-split'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'field-style field-split'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'field-style field-split'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field-style field-split'}))
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(attrs={'class':
                                                                                         'field-style field-split'}))
    is_active = forms.ChoiceField(choices=STATUS_CHOICE, widget=forms.Select(attrs={'class':
                                                                                           'field-style field-split'}))

    def clean_username(self):
        _username = self.cleaned_data.get('username')
        if Homework.objects.filter(username=_username).exists():
            raise forms.ValidationError("error")
        return _username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Homework.objects.filter(phone=phone).exists():
            raise forms.ValidationError("error")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(Homework.objects.filter(email=email)) > 1:
            raise forms.ValidationError("with one email only Two accounts can be created")
        return email



# class USerModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"