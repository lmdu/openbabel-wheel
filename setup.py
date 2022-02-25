import os
import sys
from cmake_build_extension import BuildExtension, CMakeExtension
from setuptools import setup

root_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.join(root_dir, "scripts", "python")

try:
    os.makedirs('openbabel')
except OSError:
    pass

__VERSION__ = '3.1.1.post1'

setup(
    name='openbabel-wheel',
    version=__VERSION__,
    author='Noel O\'Boyle',
    author_email='openbabel-discuss@lists.sourceforge.net',
    license='GPL-2.0',
    url='http://openbabel.org/',
    description='Python interface to the Open Babel chemistry library',
    long_description=open(os.path.join(base_dir, 'README.rst')).read(),
    zip_safe=False,
    cmdclass={'build_ext': BuildExtension},
    packages=['openbabel'],
    ext_modules=[
        CMakeExtension(
            name="OpenBabel",
            install_prefix="openbabel",
            cmake_configure_options=[
                "-DPYTHON_EXECUTABLE={}".format(sys.executable),
                "-DCMAKE_BUILD_TYPE=Release",
                "-DWITH_INCHI=ON",
                "-DPYTHON_BINDINGS=ON",
                "-DRUN_SWIG=ON",
                "-DBUILD_BY_PIP=ON",
            ]
        ),
    ],
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