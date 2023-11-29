ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Mulhouse!")

ft_dict["Hello"] = "42 Mulhouse!"

"""List:

A list is an ordered, mutable collection of elements.
Elements in a list can be of different data types.
Lists are created using square brackets [].
You can modify, add, and remove elements from a list.

Tuple:

A tuple is an ordered, immutable collection of elements.
Similar to lists, elements can be of different data types.
Tuples are created using parentheses ().
Once a tuple is created, its elements cannot be changed.

Set:

A set is an unordered collection of unique elements.
Sets do not allow duplicate values.
Created using curly braces {} or the set() constructor.
Supports various set operations like union, intersection, and difference.

Dictionary (Dict):

A dictionary is an unordered collection of key-value pairs.
Keys are unique and used to access values.
Created using curly braces {} with key-value pairs separated by colons :.
Dictionaries are mutable, allowing the addition, modification,
and deletion of key-value pairs."""


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print("\n")
