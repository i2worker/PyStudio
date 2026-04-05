import sys
import os
sys.path.insert(0, os.path.dirname(os.getcwd()))


import pytest # type: ignore
from mod.survey import AnonymousSurvey

@pytest.fixture
def survey():
    question = "What is your favorite color?"
    return AnonymousSurvey(question)

def test_store_single_response(survey):
    survey.store_response('red')
    assert 'red' in survey.responses

def test_store_three_responses(survey):
    responses = ['red', 'green', 'blue']
    for response in responses:
        survey.store_response(response)

    for response in responses:
        assert response in survey.responses
