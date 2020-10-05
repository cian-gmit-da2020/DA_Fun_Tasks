""""
New Projet counts.py
write a function that takes a list and
returns a dict where the list items
are dict keys and the value is how often 
the item appears in the list
"""

def counts(list, name="Dict of list items count"):
	dict = {}

	for i in list:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1


	print(name)
	print(dict)

list1 = ['a', 'b', 'h', 's', 'd', 's', 's', 'l' ,'p' ,'u' ,'i' ,'p' ,'r' ,'s']

counts(list1)

counts(list("mary had a little lamb"), "list of chars in mary had a little lamb")