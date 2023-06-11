#include "lists.h"

listint_t *_listRev(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * _listRev - a function that reverses a singly-linked.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *_listRev(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - A function that checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 1 is success else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2, *temp3;
	size_t i, size = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp1 = *head;
	while (temp1)
	{
		size++;
		temp1 = temp1->next;
	}

	temp1 = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp1 = temp1->next;

	if ((size % 2) == 0 && temp1->n != temp1->next->n)
		return (0);

	temp1 = temp1->next->next;
	temp2 = _listRev(&temp1);
	temp3 = temp2;

	temp1 = *head;
	while (temp2)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	_listRev(&temp3);

	return (1);
}
