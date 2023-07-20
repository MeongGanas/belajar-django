from django.contrib import admin
from dashboard.models import Anggota
# Register your models here.


@admin.register(Anggota)
class anggotaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'umur', 'jenis_kelamin', 'alamat']
