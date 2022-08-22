#include "lists.h"
/**
 * check_cycle - function in C that checks if a linked list has a cycle in it
 * @head: - Head of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *first, *last;

	first = head;
	last = head;
	while (last != NULL)
	{
		if (last->next == NULL)
			return (0);
		if (last->next == first)
			return (1);
		last = last->next;
	}
	return (0);
}
