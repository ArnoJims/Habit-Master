# Importing the required modules
import pyfiglet
import pandas as pd
from tabulate import tabulate
import os

class Menus:

    '''Class contains functions that will output each of the different menus.'''

    def output_main_menu():
        
        '''
        This function outputs the main menu and returns a dataframe with its options.
        
        Returns:
            dataframe: Returns dataframe with main menu options.
        '''

        # Heading.
        print(pyfiglet.figlet_format('Welcome to Habit Master!',width=200))
        print('\033[4mThe app that will help you master your habits\033[0m')
        print('\n')
        print('Where would you like to start?')
        # Table with options.
        _main_menu = {
            '#': [1, 2, 3],
            'Option': ['Complete a Habit✅', 'Manage Habits📋', 'Analyze Habits📊']
        }
        _main_menu_df = pd.DataFrame(_main_menu, index=_main_menu['#'], columns=['Option'])
        print(tabulate(_main_menu_df, headers='keys', tablefmt='psql'))
        print('\033[3mPress Ctrl+C any time to exit.\033[0m\n')

        return _main_menu_df
        

    def output_manage_habits_menu():

        '''
        This function outputs the habit managing menu and returns a dataframe with all the options.
        
        Returns:
            dataframe: Returns dataframe with manage habits menu options.
        '''

        # Clearing the main menu.
        os.system('cls')

        # Table with options.
        _manage_habits_menu = {
            '#': [1, 2],
            'Option': ['Add a Habit➕', 'Delete a Habit➖']
        }
        _manage_habits_menu_df = pd.DataFrame(_manage_habits_menu, index=_manage_habits_menu['#'], columns=['Option'])
        print('What would you like to do next?')
        print(tabulate(_manage_habits_menu_df, headers='keys', tablefmt='psql'))
        print('\033[3mPress Ctrl+C any time to exit.\033[0m')

        return _manage_habits_menu_df

    def output_analyze_habits_menu():

        '''
        This function outputs the habit analyzing menu and returns a dataframe with all the options.
        
        Returns:
            dataframe: Returns dataframe with analyze habits menu options.
        '''

        # Clearing the main menu.
        os.system('cls')

        # Table with options.
        _analyze_habits_menu = {
            '#': [1, 2, 3, 4],
            'Option': ['List all habits📃', 'List all daily or weekly habits📜', 'Get longest streak overall🏆', 'Get longest streak for a habit🏅']
        }
        _analyze_habits_menu_df = pd.DataFrame(_analyze_habits_menu, index=_analyze_habits_menu['#'], columns=['Option'])
        print('What would you like to do next?')
        print(tabulate(_analyze_habits_menu_df, headers='keys', tablefmt='psql'))
        print('\033[3mPress Ctrl+C any time to exit.\033[0m')

        return _analyze_habits_menu_df