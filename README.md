# CECS-343
CSU Long Beach CECS 343 Software Engineering with Prof. Phuong Nguyen (Summer 2021)

WEBSITE: **http://Team6.pro**
Apartment Rental System: Multiuser Edition v1.0
Team 6: Sterling Engle (team leader), Jacob Sunia, Larry Delgado, and Matthew Chung

Project Assignments, Python Class Ownership(*) and Roles:

Jacob:
1. UserInterface.py
2. UserList.py
3. RentalInputScreen.py
4. RentRow.py
5. RentRecords.py
6. ExpenseInputScreen.py
7. Expense.py
8. ExpenseRecords.py
9. main.py
10. UsersApartmentData.json JSON data file design
11. All JSON-related code
12. Collaboration diagram (done, needs final review)
13. Component design diagram (done, need final review)
14. State diagram
15. Installation and deployment diagram (done, needs final review)

Sterling:
1. User Interface Design (done)
2. TenantInputScreen.py (done)
3. TenantList.py (done)
4. Tenant.py (done)
5. LoginInputScreen.py (done)
6. Integration testing, open and assign github repo issues (bugs)
7. Unit Testing (Activity 10)

Larry:
1. ExpenseInputScreen.py
2. ExpenseRecords.py
3. Expense.py
4. Fix and close assigned github repo issues (bugs)
5. Implement Mac deployment
6. Document User Interface: Multiuser Login and Create New User (#34, REQUIRED)
7. Project Summary (REQUIRED)

Matthew:
1. RentInputScreen.py
2. RentRecords.py
3. RentRow.py
4. Document User Interface: Input data and Display data (REQUIRED)
5. Fix and close assigned github repo issues (before final release in time for validation)

EVERYONE:
1. Final system testing, open, assign, fix, and validate github repo issues
2. Review Final 

(*) Class Ownership means you are primarily responsible for this class and will be initially assigned all of its issues. If you need help with an issue, assign it to an additional team member.

Coding Strategy for Larry and Matthew:

Please model your *InputScreen.py coding on TenantInputScreen.py. The same goes for TenantList.py and Tenant.py, although you don’t need to implement so many methods like I did. Note the changes I made to UserInterface.py to make it work correctly - Sterling.

JSON notes for Larry and Matthew:

1. After a user logs in, you have to create ExpenseRecords and RentRecords objects and save them in UserInterface.py. See lines 73-78.
2. Follow how I handled the tenant list in UserInterface.py:105-106. You need to write a .get*Dict method in your *Records.py classes like I did for TenantList.py
