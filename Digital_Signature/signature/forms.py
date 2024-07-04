# signature/forms.py

from django import forms # type: ignore
from .models import LoanAgreement
from django.forms import formset_factory # type: ignore

class NumberOfBorrowersForm(forms.Form):
    num_borrowers = forms.IntegerField(label='Number of Borrowers', min_value=1)

class BorrowerDetailForm(forms.Form):
    loan_id = forms.CharField(label='Loan ID')
    name = forms.CharField(label='Name', max_length=100)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15)
    
BorrowerDetailFormSet = formset_factory(BorrowerDetailForm, extra=1)
    
class LoanAgreementForm(forms.ModelForm):
    class Meta:
        model = LoanAgreement
        fields = ['document']

# class SignatureForm(forms.Form):
#     lender = forms.CharField(max_length=100)
    
