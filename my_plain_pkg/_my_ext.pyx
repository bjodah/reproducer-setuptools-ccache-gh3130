# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector

def hello_world():
    cdef vector[string] v;
    v.push_back("Hello World!")
    return v[0]
