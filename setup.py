from setuptools import find_packages, setup

def get_requirements():

    requirements = []

    try:
        with open('requirements.txt', 'r') as file:

            # Read Lines from the File
            lines = file.readlines()
            
            # Append Requirements
            for requirement in lines:
                requirement = requirement.strip()
                if requirement and requirement != '-e .':
                    requirements.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirements

setup(
    name = "Network-Security",
    version = "0.0.0.1",
    author = "Mohammed Hamdy",
    author_email = "mohamedhamdy2111@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)