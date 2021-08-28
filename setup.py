"""Python setup.py for python_from_template package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_from_template", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_from_template",
    version=read("python_from_template", "VERSION"),
    description="Awesome python_from_template created by jovyan123-playground",
    url="https://github.com/jovyan123-playground/python-from-template/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jovyan123-playground",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_from_template = python_from_template.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
