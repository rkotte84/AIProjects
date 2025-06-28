import os
import base64
import json
from openai import AzureOpenAI

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1")
subscription_key = os.getenv("AZURE_OPENAI_KEY")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Who is Apparao"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "The name \"Apparao\" (sometimes spelled \"Appa Rao\") is a common South Indian given name and surname, particularly among Telugu-speaking communities. Without additional context, it is difficult to specify exactly which \"Apparao\" you are referring to, as there are many notable individuals with this name. Here are a few well-known personalities named Apparao:\n\n1. **Nookala Appa Rao** – An Indian classical vocalist of the Carnatic tradition and Padma Bhushan awardee.\n2. **Appa Rao Podile** – An Indian scientist, former Vice-Chancellor of the University of Hyderabad.\n3. **Apparao M. Rao** – An Indian-born physicist, known for his contributions in nanoscience and nanotechnology.\n4. **Kavikondala Venkata Appa Rao** – A noted Telugu writer and poet from Andhra Pradesh.\n\nIf you have a specific field (science, literature, politics, etc.) or more details, please provide them, and I can give a more precise answer!"
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(json.dumps(completion.model_dump(), indent=2))
