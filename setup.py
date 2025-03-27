from setuptools import setup, find_packages

setup(
    name="bioinfo",
    version="0.1.0",
    description="Bioinformatics algorithms",
    author="Alex BUTEAU",
    author_email="alexbuteau1@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    python_requires=">=3.6",
)
