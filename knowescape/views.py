from django.contrib import messages
from django.http import HttpResponse
from .models import Applicants, Companies
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, LearnerForm, CompanyForm


def index(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'page_title': 'Business & Skills Development'
    }

    return render(request, "knowescape/home.html", context)


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'page_title': 'Reach Out'
    }

    return render(request, "knowescape/contact.html", context)


def start_up(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'page_title': 'Start-Up Support'
    }

    return render(request, "knowescape/start-up.html", context)


def es_dev(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'page_title': 'Enterprise & Supplier Development'
    }

    return render(request, "knowescape/es-dev.html", context)


def skills_dev(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            company = request.POST['company']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'Inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'page_title': 'Skills Development'
    }

    return render(request, "knowescape/skills-dev.html", context)


def learner_signup(request):
    if request.method == "POST":
        form = LearnerForm(request.POST, request.FILES)

        if form.is_valid():
            # Check for unique email
            email_address = form.cleaned_data['email']
            if Applicants.objects.filter(email=email_address).exists():
                messages.error(request, "This e-mail is already in use.")
            else:
                # Retrieve data from form
                first_names = form.cleaned_data['first_names']
                last_name = form.cleaned_data['last_name']
                birth_date = form.cleaned_data['birth_date']
                home_address = form.cleaned_data['home_address']
                phone_number = form.cleaned_data['phone_number']
                disability = form.cleaned_data['disability']
                disability_note = form.cleaned_data.get('disability_note')
                certified_id = form.cleaned_data['certified_id']
                matric_certificate = form.cleaned_data.get('matric_certificate')

                # Save applicant to the database
                applicant = Applicants.objects.create(
                    first_names=first_names,
                    last_name=last_name,
                    birth_date=birth_date,
                    home_address=home_address,
                    email=email_address,
                    phone_number=phone_number,
                    disability=disability,
                    disability_note=disability_note,
                    certified_id=certified_id,
                    matric_certificate=matric_certificate
                )

                # Send email confirmation
                try:
                    send_mail(
                        'Skills Development Application',
                        f"""
                        First Names: {first_names}
                        Last Name: {last_name}
                        Date of Birth: {birth_date}
                        Home Address: {home_address}
                        Email Address: {email_address}
                        Disability: {disability}
                        """,
                        email_address,
                        ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                    )
                    messages.success(request, 'Application Received! Check your emails for confirmation!')
                    return redirect('home')
                except BadHeaderError:
                    return HttpResponse('Invalid Header')
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = LearnerForm()

    context = {
        'LearnerForm': form,
        'page_title': 'Skills Development'
    }

    return render(request, "knowescape/learner-signup.html", context)


def company_signup(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Validate unique email
            email = form.cleaned_data['email']
            if Companies.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
            else:
                # Retrieve data from the form
                smme_name = form.cleaned_data['smme_name']
                cipc_reg = form.cleaned_data['cipc_reg']
                operating_years = form.cleaned_data['operating_years']
                sars_compliance = form.cleaned_data['sars_compliance']
                cipc_docs = form.cleaned_data['cipc_docs']
                company_profile = form.cleaned_data['company_profile']
                bbbee_cert = form.cleaned_data['bbbee_cert']
                
                # Save company to the database
                company = Companies.objects.create(
                    smme_name=smme_name,
                    email=email,
                    cipc_reg=cipc_reg,
                    operating_years=operating_years,
                    sars_compliance=sars_compliance,
                    cipc_docs=cipc_docs,
                    company_profile=company_profile,
                    bbbee_cert=bbbee_cert
                )
                
                # Send email confirmation (optional)
                try:
                    send_mail(
                        'Company Registration Confirmation',
                        f"""
                        Thank you for registering with us!
                        Company Name: {smme_name}
                        CIPC Registration: {cipc_reg}
                        Operating Years: {operating_years}
                        SARS Compliance: {sars_compliance}
                        """,
                        ['rhulanimogotsi@gmail.com', 'info@knowescape.co.za']
                    )
                    messages.success(request, 'Registration successful! Check your email for confirmation.')
                    return redirect('home')
                except BadHeaderError:
                    return HttpResponse('Invalid header found in the email.')
        else:
            messages.error(request, form.errors.as_text())    
    else:
        form = CompanyForm()

    context = {
        'CompanyForm': form,
        'page_title': 'Company Registration'
    }

    return render(request, "knowescape/company-signup.html", context)