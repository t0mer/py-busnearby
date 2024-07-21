from setuptools import setup, find_packages

setup(
    name='busnearby',
    version='0.1.0',
    description='A library to get bus times from the Bus Nearby API',
    author='Tomer Klein',
    author_email='tomer.klein@gmail.com',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.8.0',
    ],
    python_requires='>=3.7',
)