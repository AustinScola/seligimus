"""A build script using setuptools for the seligimus package."""
import pathlib

import setuptools  # type: ignore

_HERE = pathlib.Path(__file__).parent

_README = _HERE / 'README.md'
_LONG_DESCRIPTION = _README.read_text()

setuptools.setup(
    name='seligimus',
    version='0.1.0',
    author='Austin Scola',
    author_email='austinscola@gmail.com',
    description='A mono-library.',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    packages=['seligimus'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
