

CXXFLAGS=-std=c++14 -O2 -Wall -pedantic
CXX=g++

FC=gfortran

%.cppout: %.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

%.f90out: %.f90
	$(FC) $(FCFLAGS) $^ -o $@
