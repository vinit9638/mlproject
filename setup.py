from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Meta data of the project
setup(
name = "mlproject", # Name of the module or package
version = "0.0.1", # Version of my package 
author="vinit", # Author name
author_email="hetvinitprajapati@gmail.com", # Author email
packages=find_packages(), # It will find the folder having file name "__init__.py", and consider is as a package
install_requires =get_requirements('requirements.txt'),
)