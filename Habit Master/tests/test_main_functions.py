# Importing required modules.
import Habit_Master
import pandas as pd

def test_validate_input_non_number() -> None:
        
        '''Tests the Habit_Master.validate_input function on a non numeric input.'''

        # Setting up testing input and options dataframe
        _test_input = 'test input'
        _test_df = pd.DataFrame({
            'index' : [1],
            'place_holder' : ['place holder']
        }).set_index('index')

        assert Habit_Master.validate_input(_test_input, _test_df) == False

def test_validate_input_invalid_option() -> None:
        
        '''Tests the Habit_Master.validate_input function on an invalid option.'''

        # Setting up testing input and options dataframe
        _test_input = 2
        _test_df = pd.DataFrame({
            'index' : [1],
            'place_holder' : ['place holder']
        }).set_index('index')

        assert Habit_Master.validate_input(_test_input, _test_df) == False

def test_validate_input_invalid_option() -> None:
        
        '''Tests the Habit_Master.validate_input function on a valid option.'''

        # Setting up testing input and options dataframe
        _test_input = 1
        _test_df = pd.DataFrame({
            'index' : [1],
            'place_holder' : ['place holder']
        }).set_index('index')

        assert Habit_Master.validate_input(_test_input, _test_df) == True        