#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - C function that prints some basic
 * info about Python lists
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
      int n;
      PyObject *m;

      printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
      printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
      for (n = 0; n < Py_SIZE(p); n++)
      {
            m = PyList_GetItem(p, n);
            printf("Element %i: %s\n", n, Py_TYPE(m)->tp_name);
      }
}
