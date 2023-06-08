#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - a function in C that inserts a number into
 * a sorted singly linked list.
 *
 * @head: pointer to the head of the linked list
 * @number: number to be added
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp1, *temp2;

	temp1 = (listint_t *)malloc(sizeof(listint_t));
	if (temp1 == NULL)
		return (NULL);
	temp2 = *head;
	temp1->n = number;
	if (*head == NULL)
	{
		temp1->next = *head;
		*head = temp1;
		return (temp1);
	}
	else if (temp2->n > number)
	{
		temp1->next = temp2->next;
		*head = temp1;
		return (temp1);
	}
	while (temp2->next)
	{
		if ((temp2 + 1)->n > number)
		{
			temp1->next = temp2->next;
			temp2->next = temp1;
			return (temp1);
		}
		else if ((temp2 + 1)->next == NULL)
		{
			temp1->next = (temp2 + 1)->next;
			(temp2 + 1)->next = temp1;
			return (temp1);
		}
	}
	return (NULL);
}
