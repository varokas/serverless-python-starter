from aws_lambda_powertools.utilities import data_classes
from aws_lambda_powertools.utilities.data_classes import SQSEvent
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord
from aws_lambda_powertools.utilities.data_classes.event_bridge_event import EventBridgeEvent
from aws_lambda_powertools.utilities.typing import LambdaContext
from typing import cast, List, Dict, Optional
import json

from lib.event import BaseEvent

### Events 
class TestEvent(BaseEvent):
  text: Optional[str]

  def handle(self):
    print(self)

SUPPORTED_EVENTS:List[BaseEvent] = [TestEvent]

## Handlers
EVENTS_HANDLERS:Dict[str, BaseEvent] = { c.__name__: c for c in SUPPORTED_EVENTS}

def handler(event:dict, context: LambdaContext):
  if "name" in event:
    # Raw Event / Scheduled
    handle_event(event, context)
  elif "Records" in event:
    # SQS Records
    sqsEvent = SQSEvent(event)
    for record in sqsEvent.records:
      handle_event(json.loads(record.body), context)
  else:
    raise ValueError(f"Expected SQS or Raw Event: {event}")

def handle_event(json_body:dict, context: LambdaContext):
  if not "name" in json_body:
    raise ValueError(f"No name in event")
  name = json_body["name"]

  if name not in EVENTS_HANDLERS:
    raise ValueError(f"Unrecognized Event name: {name}")

  print(f"Received Event: name={name}")

  return EVENTS_HANDLERS[name].parse_obj(json_body).handle()
  