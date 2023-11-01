## [Exercise 10](https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html)

### [Solution](https://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html)

This exercise is going to be revisiting an old exercise (see [Exercise 5](https://github.com/AlexCRosa/practicing_python/tree/b421880613bd067a9be535eb2c6e8b09ac897a3a/5_list_overlap)), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (*Hint: Remember list comprehensions from [Exercise 7](https://github.com/AlexCRosa/practicing_python/tree/b421880613bd067a9be535eb2c6e8b09ac897a3a/7_list_comprehension)*)

#### Extras:

1. Randomly generate two lists to test this.