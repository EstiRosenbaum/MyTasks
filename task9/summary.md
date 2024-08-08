# PL/SQL

To define variables you must define:
DECLARE
and after that the variables must be written for example:
my_number <number> :=5;
In the code block you must write (required)

BEGIN

END;

The EXCEPTION definition is for error handling.

After BEGIN the body of the program must be written.

After END you must mark a slash / it marks like;

### PRINT
Before running a program with outputs,

run this line:

`set server output on;`

The put_line function accepts a string as a parameter, prints it and creates a line break.
The put function accepts a string as a parameter and prints it, without line breaks.
###TYPES
There are 4 main types:
1. number
2. varcher2
3. boolean
4. date

User Defined Types (UDT)

Two ways to manually define type:
-create or replace type strings as table of varchar2(4000);
.type object. defined for each schema.
-type strings is table of varchar2(4000);
Local, defined in declare. set for the current block.

### Collections
There are 3 types of collection:
1.Variable-size array (Varray) - an array
2.Nested table - linked list
3. Index-by tables - dictionary
In collections, the index starts with 1.
####Varrays
-Varray = Variable-size array
-It has a maximum size, which can be set in the initialization of the array.

### Nested tables
Unlike arrays, their size is not predetermined but grows dynamically (up to about 2 billion elements).
### Index-by tables (associative arrays)

- consist of a set of keys and a set of values that are mapped to them.
- The key must be unique and limited to integer or string types.
- If we try to change a value in the collection by accessing a key that does not exist, then the key will be added and the value will be mapped under it - this is the way to add members to the collection.
### Control Flow
IF-ELSE
set serveroutput on;`
declare soldier_name varchar2(10);
BEGIN
IF soldier_name = 'Natalie' THEN
dbms_output.put_line('cool');
ELSIF soldier_name = 'Buda' THEN
dbms_output.put_line('Why are you not Natalie??');
ELSE
dbms_output.put_line('Where's Natalie???');
END IF;
END;
/`

### LOOPS - examples
`SET SERVEROUTPUT ON;
BEGIN
FOR a IN 1..5 LOOP
dbms_output.put_line(a);
END LOOP;
END;
/`

### Exceptions
- exceptions is a block designed to catch errors in the code and define what will happen next.
- You can catch a specific exception (for example: NO_DATA_FOUND) and you can catch "everything else" (any other error not specified) by OTHERS.
- You can define exceptions yourself, in addition to the predefined exceptions.
### Cursors
Cursor is an SQL metadata object. It contains information such as the tabular structure of the results table (in the case of a query), the number of updated records (in the case of a DML command) and more.
-Contain Cursor Attributes. For example: SQL%ROWCOUNT - will return the number of rows affected by the operation.
- Cursor can be defined in two ways: by defining a Cursor object (Explicit), or letting it be created automatically behind the scenes by using SQL directly (Implicit).
#### Explicit Cursor
-Defined by us in the DECLARE area of the code.
-It is created based on an SQL query.
-Work with it in the following way:
declare l_id soldiers.id%type;
l_name soldiers.name%type;
CURSOR c_soldiers is select id, name from soldiers; begin
open c_soldiers;
loop
FETCH c_soldiers into l_id, l_name;
EXIT WHEN c_soldiers%notfound;
dbms_output.put_line(‘id: ‘ || l_id || ’, name: ’ || l_name);
END LOOP;
CLOSE c_soldiers;
End;
/
#### Implicit Cursor
- Even when we work on a SQL command directly, a Cursor is created behind the scenes.
- Implicit Cursor properties can also be accessed by using the SQL keyword.

### SQL queries in PL/SQL

#### SELECT INTO
-select into – we will use it to save the return value of a query in variables.
- If the select query does not return information, we will receive a NO_DATA_FOUND error.
-You can't just write a query in PL/SQL without the into clause.

#### BULK COLLECT INTO

- In places where the into clause can be used, there is an option to add bulk collect and thus receive all the results and save them in the collection.

### Dynamic SQL

#### EXECUTE IMMEDIATE
- The command provides us with the ability to run dynamic queries.

#### Functions vs. Procedures
1. Unlike anonymous block, functions and procedures are saved as objects in the schema.
- Functions – signed blocks (with a signature) that return a value.
2. Functions cannot be called just like that, they must always be called in a way that makes use of the return value.
- Procedures – signed blocks that do not return a value.

### Functions
General structure:

`create [or replace] function function_name

[(param_name [in | out | in out] param_type [,…]]

return <return_datatype> {is | as} `

### Procedures
Functions and procedures have the same principles in signing and in any way of writing

### Packages
In packages we save functions, procedures and types and variables that will be recognized in the scope of the package.
The package consists of two parts:

1.declaration where we will declare the objects we want to expose as an API to the user.

2. Body Let's implement the subprograms wedeclared as well as the additional subprogramsfor internal use within the package.

### Triggers

Triggers are stored programs that are automatically activated as soon as a certain event happens.
For example: if we want that every time there is an entry in the soldiers table, then the date of his entry into the unit will be the current date, we can use a trigger.

`create or replace trigger <trigger_name>

{ before | after {
{ insert | update [ of column_name ] | delete }

on table_name

[for each row]

when (condition)

declare …

begin

// what will happen when the event occurs

end;

`