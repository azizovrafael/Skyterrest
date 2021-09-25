# Generated by Django 3.2 on 2021-05-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_service_adlari_2_seherler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Adlari_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servis_seher', models.CharField(max_length=20, verbose_name='Seher ADi :')),
                ('servis_mekan', models.CharField(max_length=20, verbose_name='Mekan ADi :')),
                ('servis_title', models.CharField(max_length=20, verbose_name='Service Adi: ')),
                ('servis_content', models.TextField(verbose_name='Service Content: ')),
                ('servis_sekil', models.ImageField(upload_to='', verbose_name='Service Image: ')),
            ],
        ),
    ]
