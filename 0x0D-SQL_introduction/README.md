Databases and SQL
-   A database is a systematic collection of data. A solid database is expected to be acid, which means it guarantees:

Atomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
Consistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
Isolation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
Durability: unplug your server at any time, boot it back up, and it didn’t lose any data. There are 4 operations that can be performed on the data itself:

Create some data;
Read some data;
Update some data;
Destroy some data.
Obviously, a database should allow all four.

Relational Database 
When people talk about databases, they’re usually referring to relational databases (such as PostgreSQL, MySQL, Oracle, …); but there are many other kinds of databases used in the industry, which are globally referred to as “NoSQL” databases, even though they can be very different from each other, and serve very various purposes. Engineers that are comfortable with SQL are very respected in the industry, even more so in this age where data has gotten so valuable. 

Say you need to store users. To do that, you create a table that is called “users”.

Your users have 3 pieces of information to store: their “id”, their “login”, and their “password”. Those are called columns, and they all have types, like integer for the “id”, varchar(32) for “login” (a string of variable length, but maximum 32), and char(32) (a string of exactly 32 characters, which is the case for all text encrypted with the md5 algorithm, for instance). The available types may vary heavily from one database “brand” to the other.

Now, let’s add a user in the database with SQL:

INSERT INTO users (login, password) VALUES ('rudy', '01234567890123456789012345678901');
This adds a row in the table (sometimes also refered to as a record, or more rarely, a tuple).

A relation as used today is something that ties two records together, most often across different tables. For instance, say you have a blog, and you have 2 tables:

posts, with the fields id, title and body
comments, with the fields id and body
In both tables, the “id” fields are primary keys, because they uniquely identify the row that they belong to (if you say “give me the post of id 4”, you’re sure to be getting only one post).

But how do you know that a given comment is attached to a given post. Well, you add a postid field to the comments table, containing the id of the post you with to attach it to. The postid field is called a foreign key, uniquely identifying another’s table primary key.

SQL stands for Structured Query Language. MySQL is an open-source database management system, commonly installed as part of the popular LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack. It implements the relational model and uses Structured Query Language (better known as SQL) to manage its data.

Tasks on Basics: SQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions
======================================================================================================================
