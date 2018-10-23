from django import forms
from .models import CarInfo
from .models import Viewcars


class ListForm(forms.ModelForm):
	class Meta:
		model = CarInfo
		fields= ["Customer_ID", "Customer_Name", "Order_ID", "Order_CreateDate", "Order_PickupDate", "Order_Pickup_Store", "Pickup_Store_Name", "Order_ReturnDate", "Order_ReturnStore", "Return_Store_Name", "Car_ID", "Car_MakeName", "Car_Model", "Car_Series", "Car_SeriesYear"]


class ListForm1(forms.ModelForm):
	class Meta:
		model = Viewcars
		fields = ["Car_MakeName", "Car_Series", "Car_SeriesYear", "Car_EngineSize", "Car_FuelSystem", "Car_TankCapacity", "Car_Power", "Car_SeatingCapacity", "Car_BodyType", "Car_Drive", "image"]