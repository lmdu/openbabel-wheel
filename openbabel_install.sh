cmake --version

wget https://github.com/openbabel/openbabel/archive/refs/tags/openbabel-3-1-1.tar.gz
tar xzf openbabel-3-1-1.tar.gz
cd openbabel-openbabel-3-1-1
mkdir build
cd build
cmake ..
make
make install
cd ../../
