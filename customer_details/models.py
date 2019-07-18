from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class ApplicantBank(models.Model):
    bank_name = models.CharField(max_length = 100)
    bank_branch = models.CharField(max_length = 100)
    account_number = models.IntegerField(max_length = 10)
    od_limit = models.IntegerField(max_length = 50)
    outstanding_loan = models.IntegerField()

    def save_applicantbank(self):
        self.save()

    def delete_applicantbank(self):
        self.delete()

    def __str__(self):
        return self.bank_name