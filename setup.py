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
            'build = create_shortcuts.commands:build',
            'up = create_shortcuts.commands:up',
            'django = create_shortcuts.commands:django',
            'djsh = create_shortcuts.commands:djsh',
            'djtest = create_shortcuts.commands:djtest',
            'flake8 = create_shortcuts.commands:flake8',
            'killcelery = create_shortcuts.commands:killcelery',
            'runsp = create_shortcuts.commands:runsp',
            'sh = create_shortcuts.commands:sh',
            'stop = create_shortcuts.commands:stop',
        ]
    }
)
