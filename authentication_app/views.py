from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import (
    messages,
)  # Import the messages module for displaying messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from contact.models import ContactSubmission


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            messages.success(
                request, "Account created successfully."
            )  # Display a success message
            return redirect("registration/login")  # Redirect to the login page
        else:
            # If the form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")

    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def visualization_view(request):
    # Fetch data for visualizations
    location_data = ContactSubmission.objects.values("location").annotate(
        count=Count("location")
    )
    age_data = ContactSubmission.objects.values("age").annotate(count=Count("age"))

    location_labels = [entry["location"] for entry in location_data]
    location_counts = [entry["count"] for entry in location_data]

    age_labels = [entry["age"] for entry in age_data]
    age_counts = [entry["count"] for entry in age_data]

    data = {
        "location_labels": location_labels,
        "location_counts": location_counts,
        "age_labels": age_labels,
        "age_counts": age_counts,
    }

    return render(request, "registration/visualization.html", {"data": data})
