# Leetcode-2642-Hard-Heap-Graph
A easy logic hard coding problem. In my solution, I used tuple, heap, and some weird dictionaries, and I learned all that in this single problem. I didn't figure this out at the first time.

At the beginning, initialize a 2d dictionary, with start:[destiny, edge cost]
Then, we use the heap to collect all the sortest past to its neighbors, and as long as the heap is not empty, we start at from poping the heap and look for shortest path to the poped neighbor


