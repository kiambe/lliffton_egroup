from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.db import transaction

from .models import *

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_admin', 'is_vendor', 'is_member')


BANK_NAMES = [
    ("COOBA", "Commercial Bank of Africa Ltd"),
    ("COOP", "Co-operative Bank of Kenya Ltd"),
    ("DTB", "Diamond Trust Bank (K) Ltd"), 
    ("FBL", "Family Bank Ltd"),
    ("EBL", "Equity Bank Ltd"),
    ("NBK", "National Bank of Kenya Ltd"),
    ("POST", "Postbank"),
    ("SCBK", "Standard Chartered Bank (K) Ltd"),
    ("KCB", " Kenya Commercial Bank Ltd"),
    ("ABP", "Absa Bank PLC")
    ] 

BUSINESS_ACTIVITIES = [
    ("Producers", "Producers"),
    ("Marketers", "Marketers"),
    ("Traders", "Marketers"), 
    ("Aggregators", "Aggregators"),
    ("Processors", "Processors"),
    ]

GROUP_TYPES = [
    ("Women Group", "Women Group"),
    ("Men Group", "Men Group"),
    ("Youth Group", "Youth Group"), 
    ("Mixed Group", "Mixed Group"),
    ]

GENDER_CATEGORIES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer Not To Say", "Prefer Not To Say"),
    ]

class CreateGroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Group Name"))
    special_code = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Special Code"))
    group_type = forms.CharField(max_length=20, widget=forms.Select(attrs={"class": "form-control"}, choices=GROUP_TYPES), label="Group Type")
   #ward_id = forms.CharField(widget=forms.Select(attrs={"class": "form-control"}), label=("Ward"))
    business_activity = forms.CharField(max_length=20, widget=forms.Select(attrs={"class": "form-control"}, choices=BUSINESS_ACTIVITIES), label="Business Activity")
    bank_name = forms.CharField(max_length=20, widget=forms.Select(attrs={"class": "form-control"}, choices=BANK_NAMES), label="Bank Name")
    mpesa_tillnumber = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Mpesa Paybill"))
    mpesa_paybill_busines_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Mpesa Business Number"))
    mpesa_paybill_account_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Mpesa Account Number"))
    secretary_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Secretary Name"))
    secretary_phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Secretary Phone"))
    opportunity = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Opportunity"))  

    class Meta:
        model = Group
        fields = ['name', 'special_code', 'group_type', 'ward_id', 'business_activity', 'bank_name','mpesa_tillnumber', 'mpesa_paybill_busines_number', 'mpesa_paybill_account_number', 'secretary_name', 'secretary_phone', 'opportunity'] 

class UpdateMemberProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("First Name"))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Last name"))
    physical_address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Physical Address"))
    national_id = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("National ID Number"))
    primary_phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Mobile Phone Number"))
    year_of_birth = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label=("Year of Birth"))
    gender = forms.CharField(max_length=20, widget=forms.Select(attrs={"class": "form-control"}, choices=GENDER_CATEGORIES), label="Gender")
   
    class Meta:
        model = Member
        fields = ['user', 'first_name', 'last_name', 'physical_address', 'national_id', 'primary_phone_number','year_of_birth', 'gender', 'ward_id'] 



class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    

    class Meta:
        model = Group
        fields = ("__all__")


class GroupMembersForm(forms.ModelForm):
    #project = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GroupMembers
        fields = ('member_id', 'group_id')

class SavingForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Saving
        fields = ("__all__" )


class VoucherForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Voucher
        fields = ("__all__" )

class LoanProductForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanProduct
        fields = ("__all__" )



class LoanForm(forms.ModelForm):
    # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Loan
        fields = ("__all__" )


class LoanRepaymentForm(forms.ModelForm):
    # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanRepayment
        fields = ("__all__" )


class PenaltyForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Penalty
        fields = ("__all__" )


class GroupAnnouncementForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GroupAnnouncement
        fields = ("__all__" )

class LoanReminderForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = LoanReminder
        fields = ("__all__" )

class VendorForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Vendor
        fields = ("__all__" )


class ProductForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Product
        fields = ("__all__" )


class CustomPasswordChangeForm(PasswordChangeForm):
    pass
        
        
class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'