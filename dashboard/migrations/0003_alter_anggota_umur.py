# Generated by Django 4.2.3 on 2023-07-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_anggota_delete_pegawai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='umur',
            field=models.IntegerField(),
        ),
    ]
