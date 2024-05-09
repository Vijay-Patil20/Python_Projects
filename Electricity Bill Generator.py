#Imported Libraries
import pandas as pd
import pdfkit
import os
from PIL import Image,ImageDraw,ImageFont
from datetime import date ,timedelta
import time
import pywhatkit

#Read the CSV file containing user data
Data=pd.read_csv(r"D:\Vijay Pc\Python\Electrcity_Bill_Project\User_Database.csv")#Used Csv Format because in excel the numbers is converted in 10's power

#Take Meter Number as input
Meter_No=int(input("Enter your meter no: "))

# Find the corresponding user data for the given Meter Number
for i in Data.index[0:]:
    if (Meter_No) == Data.Meter_Number[i]:
        break
        
# Update current reading input in the data     
Data.Cur_Reading.loc[(i)]=int(input("Enter Current Reading : "))# Loc Is used for Reading #Curent reading input

# Calculate units consumed in this billing cycle
units=int(int(Data.Cur_Reading[i])-int(Data.Prev_Reading[i]))

#Programe Specific variable 
Fix_charge=30
Fuel_charge=2*units

# Calculate energy charge based on the units consumed
if units<=50:
    Energy_Charge=units*3.05
elif units>50 and units<150:
    Energy_Charge=units*3.50
elif units>=150 and units<250:
    Energy_Charge=units*4.15
else:
     Energy_Charge=units*5.20 

# Update current units in the data
Data.Cur_Units.loc[i]=units

# Calculate tax on the total charge 
Tax= .15*(Energy_Charge+Fuel_charge+Fix_charge)
# Calculate total amount to be paid
Total_Charge= Fix_charge+ Energy_Charge + Fuel_charge + Tax
# Read the electricity bill template from a CSV file
e=pd.read_csv(r"D:\Vijay Pc\Python\Electrcity_Bill_Project\Electricity.csv")#Used Csv Format becase in excel the numbers is converted in 10's power

# Update placeholders in the bill template with user data and billing details
e.loc[1,2]=Data.Name[i]
e.loc[2,2]=Data.Address[i]
e.loc[3,2]=Data.Customer_Number[i]
e.loc[4,2]=Data.Meter_Number[i]
e.loc[5,2]=Data.Cur_Reading[i]
e.loc[6,2]=Data.Prev_Reading[i]
e.loc[7,2]=Data.Cur_Units[i]
e.loc[8,2]=Total_Charge

text=e.loc[1,2]
# Load the bill template image
im=r'D:\Vijay Pc\Python\Electrcity_Bill_Project\Bill.png'
image = Image.open(im) 
d=ImageDraw.Draw(image)
font = ImageFont.truetype("C:\Windows\Fonts\Cambria\cambriab.ttf", 35)
d.text((100,400),text,fill=(0,0,0),font=font,align ="center")      #Name


d.text((100,450),e.loc[2,2],fill=(0,0,0),font=font,align ="center")#Address

d.text((100,500),"Village :",fill=(0,0,0),font=font,align ="center")#Village
d.text((250,500),str(Data.Village[i]),fill=(0,0,0),font=font,align ="center")

d.text((100,550),"District :",fill=(0,0,0),font=font,align ="center")#District
d.text((250,550),str(Data.District[i]),fill=(0,0,0),font=font,align ="center")

d.text((100,650),"Consumer Number :",fill=(0,0,0),font=font,align ="center")#Consumer number
d.text((440,650),str(e.loc[3,2]),fill=(0,0,0),font=font,align ="center")

d.text((100,700),"Meter No :",fill=(0,0,0),font=font,align ="center") # Meter Nummber 
d.text((440,700),str(e.loc[4,2]),fill=(0,0,0),font=font,align ="center")

d.text((1500,650),"Bill Date :",fill=(0,0,0),font=font,align ="center") # Bill Date 
d.text((1920,650),str(date.today()),fill=(0,0,0),font=font,align ="center")

d.text((1500,700),"Bill Amount Rs :",fill=(0,0,0),font=font,align ="center")  # Bill Amount Rs
d.text((1920,700),str(e.loc[8,2]),fill=(0,0,0),font=font,align ="center")

d.text((1500,750),"Due Date :",fill=(0,0,0),font=font,align ="center") # Due Date
d.text((1920,750),str(date.today()+timedelta(days=15)),fill=(0,0,0),font=font,align ="center")

d.text((1500,800),"If Payed After Due Date :",fill=(0,0,0),font=font,align ="center")  # After Due date
d.text((1920,800),str(e.loc[8,2]+30),fill=(0,0,0),font=font,align ="center")

d.text((100,870),"Mobile Number :",fill=(0,0,0),font=font,align ="center")  # Mobile No.
d.text((480,870),str(Data.Mobile_No[i]),fill=(0,0,0),font=font,align ="center")

d.text((100,920),"Current Reading :",fill=(0,0,0),font=font,align ="center")#Current Reading
d.text((480,920),str(e.loc[5,2]),fill=(0,0,0),font=font,align ="center")

d.text((100,1020),"Current Units :",fill=(0,0,0),font=font,align ="center")#Current Unit
d.text((480,1020),str(Data.Cur_Units[i]),fill=(0,0,0),font=font,align ="center")

d.text((100,970),"Previous Reding :",fill=(0,0,0),font=font,align ="center") #Previous Reading 
d.text((480,970),str(e.loc[6,2]),fill=(0,0,0),font=font,align ="center")

d.text((100,1070),"Previous Reding Date :",fill=(0,0,0),font=font,align ="center") #Current Unit
d.text((480,1070),str(Data.Prev_Reading_date[i]),fill=(0,0,0),font=font,align ="center")

d.text((100,1120),"Previous Unit :",fill=(0,0,0),font=font,align ="center") #Previous Unit
d.text((480,1120),str(Data.Prev_Units[i]),fill=(0,0,0),font=font,align ="center")


# Save the modified bill image
image.save("Bill.png","PNG")

path=r"C:\Users\vp201\Untitled Folder\Bill.png"
time.sleep(2) # Add a delay of 5 seconds

# Send the bill image via WhatsApp using pywhatkit
pywhatkit.sendwhats_image("+918000667207",r"C:\Users\vp201\Untitled Folder\Bill.png")

Data.Prev_Units.loc[(i)]=Data.Cur_Units[(i)]
Data.Prev_Reading.loc[(i)]=Data.Cur_Reading[i]
Data.Cur_Units.loc[(i)]=0
Data.Cur_Reading.loc[i]=0



