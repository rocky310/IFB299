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

    def __str__(self):
        return self.Customer_ID


class HistoryInfo(models.Model):
    Order_ID = models.TextField()
    Order_CreateDate = models.TextField()
    Order_PickupDate = models.TextField()
    Order_Pickup_Store = models.TextField()
    Pickup_Store_Name = models.TextField()
    Pickup_Store_Address = models.TextField()
    Pickup_Store_Phone = models.TextField()
    Pickup_Store_City = models.TextField()
    Pickup_Store_State_Name = models.TextField()
    Order_ReturnDate = models.TextField()
    Order_ReturnStore = models.TextField()
    Return_Store_Name = models.TextField()
    Return_Store_Address = models.TextField()
    Return_Store_Phone = models.TextField()
    Return_Store_City = models.TextField()
    Return_Store_State = models.TextField()
    Customer_ID = models.TextField()
    Customer_Name = models.TextField()
    Customer_Phone = models.TextField()
    Customer_Addresss = models.TextField()
    Customer_Brithday = models.TextField()
    Customer_Occupation = models.TextField()
    Customer_Gender = models.TextField()
    Car_ID = models.TextField()
    Car_MakeName = models.TextField()
    Car_Model = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_PriceNew = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_StandardTransmission = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    Car_Wheelbase = models.TextField()

class Viewcars(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName


class Audi(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName

class Hyundai(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName

class Toyota(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName

class Mitsubishi(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName

class Kia(models.Model):
    Car_MakeName = models.TextField()
    Car_Series = models.TextField()
    Car_SeriesYear = models.TextField()
    Car_EngineSize = models.TextField()
    Car_FuelSystem = models.TextField()
    Car_TankCapacity = models.TextField()
    Car_Power = models.TextField()
    Car_SeatingCapacity = models.TextField()
    Car_BodyType = models.TextField()
    Car_Drive = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.Car_MakeName


