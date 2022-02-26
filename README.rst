Minimal non-working example for using ccache with setuptools
============================================================
See `pypa/setuptools#3130 <https://github.com/pypa/setuptools/issues/3130>`_

Invocation
----------
Bisect setuptols with SETUPTOOLS_USE_DITUTILS=stdlib/local

.. code-block:: console

   $ python3 -m pip install cython numpy
   $ python3 -m pip install setuptools==50.0.0
   $ SETUPTOOLS_USE_DISTUTILS=local CC="ccache gcc" python3 setup_no_numpy.py build_ext -i && python3 -c "import my_plain_pkg"
   $ SETUPTOOLS_USE_DISTUTILS=local CC="ccache gcc" python3 setup_with_numpy.py build_ext -i && python3 -c "import my_numpy_pkg"


Findings
--------
On Ubuntu 21.10:

 - setuptools>=60.0.0 requires: SETUPTOOLS_USE_DITUTILS=stdlib
 - When using SETUPTOOLS_USE_DITUTILS=local, then CC="ccache gcc" works with setuptools==58.0.4, but seems to be failing from 58.1.0 and onwards.
