# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector
cimport numpy as cnp
import numpy as np

def hello_multidimensional_world():
    cdef cnp.ndarray[cnp.float64_t, ndim=1] a = np.ones(2)
    cdef vector[string] v;
    v.push_back("Hello n-dim World!")
    if np.sum(a) == 2:
        return v[0]
    else:
        return "something's not quite right"
