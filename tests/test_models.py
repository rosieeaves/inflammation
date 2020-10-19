"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
from unittest.mock import patch
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    # NB: the comment 'yapf: disable' disables automatic formatting using
    # a tool called 'yapf' which we have used when creating this project
    test_array = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])  # yapf: disable

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(np.array([0, 0]), daily_mean(test_array))

@pytest.mark.parametrize(
        'test, expected'
        [
                ([[0,0],[0,0],[0,0]],[0,0])
                ([[1,2],[3,4],[5,6]],[3,4])
        ])

def test_daily_mean():
    """Test that mean function works for an array of zeroes and positive integers."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(np.array(expected), np.array(test))
    
@pytest.mark.parametrize(
        'test, expected'
        [
                ([[6,9,-4],[8,12,16],[0,-1,5]],[8,12,16])
                ([[3,9,2],[7,-2,5],[10,6,7]],[10,9,7])
        ])
    
def test_daily_max():
    """Test that max function works for an array of integers."""
    from inflammation.models import daily_max
    
    # Use Numpy testing functions to compare arrays
    npt.assert_array_equal(np.array(expected), np.array(test))
    
@pytest.mark.parametrize(
        'test, expected'
        [
                ([[5,9,1],[4,-2,8],[11,6,-7]],[4,-2,-7])
                ([[3,6,10],[4,7,12],[10,-2,9]],[3,-2,9])
        ])
    
def test_daily_min():
    """Test that min function works for an array of integers."""
    from inflammation.models import daily_min
    
    # Use Numpy testing functions to compare arrays
    npt.assert_array_equal(np.array(expected),np.array(test))
    
def test_daily_min_string():
    """Test for TypeError when passing strings."""
    from inflammation.models import daily_min
    
    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello','there'],
                                    ['General','Kenobi']])

@patch('inflammation.models.get_data_dir', return_value='/data_dir')
def test_load_csv(mock_get_data_dir):
    from inflammation.models import load_csv
    with patch('numpy.loadtxt') as mock_loadtxt:
        load_csv('test.csv')
        name, args, kwargs = mock_loadtxt.mock_calls[0]
        assert kwargs['fname'] == '/data_dir/test.csv'
        load_csv('/test.csv')
        name, args, kwargs = mock_loadtxt.mock_calls[1]
        assert kwargs['fname'] == '/test.csv'

# TODO(lesson-automatic) Implement tests for the other statistical functions
# TODO(lesson-mocking) Implement a unit test for the load_csv function
