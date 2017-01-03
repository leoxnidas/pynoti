import os

from pynoti import __author__, __email__, __license__, __version__
from setuptools import find_packages, setup


def read(filename):
    content = ''
    with open(filename, 'r') as file:
        content = file.read()
    return content

short_description = 'easy to use python wrapper for notify-send program.'
packages = find_packages()
name = 'pynoti'
url = download_url = 'https://github.com/leoxnidas/pynoti'
current_dir = os.path.dirname(os.path.abspath(__file__))
long_description = read(os.path.join(os.path.dirname(__file__), "README.md"))

setup(
    name=name,
    version=__version__,
    url=url,
    download_url=download_url,
    license=__license__,
    description=short_description,
    long_description=long_description,
    author=__author__,
    author_email=__email__,
    packages=packages,
    keywords='desktop notification notify-send',
    platforms=['linux'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)