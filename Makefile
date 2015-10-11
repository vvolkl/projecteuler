

#%.out: %.cpp
#	g++ -std=c++11 $< -o $(subst .cpp,.out,$<)
#   
#	More elegant:
CPPFLAGS=-std=c++14 -O2 -Wall -pedantic
CXX=icc
