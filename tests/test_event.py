import pytest
from pydantic import ValidationError
from datetime import datetime

from lib.event import BaseEvent, EventSource

def test_baseevent_with_schedule():
  with pytest.raises(ValidationError):
    BaseEvent(name="123", source=EventSource.schedule)

  BaseEvent(name="123", source=EventSource.schedule, time = "2021-12-21T15:34:19Z")

  with pytest.raises(ValidationError):
    BaseEvent(name="123", source=EventSource.schedule, time = "2021-12-21T15:34:19 4546")
