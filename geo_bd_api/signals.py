import csv 
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *
from tqdm import tqdm


@receiver(post_migrate)
def create_division(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    folder="geo_bd_api/data/"
    if sender.name=="geo_bd_api":
        agree=input("Do you want to genarate Division/District/Upazila/Union Data,default=NO. TYPE Y/N or YES/NO? ")
        if agree=="Y" or agree=="YES" or agree=="y" or agree=="yes":
            with open(f"{folder}divisions.csv","r",encoding="utf-8") as f:
                print("Divistion creating...")
                csv_list=[l for l in f]
                for i in tqdm(csv.reader(csv_list),total=len(csv_list)):
                    Division.objects.get_or_create(
                        id=int(i[0]),
                        english_name=i[1],
                        bangla_name=i[2],
                        website=i[3],
                        serial=i[0]
                        )
                print("✔ Done")
            with open(f"{folder}districts.csv","r",encoding="utf-8") as f:
                print("District creating...")
                csv_list=[l for l in f]
                for i in tqdm(csv.reader(csv_list),total=len(csv_list)):
                    District.objects.get_or_create(
                        id=int(i[0]),
                        division=Division.objects.get(id=int(i[1])),
                        english_name=i[2],
                        bangla_name=i[3],
                        latitude=i[4],
                        longititude=i[5],
                        website=i[6],
                        serial=i[0]
                        )
                print("✔ Done")
            with open(f"{folder}upazilas.csv","r",encoding="utf-8") as f:
                print("Upazila creating...")
                csv_list=[l for l in f]
                for i in tqdm(csv.reader(csv_list),total=len(csv_list)):
                    Upazila.objects.get_or_create(
                        id=int(i[0]),
                        district=District.objects.get(id=int(i[1])),
                        english_name=i[2],
                        bangla_name=i[3],
                        website=i[4],
                        serial=i[0]
                        )
                print("✔ Done")
            with open(f"{folder}unions.csv","r",encoding="utf-8") as f:
        
                print("Union creating...")
                csv_list=[l for l in f]
                for i in tqdm(csv.reader(csv_list),total=len(csv_list)):
                    Union.objects.get_or_create(
                        id=int(i[0]),
                        upazila=Upazila.objects.get(id=int(i[1])),
                        english_name=i[2],
                        bangla_name=i[3],
                        website=i[4],
                        serial=i[0]
                        )

            with open(f"{folder}upazilas.csv","r",encoding="utf-8") as f:
                csvfile=csv.reader(f)
                for i in csvfile:
                    Upazila.objects.get_or_create(
                        id=int(i[0]),
                        district=District.objects.get(id=int(i[1])),
                        english_name=i[2],
                        bangla_name=i[3],
                        website=i[4],
                        serial=i[0]
                        )
                print("✔ Done")