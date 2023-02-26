from setuptools import setup, find_packages
from frascii import __version__

setup(	
		name='frascii', version=__version__,
		url='https://github.com/LuggiStruggi/Frascii.git',
		author='Lukas König',
		author_email='lukasmkoenig@gmx.net',
		packages=find_packages(),
		entry_points={'console_scripts': ['frascii=frascii.commands:cmd_main']},
		decription="DESCRIPTION"
	)
