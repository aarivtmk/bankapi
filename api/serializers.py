from rest_framework import serializers
from .models import BankDetail

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = ('id','ifsc_code','branch','address','city','district','state','bank_name')