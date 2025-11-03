import requests

class LLMClient:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def query(self, prompt: str) -> str:
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'prompt': prompt,
            'max_tokens': 150
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get('choices')[0].get('text').strip()

# Example usage:
# client = LLMClient(api_key='your_api_key', api_url='https://api.llm.example.com/v1/engines/davinci/completions')
# result = client.query('Analyze the latest figure skating results.')
# print(result)