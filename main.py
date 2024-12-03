from dotenv import load_dotenv

from PyPDF2 import PdfReader
from analyzer.adapters import GeminiAnalyzer


def parse_cv():
    with open("CV.pdf", "rb") as file:
        reader = PdfReader(file)
        print(reader)


if __name__ == "__main__":
    import os

    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    analyzer = GeminiAnalyzer("GEMINI_API_KEY")
    response = analyzer.generate_resposne("Who is Albert Einstine?")
    print(response)
