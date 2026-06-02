# Habit Master

## The tool you need to master your habits.

This is a python application with a command line interface. This program allows you to store, manage, track and analyze your habits. You are able to add and remove habits as well as view their streaks. This app stores your data in a sqlite database which means there is no big setup or installation requirements. So you can just get up and go!

## Table of Contents

- [Installation Guide](#installation)
- [Usage Guide](#usage)
- [Testing the Application](#testing)

## Installation Guide

1. Download this project into you Desktop folder like so:

   Download the code zip file.
   <img width="945" height="445" alt="image" src="https://github.com/user-attachments/assets/6d2bc177-1945-4c7a-9329-d3b67cabb448" />
   
   Extract the contents into your Desktop folder. Your username will be different.
   <img width="1907" height="830" alt="image" src="https://github.com/user-attachments/assets/e531363f-9b5d-4e06-a53b-6b3f53de63da" />   

3. Download and install python here: https://www.python.org/ftp/python/3.14.5/python-3.14.5-amd64.exe.  
   Once downloaded run the .exe file and follow the instructions on the installer.
   <img width="1912" height="269" alt="image" src="https://github.com/user-attachments/assets/8ea22092-8a4e-4198-9ff7-81dd4e4941be" />
   Make sure the 'Add python.exe to PATH' box is ticked.
   <img width="817" height="517" alt="image" src="https://github.com/user-attachments/assets/4804055c-1243-421b-a8f4-cbc609a2026d" />

2. Install the required modules from the requirements.txt file by opening command prompt and entering the the following like so:  
  Open a new terminal from your Habit-Master-main file on your desktop.
  <img width="460" height="568" alt="image" src="https://github.com/user-attachments/assets/932aaed3-da5d-47b1-a373-61de37d2f59c" />

   Paste this command and press "Enter".
   
   ```python -m pip install -r requirements.txt```
   
   <img width="1483" height="760" alt="image" src="https://github.com/user-attachments/assets/3914d46b-4403-4478-b98f-eb448da53c9b" />

   All the required modules should install and once complete you can close the terminal.

4. Run the database_setup.py file to create your sqlite databases by doing the following:  
   Open a new terminal from your Habit-Master-main file on your desktop.  
   <img width="460" height="568" alt="image" src="https://github.com/user-attachments/assets/18e2f599-6ea3-4076-ba4d-0fed17801939" />

   Paste this command and press "Enter".
    
   ```python database_setup.py```

   You should see a message like the one below if you database was set up successfully. You can close the terminal.
   <img width="1478" height="755" alt="image" src="https://github.com/user-attachments/assets/356c1269-0ce7-4f49-ae91-4f53594226d0" />

   
6. All set! Follow the Usage Guide to find out how to open and use the application.

## Usage Guide

### 1. Opening Habit Master

To open your application, open a new terminal from your Habit-Master-main file on your desktop. 
<img width="460" height="568" alt="image" src="https://github.com/user-attachments/assets/4e2471e2-783c-4754-9e37-ceec68392fc0" />

Type in the following and press "Enter" to start your program. Each time you close your program you need to open it again in this same way.  

```python Habit_Master.py```

### 2. Navigating the Main Menu

The main menu contains a lovely welcome at the top with all your different navigation options. For all menus you will just have to enter the number of the option you would like to choose and press "Enter". At any point when using the application, if you want to exit, press "Ctrl+C". In the main menu there are 3 options to choose from: Complete a Habit✅, Manage Habits📋 and Analyze Habits📊. 

<img width="1481" height="757" alt="image" src="https://github.com/user-attachments/assets/f4ac6e16-6516-47d5-87c0-423faba71832" />

### 3. Completing a Habit

When completing a habit you will select from a list of your current habits which one you would like to complete. If a habit has already been complete today it will not appear in the list. If you have completed all your habits you will receive a well deserved congradulations and be directed back to the main menu.

<img width="1477" height="755" alt="image" src="https://github.com/user-attachments/assets/d69a84d3-7d51-4c42-b2f0-a985a24573a5" />

### 4. Managing Habits
In the managing section of the application you are able to add and delete habits. When adding a habit you can give it a name and specify its periodicity as Daily or Weekly. When deleting a habit you get to choose which one you want to delete from your list of current habits.

<img width="1474" height="757" alt="image" src="https://github.com/user-attachments/assets/ef1c11fe-67b7-4e4b-bc1c-4e03ecd1cc3d" />

### 5. Analyzing Habits
There are four options when analyzing your habits. You can list all your habits. You can list only ones with Daily or Weekly periodicity. You can see the longest streak of a habit of your choice and you can see the longest streak out of all your habits. When choosing an option you will be guided through if anything else is necessary like choosing the periodicity to filter by or the habit who's longest streak you want to see.

<img width="1481" height="754" alt="image" src="https://github.com/user-attachments/assets/fd08e1aa-ffa5-4af1-9d00-2b85ca5766c0" />

## Testing the Application
If you would like to run the test suit for the application, open a new terminal from you Habit-Master-main file on you desktop, paste the below and hit "Enter".  

```pytest```

<img width="1483" height="758" alt="image" src="https://github.com/user-attachments/assets/9feecb40-08f1-4a1e-9418-af2329a9d36d" />
