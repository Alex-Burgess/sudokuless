# tryNewPuzzle

## Description
This API is called by a user submits a finished sudoku puzzle.  The service retrieves the puzzle solution from an s3 bucket which is used to compare against the users solution attempt.

## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* Python dependencies, e.g. pytest, boto3, moto.
* [Docker installed](https://www.docker.com/community-edition)
* An S3 bucket with the solutions for the unsolved puzzles that users attempt.

## Setup process
Create an S3 bucket to store the SAM builds:
```
aws cloudformation create-stack --stack-name sam-builds-getnewpuzzlesolution --template-body file://sam-builds-bucket.yaml
```

## Packaging and deployment
Package our Lambda function to S3:

```
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket sam-builds-getnewpuzzlesolution
```

Create a Cloudformation Stack and deploy your SAM resources.

```
sam deploy \
    --template-file packaged.yaml \
    --stack-name Service-GetNewPuzzleSolution \
    --capabilities CAPABILITY_NAMED_IAM
```

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:
```
aws cloudformation describe-stacks \
    --stack-name Service-GetNewPuzzleSolution \
    --query 'Stacks[].Outputs[?OutputKey==`PuzzleSolutionApi`]' \
    --output table
```

## Fetch, tail, and filter Lambda function logs
Sam logs lets you fetch logs generated by your Lambda function from the command line. (In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.)
```
sam logs -n UnsolvedPuzzleFunction --stack-name Service-GetNewPuzzleSolution --tail
```

## Testing
To execute `pytest` against our `tests` folder to run our initial unit tests:
```
python -m pytest tests/ -v
```

## Local development

**Invoking function locally through local API Gateway**
```
sam local start-api
```
If the previous command ran successfully you should now be able to hit the following local endpoint to invoke your function `http://localhost:3000/tryNewPuzzle`

**Invoking function locally using a local sample payload**
```
(generate event if required - sam local generate-event apigateway aws-proxy > event.json)
sam local invoke UnsolvedPuzzleFunction --event tests/events/event.json
```

## Cleanup

In order to delete our Serverless Application recently deployed you can use the following AWS CLI Command:

```
aws cloudformation delete-stack --stack-name Service-GetNewPuzzleSolution
```

# Appendix
## SAM and AWS CLI commands

All commands used throughout this document

```
# Generate event.json via generate-event command
sam local generate-event apigateway aws-proxy > event.json

# Invoke function locally with event.json as an input
sam local invoke PuzzleSolutionFunction --event event.json

# Run API Gateway locally
sam local start-api

# Package Lambda function defined locally and upload to S3 as an artifact
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket sam-builds-getnewpuzzlesolution

# Deploy SAM template as a CloudFormation stack
sam deploy \
    --template-file packaged.yaml \
    --stack-name Service-GetNewPuzzleSolution \
    --capabilities CAPABILITY_IAM

# Describe Output section of CloudFormation stack previously created
aws cloudformation describe-stacks \
    --stack-name Service-GetNewPuzzleSolution \
    --query 'Stacks[].Outputs[?OutputKey==`UnsolvedPuzzleFunctionApi`]' \
    --output table

# Tail Lambda function Logs using Logical name defined in SAM Template
sam logs -n UnsolvedPuzzleFunction --stack-name Service-GetNewPuzzleSolution --tail

# Deploy the API Manually:
aws apigateway get-rest-apis --query 'items[?name==`Service-GetNewPuzzleSolution`].{name:name, ID:id}'

aws apigateway get-stages --rest-api-id <api-id> --query 'item[?stageName==`Prod`].{stageName:stageName, deploymentId:deploymentId}'

aws apigateway update-stage \
 --rest-api-id <api-id> \
 --stage-name Prod \
 --patch-operations op='replace',path='/deploymentId',value='<deployment-id>'
```