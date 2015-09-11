

%.out: %.cpp
	g++ -std=c++11 $< -o $(subst .cpp,.out,$<)
