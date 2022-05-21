yum install -y wget

tar xzvf swig-4.0.2.tar.gz
cd swig-4.0.2
./configure
make
make install

wget https://zlib.net/zlib-1.2.12.tar.gz

tar xzvf zlib-1.2.12.tar.gz
cd zlib-1.2.12
./configure
make
make install
