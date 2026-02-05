"""
Module for Day 04 tasks.
 - OOP in python
 - pep8 and clear code
 - logging and debugging
 - linux processes
"""

"""
OOP concepts:
 - programming paradigm
 - structure, bheavior, scalable and reusable
 - Access specifiers: 
 - key concepts:
    - class: blueprint, constructors and types
    - object: instance of class
    - inheritance: code reuse and hierarchy
    - encapsulation: modular and secure code 
    - polymorphism: multiple forms
    - abstraction: hiding the implementation 
 - 
"""


"""
Python Enhancement proposals (PEP8):
 - styling guide, maintainable and collaboration
 - Key Guidelines:
    - indentation: 4 spaces
    - line length: 79 characters
    - blank lines: 2 for top level, 1 for methods
    - imports: each import on separate line
    - naming conventions: snake_case for functions and variables, CamelCase for classes
    - whitespace: avoid extra spaces
    - comments and docstrings: use them effectively
"""

"""
Logging and Debugging:
 - track events
 - catagorisation, Destination, context, control
 - 5 levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
""" 



"""
linux processes:
  Kernel: 
   - computer program, core of os with complete control over system, manages hardware, resources, and system calls
 POrcess:
 - program, os creates a process 
 - command -> new process -> 5 digit Pid generated ->exectution -> ends the process/terminate
 How a process runs:
   - forground process: terminal, blocks terminal, takes input, output to terminal
   - background process: terminal, not block terminal, not req key input, &
   - track process uisng process status -f full, single process information with ps -p pid
   - UID, Pid, PPid, C, STIME, TTY, TIME, CMD
   - ps flags, -a , -x, -u, -e , -f 
   - SIGTSTP
   - bg, fg, kill -cont pid, kill -stop pid
   - load average: 1 5 15 min, 0.5 means 50% cpu usage, 1 means 100% cpu usage
   - zombie process, orphan process, init process
   - priority process, nice value, renice command
   - top command
 
"""