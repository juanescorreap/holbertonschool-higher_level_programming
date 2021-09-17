#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - Function that prints all the elements of a dlistint_t.
 * @h: pointer to a dlistint_t element
 * Return: A size_t value for dlistint_t
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t index = 0;

	while (h)
	{
		printf("%d", h->n);
		printf("\n");
		h = h->next;
		index = index + 1;
	}
return (index);
}
