from django.db import models

class Seher_Adlari(models.Model):
	seherler = models.CharField(max_length = 20, verbose_name = "Seher Adi: ")
	seher_sekil = models.ImageField(verbose_name="Seher Sekili: ")

class Service_Adlari_2(models.Model):
	seherler = models.CharField(max_length=20, verbose_name="Seher Adi: ")
	seher_otel_adi = models.CharField(max_length = 20,verbose_name = "Otel ADi :")
	seher_otel = models.ImageField(verbose_name="Otel Sekili: ")
	seher_rest_adi = models.CharField(max_length=20, verbose_name="Restoran ADi :")
	seher_rest = models.ImageField(verbose_name="Restoran Sekili: ")
	seher_park_adi = models.CharField(max_length=20, verbose_name="Luna Park ADi :")
	seher_park = models.ImageField(verbose_name="Luna Park Sekili: ")
	seher_cimerlik_adi = models.CharField(max_length=20, verbose_name="Cimerlik ADi :")
	seher_cimerlik = models.ImageField(verbose_name="Cimerlik Sekili: ")

class Service_Adlari_3(models.Model):
	servis_seher = models.CharField(max_length = 20,verbose_name = "Seher ADi :")
	servis_mekan = models.CharField(max_length = 20,verbose_name = "Mekan ADi :")
	servis_title = models.CharField(max_length=20, verbose_name="Service Adi: ")
	servis_content = models.TextField(verbose_name="Service Content: ")
	servis_sekil = models.ImageField(verbose_name="Service Image: ")
	servis_sekil1 = models.ImageField(verbose_name="Service Image: ")
	servis_sekil2 = models.ImageField(verbose_name="Service Image: ")
	servis_sekil3 = models.ImageField(verbose_name="Service Image: ")