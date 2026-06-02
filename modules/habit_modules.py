# Importing the required modules.
from datetime import datetime
import sqlite3
import pandas as pd
from tabulate import tabulate

class Habit:
    
    '''
    A class representing a habit.

    Attributes:
        name (str): Habit name.
        periodicity (str): How often a habit should be completed. Daily or Weekly.
        created_on (datetime): When the habit was created by the user.
    
    '''

    def __init__(self, name, periodicity, created_on = str(datetime.today())): 

        '''
        Initialize Habit object.

        Parameters:
        name (str): Habit name.
        periodicity (str): How often a habit should be completed. Daily or Weekly.
        created_on (datetime): When the habit was created by the user. DEFAULT TODAY.
        '''

        self.name = name
        self.periodicity = periodicity
        self.created_on =  created_on
    
    def add_habit(_cur, _conn, _name, _periodicity):

        '''
        Add a habit to the dim_Habits table in the database.

        Parameters:
        _cur (object) : Cursor object used to complete queries in the sqlite database.
        _conn (object) : Connection object to the sqlite database.
        _name (string) : Name of your new habit.
        _periodicity (string) : Periodicity of you new habit. Must be Daily or Weekly.
        '''

        # Creating a new habit and loading it into the database.
        _new_habit = Habit(_name, _periodicity)
        _cur.execute('INSERT INTO dim_Habits (Name, Periodicity, Created_On) VALUES (?,?,?)', [_new_habit.name, _new_habit.periodicity, _new_habit.created_on])
        _conn.commit()
        print('\n✅  Habit added successfully.\n')

    def remove_habit(_cur, _conn, _habit_id_to_delete):  
        
        '''
        Removes habit selected by the user, through inputs, from the dim_Habits table in the database. It
        also deletes all historical completions of the habit in the fact_Habit_Completions table.

        Parameters:
        _cur (object) : Cursor object used to complete queries in the sqlite database.
        _conn (object) : Connection object to the sqlite database.
        _habit_id_to_delete (int) : The Habit_Id of the habit you would like to delete.
        '''

        _current_habit_df = Habit.load_habits_from_sqlite(_conn)        
        _habit_to_delete = _current_habit_df.loc[_habit_id_to_delete, 'Name']

        # Deleting the habit from the database.
        print(f'Deleting "{_habit_to_delete}" habit from the database...')
        _cur.execute(f'DELETE FROM dim_Habits WHERE Habit_Id = {_habit_id_to_delete}')
        _cur.execute(f'DELETE FROM fact_Habit_Completions WHERE Habit_Id = {_habit_id_to_delete}')
        _conn.commit()
        print('\n✅  Habit deleted successfully.\n')

    def load_habits_from_sqlite(_conn): 

        '''
        Loads the dim_Habits table from the SQLite habits.db database into a dataframe.

        Parameters:
        _conn (object) : Connection object to the sqlite database.
        
        Returns:
            dataframe: Containing the entire dim_Habits table.
        '''

        _dim_Habits_df = pd.read_sql('SELECT * FROM dim_Habits', _conn, index_col="Habit_Id")

        return _dim_Habits_df

    def load_completions_from_sqlite(_conn):

        '''
        Loads the fact_Habit_Completions table from the SQLite habits.db database into a dataframe.

        Parameters:
        _conn (object) : Connection object to the sqlite database.
        
        Returns:
            dataframe: Containing the entire fact_Habit_Completions table.
        '''
        
        _fact_Habit_Completions_df = pd.read_sql('SELECT * FROM fact_Habit_Completions', _conn, index_col="Completion_Id")

        return _fact_Habit_Completions_df
    
    def complete_habit(_cur, _conn, _habit_id_to_complete): 

        '''
        Gets the user's selection of habit to complete and adds the completion to the fact_Habit_Completions table.

        Parameters:
        _cur (object) : Cursor object used to complete queries in the sqlite database.
        _conn (object) : Connection object to the sqlite database.
        _habit_id_to_complete (int) : Habit_Id of the habit that needs to be completed.
        '''

        _cur.execute('INSERT INTO fact_Habit_Completions (Habit_Id, Completion_Date) VALUES (?, ?)', (_habit_id_to_complete, str(datetime.today().strftime('%Y-%m-%d'))))
        _conn.commit()
        print('\n✅  Habit completed successfully. \n')