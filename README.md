# Interview Prep

This guide is for me and anyone else that stumbles across it.

Selecting the appropriate data structure for a problem is usually the hardest part. Once you have a data structure (or variation of a data structure) in mind, actually implementing the solution is pretty straightforward. So, I think the best way to optimize for time when preparing for interviews is to recognize the different classes of problems and the respective data structures/algorithms required to solve these problems. 

Here are some canonical problems and their classes listed in order of importance:

### Recursion (divide and conquer, backtracking)
- Generate all permutations of a string
- Generate all unique permutations of a string
- Insert operands in a mathematical expression to maximize the expression's value
- 24 game (https://leetcode.com/problems/24-game/)
- Generate powerset
- Generate all sets of n balanced parentheses
- Given a keypad, a list of possible words, and a phone number, return all possible words in the dictionary that can be constructed from the phone number
- Generate all valid IP addreses from a string of integers

### Dynamic Programming
- Longest Increasing Subsequence
- Longest Common Subsequence
- Number of ways to make change
- Maximal square of 1's in a matrix of 1's and 0's
- Number of ways to reach point b from point a in a matrix
- Min cost path from point b to point a in a matrix (product and sum)

### BFS, DFS, topological sort
- Number of islands in a matrix (number of connected components)
- Largest island in a matrix (largest connected component)
- Reconstruct itinerary (https://leetcode.com/problems/reconstruct-itinerary/)
- Word ladder
- Detect cycle in a graph
- Shortest path through a matrix maze
- Single source shortest path (bellman ford)
- Word Search (https://leetcode.com/problems/word-search/, https://leetcode.com/problems/word-search-ii/)

### Lists and Arrays
- Find Missing Number from a sorted list
- Find 2 Missing Numbers from a sorted list
- Set intersection of two lists without set operations 
- Maximum contigous subarray sum
- Maximum contiguous subarray product
    #### Two Pointers
    - Merge from mergesort
    - 2 Sum, 3 Sum
    #### Sliding Window
    - Longest Substring Without Repeating Characters
    - Longest Substring with 2 distint characters
    #### Pre-computation
    - Meeting rooms
    - Return product of all numbers in a list except for it without using division
    - Longest subarray with euqal number of letters and numbers
    - Return start and end index of a contiguous subarray with sum of zero

### Trees
- Convert a BST into a doubly linked list
- Inorder successor
- Invert a binary tree
- Path sum
- Autocomplete (trie)
- Given a tree, return a list of linked lists of dpeths
- Check if a tree is a BST
- Check if a tree is symmetric
- Check if a tree is balanced
- Write a function to select a random element from an input tree

### Heaps
- Return largest product from 3 numbers in an input list
- Given a list of (x, y) coordinates and a point, find the k-nearest neighbors of the point from the input list
- Return the k largest numbers in a list
- Merge k sorted lists
- Maintain the median of a data stream
- Kth order statistic (also can use quickselect)

### Stacks and Queues
- Evaluate Reverse Polish Notation
- Validate balanced parentheses 
- Merge overlapping intervals
- Sort stack using only push and pop
- Reverse stack using only push and pop
- Design a stack with O(1) min access (https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/)

### Linked Lists
- Recursively and iteratively reverse a linked list
- Split linked list into equal parts
    #### Tortoise and Hare Pointers
    - Center of a linked list
    - Detect whether linked list has cycles
    - Find strt of a cycle in a linked list
    - Delete nth element from end of linked list 

### Binary Search
- Given an integer x, find its square root. If x is not a perfect square, return floor(sqrt(x))
- Find the leftmost and rightmost occurrence of a value in a sorted array

### Uncategorized
- Print a matrix in spiral order
- Convert from one base to another
- Reverse digits of an integer using modulo and division

### Good Resources:
- Leetcode
- Geeks for Geeks
- Byte By Byte (YouTube channel)