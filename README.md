# Serverless Python Starter

Starter project for python based lambda project.

## Features
- [X] FastAPI - Frontend dev with Hot Reload
- [X] API Gateway Integration (+root proxy)
- [X] Local Dev without API Gateway
- [X] Backend with Typings
- [X] Backend Scheduler Support  - in a separate function
- [X] Backend SQS Support
- [X] S3 and DynamoDB IAM role
- [X] Pulumi Example 
- [X] Shared Lib between Frontend and Backend
- [X] PyTest
- [] Deploy via Github Action

## Prerequisite
* Python 3.9
* NodeJS 12+
* Pulumi (to create Queue and DynamoDB)
* AWS Profile set up - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

## Install
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

# Open `serverless.yml` and change `profile:` and `region:` to match
# Also uncomment API Gateway event 

$ npx serverless plugin install -n serverless-python-requirements

# If using pulumi
$ cd pulumi-example
$ npm install

# change pulumi.dev.yaml
config:
  aws:region: us-west-2
  aws:profile: varokas --- profile

$ pulumi up
```

## Dev
```
$ source .venv/bin/activate
$ uvicorn main:app --reload

$ curl localhost:8000/hello
{"message":"Hello World"}%

# Docs can be found at - http://127.0.0.1:8000/docs
```

## Serverless Dev
```
$ npx serverless invoke local -f backend -d '{"name": "TestEvent", "source":"raw", "text": "123"}'
$ npx serverless invoke local -f backend -d '{"name": "TestEvent", "source":"schedule", "time":"2021-12-21T15:34:19Z", "text": "123"}'

$ npx serverless deploy

$ python3 cli.py testevent Hello

$ npx serverless logs -f backend
```

## Github Actions
Go to Settings, Secrets and set the two secret values
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

## References
* https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless
* https://towardsaws.com/local-development-with-serverless-46a219876a67
* https://github.com/tschoffelen/lambda-sample-events
* https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/