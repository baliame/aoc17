from setuptools import *

description = 'Advent of Code 2017 solutions'

setup(
    name='aoc17',
    version='1.0.0',
    description=description,
    long_description=description,
    url='https://github.com/baliame/aoc17',
    author='Baliame',
    author_email='akos.toth@cheppers.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='aoc',
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'aocdbg=aoc17.day1:dbgin',
            'aoc1=aoc17.day1:main',
            'aoc1b=aoc17.day1:main2',
            'aoc2=aoc17.day2:main',
            'aoc2b=aoc17.day2:main2',
            'aoc3dbg=aoc17.day3:calc_dbg',
            'aoc3=aoc17.day3:main',
            'aoc3b=aoc17.day3:main2',
            'aoc4=aoc17.day4:main',
            'aoc4b=aoc17.day4:main2',
            'aoc5=aoc17.day5:main',
            'aoc5b=aoc17.day5:main2',
            'aoc6=aoc17.day6:main',
            'aoc6b=aoc17.day6:main2',
            'aoc7=aoc17.day7:main',
            'aoc7b=aoc17.day7:main2',
        ],
    }
)
