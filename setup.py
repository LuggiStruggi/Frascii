from setuptools import setup, find_packages
from frascii import __version__

def readme():
    with open('README.md', 'r', encoding="utf-8") as f:
        content = f.read()
    return content

setup(	
		name='frascii', version=__version__,
		url='https://github.com/LuggiStruggi/Frascii.git',
		author='Lukas König',
		author_email='lukasmkoenig@gmx.net',
		packages=find_packages(),
		long_description=readme(),
    	long_description_content_type='text/markdown',
		entry_points={'console_scripts': ['frascii=frascii.commands:cmd_main']},
		decription="DESCRIPTION"
	)
