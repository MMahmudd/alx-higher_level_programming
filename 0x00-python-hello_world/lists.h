#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_ss - singly linked list
 * @nn: integer
 * @nextt: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_ss
{
	int nn;
	struct listint_ss *nextt;
} listint_tt;

size_t print_listintt(const listint_tt *h);
listint_tt *add_nodeint(listint_tt **headd, const int nn);
void free_listint(listint_tt *headd);
int check_cycle(listint_tt *listt);

#endif /* LISTS_H */
