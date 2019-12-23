#Library Management System in _Odoo 13_

Features
========

Depends
=======
[library] addon Odoo

Tech
====
* [Python] - Models
* [XML] - Odoo views

Installation
============
- www.odoo.com/documentation/10.0/setup/install.html
- Install my custom addon


*Object Relational Model (ORM)* 
============
Librarian           |Library             | Books              |   
--------------------|--------------------|--------------------|                      
-Name               |-location           |-bookTitle          | 
-librarian id       |-Librarian id       |-bookAuthor         |
--------------------|--------------------|-bookId             |
+issueStatus()      |                    |--------------------|
+searchBook()       |                    |+update()           |
+verifyMember()     |                    
+issueBook()        |
+payment()          |

Patron Record       | Vendor              | Patron              |
--------------------| --------------------| --------------------|
-patronId           | -bookDetails        | -details            |
-type               | --------------------| -patronId           |
-dateOfMembership   | +search()           | --------------------|
-noBookIssued       | +supplyBooks()      | +search()           |
-maxBookLimit       | +paymentDetails()   | +request()          |
-name               |                     | +payFine()          |
-address            |
-phoneNo            |
-finesOwed          |
--------------------|
+retrieveMember()    |
+increaseBookIssued()|
+decreaseBookIssued()|
+payFine()           |

Author
------
Developer: Jordan Muthemba





