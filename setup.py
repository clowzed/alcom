from setuptools import setup, find_packages
from alcom.__init__ import __version__

setup(
		name             = 'alcom',
		version          = __version__,
		packages         = find_packages(),
		author           = 'Miasnenko Dmitry',
		author_email     = 'cl0wzed.exe@gmail.com',
		url              = 'https://github.com/YoungMeatBoy/alcom.git',
		install_requires = ['pathlib', 'argparse', 'accessify'],
		entry_points={
			'console_scripts': [
				'alcom = alcom.run:main'
		]
		}
)
