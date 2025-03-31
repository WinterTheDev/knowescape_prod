from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Applicants(models.Model):
    DISABILITY_CHOICES = (
        ("yes", "Yes"),
        ("no", "No")
    )

    first_names = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    home_address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(region="ZA")
    disability = models.CharField(max_length=3, choices=DISABILITY_CHOICES)
    disability_note = models.FileField(upload_to='disability_notes/', blank=True, null=True)
    certified_id = models.FileField(upload_to='certified_ids/')
    matric_certificate = models.FileField(upload_to='matric_certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_names} {self.last_name}"


class Companies(models.Model):

    smme_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cipc_reg = models.IntegerField()
    operating_years = models.IntegerField()
    sars_compliance = models.CharField(max_length=100)
    cipc_docs = models.FileField(upload_to='CIPC_docs/', blank=True, null=True)
    company_profile = models.FileField(upload_to='Company_profile/', blank=True, null=True)
    bbbee_cert = models.FileField(upload_to='BBBEE_certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.smme_name}"