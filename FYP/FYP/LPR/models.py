from django.urls import reverse
from django.db import models
from django.core.validators import RegexValidator
from django_resized import ResizedImageField

nameValidator = RegexValidator("^[a-zA-Z ]+$", "Name must only contain characters")
unitValidator = RegexValidator("^\d-\d{1,2}-\d$", "Unit number must match X-XX-X where X is number")
plateNumValidator = RegexValidator("^[A-Z]{1,3}[0-9]{1,4}[A-Za-z]{0,2}$", "License Plate Number should follow the format (PPP1234) no spaces required")

# Create your models here.
class Owner(models.Model):
    """Model representing owners"""
    name = models.CharField(max_length=100, help_text="Enter Resident's name (e.g. Tan Soon Lee)", validators=[nameValidator])
    unit = models.CharField(max_length=10, help_text="Enter Resident's unit number (e.g. 2-12-1)", validators=[unitValidator])

    # Sort by unit
    class Meta:
        ordering = ['unit']

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular owner instance"""
        return reverse('owner-detail', args=[str(self.id)])


class Vehicle(models.Model):
    """Model representing Vehicle"""
    brand = models.CharField(max_length=50, help_text="Enter vehicle's brand (e.g. Honda)")
    model = models.CharField(max_length=50, help_text="Enter vehicle's model (e.g. Civic)")
    colour = models.CharField(max_length=20, help_text="Enter vehicle colour (e.g. Blue)")
    plateNum = models.CharField('License Plate Number', max_length=10, help_text="Enter license plate number (e.g. PPP1234)", unique=True, validators=[plateNumValidator])
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        ordering = ['brand']

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.brand} {self.model}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this vehicle"""
        return reverse('vehicle-detail', args=[str(self.id)])

class OwnerEnterDateTime(models.Model):
    """Model representing owner vehicle enter date time"""
    dateTime = models.DateTimeField()
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.vehicle.plateNum}'

class VisitorEnterDateTime(models.Model):
    """Model representing owner vehicle enter date time"""
    dateTime = models.DateTimeField(auto_now_add=True, blank=True)
    exitDateTime = models.DateTimeField(blank=True, null=True)
    visitor = models.ForeignKey('Visitor', on_delete=models.CASCADE)
    Balance = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)


    def __str__(self):
        """String for representing the Model object"""
        return f'{self.visitor.visitorPlateNum}'

class Visitor(models.Model):
    """Model representing Visitors"""
    name = models.CharField(max_length=100, help_text="Enter name (e.g. Tan Ah Lee)", validators=[nameValidator])
    visitUnit = models.CharField('Visited Unit', max_length=10, help_text="Enter visited unit (e.g. 2-14-2)", validators=[unitValidator])
    email = models.EmailField('Email',max_length=254,help_text="Enter Your Email",default='')
    visitorPlateNum = models.CharField('License Plate Number', max_length=10, help_text="Enter vehicle's license plate number (e.g. PPP1234)", unique=True, validators=[plateNumValidator])

    class Meta:
        ordering = ['visitUnit']

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this vehicle"""
        return reverse('visitor-detail', args=[str(self.id)])

class Image(models.Model):
    image = ResizedImageField(size=[200,200], upload_to='images', force_format = 'png')

