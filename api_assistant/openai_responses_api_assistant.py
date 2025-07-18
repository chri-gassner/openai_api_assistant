from openai import OpenAI, NOT_GIVEN
import os

from openai.types.responses.response_input_param import Message



class OpenAIResponsesApiAssistant:
    def __init__(self, assistant_id: str = None, api_key: str = None, system_prompt: str = None,
                 model: str = "gpt-4.1-nano"):
        api_key = os.getenv("OPENAI_API_KEY") if api_key is None else api_key
        self.client = OpenAI(api_key=api_key)
        self.assistant_id = None if assistant_id is None else assistant_id
        self.system_prompt = NOT_GIVEN if system_prompt is None else system_prompt
        self.response_format = NOT_GIVEN
        self.message_history = [{"role": "system", "content": self.system_prompt}]
        self.model_str = model

    def set_response_format(self, response_format: str):
        self.response_format = response_format

    def set_system_prompt(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.message_history = [{"role": "system", "content": self.system_prompt}]

    def write_history_to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            for message in self.message_history:
                file.write(f"{message['role']}: {message['content']}\n")

    def retrieve_response(self, message: str, print_response: bool = True):
        self.message_history.append({"role": "user", "content": message})
        response = self.client.responses.create(
            model=self.model_str,
            input=self.message_history[-1].get("content"),
            previous_response_id=self.message_history[-1].get("id", NOT_GIVEN),
            text=self.response_format,
            instructions=self.system_prompt
        )
        self.message_history.append({"role": "assistant", "content": response.output[0].content[0].text, "id": response.id})
        if print_response:
            print(response.output[0].content[0].text)
        return response

    def clear_history(self):
        self.message_history = [{"role": "system", "content": self.system_prompt}]


"""x = OpenAIResponsesApiAssistant()
x.retrieve_response("Hello World")

for message in x.message_history:
    print(f"{message['role']}: {message['content']}")"""
