from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Sphere, CountyHub, Director, SlideshowImage

def index(request):
    """
    Renders the Base Command (Homepage) and Tactical Map.
    Pulls in Sector Spheres and the Hero Slideshow Images.
    """
    spheres = Sphere.objects.all()
    slideshow_images = SlideshowImage.objects.all().order_by('order')
    
    context = {
        'spheres': spheres,
        'slideshow_images': slideshow_images,
    }
    return render(request, 'index.html', context)

def about(request):
    """
    Renders the Mission & Philosophy page.
    """
    return render(request, 'about.html')

def directors(request):
    """
    Renders the Leadership page and pulls in all Director profiles.
    """
    directors_list = Director.objects.all()
    
    context = {
        'directors': directors_list,
    }
    return render(request, 'directors.html', context)

def hub_detail(request, hub_id):
    """
    Renders the specific County Terminal dashboard.
    Fetches a single CountyHub by its ID.
    """
    hub = get_object_or_404(CountyHub, id=hub_id)
    
    context = {
        'hub': hub,
    }
    return render(request, 'hub_detail.html', context)

def register(request):
    """
    Handles new admin/user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Sends user to login page after successful registration
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})