/*

Provides a utility function to repeat `std::string` instances by multiplying them.

To compile:
  clang++ violence.cc -o violence $(python3-config --cflags --ldflags --embed)

Python 3 must be installed.

*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <string>
#include <iostream>

struct PyObjectDeleter {
    void operator()(PyObject* p) { Py_DECREF(p); }
};

using py_unique_ptr = std::unique_ptr<PyObject, PyObjectDeleter>;

std::string operator*(const std::string& lhs, int rhs) {
    if (!Py_IsInitialized()) {
        Py_Initialize();
    }

    py_unique_ptr lhs_pystr{ PyUnicode_FromString(lhs.c_str()) };
    assert(lhs_pystr);

    py_unique_ptr rhs_pynum{ PyLong_FromLong(rhs) };
    assert(rhs_pynum);

    py_unique_ptr result_pynumber{ PyNumber_Multiply(lhs_pystr.get(), rhs_pynum.get()) };
    assert(result_pynumber);

    return std::string(PyUnicode_AsUTF8(result_pynumber.get()));
}

int main() {
    std::cout << std::string("456") * 5 << std::endl;
    return 0;
}
