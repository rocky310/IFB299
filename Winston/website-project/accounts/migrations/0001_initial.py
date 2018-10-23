# Generated by Django 2.1.1 on 2018-10-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_ID', models.TextField()),
                ('Customer_Name', models.TextField()),
                ('Order_ID', models.TextField()),
                ('Order_CreateDate', models.TextField()),
                ('Order_PickupDate', models.TextField()),
                ('Order_Pickup_Store', models.TextField()),
                ('Pickup_Store_Name', models.TextField()),
                ('Order_ReturnDate', models.TextField()),
                ('Order_ReturnStore', models.TextField()),
                ('Return_Store_Name', models.TextField()),
                ('Car_ID', models.TextField()),
                ('Car_MakeName', models.TextField()),
                ('Car_Model', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_ID', models.TextField()),
                ('Order_CreateDate', models.TextField()),
                ('Order_PickupDate', models.TextField()),
                ('Order_Pickup_Store', models.TextField()),
                ('Pickup_Store_Name', models.TextField()),
                ('Pickup_Store_Address', models.TextField()),
                ('Pickup_Store_Phone', models.TextField()),
                ('Pickup_Store_City', models.TextField()),
                ('Pickup_Store_State_Name', models.TextField()),
                ('Order_ReturnDate', models.TextField()),
                ('Order_ReturnStore', models.TextField()),
                ('Return_Store_Name', models.TextField()),
                ('Return_Store_Address', models.TextField()),
                ('Return_Store_Phone', models.TextField()),
                ('Return_Store_City', models.TextField()),
                ('Return_Store_State', models.TextField()),
                ('Customer_ID', models.TextField()),
                ('Customer_Name', models.TextField()),
                ('Customer_Phone', models.TextField()),
                ('Customer_Addresss', models.TextField()),
                ('Customer_Brithday', models.TextField()),
                ('Customer_Occupation', models.TextField()),
                ('Customer_Gender', models.TextField()),
                ('Car_ID', models.TextField()),
                ('Car_MakeName', models.TextField()),
                ('Car_Model', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_PriceNew', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_StandardTransmission', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('Car_Wheelbase', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Viewcars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_MakeName', models.TextField()),
                ('Car_Series', models.TextField()),
                ('Car_SeriesYear', models.TextField()),
                ('Car_EngineSize', models.TextField()),
                ('Car_FuelSystem', models.TextField()),
                ('Car_TankCapacity', models.TextField()),
                ('Car_Power', models.TextField()),
                ('Car_SeatingCapacity', models.TextField()),
                ('Car_BodyType', models.TextField()),
                ('Car_Drive', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
