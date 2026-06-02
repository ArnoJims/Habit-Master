# Habit Master

## The tool you need to master your habits.

This is a python application with a command line interface. This program allows you to store, manage, track and analyze your habits. You are able to add and remove habits as well as view their streaks. This app stores your data in a sqlite database which means there is no big setup or installation requirements. So you can just get up and go!

## Table of Contents

- [Installation Guide](#installation)
- [Usage Guide](#usage)

## Installation Guide

1. Download this project into you Desktop folder like so:

   Download the code zip file.
   <img width="945" height="445" alt="image" src="https://github.com/user-attachments/assets/6d2bc177-1945-4c7a-9329-d3b67cabb448" />
   
   Extract the contents into your desktop folder. Your username will be different.
   <img width="1907" height="830" alt="image" src="https://github.com/user-attachments/assets/e531363f-9b5d-4e06-a53b-6b3f53de63da" />   

3. Download and install python here: https://www.python.org/ftp/python/3.14.5/python-3.14.5-amd64.exe.  
   Once downloaded run the .exe file and follow the instructions on the installer.
   <img width="1912" height="269" alt="image" src="https://github.com/user-attachments/assets/8ea22092-8a4e-4198-9ff7-81dd4e4941be" />
   Make sure the 'Add python.exe to PATH' box is ticked.
   <img width="817" height="517" alt="image" src="https://github.com/user-attachments/assets/4804055c-1243-421b-a8f4-cbc609a2026d" />

   

2. Install the required modules from the requirements.txt file by opening command prompt and entering the the following like so:
3. Run the database_setup.py file to create your sqlite databases by doing the following:
4. All set! Follow the Usage Guide to find out how to open and use the application.

## Usage Guide

### 1. Opening Habit Master

To open your application, right click on the desktop icon and click on "Open in Terminal". Then type "python Habit_Master.py" into the terminal and press enter to run the application.

### 2. Navigating the Main Menu

The main menu contains a lovely welcome at the top with all your different navigation options. For all menus you will just have to enter the number of the option you would like to choose and press "Enter". At any point when using the application, if you want to exit, press "Ctrl+C". In the main menu there are 3 options to choose from: Complete a Habit✅, Manage Habits📋 and Analyze Habits📊. 

### 3. Completing a Habit

When completing a habit you will select from a list of your current habits which one you would like to complete. If a habit has already been complete today it will not appear in the list. If you have completed all your habits you will receive a well deserved congradulations and be directed back to the main menu.

### 4. Managing Habits
In the managing section of the application you are able to add and delete habits. When adding a habit you can give it a name and specify its periodicity as Daily or Weekly. When deleting a habit you get to choose which one you want to delete from your list of current habits.

### 5. Analyzing Habits
There are four options when analyzing your habits. You can list all your habits. You can list only ones with Daily or Weekly periodicity. You can see the longest streak of a habit of your choice and you can see the longest streak out of all your habits. When choosing an option you will be guided through if anything else is necessary like choosing the periodicity to filter by or the habit who's longest streak you want to see.
