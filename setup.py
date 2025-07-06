from setuptools import setup, find_packages

setup(
    name="billcraft",
    version="0.1.0",
    author="SABBIR28",
    author_email="your@email.com",
    description="Modular PDF invoice generator for e-commerce",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sabbir28/billcraft",  # update with your repo
    packages=find_packages(),
    install_requires=[
        "fpdf==1.7.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
