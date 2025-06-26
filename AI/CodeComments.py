import openai

# Azure OpenAI configuration
AZURE_OPENAI_ENDPOINT = "<YOUR_AZURE_OPENAI_ENDPOINT>"  # e.g., https://<your-resource-name>.openai.azure.com/
AZURE_OPENAI_KEY = "<YOUR_AZURE_OPENAI_KEY>"
DEPLOYMENT_NAME = "<YOUR_DEPLOYMENT_NAME>"  # e.g., gpt-4-0

openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2024-02-15-preview"
openai.api_key = AZURE_OPENAI_KEY

def generate_code_comments_csharp(code: str) -> str:
    """
    Uses Azure OpenAI GPT-4.0 to generate meaningful code comments for a C# code snippet.
    """
    prompt = (
        """You are an expert C# developer. Add meaningful XML documentation comments and inline comments to the following legacy C# code. 
        Only return the improved code with comments, do not explain your changes.\n\n""" + code
    )
    response = openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=2048
    )
    return response["choices"][0]["message"]["content"]

# Example usage:
if __name__ == "__main__":
    # Read your C# file
    with open("test.cs", "r", encoding="utf-8") as f:
        legacy_code = f.read()
    commented_code = generate_code_comments_csharp(legacy_code)
    with open("test_file.cs", "w", encoding="utf-8") as f:
        f.write(commented_code)