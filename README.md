Data Cleaning Application

The software is a simple GUI-based app for cleaning and preprocessing CSV data files using Python and Tkinter. It offers an intuitive interface to handle missing values, removes duplicates, fixes data types, standardizes text data, and handles outliers.

Features
o	Import CSV File : Opening of CSV files for processing
o	Handle Missing Values: Replacing missing numeric values with column mean and the text values as "Unknown".
o	Remove Duplicates : Automatic identification and removal of duplicate rows.
o	Fix Data Types: Convert numeric columns to integers and standardize text columns.
o	Standardize Text Data: Remove extra spaces and convert text to title case. Handle the missing text value.
o	Remove Outliers: Find outliers and remove the outliers using the 3-sigma rule.

Screenshots
 
![image](https://github.com/user-attachments/assets/0d961a4d-84e0-4a90-a54f-54db8ac0bd5f)
![image](https://github.com/user-attachments/assets/a0e1f2ca-cec1-4f1b-a0cb-97167eb8914e)
![image](https://github.com/user-attachments/assets/10fce84f-83c8-415e-a386-ca6b8ccf7451)
![image](https://github.com/user-attachments/assets/dba61364-69ff-49e2-b8ba-3b56d08103ca)
![image](https://github.com/user-attachments/assets/32fafe61-3dd5-4266-b526-ce20c451b5c0)

 

Prerequisites
For the application to work efficiently, make sure the followings are installed:
o	Python 3.8+
o	Required packages:
o	pandas
o	numpy
o	tkinter
Usage 
o	This window launches the application. Use the buttons to perform several operations:
o	Load CSV File: Lets select a CSV file to load into the application
o	Handle Missing Values: Automatically fills missing values with appropriate values
o	Remove Duplicates: Removes duplicate rows from your dataset
o	Fix Data Types: Converts numeric columns to integers. Standardizes text columns
o	Standardize Text Data: Cleans text data (strip spaces, title case)
o	Handle Outliers: Removes outliers based on statistical thresholds.

The processed data will appear in the text area of the application. 
Now open the application window. It can be used with buttons for various operations, such as loading a CSV file into the application.

