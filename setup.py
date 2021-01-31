"""A build script using setuptools for the seligimus package."""
import setuptools  # type: ignore

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='seligimus',
    version='0.1.0',
    author='Austin Scola',
    author_email='austinscola@gmail.com',
    description='A mono-library.',
    long_description=long_description,
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
