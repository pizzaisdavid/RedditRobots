import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..FrequencyTable import *

def test_buildUserSubmissionFrequencyTable():
    submissions = [
        makeMockSubmission('username', 0),
        makeMockSubmission('username', 1),
        makeMockSubmission('username', 2)
    ]
    
    table = buildUserSubmissionFrequencyTable(submissions)
    
    assert 'username' in table
    assert len(table['username']) == 3
    