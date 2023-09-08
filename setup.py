import setuptools
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

from mysqltop import VERSION

setuptools.setup(
    name="mysqltop",
    version=VERSION,
    author="ponponon",
    author_email="1729303158@qq.com",
    maintainer='ponponon',
    maintainer_email='1729303158@qq.com',
    license='MIT License',
    platforms=["all"],
    description="docker cli with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ponponon/mysqltop",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mysqltop=mysqltop.cli.main:cli',
        ]
    },
    install_requires=[
        'click',
        'tabulate[widechars]'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
