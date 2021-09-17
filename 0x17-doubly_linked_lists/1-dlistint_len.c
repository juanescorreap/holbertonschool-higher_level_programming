#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * dlistint_len - Function that returns the number of
 * elements in a linked dlistint_t list.
 * @h: pointer to a dlistint_t element
 * Return: A size_t value for dlistint_t
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t index = 0;

	while (h)
	{
		h = h->next;
		index = index + 1;
	}
	return(index);
}
