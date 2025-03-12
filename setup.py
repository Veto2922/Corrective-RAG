from setuptools import setup, find_packages

setup(
    name="your_project_name",  # Replace with your package name
    version="0.1.0",  # Versioning
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your project",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_project",  # Replace with your repo
    packages=find_packages(),  # Automatically find all packages
    python_requires=">=3.10",
)
