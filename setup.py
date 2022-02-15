from setuptools import setup, find_packages
import pathlib
from alcom.__init__ import __version__

long_description = (pathlib.Path(__file__).parent / "readme.md").read_text(encoding = "utf-8")

setup(
		name             = 'alcom',
		version          = __version__,
		packages         = find_packages(),
		author           = 'Miasnenko Dmitry',
		author_email     = 'clowzed.work@gmail.com',
		url              = 'https://github.com/clowzed/alcom.git',
		long_description = long_description,
        long_description_content_type ='text/markdown',
		install_requires = ['argparse', 'accessify'],
		entry_points = {
			'console_scripts': [
				'alcom = alcom.run:main'
		]
		}
)
