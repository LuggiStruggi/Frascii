from setuptools import setup, find_packages
from frascii import __version__

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(	
		name='frascii', version=__version__,
		url='https://github.com/LuggiStruggi/Frascii.git',
		author='Lukas König',
		author_email='lukasmkoenig@gmx.net',
		packages=find_packages(),
		long_description=long_description,
    	long_description_content_type='text/markdown',
		entry_points={'console_scripts': ['frascii=frascii.commands:cmd_main']},
		decription="DESCRIPTION"
	)
