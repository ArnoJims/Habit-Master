# ----- Importing the needed modules -----
from datetime import datetime, timedelta
import sqlite3
import pandas as pd
from tabulate import tabulate
import os
import pyfiglet
# Importing the program spesific modules.
from modules.habit_modules import Habit
from modules.analytics_modules import Analytics
from modules.menu_modules import Menus

def validate_input(_input, _option_df):

    '''
    Validating the user's input based on the options given.

    Parameters:
        _input (string) : The user's input.
        _option_df (dataframe) : Dataframe with all the valid options.
    
    Returns:
            boolean: Returns boolean indicating if the input is valid or not.
    '''

    try:
        _int_input = int(_input)
        if _int_input in _option_df.index:
            return True
        else:
            print("ℹ️  Please enter a valid option.")
            return False
    except ValueError:
        print("ℹ️  Please enter a number.")
        return False


def __main__():
    
    '''
    This is the main Habit Master program. This will run the entire habit tracking application 
    and call on the other modules as needed.
    '''

    # Ensuring the database exists which would indicate that the database_setup.py file has been run.
    try:
        # Connecting to the database.
        _conn = sqlite3.connect('file:habits.db?mode=rw', uri=True)
        _cur = _conn.cursor()

    except sqlite3.OperationalError:
        print('\n⚠️  Could not connect to database. Please ensure you have run the setup.py file and that a habits.db file exists '
            'in the same folder as your Habit_Master.py program.')
        print('🔄️  Then restart the program and try again.\n')
        exit()

    # Giving the user the option to exit the program at any time using Ctrl+C which is a KeyboardInterrupt error.
    try:
        # ----- Main loop -----
        while True:
            os.system('cls')
            # Main menu.
            _main_menu_option_df = Menus.output_main_menu()
            while True:
                _input = input("Please enter the option you choose: ")
                if validate_input(_input, _main_menu_option_df) == False:
                    continue
                else:
                    break
            _chosen_main_menu_option = int(_input)
            # Following the proper course of action based on the user's input.
            # ----- Completing a habit. -----
            if _chosen_main_menu_option == 1:
                # Clearing the main menu
                os.system('cls')
                # Setting up variables.
                _today = str(datetime.today().strftime('%Y-%m-%d'))

                _completions_df = Habit.load_completions_from_sqlite(_conn)
                _completed_today_df = _completions_df[_completions_df['Completion_Date'] == _today]

                # Outputing a list of the current habits that have not been completed today for the user to select from.
                _current_habit_df = Habit.load_habits_from_sqlite(_conn)
                _non_completed_habits = _current_habit_df[~_current_habit_df.index.isin(_completed_today_df['Habit_Id'])]

                if len(_non_completed_habits) == 0:
                    print('\n✅  Well done! All habits have been completed for today. Please come back tomorrow :) \n')
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    continue
                else:
                    print(tabulate(_non_completed_habits, headers='keys', tablefmt='psql'))

                # Getting and validating the user's input.
                while True:
                    _input = input("Please select which habit you want to complete by inputting its Habit_Id:")              
                    if validate_input(_input, _non_completed_habits) == False:
                        continue
                    else:
                        break
                _habit_id_to_complete = int(_input)
                
                Habit.complete_habit(_cur, _conn, _habit_id_to_complete)
                # Directing the user back to the main menu.
                print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                input()
                os.system('cls')
                continue
            # ----- Managing Habits -----.
            elif _chosen_main_menu_option == 2:
                # Clearing the main menu
                os.system('cls')
                _manage_habits_menu_option_df = Menus.output_manage_habits_menu()
                while True:
                    _input = input("Please enter the option you choose: ")
                    if validate_input(_input, _manage_habits_menu_option_df) == False:
                        continue
                    else:
                        break
                _chosen_manage_habits_menu_option = int(_input)
                # --- Adding a habit. ---
                if _chosen_manage_habits_menu_option == 1:
                    # Clearing the manage habits menu
                    os.system('cls')
                    # Gathering inputs from the user.
                    _name = input('Please enter the name of your habit:')
                    # Making sure they enter a valid option.
                    while True:
                        _input = input('What type of habit is it, Daily or Weekly?')
                        _cap_input = _input.capitalize().strip()
                        if _cap_input == 'Daily' or _cap_input == 'Weekly':
                            _periodicity = _cap_input
                            break
                        else:
                            print("ℹ️  Invalid input. Please only enter Daily or Weekly. Please try again.") 
                    Habit.add_habit(_cur, _conn, _name, _periodicity)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                # --- Deteling a habit. ---
                elif _chosen_manage_habits_menu_option == 2:
                    # Clearing the manage habits menu
                    os.system('cls')
                    # Outputing a list of the current habits for the user to select from.
                    _current_habit_df = Habit.load_habits_from_sqlite(_conn)
                    print(tabulate(_current_habit_df, headers='keys', tablefmt='psql'))

                    # Getting the user's selection and making sure its a valid selection.
                    while True:
                        _input = input("Please select which habit you want to delete by inputting its Habit_Id: ")
                        try:
                            _int_input = int(_input)
                            if _int_input in _current_habit_df.index:
                                _habit_id_to_delete = _int_input
                                break
                            else:
                                print("ℹ️  Please enter a valid option.")
                        except ValueError:
                            print("ℹ️  Please enter a number.")

                    Habit.remove_habit(_cur, _conn, _habit_id_to_delete)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                else:
                    continue
            # ----- Analyzing habits. -----
            elif _chosen_main_menu_option == 3:
                # Clearing the main menu
                os.system('cls')
                _analyze_habits_menu_option_df = Menus.output_analyze_habits_menu()
                while True:
                    _input = input("Please enter the option you choose: ")
                    if validate_input(_input, _analyze_habits_menu_option_df) == False:
                        continue
                    else:
                        break
                _chosen_analyze_habits_menu_option = int(_input)
                # --- Listing all habits. ---
                if _chosen_analyze_habits_menu_option == 1:
                    # Clearing the analyze habits menu
                    os.system('cls')
                    _habits_df = Habit.load_habits_from_sqlite(_conn)
                    Analytics.list_all_habits(_habits_df)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                # --- Listing only habits of a certain periodicity. ---
                elif _chosen_analyze_habits_menu_option == 2:
                    # Clearing the analyze habits menu
                    os.system('cls')
                    # Loop to gather the user's input and retry until a valid input is entered.
                    while True:
                        # Gathering the user's choice.
                        _user_input = input('Which habits whould you like to see?\n1. Daily \n2. Weekly \nPlease enter 1 or 2:')
                        # Making sure they enter a number.
                        try:
                            _periodicity_selection = int(_user_input)
                            # Checking that it is a valid number.
                            if _periodicity_selection == 1 or _periodicity_selection == 2:
                                break
                            else:
                                print('ℹ️  Please enter a valid option.')
                        except ValueError:
                            print('ℹ️  Please enter a number.')

                    _habits_df = Habit.load_habits_from_sqlite(_conn)
                    Analytics.list_habits_by_periodicity(_periodicity_selection, _habits_df)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                # --- Printing the longest streak overall. ---
                elif _chosen_analyze_habits_menu_option == 3:
                    # Clearing the analyze habits menu
                    os.system('cls')
                    # Loading all the habits and completions.
                    _habits_df = Habit.load_habits_from_sqlite(_conn)
                    _completions_df = Habit.load_completions_from_sqlite(_conn)
                    Analytics.print_longest_streak_overall(_completions_df, _habits_df)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                # --- Printing the longest streak of a chosen habit. ---
                elif _chosen_analyze_habits_menu_option == 4:
                    # Clearing the analyze habits menu
                    os.system('cls')

                    # Loading all the habits and completions.
                    _habits_df = Habit.load_habits_from_sqlite(_conn)
                    _completions_df = Habit.load_completions_from_sqlite(_conn)

                    # Listing all the habits for the user to choose from.
                    Analytics.list_all_habits(_habits_df)

                    # Loop to gather and validate user's input.
                    while True:
                        _input = input('Please enter the Habit_Id of the habit who\'s longest streak you would like to see:')
                        if validate_input(_input, _habits_df) == False:
                            continue
                        else:
                            break
                    _habit_id = int(_input)

                    Analytics.print_longest_streak_of_a_habit(_completions_df, _habits_df, _habit_id)
                    # Directing the user back to the main menu.
                    print('\033[3mPress Enter to head back to the main menu OR Press Ctrl+C to exit the app.\033[0m')
                    input()
                    os.system('cls')
                    continue
                else:
                    continue
            else:
                exit()
    except KeyboardInterrupt:
        os.system('cls')
        print('\nGoodbye👋 See you again soon!\n')
        os.system('exit')

# Calling the main function.
if __name__ == '__main__':
    __main__()