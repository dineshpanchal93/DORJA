from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dorja/__init__.py
from dorja import __version__ as version

setup(
	name="dorja",
	version=version,
	description="Dojra Project Progress",
	author="dineshpanchal432@gmail.com",
	author_email="dineshpanchal432@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
