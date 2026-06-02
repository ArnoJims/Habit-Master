# Importing the required modules.
from modules.menu_modules import Menus
import pandas as pd

def test_output_main_menu(capsys) -> None:

    '''Testing the Menus.output_main_menu() function.'''

    _main_menu = {
            '#': [1, 2, 3],
            'Option': ['Complete a Habit✅', 'Manage Habits📋', 'Analyze Habits📊']
        }
    _main_menu_df = pd.DataFrame(_main_menu, index=_main_menu['#'], columns=['Option'])

    _test_return = Menus.output_main_menu()

    # Capturing the console output.
    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests for key elements in output.
    assert 'The app that will help you master your habits' in _test_output
    assert 'Where would you like to start?' in _test_output

    # Tests for menu output.
    assert 'Complete a Habit✅' in _test_output
    assert 'Manage Habits📋' in _test_output
    assert 'Analyze Habits📊' in _test_output

    # Test for exit footer.
    assert 'Press Ctrl+C any time to exit.' in _test_output

    # Test the returned dataframe.
    assert isinstance(_test_return, pd.DataFrame)
    assert _test_return.shape == (3,1)
    assert list(_test_return['Option']) == ['Complete a Habit✅', 'Manage Habits📋', 'Analyze Habits📊']

def test_output_manage_habits_menu(capsys) -> None:

    '''Testing the Menus.output_manage_habits_menu() function.'''

    _test_return = Menus.output_manage_habits_menu()

    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests for test outputs.
    assert 'What would you like to do next?' in _test_output
    assert 'Add a Habit➕' in _test_output
    assert 'Delete a Habit➖' in _test_output
    assert 'Press Ctrl+C any time to exit.' in _test_output

    # Tests for returned dataframe.
    assert isinstance(_test_return, pd.DataFrame)
    assert _test_return.shape == (2,1)
    assert list(_test_return['Option']) == ['Add a Habit➕', 'Delete a Habit➖']

def test_output_analyze_habits_menu(capsys) -> None:

    '''Testing the Menus.output_analyze_habits_menu() function.'''

    _test_return = Menus.output_analyze_habits_menu()

    _captured = capsys.readouterr()
    _test_output = _captured.out

    # Tests for test outputs.
    assert 'What would you like to do next?' in _test_output
    assert 'List all habits📃' in _test_output
    assert 'List all daily or weekly habits📜' in _test_output
    assert 'Get longest streak overall🏆' in _test_output
    assert 'Get longest streak for a habit🏅' in _test_output
    assert 'Press Ctrl+C any time to exit.' in _test_output

    # Tests for returned dataframe.
    assert isinstance(_test_return, pd.DataFrame)
    assert _test_return.shape == (4,1)
    assert list(_test_return['Option']) == ['List all habits📃', 'List all daily or weekly habits📜', 'Get longest streak overall🏆', 'Get longest streak for a habit🏅']
