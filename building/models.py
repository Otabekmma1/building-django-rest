from django.db import models

class Hudud(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_company = models.DateField(auto_now_add=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class QurilishBinosi(models.Model):
    qurilish_tashkiloti = models.ForeignKey(QurilishTashkiloti, on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    maydoni = models.FloatField(default=0)
    qavat = models.IntegerField(default=0)
    parkovka = models.IntegerField(default=0)
    lift = models.IntegerField(default=0)

    def __str__(self):
        return self.name


