from django.db import models


class Division(models.Model):
    english_name=models.CharField(max_length=100)
    bangla_name=models.CharField(max_length=100)
    website=models.URLField()
    serial=models.IntegerField()

    def __str__(self):
        return self.english_name

class District(models.Model):
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    english_name=models.CharField(max_length=100)
    bangla_name=models.CharField(max_length=100)
    latitude=models.CharField(max_length=20)
    longititude=models.CharField(max_length=20)
    website=models.URLField()
    serial=models.IntegerField()

    def __str__(self):
        return self.english_name
        
class Upazila(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    english_name=models.CharField(max_length=100)
    bangla_name=models.CharField(max_length=100)
    website=models.URLField()
    serial=models.IntegerField()


    def __str__(self):
        return self.english_name


class Union(models.Model):
    upazila=models.ForeignKey(Upazila,on_delete=models.CASCADE)
    english_name=models.CharField(max_length=100)
    bangla_name=models.CharField(max_length=100)
    website=models.URLField()
    serial=models.IntegerField()

    def __str__(self):
        return self.english_name

    def district(self):
        return self.upazila.district.english_name

    def division(self):
        return self.upazila.district.division.english_name