import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..FrequencyTable import *

def test_buildUserSubmissionFrequencyTable():
    s = []
    buildUserSubmissionFrequencyTable(s)