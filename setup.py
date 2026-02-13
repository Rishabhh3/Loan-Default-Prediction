from setuptools import find_packages, setup
from typing import List

def get_requirements() ->List[str]:
    requirements_list:list[str]=[]
    try:
        with open('requirements.txt','r')as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='e':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt not found")

    return requirements_list


setup(
    name= "Loan Default Detection System",
    version="0.0.1",
    author="Rishabh",
    author_email="rishabhchamoli0120@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)