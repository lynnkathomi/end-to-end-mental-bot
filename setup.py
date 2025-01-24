from setuptools import find_packages, setup

setup(
    name='generative-ai-project',  # Changed to use hyphens instead of spaces
    version='0.1.0',  # Changed to semantic versioning
    author='Bappy Ahmed',  # Added author name
    author_email='entbappy73@gmail.com',  # Removed duplicate
    description='A generative AI project for mental health chatbot',  # Added description
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'streamlit',
        'langchain',
        'python-box',
        'PyYAML'
    ],
    python_requires='>=3.8'  # Added Python version requirement
)