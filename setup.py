from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name='emoticon',
    version='1.0.4',
    description='python package to transform any emoticon to text or its meaning',
    long_description=readme(),
    long_description_content_type='text/markdown',
    github='https://github.com/egafdharmawan/emoticon',
    author='Ega Febri Dharmawan',
    author_email='egafebridh@gmail.com',
    license='MIT',
    classifiers={
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    },
    packages=['emoticon'],
    include_package_data=True,
    install_requires=['NLTK','mtranslate','csv']
)