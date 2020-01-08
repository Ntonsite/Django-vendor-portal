from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendorName          = models.TextField(max_length=200,unique=True,default='some vendor')
    contactPerson       = models.CharField(max_length=200, unique=True, default='someone')
    contactPhone        = models.IntegerField(default=255, unique=True)
    contactEmail        = models.EmailField(max_length=254, unique=True, default='someone@gmail.com')
    locationAddress     = models.TextField(max_length=254, default='some place')
    service             = models.TextField(max_length=200, default='some service')
    def __str__(self):
       return self.vendorName

class Contract(models.Model):
    vendor              = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    contractName        = models.TextField(max_length=200)
    dateRegistered      = models.DateTimeField(auto_now_add=True,blank=True)
    dateExpiry          = models.DateTimeField(blank=False)
    file                = models.FileField(blank=False, upload_to='contracts/')

    def __str__(self):
           return self.contractName

class License(models.Model):
    vendor               = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    licenseName          = models.TextField(max_length=200)
    dateRegistered       = models.DateTimeField(auto_now_add=True,blank=True)
    dateExpiry           = models.DateTimeField(blank=False)
    file                 = models.FileField(blank=False, upload_to='licenses/')

    def __str__(self):
            return self.licenseName
