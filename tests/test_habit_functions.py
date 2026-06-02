# Importing required modules.
from modules.habit_modules import Habit
import sqlite3
from datetime import datetime

# Creating and connecting to the testing database.
_test_conn = sqlite3.connect('testing.db')
_test_cur = _test_conn.cursor()

def test_initialize_habit():
    
    '''Tesing if a habit object can be created successfully.'''

    # Setting up testing variables.
    _name = 'Test Name'
    _periodicity = 'Daily'
    _created_date = '2026-01-03'

    _habit = Habit(_name, _periodicity, _created_date)

    # Test if attributes of created habit match initial test variables.
    assert _habit.name == 'Test Name' and _habit.periodicity == 'Daily' and _habit.created_on == '2026-01-03'
    
def test_add_habit() -> None:
        
    '''Tests the Habit.add_habit() function.'''

    # Setting up testing variables.
    _test_name = 'Test Name'
    _test_periodicity = 'Weekly'
    _test_created_on = str(datetime.today().strftime('%Y-%m-%d %H:%M:00.000'))

    Habit.add_habit(_test_cur, _test_conn, _test_name, _test_periodicity)

    # Test to see if habit was successfully added to the dim_Habits table.
    _test_cur.execute(f"SELECT * FROM dim_Habits WHERE Name = 'Test Name' AND Periodicity = 'Weekly' AND strftime('%Y-%m-%d %H:%M:00.000', Created_On) = '{_test_created_on}'")
    _test_len = len(_test_cur.fetchall())

    assert _test_len > 0
    
def test_remove_habit() -> None:
    
    '''Testing the Habit.remove_habit() function.'''

    # Getting a habit id to test with.
    _test_cur.execute('SELECT MAX(Habit_Id) From dim_Habits')
    _test_habit_id_to_remove = _test_cur.fetchall()[0][0]

    Habit.remove_habit(_test_cur, _test_conn, _test_habit_id_to_remove)

    # Test to see if habit with test id no longer exists.
    _test_cur.execute(f'SELECT * FROM dim_Habits WHERE Habit_Id = {_test_habit_id_to_remove}')
    _test_len = len(_test_cur.fetchall())

    assert _test_len == 0

def test_load_habits_from_sqlite() -> None:

    '''Testing Habit.load_habits_from_sqlite() function.'''

    _test_df = Habit.load_habits_from_sqlite(_test_conn)

    # Test if dataframe was loaded by confirming all columns exist.
    assert 'Name' in _test_df.columns and 'Periodicity' in _test_df.columns and 'Created_On' in _test_df.columns

def test_load_completions_from_sqlite() -> None:

    '''Testing the Habit.load_completions_from_sqlite() function.'''

    _test_df = Habit.load_completions_from_sqlite(_test_conn)

    # Test if dataframe was loaded by confirming all columns exist.
    assert 'Habit_Id' in _test_df.columns and 'Completion_Date' in _test_df.columns

def test_complete_habit() -> None:

    '''Testing the Habit.complete_habit()' function.'''

    # Getting a habit id to test with.
    _test_cur.execute('SELECT MIN(Habit_Id) From dim_Habits')
    _test_habit_id_to_complete = _test_cur.fetchall()[0][0]

    Habit.complete_habit(_test_cur, _test_conn, _test_habit_id_to_complete)

    # Test if completion was added to the fact_Habit_Completions table.
    _test_cur.execute(f"SELECT * FROM fact_Habit_Completions WHERE Habit_Id = {_test_habit_id_to_complete} AND Completion_Date = '{str(datetime.today().strftime('%Y-%m-%d'))}'")
    _test_len = len(_test_cur.fetchall())

    assert _test_len > 0