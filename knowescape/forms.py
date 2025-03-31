from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)


class LearnerForm(forms.Form):

    disability_choices = (
        ("yes", "yes"),
        ("no", "no")
    )

    first_names = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth"
    )
    home_address = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = PhoneNumberField(required=True, region="ZA")
    disability = forms.ChoiceField(required=True, choices=disability_choices)
    disability_note = forms.FileField(required=False)
    certified_id = forms.FileField(required=True)
    matric_certificate = forms.FileField(required=False)


class CompanyForm(forms.Form):

    smme_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    cipc_reg = forms.IntegerField(required=True)
    operating_years = forms.IntegerField(required=True)
    sars_compliance = forms.CharField(required=True)
    cipc_docs = forms.FileField(required=True)
    company_profile = forms.FileField(required=True)
    bbbee_cert = forms.FileField(required=True)

    # def clean_disability_note(self):
    #     file = self.cleaned_data.get('disability_note')
    #     if file and not file.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
    #         raise ValidationError("Only PDF, JPG, and PNG files are allowed for the doctor's note.")
    #     return file

    # def clean_certified_id(self):
    #     file = self.cleaned_data.get('certified_id')
    #     if file and not file.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
    #         raise ValidationError("Only PDF, JPG, and PNG files are allowed for the certified ID.")
    #     return file

    # def clean_matric_certificate(self):
    #     file = self.cleaned_data.get('matric_certificate')
    #     if file and not file.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
    #         raise ValidationError("Only PDF, JPG, and PNG files are allowed for the matric certificate.")
    #     return file