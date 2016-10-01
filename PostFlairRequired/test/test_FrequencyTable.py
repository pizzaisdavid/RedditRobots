import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..src.FrequencyTable import *

USERNAME_1 = 'Im_number_one'
USERNAME_2 = 'someone_else'

def test_buildUserSubmissionFrequencyTable_oneUser():
    submissions = [
        makeMockSubmission(USERNAME_1),
        makeMockSubmission(USERNAME_1),
        makeMockSubmission(USERNAME_1)
    ]
    
    table = buildUserSubmissionFrequencyTable(submissions)
    
    assert USERNAME_1 in table
    assert len(table[USERNAME_1]) == 3
    
def test_buildUserSubmissionFrequencyTable_multipleUsers():
    submissions = [
        makeMockSubmission(USERNAME_1),
        makeMockSubmission(USERNAME_1),
        makeMockSubmission(USERNAME_1),
        makeMockSubmission(USERNAME_2),
        makeMockSubmission(USERNAME_2)
    ]
    
    table = buildUserSubmissionFrequencyTable(submissions)
    
    assert USERNAME_1 in table
    assert len(table[USERNAME_1]) == 3
    
    assert USERNAME_2 in table
    assert len(table[USERNAME_2]) == 2
    