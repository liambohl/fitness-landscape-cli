"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from placeholder_name import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['pytest', '--cov=placeholder_name', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='Fitness landscape command line interface',
    version=__version__,
    description='Command-line interface for adding data from evolution experiments to the fitness landscape database',
    long_description=long_description,
    url='https://github.com/liambohl/fitness-landscape-cli',
    author='Liam Bohl',
    author_email='liambohl@gmail.com',
    license='UNLICENSE',
    classifiers=[
        'Intended Audience :: Evolution researchers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'placeholder_name=placeholder_name.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
