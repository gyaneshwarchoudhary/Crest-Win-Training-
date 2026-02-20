"""
Docstring for Day-14.__Doc__

Day 14
• MongoDB	fundamentals
• Document	modeling
• Indexes
• use cases
"""

"""
mongodb fundamentals
     - document database
     - key-value
     - schema-flexible 
     - scalibilty
     - wired-tiger storage engine
     - memory usage 
     - bson format
     - replication 
"""


"""
document modeling:
    - process of designing 
    - golden rule: data that is accessed together should be stored together
    two main approaches:
     - Embedding
     - referencing (normalization)
    Handling relationships:
     - one-to-one: embedding or referencing
     - one-to-many: embedding (if few related documents) or referencing (if many related documents)
     - many-to-many: referencing (using arrays of ObjectIDs or separate join collection)

"""

"""
indexes:
    - naively navigate from start to end (collection scan || COLLSCAN)
    - to prevent this (IXSCAN)
    - use btree 
    Types of indexes:
        - the default _id index
        - single field index
        - compound index
        - multikey index
        Specialized indexes:
        - text index
        - geospatial index
        - ttl index
    cons:
        - additional storage space
        - slower write performance
        - RAM usage
"""


"""
Use cases:
    - content management systems
    - real-time analytics
    - Internet of Things (IoT)
    - social media applications
    - e-commerce platforms
    - gaming applications

"""
