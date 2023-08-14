#include "list.h"

/**
 * reverse_listint - it reverses a linked list listint_t
 * @head: a pointer to the head of the list
 * Reeturn: pointer to the head
 */

listint_t *reverse_listint(listint_t **head);
{
  listint_t *curnode = *head, *nextnode = *head, prevnode = NULL;

  while (nextnode != NULL)
    {
      nextnode = nextnode->next;
      curnode-next = prevnode;
      prenode = curnode;
      curnode = nextnode;
    }
  *head = prenode;
  return (*head);
}

/**
 * is_palindrome - it checks if a list is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if it is a palindrome, else 0
 */

int is_palindrome(listint_t **head)
{
  listint_t *temp, *r, *mid;
  size_t size = 0, i;

  temp = *head;
  while (temp)
    {
      size++;
      temp = temp->next;
    }

  temp = *head;
  for (i = 0; i < (size / 2) -1; i++)
    temp = temp->next;

  if ((size % 2) == 0 && temp->n != temp->next->n)
    return (0);

  temp = temp->next->next;
  r = reverse_listint(&temp);
  mid = r;

  tmp = *head;
  while(r)
    {
      if (temp->n != r->n)
	return (0);
      temp = temp->next;
      r = r->next;
    }
  reverse_listint(&mid);

  return (1);
}
