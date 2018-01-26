
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/class.hpp>
#include <boost/python/copy_const_reference.hpp>
#include <boost/python/return_by_value.hpp>
#include <boost/python/return_value_policy.hpp>
#include <boost/python/to_python_converter.hpp>
#include <boost/python/list.hpp>

#include "primehelpersmodule.h"

using namespace boost::python;
using namespace std; 
using namespace Primes;

template<class T>
struct VecToList
{
    static PyObject* convert(const vector<T>& vec)
    {
        list* l = new list();
        for(size_t i = 0; i < vec.size(); i++)
            (*l).append(vec[i]);
        return l->ptr();
    }
};

BOOST_PYTHON_MODULE(libprimehelpersmodule)
{
    //to_python_converter<vector<int,allocator<int> >, VecToList<int> >();
    to_python_converter<std::vector<int, std::allocator<int> >, VecToList<int> >();
    def("checkTwoPrimes", checkTwoPrimes);
    def("sieve", sieve );//, return_value_policy<return_by_value>());
}

