from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="common_utils",
    version="0.1",
    include_package_data=True,
    python_requires='>=3.12',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="Sina Astani",
    author_email="sastani@meetklariva.com",
    description="Commonly used utilities in cloud run jobs for interacting with Google Cloud Storage and Postgres",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)