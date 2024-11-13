from django.shortcuts import render, redirect
from .models import Obituary
from django.utils.text import slugify
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

def submit_obituary(request):
    if request.method == 'POST':
        # Handle the form data and image upload
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = slugify(name)
        
        # Handle the image upload (if present)
        image = request.FILES.get('image')

        # Create the obituary instance
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug,
            image=image  # Save the image if uploaded
        )
        
        # Save the obituary to the database
        obituary.save()

        # Redirect to the view obituaries page
        return HttpResponseRedirect(reverse('view_obituaries'))
    else:
        # If the request is GET, render the submission form
        return render(request, 'obituary_form.html')


def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
