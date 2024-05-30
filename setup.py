from setuptools import setup, find_packages

setup(
    name="MCQGenerator",
    version="0.1.0",
    description="Generate MCQs from given Data",
    author="Swapnil Podishetti",
    author_email="u83285@gmail.com",
    url="https://github.com/swapnil0402/MCQGEN",
    packages=find_packages(),
    install_requires=[
            "openai",
            "langchain",
            "streamlit",
            "python-dotenv",
            "PyPDF2",
            "huggingface_hub",
            "transformers",
            "accelerate",
            "bitsandbytes",
    ],
)