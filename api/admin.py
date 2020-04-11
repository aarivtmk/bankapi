from django.contrib import admin
from api.models import BankDetail
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class BankDetailAdmin(ImportExportModelAdmin):

    list_display = ('bank_name','ifsc_code')
    list_display_links = ('bank_name',)
    list_filter = ('bank_name','state')
    search_fields = ('bank_name', 'ifsc_code')
    list_per_page = 25

admin.site.register(BankDetail,BankDetailAdmin)