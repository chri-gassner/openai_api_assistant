from setuptools import setup, find_packages

setup(
    name="openai_responses_api_assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Christoph Gassner",
    description="This Package provides an easy to use interface to the OpenAI Responses API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/deinuser/dein_package",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)