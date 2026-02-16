"""
Docstring for Day-11.__Doc__
  PostgreSQL	basics
  SQL	queries
  Indexes
  Transactions
"""

"""
postgresql:
    - postgresql is rdms
    - postgresql is open source
    - inbuilt acid compliant
    - high performance and scalable (mvcc,vaccum)
    - robust and secure  
    - supports multiple programming languages
    
"""

"""
sql queries:
    ddl: data definition language
    dml: data manipulation language
    drl: data retrieval language
    dcl: data control language
    tcl: transaction control language

"""

"""
indexes:
    - indexing
    - types of indexing
    - advantages of indexing
    - disadvantages of indexing

 
"""


"""
transactions:
    - transaction
    - properties of transaction (ACID)
    - transaction states
"""


"""
queries:
    ddl:
     - create table table_name (co1 datatype, col2 datatype);
     - alter table table_name add column col3 datatype:
     - alter table old_table_name RENAME TO new_table_name;
     - drop table table_name;
     - truncate table table_name;
     
    DMl:
     - insert into table_name (col1, col2) values (val1, val2);
     - update table_name set col1 = val1 where condition;
     - delete from table_name where condition;
     
    DRL:
     - select col1, col2 from table_name where condition;
     - select col from table_name left join another_table on table_name.col = another_table.col where condition;
    
    DCL:
     - grant select, insert on table_name to user_name;
     - revoke update on table_name from user_name;
     
    TCL:
        - begin;
        - commit;
        - rollback;

"""
