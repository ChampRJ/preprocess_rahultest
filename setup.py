import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_rahultest', #This should be unique globally
	version = '0.0.1',
	author = 'Rahul Jain',
	author_email = 'rhljn42@gmail.com',
	description = 'This is NLP preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License', 
	'Operating System :: OS Independent'],
	python_requires = '>= 3.5'
	)