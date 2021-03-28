"""A build script using setuptools for the seligimus package."""
import pathlib
from typing import List

import setuptools  # type: ignore

_HERE = pathlib.Path(__file__).parent

_README = _HERE / 'README.md'
_LONG_DESCRIPTION = _README.read_text()

_VERSION_FILE = _HERE / 'VERSION.txt'
_VERSION = _VERSION_FILE.read_text()

_PACKAGES: List[str] = setuptools.find_packages(where=_HERE, include=['seligimus*'])

setuptools.setup(
    name='seligimus',
    version=_VERSION,
    author='Austin Scola',
    author_email='austinscola@gmail.com',
    description='A mono-library.',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/AustinScola/seligimus',
    packages=_PACKAGES,
    package_data={'seligimus': ['py.typed']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed',
    ],
    python_requires='>=3.6',
)
