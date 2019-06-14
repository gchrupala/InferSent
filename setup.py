from setuptools import setup
setup(
    name='infersent',
    version='1.0',
    url='https://github.com/gchrupala/InferSent',
    packages=['infersent'],
    license='Attribution-NonCommercial 4.0 International',
    description='Neural representation analysis with representational similarity',
    install_requires = [
        'torch == 1.1.0',
        'nltk ==  3.4'
        ]
)

