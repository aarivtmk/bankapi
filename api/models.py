from django.db import models

# Create your models here.
class BankDetail(models.Model):
    ifsc_code = models.CharField(max_length=30,null=False)
    bank_id = models.CharField(max_length=5,null=False)
    branch = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=500,null=False)
    city = models.CharField(max_length=100,null=False)
    district = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    bank_name = models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.bank_name
    
    