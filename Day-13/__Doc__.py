"""
Docstring for Day-13.__Doc__

• Async	DB	access
• Query	optimization
• N+1	problem
• Performance	tuning

"""

"""
async Db:
    - Non-blocking I/O

    - Better scalability

    - FastAPI nature
 
"""


"""
query optimization:
   - find plan with minimum cost
   - goal is to min system resources and response timex
   - faster query better user experience
   - optimised query better concurrency and scalability
   - reduced hardware and tear (lower power and memory usage)
   Best practices:
    - use indexes
    - use temporary tables
    - avoid select *
    - use joins instead of subqueries
    - use explain to analyze query plans
    - avoid functions on indexed columns
    - use limit to restrict result set
"""


"""
N+1 problem:
    - occurs when an application executes one query to retrieve a list of items (N) and then executes an additional query for each item to retrieve related data (1)
    how to solve:
    - eager loading: retrieve all related data in a single query using joins or prefetching(joinedload,selectinload, subqueryload)
    - batch loading: retrieve related data in batches using IN clause or multiple queries
    - data loader pattern: use a data loader library to batch and cache related data retrieval
    -  reduce database round‑trips, lower latency, and ensure your application scales gracefully.


"""

"""
performance tuning:
    - techninqus used to optimise the speed of db operations
    - iterative process involves anylising current performance, identifying bottlenecks, and implementing optimizations, and measuring the impact
    Identify bottlenecks:
       - database logs, explain plans, performance schema, APM tools
       - analyse the workload: read-heavy, write-heavy, mixed, identify most frq and most expensive queries
       - apply optimizations query , shcehma, configuration, hardware
       - test and measure
    strategies:
        - indexing 
        - denormalization
        - partitioning 
        - clustering
        - caching
        - connection pooling
        - bathc processing
        - cqrs  
        - msa 

"""
