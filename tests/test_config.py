import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service


class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
