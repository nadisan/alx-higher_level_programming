#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newlist;
	listint_t *old = *head;

	newlist = malloc(sizeof(listint_t));
	if (newlist == NULL)
		return (NULL);
	newlist->n = number;
	if (*head == NULL || old->n > newlist->n)
	{
		newlist->next = old;
		*head = newlist;
		return (newlist);
	}
	while (old)
	{
		if (old->n == newlist->n)
		{	free(newlist);
			return (NULL);
		}
		else if (old->next->n > newlist->n)
		{	newlist->next = old->next;
			old->next = newlist;
			return (newlist);
		}
		old = old->next;
	}
	free(newlist);
	return (NULL);
}
