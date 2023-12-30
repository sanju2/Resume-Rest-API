import json

def lambda_handler(event, context):
    json_data = [
        # Your JSON Code
    ]

    json_str = json.dumps(json_data, indent=4)

    return {'statusCode': 200,
            'body': json_str
            }