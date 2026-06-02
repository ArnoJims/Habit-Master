# Importing the required libraries.
import sqlite3

# Creating and connecting to the habits database.
_conn_habits = sqlite3.connect('habits.db')
_cur_habits = _conn_habits.cursor()

# Creating and connecting to the habits database.
_conn_testing = sqlite3.connect('testing.db')
_cur_testing = _conn_testing.cursor()

# SQL queries to create the 2 required tables; dim_Habits and fact_Habit_Completions.
_habits_table_command = '''
/*====================================================  
Table Name: dim_Habits
Columns: Habit_Id, Name, Periodicity, Created_On
Purporse: Stores the unique list of habits and their
          attributes.
====================================================*/

CREATE TABLE IF NOT EXISTS dim_Habits (
Habit_Id INTEGER PRIMARY KEY,
Name TEXT,
Periodicity TEXT,
Created_On TEXT)'''

_habit_completions_table_command = '''
/*=======================================================  
Table Name: fact_Habit_Completions
Columns: Completion_Id, Habit_Id, Completion_Date
Purporse: Used as a logging table for habit completions.
=======================================================*/

CREATE TABLE IF NOT EXISTS fact_Habit_Completions (
Completion_Id INTEGER PRIMARY KEY,
Habit_Id INTEGER,
Completion_Date TEXT,
FOREIGN KEY (Habit_Id) REFERENCES dim_Habits(Habit_Id))'''

# Creating dummy data to use as an example for new users and to fullfill my assignment requirements.
_habits_dummy_data = [('Exercise', 'Daily', '2026-01-01 00:00:00.000'), ('Sleep 8 Hours', 'Daily', '2026-01-01 00:00:00.000'), 
                      ('Read 30 Min', 'Daily', '2026-01-01 00:00:00.000'), ('Get in Nature', 'Weekly', '2026-01-01 00:00:00.000'), 
                      ('Stick to Diet', 'Daily', '2026-01-01 00:00:00.000')]

_completions_dummy_data = [(1, '2026-01-01'), (2, '2026-01-01'), (3, '2026-01-01'),                    (5, '2026-01-01'),
                           (1, '2026-01-02'), (2, '2026-01-02'), (3, '2026-01-02'),                    (5, '2026-01-02'),
                           (1, '2026-01-03'), (2, '2026-01-03'),                    (4, '2026-01-03'), (5, '2026-01-03'),
                           (1, '2026-01-04'), (2, '2026-01-04'), (3, '2026-01-04'),                    (5, '2026-01-04'),
                                              (2, '2026-01-05'),                                       (5, '2026-01-05'),
                           (1, '2026-01-06'), (2, '2026-01-06'),                                       (5, '2026-01-06'),
                           (1, '2026-01-07'),                                                          (5, '2026-01-07'),
                           (1, '2026-01-08'), (2, '2026-01-08'),                                       (5, '2026-01-08'),
                           (1, '2026-01-09'), (2, '2026-01-09'),                                       (5, '2026-01-09'),
                           (1, '2026-01-10'), (2, '2026-01-10'), (3, '2026-01-10'),                    (5, '2026-01-10'),
                           (1, '2026-01-11'),                    (3, '2026-01-11'), (4, '2026-01-11'), (5, '2026-01-11'),
                           (1, '2026-01-12'),                    (3, '2026-01-12'),                    (5, '2026-01-12'),
                           (1, '2026-01-13'),                    (3, '2026-01-13'),                    (5, '2026-01-13'),
                           (1, '2026-01-14'), (2, '2026-01-14'),                                       (5, '2026-01-14'),
                           (1, '2026-01-15'), (2, '2026-01-15'),                                       (5, '2026-01-15'),
                           (1, '2026-01-16'), (2, '2026-01-16'), (3, '2026-01-16'), (4, '2026-01-16'),                   
                                              (2, '2026-01-17'), (3, '2026-01-17'),                                      
                           (1, '2026-01-18'), (2, '2026-01-18'), (3, '2026-01-18'),                                      
                           (1, '2026-01-19'), (2, '2026-01-19'),                                       (5, '2026-01-19'),
                                              (2, '2026-01-20'), (3, '2026-01-20'),                    (5, '2026-01-20'),
                           (1, '2026-01-21'), (2, '2026-01-21'), (3, '2026-01-21'),                    (5, '2026-01-21'),
                                                                                                       (5, '2026-01-22'),
                           (1, '2026-01-23'), (2, '2026-01-23'),                                       (5, '2026-01-23'),
                           (1, '2026-01-24'),                    (3, '2026-01-24'),                    (5, '2026-01-24'),
                           (1, '2026-01-25'), (2, '2026-01-25'),                                       (5, '2026-01-25'),
                                              (2, '2026-01-26'), (3, '2026-01-26'),                    (5, '2026-01-26'),
                                              (2, '2026-01-27'),                                       (5, '2026-01-27'),
                           (1, '2026-01-28'),                    (3, '2026-01-28'), (4, '2026-01-28'), (5, '2026-01-28'),]

# Queries to insert the dummy data.
_habits_dummy_insert_query = 'INSERT INTO dim_Habits (Name, Periodicity, Created_On) VALUES (?,?,?)'
_completions_dummy_insert_query = 'INSERT INTO fact_Habit_Completions (Habit_Id, Completion_Date) VALUES (?,?)'

# ----- Executing the table creating queries for the habits database -----.
_cur_habits.execute(_habits_table_command)
_cur_habits.execute(_habit_completions_table_command)

# Getting the length or number of rows from both tables to later determine if the dummy data already exists.
_cur_habits.execute('SELECT * FROM dim_Habits')
_len_habits = len(_cur_habits.fetchall())
_cur_habits.execute('SELECT * FROM fact_Habit_Completions')
_len_completions = len(_cur_habits.fetchall())

# Executing the dummy data insertion queries but first checking if there is already data in the tables as to not add it twice. If the user for some reason runs the setup.py file twice.
if _len_completions == 0 and _len_habits == 0:
    _cur_habits.executemany(_habits_dummy_insert_query, _habits_dummy_data)
    _cur_habits.executemany(_completions_dummy_insert_query, _completions_dummy_data)
    print('✅  Your habits database has been set up successfully.')
    print("✅  Dummy data entered successfully into habits.db.")
else:
    print("ℹ️  Your database has already been set up and filled with dummy data.")

# Commiting my changes and closing the connection to the database.
_conn_habits.commit()
_conn_habits.close()

# ----- Executing the table creating queries for the testing database -----.
_cur_testing.execute(_habits_table_command)
_cur_testing.execute(_habit_completions_table_command)

# Getting the length or number of rows from both tables to later determine if the dummy data already exists.
_cur_testing.execute('SELECT * FROM dim_Habits')
_len_habits = len(_cur_testing.fetchall())
_cur_testing.execute('SELECT * FROM fact_Habit_Completions')
_len_completions = len(_cur_testing.fetchall())

# Executing the dummy data insertion queries but first checking if there is already data in the tables as to not add it twice. If the user for some reason runs the setup.py file twice.
if _len_completions == 0 and _len_habits == 0:
    _cur_testing.executemany(_habits_dummy_insert_query, _habits_dummy_data)
    _cur_testing.executemany(_completions_dummy_insert_query, _completions_dummy_data)
    print('✅  Your testing database has been set up successfully.')
    print("✅  Dummy data entered successfully into testing.db.")
else:
    print("ℹ️  Your testing database has already been set up and filled with dummy data.")

# Commiting my changes and closing the connection to the database.
_conn_testing.commit()
_conn_testing.close()