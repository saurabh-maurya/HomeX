from django.db import  models
from django.utils.translation import gettext_lazy as _
from django import forms

class ApplianceStatus(models.Model):
    CHOICE = (
        ('OFF','OFF'),
        ('ON','ON')
    )
    user_id = models.AutoField(primary_key = True)
    email_add = models.EmailField(blank=False)
    f_name = models.CharField(max_length=20)
    fan = models.CharField(max_length=3,choices=CHOICE)
    light = models.CharField(max_length=3, choices=CHOICE)
    motor = models.CharField(max_length=3, choices=CHOICE)
    class Meta:
        verbose_name_plural = "Appliance Status"

    def __str__(self):
        return self.f_name

