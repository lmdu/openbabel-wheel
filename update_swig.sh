yum install -y wget
wget https://sourceforge.net/projects/swig/files/swig/swig-4.0.2/swig-4.0.2.tar.gz
tar xzvf swig-4.0.2.tar.gz
cd swig-4.0.2
./configure
make
make install
