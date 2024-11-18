# Serverless Retrieval-Augmented Generation (RAG) in Amazon Web Services (AWS) Bedrock

This example shows serverless RAG in AWS Bedrock. It uses a Bedrock Knowledge Base (semantic database) and Bedrock Guardrails, which protect against prompt attacks, malicious input, and inappropriate output.

The key benefits of Knowledge Bases in Bedrock include the following:

- Seamless RAG workflow: There is no need to set up and manage the components yourself. You can just provide your data and let Bedrock handle ingestion, embedding, storage, and querying.
- Custom vector embeddings: Your data is ingested and converted into vector representations tailored to your use case with a choice of embedding models.
- Attribution and memory: The `RetrieveAndGenerate` API within Bedrock provides attribution back to source documents and manages conversation history for contextual responses.
- Flexible integration: Incorporate RAG into your workflows with API access and integration support for other generative Artificial Intelligence (AI) tools.

This example also includes Bedrock Guardrails. Guardrails can foil prompt attacks, stop malicious input, and prevent inappropriate output. You can create Guardrails either via program code, or through the Bedrock section of the AWS Management Console. If (as in this example) no explicit Guardrail version is set, then the Guardrail version will automatically be `DRAFT`. If you set a version, then you will have change this setting in the `main.py` script.

In the `RetrieveAndGenerate` API, the generated response output contains three components: The text of the model-generated response itself, source attribution indicating where the Large Language Model (LLM) retrieved information from, and the specific text excerpts that were retrieved from those sources as part of generating the response. This API provides full transparency by returning not just the final output text, but also the underlying source materials and attributions that informed the LLM's response generation process. This allows users to inspect both the final output, as well as the intermediate retrieved texts that were used by the system during response generation.

Please note that you might first have to enable any LLM (Foundation Model) that you want to use in Bedrock for your desired region, before you can use it. This process includes agreeing to the end user licensing agreement for the desired LLM.

## AWS account requirement

For this example, you need an AWS account. If you just want to try out AWS, then you can get a [AWS Free Tier account](https://aws.amazon.com/free/) for a year. This gives you a fair amount of free AWS usage.

In the AWS Management Console, under "IAM" -> "Security credentials", you will have to create an API key and secret. You will need to enter your AWS API key (access key) and you AWS API secret access key into the `main.py` script.

## Setup

1. In the AWS Management Console, create a S3 (file storage) bucket with your document(s). You can use the example `AI_Report.pdf` document that is provided in the `data` folder. [Follow these instructions to create a S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
2. In the Bedrock section of the AWS Management Console, create a Knowledge Base that uses your S3 bucket as data source. [Follow these instructions to create a Knowledge Base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html). At the end of this process, you will get a Knowledge Base ID that you will have to insert into the `main.py` script.
3. In the Bedrock section of the AWS Management Console, create Guardrails. [Follow these instructions to create Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html). At the end of this process, you will get a Guardrail ID that you will have to insert into the `main.py` script.

## Usage

You can enter your prompt in the `main.py` script, for example (if your Knowledge Base contains the provided example PDF document):

```
Summarise the recommendations for Artificial Intelligence usage within investment management
```

To test the Guardrails, you can try prompt attacks, malicious prompts, and check, if you can get inappropriate answers.
