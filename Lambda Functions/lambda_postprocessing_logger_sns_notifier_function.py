import json
import boto3
 
def lambda_handler(event, context):
    job_name = event['detail']['jobName']
    state = event['detail']['state']
    run_id = event['detail']['jobRunId']
 
    message = f"Glue job '{job_name}' finished with state: {state}, Run ID: {run_id}"
    print("Event received:", json.dumps(event))
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:899274783510:glue-job-alerts',  # Replace with your actual ARN
        Message=message,
        Subject='Glue Job Status'
    )
 
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent.')
    }