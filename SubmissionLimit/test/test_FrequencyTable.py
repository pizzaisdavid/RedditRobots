import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..src.FrequencyTable import *

def test_buildUserSubmissionFrequencyTable():
    submissions = [
        makeMockSubmission('username'),
        makeMockSubmission('username'),
        makeMockSubmission('username')
    ]
    
    table = buildUserSubmissionFrequencyTable(submissions)
    
    assert 'username' in table
    assert len(table['username']) == 3
    