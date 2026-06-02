# Importing the required modules.
from datetime import datetime, timedelta
import sqlite3
import pandas as pd
from tabulate import tabulate
from modules.habit_modules import Habit
import os

class Analytics:

    '''This class stores all analytics functions.'''

    def list_all_habits(_habits_df):

        '''
        Lists all the habits currently stored in dim_Habits table in the habits.db database.
        
        Parameters:
        _habits_df (dataframe) : The dataframe containing your habits.
        '''

        print('Here are all your habits:')
        print(tabulate(_habits_df, headers='keys', tablefmt='psql'))

    def list_habits_by_periodicity(_periodicity_selection, _habits_df): 

        '''
        Lists all habits currently stored in the dim_Habits table in the habits.db database and allows the user to filter by periodicity.
        
        Parameters:
        _periodicity_selection (int) : 1 or 2. Indicates which periodicity to filter by.
        _habits_df (dataframe) : Dataframe with habits.
        '''

        # Processing their choice.
        if _periodicity_selection == 1:
            _periodicity = 'Daily'
        else:
            _periodicity = 'Weekly'
        # Filtering and displaying the chosen habits.
        _filtered_df = _habits_df[_habits_df['Periodicity'] == _periodicity]
        os.system('cls')
        print(f'Here are all the habits with a {_periodicity} periodicity:')
        print(tabulate(_filtered_df, headers='keys', tablefmt='psql'))

    def calculate_habit_streaks(_completions_df, _habits_df): 

        '''
        Calculates all streaks for all habits. Uses data from the dim_Habits and fact_Habit_Completions tables.
        Calculates Daily and Weekly habit streaks separately and then combines them into one dataframe.

        Parameters:
        _completions_df (dataframe) : Dataframe with habit completions.
        _habits_df (dataframe) : Dataframe with habits.
        
        Returns:
            dataframe: Returns dataframe with one row per habit streak. With columns containing habit information and
            columns for streak information such as Streak_Length.
        '''

        # Preparing habits and completions tables.
        _completions_df['Completion_Date'] = pd.to_datetime(_completions_df['Completion_Date'])
        _completions_with_habits_df = pd.merge(_completions_df, _habits_df, on='Habit_Id')

        # ----- Calculating daily habit streaks -----
        _daily_completions_df = _completions_with_habits_df[_completions_with_habits_df['Periodicity'] == 'Daily']
        # Using the difference between the cumcount and date to group completions into streaks.
        _daily_completions_df = _daily_completions_df.sort_values(['Habit_Id', 'Completion_Date'])
        _daily_completions_df['Row_Num'] = _daily_completions_df.groupby('Habit_Id').cumcount()
        _daily_completions_df['Date_Row_Diff'] = _daily_completions_df['Completion_Date'] - pd.to_timedelta(_daily_completions_df['Row_Num'], unit='D')
        _daily_streak_groups_df = _daily_completions_df.groupby(['Habit_Id', 'Date_Row_Diff'])
        # Aggregating to get the start and end of a streak. As well as its length.
        _daily_streaks_df = _daily_streak_groups_df.agg(
            Streak_Start=('Completion_Date', 'min'),
            Streak_End=('Completion_Date', 'max'),
            Streak_Length=('Completion_Date', 'count')
        ).reset_index(drop=False).drop(columns='Date_Row_Diff')
        # Adding habit information to the dataframe.
        _daily_streaks_df = pd.merge(_daily_streaks_df, _habits_df, on='Habit_Id')
        
        # ----- Calculating weekly habit streaks -----
        _weekly_completions_df = _completions_with_habits_df[_completions_with_habits_df['Periodicity'] == 'Weekly']
        # Adding a Year_Week column to track streaks and removing multiple completions within a single week.
        _weekly_completions_df['Year_Week'] = _weekly_completions_df['Completion_Date'].dt.isocalendar().year * 53 + _weekly_completions_df['Completion_Date'].dt.isocalendar().week
        _weekly_completions_df = _weekly_completions_df.drop_duplicates(subset=['Habit_Id', 'Year_Week'])
        # Using the difference between the cumcount and Year_Week to group completions into streaks.
        _weekly_completions_df = _weekly_completions_df.sort_values(['Habit_Id', 'Year_Week'])
        _weekly_completions_df['Row_Num'] = _weekly_completions_df.groupby('Habit_Id').cumcount()
        _weekly_completions_df['Date_Row_Diff'] = _weekly_completions_df['Year_Week'] - _weekly_completions_df['Row_Num']
        _weekly_streak_groups_df = _weekly_completions_df.groupby(['Habit_Id', 'Date_Row_Diff'])
        # Aggregating to get the start and end of a streak. As well as its length.
        _weekly_streaks_df = _weekly_streak_groups_df.agg(
            Streak_Start=('Completion_Date', 'min'),
            Streak_End=('Completion_Date', 'max'),
            Streak_Length=('Completion_Date', 'count')
        ).reset_index(drop=False).drop(columns='Date_Row_Diff')
        # Adding habit information to the dataframe.
        _weekly_streaks_df = pd.merge(_weekly_streaks_df, _habits_df, on='Habit_Id')

        # Appending daily and weekly streak dataframes.
        _streaks_df = pd.concat([_daily_streaks_df, _weekly_streaks_df])
        # Formatting the date columns.
        _streaks_df['Streak_Start'] = _streaks_df['Streak_Start'].dt.strftime('%Y-%m-%d')
        _streaks_df['Streak_End'] = _streaks_df['Streak_End'].dt.strftime('%Y-%m-%d')
        _streaks_df = _streaks_df[['Habit_Id', 'Name', 'Periodicity', 'Created_On', 'Streak_Start', 'Streak_End', 'Streak_Length']]

        return _streaks_df
    
    def print_longest_streak_of_a_habit(_completions_df, _habits_df, _habit_id):

        '''
        Outputs the longest streak of a habit.
        
        Parameters:
        _completions_df (dataframe) : Dataframe with habit completions.
        _habits_df (dataframe) : Dataframe with habits.
        _habit_id (int) : Habit_Id of the habit who's streak should be shown.
        '''

        # Clearing the terminal.
        os.system('cls')
        # Calculating habit streaks, filtering for the longest streak per habit and then for the selected habit.
        _streaks_df = Analytics.calculate_habit_streaks(_completions_df, _habits_df)
        _longest_streaks_df = _streaks_df.sort_values('Streak_Length', ascending=False).drop_duplicates(subset=['Habit_Id'])
        _filtered_longest_streaks_df = _longest_streaks_df[_longest_streaks_df['Habit_Id'] == _habit_id]
        _filtered_longest_streaks_df.set_index('Habit_Id', inplace=True)

        print('\nThe longest streak of the habit chosen is:')
        print(tabulate(_filtered_longest_streaks_df, headers='keys', tablefmt='psql'))

    def print_longest_streak_overall(_completions_df, _habits_df):

        '''
        Outputs the longest streak out of all habits.
        
        Parameters:
        _completions_df (dataframe) : Dataframe with habit completions.
        _habits_df (dataframe) : Dataframe with habits.
        '''

        # Calculating habit steaks and then filtering for the longest one or multiple if two have the longest streak.
        _streaks_df = Analytics.calculate_habit_streaks(_completions_df, _habits_df)
        _longest_streak_df = _streaks_df.loc[_streaks_df['Streak_Length'] == _streaks_df['Streak_Length'].max()]
        _longest_streak_df.set_index('Habit_Id', inplace=True)
        print('\nThe longest streak of all habits is:')
        print(tabulate(_longest_streak_df, headers='keys', tablefmt='psql'))