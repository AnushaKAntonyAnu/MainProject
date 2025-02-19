from django.db import models

# Create your models here.
class BrandDB(models.Model):
    Brand_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=300,null=True,blank=True)
    Brand_Image=models.ImageField(upload_to="Brand Images",null=True,blank=True)

class CategoryDB(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=300,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="Category Images",null=True,blank=True)

class DistrictDB(models.Model):
    District_Name=models.CharField(max_length=100,null=True,blank=True)

class PlaceDB(models.Model):
    Place_Name=models.CharField(max_length=100,null=True,blank=True)
    District=models.CharField(max_length=100,null=True,blank=True)

class TechnicianDB(models.Model):
    Technician_name=models.CharField(max_length=100,null=True,blank=True)
    Technician_gender=models.CharField(max_length=100,null=True,blank=True)
    Technician_Contact=models.IntegerField(null=True,blank=True)
    Technician_email=models.EmailField(max_length=100,null=True,blank=True)
    Technician_password=models.CharField(max_length=100,null=True,blank=True)
    Technician_Image=models.ImageField(upload_to="Technician Images",null=True,blank=True)
    Technician_skill=models.CharField(max_length=100,null=True,blank=True)
    Technician_experience=models.CharField(max_length=100,null=True,blank=True)
    Technician_address=models.CharField(max_length=500,null=True,blank=True)

class EWasteCollectorDB(models.Model):
    EWCollector_name=models.CharField(max_length=100,null=True,blank=True)
    EWCollector_gender=models.CharField(max_length=100,null=True,blank=True)
    EWCollector_Contact=models.IntegerField(null=True,blank=True)
    EWCollector_email=models.EmailField(max_length=100,null=True,blank=True)
    EWCollector_password=models.CharField(max_length=100,null=True,blank=True)
    EWCollector_Image=models.ImageField(upload_to="EWCollector Images",null=True,blank=True)
    EWCollector_DL=models.ImageField(upload_to="EWCollector Images",null=True,blank=True)
    EWCollector_Vehicleno=models.CharField(max_length=100,null=True,blank=True)
    EWCollector_modelname=models.CharField(max_length=100,null=True,blank=True)
    EWCollector_vehicleimage=models.ImageField(upload_to="EWCollector Images",null=True,blank=True)



class YardDB(models.Model):
    Yard_Name=models.CharField(max_length=100,null=True,blank=True)

class ProductTypeDB(models.Model):
    Pdtype_Name=models.CharField(max_length=100,null=True,blank=True)


class ProductDB(models.Model):
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Product_type=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=300,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Product Images",null=True,blank=True)


