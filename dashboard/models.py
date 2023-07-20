from django.db import models

# Create your models here.


class Anggota(models.Model):
    nama = models.CharField(max_length=225)
    alamat = models.CharField(max_length=225)
    umur = models.IntegerField()

    JENIS_KELAMIN = (
        ('laki-laki', 'laki-laki'),
        ('perempuan', 'perempuan')
    )
    jenis_kelamin = models.CharField(max_length=225, choices=JENIS_KELAMIN)
