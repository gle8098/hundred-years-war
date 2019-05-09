import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hundred-years-war-gle8098",
    version="0.1." + os.environ['TRAVIS_BUILD_ID'],
    author="gle8098",
    author_email="gle8098@yandex.ru",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gle8098/hundred-years-war",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)