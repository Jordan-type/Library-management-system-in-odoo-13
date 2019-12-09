###-- Object Relational Model (ORM) --
#--- Library Mangement System ---

Library 
--------------------                       
-location
-librarian id 
--------------------

Librarian
-Name
-Librarian id 
--------------------
+issueStatus()
+searchBook()
+verifyMember()
+issueBook()
+payment()

Books Database
--------------------
-bookTitle
-bookAuthor
-bookId
--------------------
+update()

Patron
--------------------
-details
-patronId
--------------------
+search()
+request()
+payFine()

Patron Record
--------------------
-patronId
-type
-dateOfMembership
-noBookIssued
-maxBookLimit
-name
-address
-phoneNo
-finesOwed
--------------------
+retriveMember()
+increaseBookIssued()
+decreaseBookIssued()
+payFine()

Vendor
--------------------
-bookDetails
--------------------
+search()
+supplyBooks()
+paymentDetails()


   


