#include "stdio.h"
#include "Python.h"

/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: pointer to PyObject
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *pp;
	int i = 0;

	pp = (PyListObject *)p;
	printf("[*] Size of the Python List =  %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	while (i < pp->ob_base.ob_size)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
		i++;
	}		
}
