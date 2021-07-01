from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Get SFW Neko Images'
LONG_DESCRIPTION = 'A api wrapper that get links for SFW neko images and has a basic rate limit handler.'

# Setting up
setup(
    name="nekosfw",
    version=VERSION,
    author="Crain69 (Chirayu Prasai)",
    author_email="<chirayuprasai11@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['aiohttp'],
    keywords=['python', 'neko', 'sfw',
              'rate limit', 'handler', 'images'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
