import json

import boto3
 
def lambda_handler(event, context):

    glue = boto3.client('glue')

    # Optional: print event for debugging

    print("Event received:", json.dumps(event))
 
    response = glue.start_job_run(

        JobName='Spotify-Job-team4'  # Replace with your Glue job name exactly

    )

    return {

        'statusCode': 200,

        'body': json.dumps(f"Started Glue job: {response['JobRunId']}")

    }

 