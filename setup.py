from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    """    """
    requirements=[]
    HYPHEN_E_DOT='-e .'

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(name='DMLProject',
      version='1.0',
      description='Python MLProject',
      author='Ahmad',
      author_email='ahmadmponda@gmail.com',
      url='https://www.google.com/mails',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
     )