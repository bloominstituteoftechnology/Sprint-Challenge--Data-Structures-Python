Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
<br> O(log(n)) 

2. What is the space complexity of your `depth_first_for_each` function?
<br> because I used a recursive solution, O(log(n)) because of the potential stack growth

3. What is the runtime complexity of your `breadth_first_for_each` method?
<br> O(log(n))

4. What is the space complexity of your `breadth_first_for_each` method?


5. What is the runtime complexity of the provided code in `names.py`?
<br>
O(N4) 4 nested loops, each growing by the size of the input, since they are nested - they are multiplied. 

6. What is the space complexity of the provided code in `names.py`?
<br>  O(n) as the size of the duplicates array will grow in proportion to the names inputs

7. What is the runtime complexity of your optimized code in `names.py`?
<br> O(1) because python's 'set' is implemented as a hash table, and the lookup/insert/delete functions of a hash table are O(1)

8. What is the space complexity of your optimized code in `names.py`?
<br> O(n) because the hash table grows with the size of the data 
