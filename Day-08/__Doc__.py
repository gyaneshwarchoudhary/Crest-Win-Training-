"""
Docstring for Day-08.__Doc__
• FastAPI	project	setup
• Routing
• Pydantic	models
• Dependency	injection
"""


"""
FastAPI:
    FastAPI is a modern, fast(high performance) web framework, allows you to create a restful apis
    automatically generated api docs
    fefatrues:
        - Automatic docs
        - python type hints
        - data validation 
        - asynchrounous support 
        - depenedency injection
        - security support 
    WSGI and ASGI
        - wsgi one req at a time
        - asgi handles asycn protocols like websocket, http polling etc all allowing multiple tasks concurrently
        - starllite toolkit
        - fastapi is just a logic, The ASGI server handles the "networking" and hands off the organized request to FastAPi
    working with asgi:
        - The multiplexer
        - the wait state
        - concurrency
        - callbacks
        - (number of cpu cores * 2) + 1

"""
"""
pydantic models:
    - schema
    - inherits from the basemodle
    - basemodel, typing 
    - field
    - field validator(decorator), modelvalidator and computed validator
    - nested model referencing and self referencing model -> comment (forward referencing)
    - serialisation model_dump()
    - configDict from pydantic 
    - 

"""
