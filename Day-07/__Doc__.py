"""
Docstring for Day-07.__Doc__
- Async	Python	basics
- Evnt	loop
- REST	principles
- API	security	basics
"""


"""
Gil: Global Interpreter Lock
 - mutex (mutual exclusion lock), ensures that only one thread executes Python bytecode at a time, even on multi-core processors
 - i/o operations works well 
 - if two threads simultaneously access a ref count, cause corrupt memeory
 - Threads, multiprocessing
 
"""


"""
Async python:
    Event loop: 
     - deciedes which piece of code to run at givn moment, runs on single thread, !parellism, switches b/w tasks quickly whenever one task is waiting for something, like i/o operation, network request, etc (concurrency)
     - event loop does not runs the threads or process, it deligates and holds the reciept/function 
     - rule of thumb:
        - parellelism: use mulitiprocessing, for cpu bound tasks, like data processing, machine learning, etc
        - If the need is to handle blocking I/O with limited concurrency, use threads 
        - If the need is to handle huge concurrency with I/O, use asyncio (for example, chat servers, web scraping, APIs).
    coroutine: fun 
          - does not exectute immediately when called, it must be attached to an event loop
          - Schedule concurrent execution with asyncio.create_tasks

"""

"""
EVent loop:
 - central schedular and runs on single thread
    - monitor os i/o events, 
    - run ready callbacks.
    - resumes coroutines when their awaited operations are complete

"""

"""
REST principles:
    - Api: application prog interface.
    - rest: repesentational state transfer, type of api architecture 
    - stateless, scalable and flexible
    - platform independent
    - multiple data formats (json, xml, etc)
    - http caching mechanism
    Six principles of REST:
     - seperation of client and server
     - stateless
     - uniformity of the interface
     - caching 
     - layered architecture
     - code on demand (optional)
    Guidelines for designing RESTful APIs:
    - use nouns, not verbs example /api/users, not /api/getusers
    - heirarchy and nesting: /api/users/{user_id}/posts/{post_id}
    - plural names for collections: /api/users, not /api/user
    - user Hyphen for readability: /api/user-profiles, not /api/userprofiles

"""


"""
Api Security:
 - sensitive data, can perform MITM and DDoS attack, etc
   Api security standards:
    - vulnerability 
    - token 
    - Encryption
    - throttling and rate limiting
    - input validation and sanitization
    - Api gateway 
    - zero trust approach
    - OAuth 2.0 and OpenID Connect
"""

