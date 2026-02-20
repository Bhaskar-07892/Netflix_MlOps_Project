from setuptools import setup , find_packages 
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the given file, 
    excluding the '-e .' line used for editable installs.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='netflix_analyzer',
    version='0.0.1',
    description="Netflix Data Analyzer - Mini MLOps Project",
    author='Bhaskar Pathak',
    author_email='bhaskarpathak5607@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt')
)