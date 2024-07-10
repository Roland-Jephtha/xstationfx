from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        # Customize form fields if needed
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})






class CustomPasswordResetForm(PasswordResetForm):
        #Add css class
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'pl-5 form-control'})
        


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',]

    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        # self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})
    
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['avatar','full_name', 'address', 'email', 'phone', ]
        
        
    #Add css class
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control  deposit-form', 'id': 'image1', 'onchange': "displaySelectedImage(event, 'photo_1')"})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['address'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['email'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['email'].widget.attrs['readonly'] = True
        
        
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields  = ['currency', 'amount', 'payment_slip', 'user' ]
        
        
    #Add css class
    def __init__(self, *args, **kwargs):
        super(DepositForm, self).__init__(*args, **kwargs)
        self.fields['currency'].widget.attrs.update({'class': 'form-control deposit-form', 'onchange':'updatePaymentOptions()'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['payment_slip'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['user'].widget.attrs.update({'class': 'hidden'})
        
        
class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields  = ['currency', 'amount', 'wallet_address', 'user'  ]
        
        
        
        #Add css class
    def __init__(self, *args, **kwargs):
        super(WithdrawForm, self).__init__(*args, **kwargs)
        self.fields['currency'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['wallet_address'].widget.attrs.update({'class': 'form-control deposit-form'})
        # self.fields['withdraw_from'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['user'].widget.attrs.update({'class': 'hidden'})
        
class Withdraw_bankForm(forms.ModelForm):
    class Meta:
        model = Withdraw_bank
        fields  = ['account_number', 'bank_name','amount', 'name_of_account', 'user']
        
        
        
        #Add css class
    def __init__(self, *args, **kwargs):
        super(Withdraw_bankForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['bank_name'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['name_of_account'].widget.attrs.update({'class': 'form-control deposit-form'})
        self.fields['user'].widget.attrs.update({'class': 'hidden'})