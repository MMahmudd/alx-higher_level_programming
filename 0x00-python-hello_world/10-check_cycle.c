#include "lists.h"

/**
 * check_cycl - checks if a linked list contains a cycle
 * @lists: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycl(listint_tt *lists)
{
	listint_tt *sloow = lists;
	listint_tt *faast = lists;

	if (!lists)
		return (0);

	while (sloow && faast && faast->nextt)
	{
		slow = sloow->nextt;
		fast = faast->nextt->nextt;
		if (sloow == faast)
			return (1);
	}

	return (0);
}
