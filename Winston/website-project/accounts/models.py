from django.db import models


class CarInfo(models.Model):
    Customer_ID = models.TextField()
    Customer_Name = models.TextField()
    Order_ID = models.TextField()
    Order_CreateDate = models.TextField()
    Order_PickupDate = models.TextField()
    Order_Pickup_Store = models.TextField()
    Pickup_Store_Name = models.TextField()
    Order_ReturnDate = models.TextField()
    Order_ReturnStore = models.TextField()
    Return_Store_Name = models.TextField()
    Car_ID = models.TextField()
    Car_MakeName = models.TextField()
    Car_Model = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
