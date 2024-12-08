from django import forms

class contact_us_form(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',max_length=50,error_messages={
        'required':'لطفا نام و نام خانوادگی خود را وارد نمایید',
        'max_lenghth':'نام و نام خانوادگی نمی تواند بیشتر از 50 کرکتر باشد'
    },
        widget=forms.TextInput(attrs={
        'class':'form control',
        'placeholder':'نام و نام خانوادگی'
        }))
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={
        'class':'form control',
        'placeholder':'ایمیل'
    }))
    subject = forms.CharField(label='عنوان',widget=forms.TextInput(attrs={
        'class':'form control',
        'placeholder':'عنوان'
    }))
    message = forms.CharField(label='متن پیام',widget=forms.Textarea(attrs={
        'class':'form control',
        'placeholder':'متن پیام',
        'id':'message'
    }))