

#%.out: %.cpp
#	g++ -std=c++11 $< -o $(subst .cpp,.out,$<)
#   
#	More elegant:
CPPFLAGS=-std=c++14 -O2 -Wall -pedantic
CXX=icc

CXXFLAGS += -fPIC
LDFLAGS += -lgmp
%.so: %.cpp
	$(CXX) -shared -c $(CXXFLAGS)  $(LDFLAGS) $< -o lib$@

primes: LDFLAGS+=-L${PWD} -lprimehelpersmodule
primes: e060 




all: primes


