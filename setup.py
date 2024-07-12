from typing import List
from setuptools import find_packages,setup

def get_requirements(file_path:str)->List[str]:
    '''
    This function is going to return list of requirements from the requirements.txt file
    '''
    requirements_list = []
    with open(file_path) as f:
        requirements_list = f.readlines()
        requirements_list = [req.replace("\n", "") for req in requirements_list]

        if '-e .' in requirements_list:
            requirements_list.remove('-e .')
            
    return requirements_list


setup(
name='ml_e2e_project',
version='0.0.1',
author='Simant',
author_email='simantnigam@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
