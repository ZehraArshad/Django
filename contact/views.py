from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import ContactSubmission  # Import the ContactSubmission model
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        age = request.POST["age"]  # Get age from form data
        location = request.POST["location"]  # Get location from form data

        # Save the submission to the database
        submission = ContactSubmission(
            message_name=message_name,
            message_email=message_email,
            message=message,
            age=age,  # Save age
            location=location,  # Save location
        )
        submission.save()

        # Send email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ["zehraarshadmulla@gmail.com"],  # to email
        )

        return render(request, "index.html", {"message_name": message_name})
    else:
        return render(request, "index.html", {})
