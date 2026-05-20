import os, requests, json

api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
github_token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("GITHUB_REPOSITORY")
pr_number = os.getenv("PR_NUMBER")

DEPLOYMENT_NAME = "cloudpratice-ai"

def get_ai_rectification(issue):

    base_url = endpoint.split("/openai")[0].rstrip("/")
    url = f"{base_url}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2023-05-15"

    headers = {"Content-Type": "application/json", "api-key": api_key}
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a security expert. You are given a security issue and you need to rectify it."
            },
            {
                "role": "user",
                "content": f"The following is a security issue: {issue}. Please rectify it."
            }
        ]
    }

    print(f"Fetching AI rectification for issue: {issue}")
    response = requests.post(url, headers=headers, json=data)