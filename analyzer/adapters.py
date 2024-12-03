from abc import abstractmethod

import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel


class GenericAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def get_connection(self) -> any:
        raise NotImplementedError()

    @abstractmethod
    def generate_resposne(self, prompt: str) -> any:
        raise NotImplementedError()


class GeminiAnalyzer(GenericAnalyzer):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.model: GenerativeModel = GenerativeModel("gemini-1.5-flash")

    def get_connection(self) -> any:
        genai.configure(api_key=self.api_key)

    def generate_resposne(self, prompt: str) -> any:
        return self.model.generate_content(prompt).text
