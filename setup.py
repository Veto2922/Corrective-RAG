from setuptools import setup, find_packages

setup(
    name="Corrective RAG",  # Replace with your package name
    version="0.1.0",  # Versioning
    author="Abdelrahman Moahmed",
    author_email="Abdelrahman.m2922@gmail.com",
    description="Corrective RAG (Retrieval-Augmented Generation) is an advanced approach to RAG that **iteratively refines retrieved documents** to improve the final response quality.",
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically find all packages
    python_requires=">=3.10",
)
