import os
import sys
import shutil
import subprocess
from setuptools import Extension, find_packages, setup

def find_version():
	with open(os.path.join('openbabel', '__init__.py')) as fp:
		for line in fp:
			if line.startswith('__version__'):
				return line.split('=')[1].strip().strip('"')

def find_data():
	if sys.platform == 'darwin':
		src_dir = '/usr/local/Cellar/open-babel/3.1.1_2/share/openbabel/3.1.0'
	else:
		src_dir = '/usr/share/openbabel/3.1.1'

	dest_dir = 'openbabel/data'

	if os.path.exists(dest_dir):
		shutil.rmtree(dest_dir)

	shutil.copytree(src_dir, dest_dir)

def pkg_config(option):
	return subprocess.check_output(
		[ 'pkg-config', option, 'openbabel-3'],
		universal_newlines = True
	).strip()

inc_dirs = pkg_config('--variable=pkgincludedir')
lib_dirs = pkg_config('--variable=libdir')

obextension = Extension(
	name = 'openbabel._openbabel',
	swig_opts = ['-c++', '-small', '-O', '-templatereduce', '-naturalvar',
		'-I{}'.format(inc_dirs)
	],
	sources = [os.path.join('openbabel', 'openbabel-python.i')],
	library_dirs = [lib_dirs],
	include_dirs = [inc_dirs],
	extra_compile_args = [
	],
	extra_link_args = [
		'-lopenbabel'
	]
)

find_data()

setup(
	name='openbabel',
	version=find_version(),
	author='Noel O\'Boyle',
	author_email='openbabel-discuss@lists.sourceforge.net',
	license='GPL-2.0',
	url='http://openbabel.org/',
	description='Python interface to the Open Babel chemistry library',
	long_description=open('README.rst').read(),
	zip_safe=False,
	packages=['openbabel'],
	package_data = {'': ['data/*']},
	ext_modules=[obextension],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Environment :: Other Environment',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Natural Language :: English',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: OS Independent',
		'Operating System :: POSIX',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Unix',
		'Programming Language :: C++',
		'Programming Language :: Python',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'Topic :: Scientific/Engineering :: Chemistry',
		'Topic :: Software Development :: Libraries'
	]
)