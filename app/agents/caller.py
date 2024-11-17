
import openai
from  openai import OpenAI
import google.generativeai as genai
import anthropic
import requests



# OpenAI

class OpenAICaller:
    def __init__(self, api_key) -> None:
        self.openai_client = OpenAI(api_key=api_key)
        

    def call_openai(self,system_prompt, user_prompt, model="gpt-4o-mini", temperature = 0.5, top_p = 0.5):
        """
        Calls the OpenAI API with the given system and user prompts.

        Args:
            system_prompt: The system prompt for the OpenAI API.
            user_prompt: The user prompt for the OpenAI API.

        Returns:
            The response from the OpenAI API.  Returns None if there's an error.
        """
        try:
            
            response = self.openai_client.chat.completions(
                model=model,  
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
                top_p=top_p
            )

            return response.choices[0].message['content']
        except openai.error.OpenAIError as e:
            print(f"OpenAI API error: {e}")
            return None


# Gemini 

class GeminiCaller:
    """
        Calls the Gemini API with the given system and user prompts using the google-generativeai library.

        Args:
            system_prompt: The system prompt for the Gemini API.
            user_prompt: The user prompt for the Gemini API.
            model: The name of the Gemini model to use. Defaults to "models/gemini-pro".  Check Google's documentation for available models.

        Returns:
            The response from the Gemini API. Returns None if there's an error.
    """
    def __init__(self, api_key) -> None:
        self.api_key = api_key
    
    def call_gemini(self, system_prompt, user_prompt, model = "gemini-1.5-flash"):
        model=genai.GenerativeModel(
            model_name=model,
            system_instruction=system_prompt)
        response = model.generate_content(user_prompt)
        return response.text



# Anthropic/Claude


class AnthropicClient:
    def __init__(self, api_key):
        client = anthropic.Anthropic(
            # defaults to os.environ.get("ANTHROPIC_API_KEY")
            api_key=api_key,
        )

    def call_anthropic(self, system_prompt, user_prompt, model="claude-3-5-sonnet-20241022", temperature=0.5, top_p=0.5):
        """
        Calls the Anthropic API with the given system and user prompts.

        Args:
            system_prompt: The system prompt for the Anthropic API.
            user_prompt: The user prompt for the Anthropic API.
            model: The name of the Anthropic model to use. Defaults to "claude-v2".
            temperature: Controls the randomness of the response.  Higher values (e.g., 1.0) result in more random responses.
            top_p: Controls the diversity of the response.  Lower values (e.g., 0.1) result in more focused responses.

        Returns:
            The response from the Anthropic API. Returns None if there's an error.
        """
        try:
            response = anthropic.Completion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                top_p=top_p,
            )
            return response.completion
        except Exception as e:
            print(f"Anthropic API error: {e}")
            return None
        
# Ollama 

class OllamaCaller:
    def __init__(self, server_url="http://localhost:8000"):
        self.server_url = server_url

    def call_ollama(self, model_name, system_prompt, user_prompt):
        """
        Calls the Ollama server with the given model name, system prompt, and user prompt.

        Args:
            model_name: The name of the model to use.
            system_prompt: The system prompt for the model.
            user_prompt: The user prompt for the model.

        Returns:
            The response from the Ollama server. Returns None if there's an error.
        """
        try:
            # Format the prompts according to the model's requirements
            formatted_prompts = self.format_prompts(model_name, system_prompt, user_prompt)

            # Make a request to the Ollama server
            response = self.send_request(model_name, formatted_prompts)

            return response
        except Exception as e:
            print(f"Ollama server error: {e}")
            return None

    def format_prompts(self, system_prompt, user_prompt,prompt_format = "openai"):
        """
        Add supported prompt formats here
        "openai"
        "llama"
        
        
        """

        # Example formatting logic; adjust as needed for specific models
        if prompt_format == "openai":
            return [
                        {"role":"system","content":system_prompt},
                        {"role":"user", "content":user_prompt}
                    ]
        elif prompt_format == "something else":
            return f"[SYS]{system_prompt}[USR]{user_prompt}"
        else:
            return f"{system_prompt}\n{user_prompt}"

    def send_request(self, model_name, formatted_prompts):
        try:
            # Define the endpoint URL
            url = f"{self.server_url}/models/{model_name}/generate"

            # Define the payload
            payload = {
                "prompts": formatted_prompts
            }

            # Send the POST request
            response = requests.post(url, json=payload)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json().get('result', 'No result found')
            else:
                print(f"Failed to call model: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None