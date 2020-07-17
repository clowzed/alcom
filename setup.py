from setuptools import setup, find_packages

setup(
		name             = 'alcom',
		version          = '1.0.0',
		packages         = find_packages(),
		author           = 'Miasnenko Dmitry',
		author_email     = 'cl0wzed.exe@gmail.com',
		url              = 'https://github.com/YoungMeatBoy/alcom.git',
		install_requires = ['pathlib', 'argparse'],
		entry_points={
			'console_scripts': [
				'alcom = alcom.converter:main'
		]
		}
)