/*
 * File: 102-python.c
 * Auther: Mahmud M.
 */

#include "Python.h"

/**
 * print_python_string - Printing information of a Python string.
 * @p: A PyObject string_object.
 */
void print_python_string(PyObject *p)
{
	long int length_of;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length_of = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length_of);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length_of));
}
