curl -O http://zlib.net/zlib-1.2.11.tar.gz
tar xzf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure
make
make install
cd ..

cmake --version

curl -O https://github.com/openbabel/openbabel/archive/refs/tags/openbabel-3-1-1.tar.gz
tar xzf openbabel-3-1-1.tar.gz
cd openbabel-openbabel-3-1-1
mkdir build
cd build
cmake ..
make
make install
cd ../../
