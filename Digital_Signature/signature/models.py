# signature/models.py
from django.db import models # type: ignore
import datetime
import uuid
from django.utils import timezone # type: ignore

class LoanAgreement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    borrower = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.borrower

    
class BorrowerSignature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agreement = models.ForeignKey(LoanAgreement, on_delete=models.CASCADE)
    loan_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    #borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100, default='Default Borrower')
    signed_at = models.DateTimeField(auto_now_add=True)
    signed_document = models.FileField(upload_to='signed_documents/', null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    x_position = models.IntegerField(default=100)
    y_position = models.IntegerField(default=50)
    def __str__(self):
        return f"Signature of {self.name} on {self.signed_at}"
    