wget http://zlib.net/zlib-1.2.11.tar.gz
tar xzf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure
make
make install
cd ..

cmake --version

cd openbabel-openbabel-3-1-1
mkdir build
cd build
cmake ..
make
make install
cd ../../


