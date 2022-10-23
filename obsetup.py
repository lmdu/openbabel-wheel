import os
import sys
import shutil
import subprocess
from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

def find_version():
	with open(os.path.join('openbabel', '__init__.py')) as fp:
		for line in fp:
			if line.startswith('__version__'):
				return line.split('=')[1].strip().strip('"')

def find_data():
	if sys.platform == 'darwin':
		data_src = '/usr/local/Cellar/open-babel/3.1.1_2/share/openbabel/3.1.0'
		libs_src = '/usr/local/Cellar/open-babel/3.1.1_2/lib/openbabel/3.1.0'
	else:
		data_src = '/usr/share/openbabel/3.1.1'
		libs_src = '/usr/lib64/openbabel'

	data_dest = 'openbabel/data'
	libs_dest = 'openbabel/plugin'

	if os.path.exists(data_dest):
		shutil.rmtree(data_dest)

	if os.path.exists(libs_dest):
		shutil.rmtree(libs_dest)

	shutil.copytree(data_src, data_dest)
	shutil.copytree(libs_src, libs_dest)

class BuildPy(build_py):
	def run(self):
		find_data()

		self.run_command('build_ext')
		super(build_py, self).run()

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
		'-fopenbabel'
	]
)

setup(
	name = 'openbabel',
	version = find_version(),
	author = 'Noel O\'Boyle',
	author_email = 'openbabel-discuss@lists.sourceforge.net',
	license = 'GPL-2.0',
	url = 'http://openbabel.org/',
	description = 'Python interface to the Open Babel chemistry library',
	long_description = open('README.rst').read(),
	zip_safe = False,
	packages = ['openbabel'],
	package_data = {'': ['data/*', 'plugin/*']},
	ext_modules = [obextension],
	cmdclass = {'build_py': BuildPy},
	classifiers = [
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