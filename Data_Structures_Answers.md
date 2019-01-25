Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?
    A: O(n) based on the number of nodes

4. What is the space complexity of your `breadth_first_for_each` method?
    A: O(n) based on the number of nodes

5. What is the runtime complexity of the provided code in `names.py`?
    A: O(n^2)

6. What is the space complexity of the provided code in `names.py`?
    A: O(1) because it is not dependent on the number of names in the list, but on whether the names match.

7. What is the runtime complexity of your optimized code in `names.py`?
    A: I believe it is O(n^2), due to the list comprehension pulling out one name from the first list and then having to iterate through the names in the second list for comparison before the name being added to the duplicates list. So, it depends on the number of names in list_one * list_two.

8. What is the space complexity of your optimized code in `names.py`?
    A: O(1) because it is not dependent on the number of names in the list, but on whether the names match.