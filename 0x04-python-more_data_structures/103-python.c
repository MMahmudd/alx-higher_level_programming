#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Printi byt information
 *
 * @p: Python Objects
 * Return: not return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int siz, ii, limitt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	siz = ((PyVarObject *)(p))->ob_siz;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", siz);
	printf("  trying string: %s\n", string);

	if (siz >= 10)
		limitt = 10;
	else
		limitt = siz + 1;

	printf("  first %ld bytes:", limitt);

	for (ii = 0; ii < limitt; ii++)
		if (string[ii] >= 0)
			printf(" %02x", string[ii]);
		else
			printf(" %02x", 256 + string[ii]);

	printf("\n");
}

/**
 * print_python_list - Print lists an information
 *
 * @p: Python Objects
 * Return: not return
 */
void print_python_list(PyObject *p)
{
	long int siz, ii;
	PyListObject *list;
	PyObject *obj;

	siz = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (ii = 0; ii < siz; ii++)
	{
		obj = ((PyListObject *)p)->ob_item[ii];
		printf("Element %ld: %s\n", ii, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
