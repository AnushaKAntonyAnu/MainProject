from django.shortcuts import render,redirect
from Backend.models import BrandDB,CategoryDB,DistrictDB,PlaceDB,TechnicianDB,EWasteCollectorDB,YardDB,ProductTypeDB,ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Frontend.models import ComplaintDB,ReportDB,PaymentDb



# Create your views here.
def Indexpage(req):
    return render(req,"index.html")

def AllCompliants(req):
    data=ComplaintDB.objects.all()
    return render(req,"AllCompliants.html",{'data':data})

#Add Brand
def AddBrand(req):
    return render(req,"AddBrand.html")

#Saving Brand to Database

def save_brand(req):
    if req.method=="POST":
        a=req.POST.get('Brand_Name')
        b=req.POST.get('Description')
        Img=req.FILES['Brand_Image']
        obj=BrandDB(Brand_Name=a,Description=b,Brand_Image=Img)
        obj.save()
        messages.success(req,"Brand added sucessfully..!")
        return redirect(AddBrand)

#Display Brand Details

def DisplayBrand(req):
    data=BrandDB.objects.all()
    return render(req,"DisplayBrand.html",{'data':data})


#Edit Brand Details

def EditBrand(req,Bid):
    data = BrandDB.objects.get(id=Bid)
    return render(req,"EditBrand.html",{'data':data})


#Update Brand Details

def Update_Brand(req,Bid):
    if req.method == "POST":
        a = req.POST.get('Brand_Name')
        b = req.POST.get('Description')
        try:
            Img = req.FILES['Brand_Image']
            fs = FileSystemStorage()
            file = fs.save(Img.name, Img)
        except MultiValueDictKeyError:
            file = BrandDB.objects.get(id=Bid).Brand_Image
        BrandDB.objects.filter(id=Bid).update(Brand_Name=a,Description=b,Brand_Image=file)
        messages.success(req,"Brand Edited sucessfully..!")
        return redirect(DisplayBrand)

#Delete Brand
def DeleteBrand(req,Bid):
    data = BrandDB.objects.filter(id=Bid)
    data.delete()
    messages.error(req,"Brand Deleted..!")
    return redirect(DisplayBrand)


# Category Details
def AddCategory(req):
    return render(req,"AddCategory.html")


def save_category(req):
    if req.method=="POST":
        a=req.POST.get('Category_Name')
        b=req.POST.get('Description')
        Img=req.FILES['Category_Image']
        obj=CategoryDB(Category_Name=a,Description=b,Category_Image=Img)
        obj.save()
        messages.success(req,"Category added sucessfully..!")
        return redirect(AddCategory)


#Display Brand Details

def DisplayCategory(req):
    data=CategoryDB.objects.all()
    return render(req,"DisplayCategory.html",{'data':data})

#Edit Brand Details

def EditCategory(req,Cid):
    data = CategoryDB.objects.get(id=Cid)
    return render(req,"EditCategory.html",{'data':data})


#Update Brand Details

def Update_Category(req,Cid):
    if req.method == "POST":
        a = req.POST.get('Category_Name')
        b = req.POST.get('Description')
        try:
            Img = req.FILES['Category_Image']
            fs = FileSystemStorage()
            file = fs.save(Img.name, Img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=Cid).Category_Image
        CategoryDB.objects.filter(id=Cid).update(Category_Name=a,Description=b,Category_Image=file)
        messages.success(req,"Category Edited sucessfully..!")
        return redirect(DisplayCategory)

#Delete Brand
def DeleteCategory(req,Cid):
    data = CategoryDB.objects.filter(id=Cid)
    data.delete()
    messages.error(req,"Category Deleted..!")
    return redirect(DisplayCategory)


#Add district

def AddDistrict(req):
    data=DistrictDB.objects.all()
    return render(req,"AddDistrict.html",{'data':data})

def save_district(req):
    if req.method=="POST":
        a=req.POST.get('District_Name')
        obj=DistrictDB(District_Name=a)
        obj.save()
        messages.success(req,"District added sucessfully..!")
        return redirect(AddDistrict)

def DeleteDistrict(req,Did):
    data = DistrictDB.objects.filter(id=Did)
    data.delete()
    messages.error(req,"District Deleted..!")
    return redirect(AddDistrict)


def AddPlaces(req):
    district=DistrictDB.objects.all()
    data=PlaceDB.objects.all()
    return render(req,"AddPlaces.html",{'data':data,'district':district})

def save_place(req):
    if req.method=="POST":
        a=req.POST.get('District')
        b=req.POST.get('Place_Name')
        obj=PlaceDB(District=a,Place_Name=b)
        obj.save()
        messages.success(req,"Place added sucessfully..!")
        return redirect(AddPlaces)

def DeletePlace(req,Pid):
    data = PlaceDB.objects.filter(id=Pid)
    data.delete()
    messages.error(req,"Place Deleted..!")
    return redirect(AddPlaces)


 #Add Technician
def RegisterTechnician(req):
    data=CategoryDB.objects.all()
    return render(req,"RegisterTechnician.html",{'data':data})


def save_technician(req):
    if req.method=="POST":
        a=req.POST.get('Technician_name')
        b=req.POST.get('Technician_gender')
        c=req.POST.get('Technician_Contact')
        d=req.POST.get('Technician_email')
        e=req.POST.get('Technician_password')
        f=req.POST.get('Technician_skill')
        g=req.POST.get('Technician_experience')
        h=req.POST.get('Technician_address')
        Img=req.FILES['Technician_Image']
        obj=TechnicianDB(Technician_name=a,Technician_gender=b,Technician_Contact=c,Technician_email=d,Technician_password=e,Technician_skill=f,Technician_experience=g,Technician_address=h,Technician_Image=Img)
        obj.save()
        messages.success(req,"Technician Registered sucessfully..!")
        return redirect(RegisterTechnician)



def DisplayTechnician(req):
    data=TechnicianDB.objects.all()
    return render(req,"DisplayTechnician.html",{'data':data})


def EditTechnician(req,Tid):
    data = CategoryDB.objects.all()
    Tech = TechnicianDB.objects.get(id=Tid)
    return render(req,"EditTechnician.html",{'data':data,'Tech':Tech})


def Update_Technician(req,Tid):
    if req.method == "POST":
        a = req.POST.get('Technician_name')
        b = req.POST.get('Technician_gender')
        c = req.POST.get('Technician_Contact')
        d = req.POST.get('Technician_email')
        e = req.POST.get('Technician_password')
        f = req.POST.get('Technician_skill')
        g = req.POST.get('Technician_experience')
        h = req.POST.get('Technician_address')
        try:
            Img = req.FILES['Technician_Image']
            fs = FileSystemStorage()
            file = fs.save(Img.name, Img)
        except MultiValueDictKeyError:
            file = TechnicianDB.objects.get(id=Tid).Technician_Image
        TechnicianDB.objects.filter(id=Tid).update(Technician_name=a,Technician_gender=b,Technician_Contact=c,Technician_email=d,Technician_password=e,Technician_skill=f,Technician_experience=g,Technician_address=h,Technician_Image=file)
        messages.success(req, "Technician Edited sucessfully..!")
        return redirect(DisplayTechnician)


def DeleteTechnician(req,Tid):
    data = TechnicianDB.objects.filter(id=Tid)
    data.delete()
    messages.error(req,"Technician Deleted..!")
    return redirect(DisplayTechnician)

#Ewaste Collector

def RegisterEwasteCollector(req):
    return render(req,"RegisterEwasteCollector.html")


def save_ewastecollector(req):
    if req.method=="POST":
        a=req.POST.get('EWCollector_name')
        b=req.POST.get('EWCollector_gender')
        c=req.POST.get('EWCollector_Contact')
        d=req.POST.get('EWCollector_email')
        e=req.POST.get('EWCollector_password')
        f=req.POST.get('EWCollector_Vehicleno')
        g=req.POST.get('EWCollector_modelname')
        Img1=req.FILES['EWCollector_Image']
        Img2=req.FILES['EWCollector_DL']
        Img3=req.FILES['EWCollector_vehicleimage']
        obj=EWasteCollectorDB(EWCollector_name=a,EWCollector_gender=b,EWCollector_Contact=c,EWCollector_email=d,EWCollector_password=e,EWCollector_Vehicleno=f,EWCollector_modelname=g,EWCollector_Image=Img1,EWCollector_DL=Img2,EWCollector_vehicleimage=Img3)
        obj.save()
        messages.success(req,"Ewaste-Collector Registered sucessfully..!")
        return redirect(RegisterEwasteCollector)


def DisplayEWcollector(req):
    data=EWasteCollectorDB.objects.all()
    return render(req,"DisplayEWcollector.html",{'data':data})


def EditEWCollector(req,Eid):
    data = EWasteCollectorDB.objects.get(id=Eid)
    return render(req,"EditEWCollector.html",{'data':data})



def Update_EWCollector(req,Eid):
    if req.method == "POST":
        a = req.POST.get('EWCollector_name')
        b = req.POST.get('EWCollector_gender')
        c = req.POST.get('EWCollector_Contact')
        d = req.POST.get('EWCollector_email')
        e = req.POST.get('EWCollector_password')
        f = req.POST.get('EWCollector_Vehicleno')
        g = req.POST.get('EWCollector_modelname')
        try:
            Img1 = req.FILES['EWCollector_Image']
            Img2 = req.FILES['EWCollector_DL']
            Img3 = req.FILES['EWCollector_vehicleimage']
            fs = FileSystemStorage()
            file1 = fs.save(Img1.name, Img1)
            file2 = fs.save(Img2.name,Img2)
            file3 = fs.save(Img3.name,Img3)
        except MultiValueDictKeyError:
            file1 = EWasteCollectorDB.objects.get(id=Eid).EWCollector_Image
            file2 = EWasteCollectorDB.objects.get(id=Eid).EWCollector_DL
            file3 = EWasteCollectorDB.objects.get(id=Eid).EWCollector_vehicleimage
        EWasteCollectorDB.objects.filter(id=Eid).update(EWCollector_name=a,EWCollector_gender=b,EWCollector_Contact=c,EWCollector_email=d,EWCollector_password=e,EWCollector_Vehicleno=f,EWCollector_modelname=g,EWCollector_Image=file1,EWCollector_DL=file2,EWCollector_vehicleimage=file3)
        messages.success(req, "Ewaste Collector Edited sucessfully..!")
        return redirect(DisplayEWcollector)



def DeleteEWCollector(req,Eid):
    data = EWasteCollectorDB.objects.filter(id=Eid)
    data.delete()
    messages.error(req,"E-Waste Collector Deleted..!")
    return redirect(DisplayEWcollector)


#Admin Login



def adminlogin(req):
    return render(req,"Adminlogin.html")

def admin(req):
    if req.method=="POST":
        a=req.POST.get('username')
        b=req.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a,password=b)
            if x is not None:
                login(req,x)
                req.session['username']=a
                req.session['password']=b
                messages.success(req,"Welcome ")
                return redirect(Indexpage)
            else:
                messages.warning(req,"Invalid username or password")
                return redirect(adminlogin)
        else:
            messages.warning(req, "User not found ")
            return redirect(adminlogin)


def admin_logout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"Logged Out Successfully ")
    return redirect(adminlogin)


#Yard Details


def AddYard(req):
    data=YardDB.objects.all()
    return render(req,"AddYard.html",{'data':data})

def save_yard(req):
    if req.method=="POST":
        a=req.POST.get('Yard_Name')
        obj=YardDB(Yard_Name=a)
        obj.save()
        messages.success(req,"Yard_Name added sucessfully..!")
        return redirect(AddYard)

def DeleteYard(req,Yid):
    data = YardDB.objects.filter(id=Yid)
    data.delete()
    messages.error(req,"Yard Deleted..!")
    return redirect(AddYard)



#PrroductType

def AddProductType(req):
    data=ProductTypeDB.objects.all()
    return render(req,"AddProductType.html",{'data':data})

def save_Producttype(req):
    if req.method=="POST":
        a=req.POST.get('Pdtype_Name')
        obj=ProductTypeDB(Pdtype_Name=a)
        obj.save()
        messages.success(req,"Product Type added sucessfully..!")
        return redirect(AddProductType)

def Deleteproducttype(req,PDid):
    data = ProductTypeDB.objects.filter(id=PDid)
    data.delete()
    messages.error(req,"Product Type Deleted..!")
    return redirect(AddProductType)


#Add Product

def AddProduct(req):
    type=ProductTypeDB.objects.all()
    return render(req,"AddProduct.html",{'type':type})

def save_product(req):
    if req.method=="POST":
        a=req.POST.get('Product_Name')
        b=req.POST.get('Description')
        c=req.POST.get('Product_type')
        Img=req.FILES['Product_Image']
        obj=ProductDB(Product_Name=a,Description=b,Product_type=c,Product_Image=Img)
        obj.save()
        messages.success(req,"Product added sucessfully..!")
        return redirect(AddProduct)


def DisplayProduct(req):
    data=ProductDB.objects.all()
    return render(req,"DisplayProduct.html",{'data':data})


def EditProduct(req,PRid):
    type=ProductTypeDB.objects.all()
    data = ProductDB.objects.get(id=PRid)
    return render(req,"EditProduct.html",{'data':data,'type':type})


def Update_Product(req,PRid):
    if req.method == "POST":
        a = req.POST.get('Product_Name')
        b = req.POST.get('Description')
        c = req.POST.get('Product_type')
        try:
            Img = req.FILES['Product_Image']
            fs = FileSystemStorage()
            file = fs.save(Img.name, Img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=PRid).Product_Image
        ProductDB.objects.filter(id=PRid).update(Product_Name=a,Description=b,Product_type=c,Product_Image=file)
        messages.success(req,"Product Edited sucessfully..!")
        return redirect(DisplayProduct)

def DeleteProduct(req,PRid):
    data = ProductDB.objects.filter(id=PRid)
    data.delete()
    messages.error(req,"Product Deleted..!")
    return redirect(DisplayProduct)



def UserComplaints(req):
    data=ComplaintDB.objects.filter(Cstatus='0')
    Tech=TechnicianDB.objects.all()
    if req.method == 'POST':
        Complaint_id = req.POST.get('Complaint_id')
        Cstatus = req.POST.get('Cstatus')
        if Cstatus == '1':
            ComplaintDB.objects.filter(id=Complaint_id).update(Cstatus='1')
        elif Cstatus == '2':
            ComplaintDB.objects.filter(id=Complaint_id).update(Cstatus='2')
    return render(req,"UserComplaints.html",{'data':data,'Tech':Tech})


def DeleteComplaint(req,Did):
    data = ComplaintDB.objects.filter(id=Did)
    data.delete()
    messages.error(req,"Complaint Deleted..!")
    return redirect(UserComplaints)



def AcceptedRepairs(req):
    data=ComplaintDB.objects.filter(Cstatus='1')
    Tech=TechnicianDB.objects.all()
    if req.method == 'POST':
        Complaint_id = req.POST.get('Complaint_id')
        CTech = req.POST.get('CTech')
        ComplaintDB.objects.filter(id=Complaint_id).update(CTech=CTech)
    return render(req,"AcceptedRepairs.html",{'data':data,'Tech':Tech})




def AllocatedRepairs(req):
    data=ComplaintDB.objects.filter(Cstatus='1')
    return render(req,"AllocatedRepairs.html",{'data':data})

def WorkReports(req):
    Report=ComplaintDB.objects.filter(Cstatus='5')
    return render(req,"WorkReports.html",{'Report':Report})


def UpdateReport(req,Workid):
    Work=ComplaintDB.objects.get(id=Workid)
    return render(req,"UpdateReport.html",{'Work':Work})


def UpdateComplaint(req,Workid):
    a = req.POST.get('CTech')
    b = req.POST.get('Cusername')
    c = req.POST.get('CBrand')
    d = req.POST.get('CProduct')
    e = req.POST.get('CComplaint')
    f = req.POST.get('CAddress')
    g = req.POST.get('CEmail')
    h = req.POST.get('CPhone')
    i = req.POST.get('CReport')
    j = req.POST.get('Ccharge')
    ComplaintDB.objects.filter(id=Workid).update(CTech=a, Cusername=b, CBrand=c, CProduct=d, CComplaint=e, CAddress=f,CEmail=g, CPhone=h, CReport=i, Ccharge=j)
    messages.success(req, "Complaint Updated..!")
    return redirect(WorkReports)


def PaymentList(req):
    data=PaymentDb.objects.all()
    return render(req,"PaymentList.html",{'data':data})



