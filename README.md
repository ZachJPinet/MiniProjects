# MiniProjects
My repository for very small projects, typically only 1 file for each.

**MiniProject 1: list_sorter.py**

Though I'm sure this program can have many uses, I originally created it to help me sort songs in a playlist to order them from my most favorite to least favorite. It's difficult to order 50 or 100 songs at a time into a list that accurately reflects which songs I like more than others, so I created this so that I would only ever have to compare two songs at a time.

This program allows the user to input a list of items, one at a time. It then starts at the end of the list and iterates towards the front, picking two items at a time and asking the user which one is 'higher up' than the other. If the item lower in the list should be 'higher up', then the items' positions are swapped. If this happens, the current_position will iterate into the same item again. Once it gets to the top of the list, it will have the 'highest up' item in its proper spot, and will begin iterating back down the list. Two items will never be compared twice. Two items that are not adjacent will never be compared. Each time the program hits one of the ends of the list, it moves the 'endpoint' of the list, so that it never pointlessly compares an item to one that has already been placed at the top or bottom.

Example 1:
Let's say we want to sort 6 items in alphabetical order. We input them in the order of: \['f', 'c', 'd', 'a', 'e', 'b']. 
After 1 iteration, and 5 questions, the list looks like this: \['a', 'f', 'c', 'd', 'b', 'e'].
After 2 iterations, and 4 more questions, the list looks like this: \['a', 'c', 'd', 'b', 'e', 'f'].
After 3 iterations, and 2 more questions, the list looks like this: \['a', 'b', 'c', 'd', 'e', 'f'].
After a final iteration, and 2 final questions, the program determines that the list is sorted, and finishes running.

Example 2:
Let's say we want to sort the 26 letters of the alphabet, and we input them in alphabetical order. On its first iteration up, it asks 25 questions. It then repeatedly iterates back and forth without asking the user a single extra question, and determines that all items are in order.

Based off of these, we can see that it is recommended to try and have the items roughly in order to begin with. The more out of order they are, the longer it takes to sort them, and the more questions the user will have to answer.
