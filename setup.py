#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='create_shortcuts',
    version="0.1",
    description='Shortcuts for commonly used programs. To be used with Buildout.',
    author='Vladimir Shulyak',
    author_email='vladimir@shulyak.net',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'up = create_shortcuts.commands:up',
            'build = create_shortcuts.commands:build',
            'django = create_shortcuts.commands:django',
            'djsh = create_shortcuts.commands:djsh',
            'djtest = create_shortcuts.commands:djtest',
        ]
    }
)