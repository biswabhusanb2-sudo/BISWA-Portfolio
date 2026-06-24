from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Direct URL to an image for this package")
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    travel_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.package.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
