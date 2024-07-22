from setuptools import setup, find_packages
from pathlib import Path


with open("README.md", "r", encoding="UTF-8") as f:
     readme = f.read()


setup_args = dict(
    name='busnearby',
    version='0.1.2',
    description='A library to get bus times from the Bus Nearby API',
    long_description_content_type="text/markdown",
    long_description=readme,
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.7',
    author='Tomer Klein',
    author_email='tomer.klein@gmail.com',
    keywords=['public transportation', 'bus', 'trains','home automation'],
    url='https://github.com/t0mer/py-busnearby',
    download_url='https://github.com/t0mer/py-busnearby/',
    project_urls={
        "Documentation": "https://github.com/t0mer/py-busnearby",
        "Source": "https://github.com/t0mer/py-busnearby",
    },
)



install_requires=[
        'aiohttp>=3.8.0',
     ]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
