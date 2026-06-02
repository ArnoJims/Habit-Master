# Importing the required modules.
from modules.analytics_modules import Analytics
import pandas as pd

# Setting up testing dim_Habits and fact_Habit_Completions dataframes.
_test_dim_Habits = {
    'Habit_Id': [1, 2, 3],
    'Name': ['Exercise', 'Read', 'Get in Nature'],
    'Periodicity': ['Daily', 'Daily', 'Weekly'],
    'Created_On': ['2026-01-01 00:00:00.000', '2026-01-01 00:00:00.000', '2026-01-01 00:00:00.000']
}
_test_dim_Habits_df = pd.DataFrame(_test_dim_Habits, index=_test_dim_Habits['Habit_Id'])

_test_fact_completions = {
    'Completion_Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Habit_Id': [1, 2, 3, 1, 2, 1, 2, 2, 3, 1],
    'Completion_Date': ['2026-01-01', '2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05', '2026-01-06', '2026-01-12']
}
_test_fact_completions_df = pd.DataFrame(_test_fact_completions, index=_test_fact_completions['Completion_Id'])

def test_list_all_habits(capsys) -> None:

    '''Testing the Analytics.list_all_habits() function.'''

    Analytics.list_all_habits(_test_dim_Habits_df)

    # Using capsys to evaluate the output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'Here are all your habits:' in _test_output
    assert 'Exercise' in _test_output
    assert 'Read' in _test_output
    assert 'Get in Nature' in _test_output
    assert 'Daily' in _test_output
    assert 'Weekly' in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output

def test_list_habits_by_periodicity_daily(capsys) -> None:

    '''Testing the Analytics.list_habits_by_periodicity() function.'''

    Analytics.list_habits_by_periodicity(1, _test_dim_Habits_df)

    # Using capsys to evaluate the output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'Here are all the habits with a Daily periodicity:' in _test_output
    assert 'Exercise' in _test_output
    assert 'Read' in _test_output
    assert 'Daily' in _test_output
    assert 'Weekly' not in _test_output
    assert 'Get in Nature' not in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output

def test_list_habits_by_periodicity_weekly(capsys) -> None:

    '''Testing the Analytics.list_habits_by_periodicity() function.'''

    Analytics.list_habits_by_periodicity(2, _test_dim_Habits_df)

    # Using capsys to evaluate the output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'Here are all the habits with a Weekly periodicity:' in _test_output
    assert 'Exercise' not in _test_output
    assert 'Read' not in _test_output
    assert 'Daily' not in _test_output
    assert 'Weekly' in _test_output
    assert 'Get in Nature' in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output

def test_calculate_habit_streaks() -> None:

    '''Testing the Analytics.calculate_habit_streaks() function.'''

    _test_streaks_df = Analytics.calculate_habit_streaks(_test_fact_completions_df, _test_dim_Habits_df)

    # Creating a mask for each habit to verify the information returned in the streaks dataframe.
    _exercise_expected = {'Habit_Id':1, 'Name':'Exercise', 'Periodicity':'Daily', 'Created_On':'2026-01-01 00:00:00.000', 'Streak_Start':'2026-01-01', 'Streak_End':'2026-01-03', 'Streak_Length':3}
    _exercise_mask = (_test_streaks_df[list(_exercise_expected.keys())] == pd.Series(_exercise_expected)).all(axis=1)

    _read_expected = {'Habit_Id':2, 'Name':'Read', 'Periodicity':'Daily', 'Created_On':'2026-01-01 00:00:00.000', 'Streak_Start':'2026-01-01', 'Streak_End':'2026-01-02', 'Streak_Length':2}
    _read_mask = (_test_streaks_df[list(_read_expected.keys())] == pd.Series(_read_expected)).all(axis=1)

    _nature_expected = {'Habit_Id':3, 'Name':'Get in Nature', 'Periodicity':'Weekly', 'Created_On':'2026-01-01 00:00:00.000', 'Streak_Start':'2026-01-01', 'Streak_End':'2026-01-06', 'Streak_Length':2}
    _nature_mask = (_test_streaks_df[list(_nature_expected.keys())] == pd.Series(_nature_expected)).all(axis=1)

    # Tests to ensure rows matching the expected criteria exist.
    assert not _test_streaks_df[_exercise_mask].empty
    assert not _test_streaks_df[_read_mask].empty
    assert not _test_streaks_df[_nature_mask].empty

def test_print_longest_streak_of_a_habit_daily(capsys) -> None:

    '''Testing the Analytics.print_longest_streak_of_a_habit() function with a daily habit.'''

    Analytics.print_longest_streak_of_a_habit(_test_fact_completions_df, _test_dim_Habits_df, 1)

    # Using capsys to evaluate the output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'The longest streak of the habit chosen is:' in _test_output
    assert 'Exercise' in _test_output
    assert 'Daily' in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output
    assert '2026-01-01' in _test_output
    assert '2026-01-03' in _test_output
    assert 'Streak_Start' in _test_output
    assert 'Streak_End' in _test_output
    assert '3' in _test_output
    assert 'Streak_Length' in _test_output

def test_print_longest_streak_of_a_habit_weekly(capsys) -> None:

    '''Testing the Analytics.print_longest_streak_of_a_habit() function with a weekly habit.'''

    Analytics.print_longest_streak_of_a_habit(_test_fact_completions_df, _test_dim_Habits_df, 3)

    # Using capsys to evaluate the output
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'The longest streak of the habit chosen is:' in _test_output
    assert 'Get in Nature' in _test_output
    assert 'Weekly' in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output
    assert '2026-01-01' in _test_output
    assert '2026-01-06' in _test_output
    assert 'Streak_Start' in _test_output
    assert 'Streak_End' in _test_output
    assert '2' in _test_output
    assert 'Streak_Length' in _test_output

def test_print_longest_streak_overall(capsys) -> None:

    '''Testing the Analytics.print_longest_streak_overall() function.'''

    Analytics.print_longest_streak_overall(_test_fact_completions_df, _test_dim_Habits_df)

    # Using capsys to evaluate the output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests to verify the expected output based on input.
    assert 'The longest streak of all habits is:' in _test_output
    assert 'Exercise' in _test_output
    assert 'Daily' in _test_output
    assert '2026-01-01 00:00:00.000' in _test_output
    assert '2026-01-01' in _test_output
    assert '2026-01-03' in _test_output
    assert 'Streak_Start' in _test_output
    assert 'Streak_End' in _test_output
    assert '3' in _test_output
    assert 'Streak_Length' in _test_output