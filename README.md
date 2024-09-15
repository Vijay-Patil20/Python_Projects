# Electricity Bill Generator with User Data Management and WhatsApp Notification

**Description:**
This Python script automates electricity bill generation, user data management, and WhatsApp notification for bill delivery. It efficiently calculates charges, updates user data, and sends the customized bill image via WhatsApp.

**Features:**
User Data Management:
Reads user data (name, address, etc.) from a CSV file.
Updates current readings and units consumed for each billing cycle.
Bill Generation:
Calculates charges based on units consumed and rate slabs.
Updates bill details (consumer number, meter number, bill amount) dynamically.
Bill Customization:
Overlays user data and billing details on a template image using Pillow library.
WhatsApp Notification:
Sends the generated bill image to a specified WhatsApp number using pywhatkit.

**Requirements:**
Python 3
Libraries:
pandas
pdfkit (not used in this version, for future PDF generation)
os
Pillow (PIL Fork)
datetime
time
pywhatkit

**Instructions:**
Install Libraries:
Bash
pip install pandas Pillow datetime time pywhatkit
Use code with caution.
content_copy

Prepare Data Files:
Create a CSV file named User_Database.csv with columns for user information (name, address, meter number, etc.).
Create an image file named Bill.png to serve as the bill template.

Customize Paths :
Update file paths in the script for User_Database.csv, Bill.png, and the output bill image ("Bill.png" in this case).

Run the Script:
Execute the script using python electricity_bill_generator.py.
Enter your meter number when prompted.
Enter the current reading when prompted.


