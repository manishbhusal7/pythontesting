"""
Sample Test
"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
from badcode import sum_all, multiply_all, count_characters, count_words, count_lines, greet,check_is_palindrome


@pytest.mark.parametrize("num_list, value",
                        [
                        ( [1,2,3],6),
                          ( [1,5,7,9],22),
                          ( [-1,1],0),
                          ([1.5,1.5],3.0),
                          ( ['a',1,'b'],None)
                         ])                    
def test_sum_all(num_list, value):
    if value is None:
        with pytest.raises(ValueError):
            sum_all(num_list)

    else:
     assert sum_all (num_list)== value


@pytest.mark.parametrize("num_list, value",
                        [
                        ( [1,2,3],6),
                          ( [1,5,7,9],315),
                          ( [-1,1],-1),
                          ([1.5,1.5],2.25),
                          ( ['a',1,'b'],None)
                         ])                    
def test_multiply_all(num_list, value):
    if value is None:
        with pytest.raises(ValueError):
            multiply_all(num_list)

    else:
     assert multiply_all (num_list)== value


@pytest.mark.parametrize("input_str,input_char,expected",
                        [
                        ( ["Manish",'M',1]),
                          (["Bhusal",'B',1]),
                          ["AAPLE", 'A',2]
                         ])                    
def test_count_characters(input_str,input_char,expected):
     assert count_characters (input_str,input_char)== expected

@pytest.mark.parametrize("input,expected",[("I am Manish",3),("Hello World",2), ("My",1)])
def test_count_words(input,expected):
    assert count_words(input) == expected



@pytest.mark.parametrize("input,expected",[("I am from Nepal \n \n \n I am a computer science student",4)])
def test_count_lines(input,expected):
    assert count_lines(input) == expected


@pytest.mark.parametrize("input,expected",[("Manish","Hello, Manish!"),("Jack","Hello, Jack!"),('Bhusal', 'Hello, Bhusal!')])
def test_greet(input,expected):
    assert greet(input) == expected

@pytest.mark.parametrize("input,expected",[("roger",False),("radar",True),("madam",True),('racecar',True),('MAMA',False)])
def test_check_is_palidrome(input,expected):
    assert check_is_palindrome(input) == expected

    # assert sum_all([1, 2, 3]) == 6

    # assert sum_all([1,5,7,9]) == 22
    
    # assert sum_all ([-1,1]) == 0

    # assert sum_all (['a'])
    
    # with pytest.raises(ValueError):
    #     sum_all(['a', 1 , 'c'])