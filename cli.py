profile = "varokas"
queue_name = "serverless-python-starter-events"

import click
import boto3
from typing import Optional

from backend import TestEvent
from lib.event import EventSource

@click.group()
def cli():
    pass

@click.command("testevent")
@click.argument('text', required=True, type=click.UNPROCESSED)
def testevent(text: str):
  event = TestEvent(name = "TestEvent", source = EventSource.queue, text = text)

  session = boto3.session.Session(profile_name=profile)
  sqs = session.resource('sqs')
  queue = sqs.get_queue_by_name(QueueName=queue_name)

  print(f"Sending Message: {event}")
  queue.send_message(
    MessageBody=event.json()
  )


cli.add_command(testevent)

if __name__ == '__main__':
    cli()