#include "lists.h"
/**
 * check_cycle - function in C that checks if a linked list has a cycle in it
 * @head: - Head of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1 = NULL, *temp2 = NULL;

	temp1 = list;
	temp2 = list;

	while (list)
	{
		temp2 = temp2->next;
		if (!temp1 || !temp2)
			return (0);
		if (temp2 == temp1)
			return (1);
	}
	return (0);
}
