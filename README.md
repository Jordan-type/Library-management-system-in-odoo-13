#Library Management System in _Odoo 13_ 
##*Object Relational Model (ORM)* 


Library             |   
--------------------|                      
-location           |   
-librarian id       |

Librarian           | Books Database      |
--------------------| --------------------|
-Name               | -bookTitle          |
-Librarian id       | -bookAuthor         |
--------------------| -bookId             |
+issueStatus()      | --------------------|
+searchBook()       | +update()           |
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







