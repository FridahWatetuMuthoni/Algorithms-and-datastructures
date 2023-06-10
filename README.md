# Data Structures and Algorithms

## Steps of creating an algorithm

1. Define the problem statement
2. check the input and the expected output
3. The steps in the algorithm need to be in a very specific order
4. The steps also need to be distint
5. The algorithm should produce a result
6. The algorithm should complete in a finite amount of time

## Algorithm Creation

An algorithm is a set of steps that solves the problem statement
An algorithm defination must contain a specific set of instructions in a particular order
So basically an algorithm is a clearly defined problem statement, input and output

1. The problem must have a clear problem statement
2. How the input is defined and the expected output
3. The algorithm must contain a specific order
4. You shouldmnt be able to break a step in an algorithm in far statement...it should be simple and precise
5. An algorithm should produce a result
6. The algorithm should not be infinite it should end at some point

## Algorithm Efficiency

Time Space Complexity:
To measure the efficiency of an algorithm you need to consider space and time
Time Complexity is how long it takes an algorithm to run
Space Complexity is the amount of memory taken by the computer to compute your algorithm
The running time of an algortihm is the number of times an algorithm has to run to complete a dataset
To check the running time of an algorithm always use the worst case scenario

## Big O notation

Big O notation is the theoritical defination of the complexity of an algorithm as a function of the size
Big O is a notation used to describe complexity. it basically simplifies time and space compexity to a single variable.

O(n):
O-> Order of magnitude of complexity
n-> a function of the size
O(n)-> therefore this measures the complexity of an algorthim as the data grows

The time complexity of a linear search is O(n)
The time complexity of a binary search is O(log n)

Each step in an algorithm has its own space time complexity
Logarithmic runtime is O(log n)

## Big O notation space time complexies

![Alt Text](./images/big-O-notation.jpeg)

O(1)-> constant time complexity
O(n)-> linear time complexity
O(log n)-> logarithmic time complexity

## Logarithms

Let's say you have the number 10 and want to know what power you need to raise another number, like 2, to get 10. The power you're looking for is called the logarithm.

So, in this case, the logarithm of 10 to the base 2 would tell you that 2 raised to what power equals 10. It turns out that 2 raised to the power of 3 (2³) equals 8, which is less than 10. But if you raise 2 to the power of 4 (2⁴), you get 16, which is more than 10. So, the logarithm of 10 to the base 2 is between 3 and 4. We can use decimal numbers to get a more precise answer, like 3.3219.

Logarithms are useful because they help us solve equations where we have an unknown exponent. For example, if we have the equation 2 raised to what power equals 8, we can rewrite it as log₂(8) = 3. So, the logarithm helps us find the missing exponent.

The logarithm function is typically written as "log" followed by a subscript that indicates the base of the logarithm. For example, if we have a base 10 logarithm, it is denoted as "log₁₀," and if we have a base e logarithm (where e is Euler's number, approximately equal to 2.71828), it is denoted as "ln" (natural logarithm).

The logarithm of a number, denoted as logₐ(b), is defined as the exponent to which the base (a) must be raised to obtain the number (b). Mathematically, it can be represented as:

b = a^logₐ(b)

Here are a few important properties of logarithms:

1. The logarithm of 1 to any base is always 0: logₐ(1) = 0.
2. The logarithm of a number to its own base is always 1: logₐ(a) = 1.
3. The logarithm of any base to itself is always 1: logₐ(a) = 1.
4. Logarithms can be used to solve exponential equations. For example, if we have the equation a^x = b, we can rewrite it as x = logₐ(b).

## linear search algorithm

Linear search does not require the data to be sorted

1. Start at the beginning
2. Move Sequentially
3. Compare current value to target
4. Reach end of list

## binary search algorithm

Binary search requires the data to be sorted

1. Determine the middle position of the sorted list
2. Compare the element in the middle position to the target element
3. If the elements match we return the middle position and end
4. If the elements dont match we check whether the element in the middle position is smaller or larger than the target element. If it is we go back to step 3 with the new list and repeat the process until you find it or it returns a subli
