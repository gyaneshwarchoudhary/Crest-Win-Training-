"""
  - linux processes

Docstring for Day-05 Tasks:
 - Advace OOP concepts
 - Python Decorators
 - Git rebase and conflict resolution
 - shell automation and scripting
"""


"""
linux processes:
 POrcess:
 - program, os creates a process 
 - command -> new process -> 5 digit Pid generated ->exectution -> ends the process/terminate
  Kernel: 
   - computer program, core of os with complete control over system, manages hardware, resources, and system calls
 How a process runs:
   - forground process: terminal, blocks terminal, takes input, output to terminal
   - background process: terminal, not block terminal, not req key input, &
   - track process uisng process status -f full, single process information with ps -p pid
   - UID, Pid, PPid, C, STIME, TTY, TIME, CMD
   - ps flags, -a , -x, -u, -e , -f 
   - SIGTSTP
   - bg, fg, kill -cont pid, kill -stop pid
   - load average: 1 5 15 min, 0.5 means 50% cpu usage, 1 means 100% cpu usage
   - prent and child process, orphan process, zombie process, Daemon process
   - priority process, nice value, renice command
   - top command
 
"""

"""
Python Decorators:
 - modify or extend behavior
 - function extendible
 - authenication, logging 
 - syntax: @decorator_name above function definition
 - Decorator with parameters:
    - passed by using args and kwargs in the wrapper function
 - Types of Decorators:
    - Function decorators
    - Class decorators
    - Method decorators    
 - Built in decorators:
    - @staticmethod, @classmethod, @property

"""

"""
Git rebase and conflict resolution:
 - git rebase top of the latest 
 - merge vs rebase
 - conflict: 
     - occurs when changes in two branches conflict with each other
     - mostly occurs on git merge, rebase and cherry-pick
        - conflict resolution:
            - identify conflicting files
            - open the file and look for conflict markers (<<<<<<<, =======, >>>>>>>)
            - manually edit the file to resolve the conflict
            - after resolving, stage the file and commit the changes
"""


"""
Shell Automation and Scripting:
    - text file 
    - handy tool 
    - command language
    - Automation
    - Flexibility
    - Ease of use
    - Portability
    
"""
