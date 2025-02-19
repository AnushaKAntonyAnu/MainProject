from django.urls import path
from Backend import views

urlpatterns=[
    path('Indexpage/',views.Indexpage,name="Indexpage"),
    path('AllCompliants/',views.AllCompliants,name="AllCompliants"),

    path('AddBrand/',views.AddBrand,name="AddBrand"),
    path('save_brand/',views.save_brand,name="save_brand"),
    path('DisplayBrand/',views.DisplayBrand,name="DisplayBrand"),
    path('EditBrand/<int:Bid>/', views.EditBrand, name="EditBrand"),
    path('Update_Brand/<int:Bid>/', views.Update_Brand, name="Update_Brand"),
    path('DeleteBrand/<int:Bid>/', views.DeleteBrand, name="DeleteBrand"),

    path('AddCategory/', views.AddCategory, name="AddCategory"),
    path('save_category/', views.save_category, name="save_category"),
    path('DisplayCategory/', views.DisplayCategory, name="DisplayCategory"),
    path('EditCategory/<int:Cid>/', views.EditCategory, name="EditCategory"),
    path('Update_Category/<int:Cid>/', views.Update_Category, name="Update_Category"),
    path('DeleteCategory/<int:Cid>/', views.DeleteCategory, name="DeleteCategory"),

    path('AddDistrict/', views.AddDistrict, name="AddDistrict"),
    path('save_district/', views.save_district, name="save_district"),
    path('DeleteDistrict/<int:Did>/', views.DeleteDistrict, name="DeleteDistrict"),

    path('AddPlaces/', views.AddPlaces, name="AddPlaces"),
    path('save_place/', views.save_place, name="save_place"),
    path('DeletePlace/<int:Pid>/', views.DeletePlace, name="DeletePlace"),

    path('RegisterTechnician/', views.RegisterTechnician, name="RegisterTechnician"),
    path('save_technician/', views.save_technician, name="save_technician"),
    path('DisplayTechnician/', views.DisplayTechnician, name="DisplayTechnician"),
    path('EditTechnician/<int:Tid>/', views.EditTechnician, name="EditTechnician"),
    path('Update_Technician/<int:Tid>/', views.Update_Technician, name="Update_Technician"),
    path('DeleteTechnician/<int:Tid>/', views.DeleteTechnician, name="DeleteTechnician"),

    path('save_ewastecollector/', views.save_ewastecollector, name="save_ewastecollector"),
    path('RegisterEwasteCollector/', views.RegisterEwasteCollector, name="RegisterEwasteCollector"),
    path('DisplayEWcollector/', views.DisplayEWcollector, name="DisplayEWcollector"),
    path('EditEWCollector/<int:Eid>/', views.EditEWCollector, name="EditEWCollector"),
    path('Update_EWCollector/<int:Eid>/', views.Update_EWCollector, name="Update_EWCollector"),
    path('DeleteEWCollector/<int:Eid>/', views.DeleteEWCollector, name="DeleteEWCollector"),


    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin/', views.admin, name="admin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('AddYard/', views.AddYard, name="AddYard"),
    path('save_yard/', views.save_yard, name="save_yard"),
    path('DeleteYard/<int:Yid>/', views.DeleteYard, name="DeleteYard"),

    path('AddProductType/', views.AddProductType, name="AddProductType"),
    path('save_Producttype/', views.save_Producttype, name="save_Producttype"),
    path('Deleteproducttype/<int:PDid>/', views.Deleteproducttype, name="Deleteproducttype"),

    path('AddProduct/', views.AddProduct, name="AddProduct"),
    path('save_product/', views.save_product, name="save_product"),
    path('DisplayProduct/', views.DisplayProduct, name="DisplayProduct"),
    path('EditProduct/<int:PRid>/', views.EditProduct, name="EditProduct"),
    path('Update_Product/<int:PRid>/', views.Update_Product, name="Update_Product"),
    path('DeleteProduct/<int:PRid>/', views.DeleteProduct, name="DeleteProduct"),

    path('UserComplaints/', views.UserComplaints, name="UserComplaints"),
    path('AcceptedRepairs/', views.AcceptedRepairs, name="AcceptedRepairs"),
    path('AllocatedRepairs/', views.AllocatedRepairs, name="AllocatedRepairs"),
    path('DeleteComplaint/<int:Did>/', views.DeleteComplaint, name="DeleteComplaint"),

    path('WorkReports/', views.WorkReports, name="WorkReports"),
    path('UpdateReport/<int:Workid>/', views.UpdateReport, name="UpdateReport"),
    path('UpdateComplaint/<int:Workid>/', views.UpdateComplaint, name="UpdateComplaint"),
    path('PaymentList/', views.PaymentList, name="PaymentList"),

]