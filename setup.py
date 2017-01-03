import os

from codecs import open
from pynoti import __author__, __email__, __license__, __version__
from setuptools import find_packages, setup


def read(filename):
    content = ''
    with open(filename, encoding='utf-8') as file:
        content = file.read()
    return content

short_description = 'easy to use python wrapper for notify-send program.'
packages = find_packages()
name = 'pynoti'
url = download_url = 'https://github.com/leoxnidas/pynoti'
current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    long_description = read(os.path.join(os.path.dirname(__file__), "README.md"))
except:
    long_description = 'no readme'

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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)