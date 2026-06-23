from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Package, Booking, ContactMessage

def home(request):
    packages = Package.objects.all()
    return render(request, 'home.html', {'packages': packages})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
            
    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        package_id = request.POST.get('package')
        travel_date = request.POST.get('date')
        
        if name and email and package_id and travel_date:
            try:
                package = Package.objects.get(id=package_id)
                Booking.objects.create(
                    name=name,
                    email=email,
                    package=package,
                    travel_date=travel_date
                )
                messages.success(request, 'Your booking was successful! We will contact you soon.')
                return redirect('booking')
            except Package.DoesNotExist:
                messages.error(request, 'Selected package does not exist.')
        else:
            messages.error(request, 'Please fill in all fields.')
            
    packages = Package.objects.all()
    return render(request, 'booking.html', {'packages': packages})
