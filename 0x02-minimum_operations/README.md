
Curriculum
Short Specializations
Average: 149.46%
You have a captain's log due before 2024-01-21 (in 3 days)! Log it now!
0x02. Minimum Operations
Algorithm
Python
 By: Carrie Ybay, Software Engineer at Holberton School
 Weight: 1
 Project will start Jan 14, 2024 10:00 PM, must end by Jan 18, 2024 10:00 PM
 Checker was released at Jan 15, 2024 10:00 PM
 An auto review will be launched at the deadline
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should be documented
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable
Tasks
0. Minimum Operations
mandatory
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
Repo:

GitHub repository: alx-interview
Directory: 0x02-minimum_operations
File: 0-minoperations.py
  
Copyright © 2024 ALX, All rights reserved.


