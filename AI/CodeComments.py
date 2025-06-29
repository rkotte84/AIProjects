import openai
import os

def generate_code_comments_csharp(code: str) -> str:
    """
    Uses Azure OpenAI GPT-4 to generate meaningful code comments for a C# code snippet.
    """
    prompt = (
        "You are an expert C# developer. Add meaningful XML documentation comments and inline comments to the following legacy C# code. "
        "Only return the improved code with comments, do not explain your changes.\n\n" + code
    )
    response = openai.ChatCompletion.create(
        engine=os.getenv("DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=2048
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    # Set up Azure OpenAI configuration from environment variables
    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_ENDPOINT")
    openai.api_version = "2025-01-01-preview"
    openai.api_key = os.getenv("AZURE_KEY")

    # Read the input C# file
    with open("text.cs", "r", encoding="utf-8") as f:
        legacy_code = f.read()
    # Generate commented code
    commented_code = generate_code_comments_csharp(legacy_code)
    # Write the output to a new file
    with open("text_file.cs", "w", encoding="utf-8") as f:
        f.write(commented_code)
