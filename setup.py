from setuptools import setup
from setuptools import find_packages


with open('requirements.txt', 'rb') as req:
    REQUIREMENTS = [r for r in req.read().split() if r]

setup(
    name='seq2seq',
    version='1.0.0',
    description='Sequence to Sequence Learning with Keras',
    author='Fariz Rahman',
    author_email='farizrahman4u@gmail.com',
    url='https://github.com/farizrahman4u/seq2seq',
    license='GNU GPL v2',
    install_requires=REQUIREMENTS,
    packages=find_packages()
)
