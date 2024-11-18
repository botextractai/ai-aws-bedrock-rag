import boto3

# Set the Amazon Web Services (AWS) region name (for example "us-east-1")
aws_region_name = 'REPLACE_THIS_WITH_YOUR_AWS_REGION_NAME'

# Connect to AWS with your AWS credentials
session = boto3.Session(
    aws_access_key_id='REPLACE_THIS_WITH_YOUR_AWS_ACCESS_KEY_ID',
    aws_secret_access_key='REPLACE_THIS_WITH_YOUR_AWS_SECRET_ACCESS_KEY'
)

# Define the Bedrock agent runtime
bedrock_agent_rn = session.client(service_name='bedrock-agent-runtime', region_name=aws_region_name)

# Define the method to invoke the RetrieveAndGenerate API
# You can use any Bedrock Foundation Model (LLM) of your choice
def retrieveAndGenerate(input, guardrail_Id, kb_Id):
    return bedrock_agent_rn.retrieve_and_generate(
        input={
            'text': input
        },
        retrieveAndGenerateConfiguration={
            'knowledgeBaseConfiguration': {
                'generationConfiguration': {
                    'guardrailConfiguration': {
                        'guardrailId': guardrail_Id,
                        'guardrailVersion': 'DRAFT'
                    }
                },
                'knowledgeBaseId': kb_Id,
                'modelArn': 'arn:aws:bedrock:' + aws_region_name + '::foundation-model/anthropic.claude-v2'
            },
            'type': 'KNOWLEDGE_BASE'
        }
    )

# Invoke the API to generate the desired response
response = retrieveAndGenerate("Summarise the recommendations for Artificial Intelligence usage within investment management", "REPLACE_THIS_WITH_YOUR_GUARDRAIL_ID", "REPLACE_THIS_WITH_YOUR_KNOWLEDGE_BASE_ID")["output"]["text"]
print(response)
