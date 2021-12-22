from pydantic import validator, ValidationError, BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class EventSource(Enum):
  raw = 'raw'
  queue = 'queue'
  schedule = 'schedule'

class BaseEvent(BaseModel):
  name: str
  source: EventSource
  time: Optional[datetime] # required for EventSource.schedule, "YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]"

  def handle(self):
    raise NotImplementedError(f"Event not implemented: {self.__class__.__name__}")

  @validator('time', always=True)
  def validate_time(cls, v, values, **kwargs):
    if values["source"]==EventSource.schedule and not v:
      raise ValueError('time is required for scheduled event')
    return v
