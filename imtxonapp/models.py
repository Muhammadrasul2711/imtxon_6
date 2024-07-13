from django.db import models

class Companya_foalyati(models.Model):
    cilent_soni=models.CharField(max_length=255)
    qilingan_project_soni=models.CharField(max_length=255)
    ish_foalayti=models.CharField(max_length=255)
    buyurt_malar=models.IntegerField()

    def __str__(self):
        return self.cilent_soni


class Companya_tarixi(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to='media/',blank=True)
    content=models.TextField()
    asoschi=models.TextField(blank=True)
    companiya_disigner=models.CharField(max_length=255,default='Noma’lum')


    def __str__(self):
        return self.title



class Murtojat(models.Model):
    full_name=models.CharField(max_length=255)
    kompanyia_name=models.CharField(max_length=255)
    telefon=models.CharField(max_length=13)
    email=models.CharField(max_length=255)
    murojat=models.TextField(blank=True)
    kompaniy_address=models.CharField(max_length=255)

    def __str__(self):
        return self.murojat


class Img(models.Model):
    img=models.ImageField(upload_to='media')
    title=models.CharField(max_length=255)


def __str__(self):
    return self.title







