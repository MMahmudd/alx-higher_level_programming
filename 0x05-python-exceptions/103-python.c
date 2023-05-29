/*
 * File: c file named 103-python.c
 * Auther: Mahmud M.
 */

#include <Python.h>

/* declaration of function*/
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prining basic information of Python_lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t p_size, p_alloc, ii;
	const char *type;
	PyListObject *p_list = (PyListObject *)p;
	PyVarObject *p_var = (PyVarObject *)p;

	p_size = p_var->ob_size;
	p_alloc = p_list->allocated;

	fflush(stdout);

	printf("[*] Python_list information\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List_Object\n");
		return;
	}

	printf("[*] Size of the Python_List = %ld\n", p_size);
	printf("[*] Allocated = %ld\n",p_alloc);

	for (ii = 0; ii < p_size; ii++)
	{
		type = p_list->ob_item[ii]->ob_type->tp_name;
		printf("Element %ld: %s\n", ii, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(p_list->ob_item[ii]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[ii]);
	}
}

/**
 * print_python_bytes - Printing basic information of Python byte_objects.
 * @p: A PyObject byte_object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t p_size, ii;
	PyBytesObject *p_bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes_object information\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes_Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", p_bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		p_size = 10;
	else
		p_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", p_size);
	for (ii = 0; ii < p_size; ii++)
	{
		printf("%02hhx", p_bytes->ob_sval[ii]);
		if (ii == (p_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Printing basic information of Python float_objects.
 * @p: A PyObject float_object.
 */
void print_python_float(PyObject *p)
{
	char *p_buffer = NULL;

	PyFloatObject *p_float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float_object information\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float_Object\n");
		return;
	}

	p_buffer = PyOS_double_to_string(p_float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n",p_buffer);
	PyMem_Free(p_buffer);
}
