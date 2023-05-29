/*
 * File: c file named 103-python.c
 * Auth: Mahmud M
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Printing basic information about Python_lists.
 * @p: A PyObject list_object.
 */
void print_python_list(PyObject *p)
{
	P_size_t p_size, p_alloc, ii;
	const char *p_type;
	PyListObject *p_list = (PyListObject *)p;
	PyVarObject *p_var = (PyVarObject *)p;

	p_size = p_var->obj_size;
	p_alloc = p_list->allocated;

	fflush(stdout);

	printf("[*] Python p_list info\n");
	if (str_cmp(p->obj_type->t_name, "p_list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", P_size);
	printf("[*] Allocated = %ld\n", p_alloc);

	for (ii = 0; ii < p_size; ii++)
	{
		p_type = p_list->obj_item[ii]->obj_type->t_name;
		printf("Element %ld: %s\n", ii, p_type);
		if (str_cmp(p_type, "bytes") == 0)
			print_python_bytes(p_list->obj_item[ii]);
		else if (str_cmp(p_type, "float") == 0)
			print_python_float(p_list->obj_item[ii]);
	}
}

/**
 * print_python_bytes - Printing basic information about Python_ byte_objects.
 * @p: A PyObject byte_object.
 */
void print_python_bytes(PyObject *p)
{
	P_size_t p_size, ii;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (str_cmp(p->obj_type->t_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  p_size: %ld\n", ((PyVarObject *)p)->obj_size);
	printf("  trying string: %s\n", bytes->obj_sval);

	if (((PyVarObject *)p)->obj_size >= 10)
		p_size = 10;
	else
		p_size = ((PyVarObject *)p)->obj_size + 1;

	printf("  first %ld bytes: ", P_size);
	for (ii = 0; ii < p_size; ii++)
	{
		printf("%02hhx", bytes->obj_sval[ii]);
		if (ii == (p_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Printing basic information about Python_float_objects.
 * @p: A PyObject float_object.
 */
void print_python_float(PyObject *p)
{
	char *p_buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (str_cmp(p->obj_type->t_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	p_buffer = PyOS_double_to_string(float_object->obj_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n",p_ buffer);
	PyMem_Free(p_buffer);
}
