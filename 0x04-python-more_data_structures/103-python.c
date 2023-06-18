#include "stdio.h"
#include "Python.h"

/**
 * print_python_bytes -  prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyListObject *pp;
        int i = 0;

	while (i < pp->ob_base.ob_size)
        {
                if (( pp->ob_item[i]->ob_type->tp_name) == "bytes")
		{	printf("[.] bytes object info\n");
			printf("size: %ld\n", p->ob_item[i]->ob_type->tp_size);
			pritntf("trying string: Hello");
			printf("first 6 bytes: 48 65 6c 6c 6f 00");
		}
		i++;
        }
}

/**
 * print_python_list -  prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p);
{
	PyListObject *pp;
	int i = 0;

	pp = (PyListObject *)p
	printf("[*] Python list info");
	printf("[*] Size of the Python List = ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	while (i < pp->ob_base.ob_size)
	{

		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
		if (( pp->ob_item[i]->ob_type->tp_name) == "bytes")
			 print_python_bytes(PyObject *p);
		i++;
	}
}
