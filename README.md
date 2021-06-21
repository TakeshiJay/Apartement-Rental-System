# CECS-343
CSU Long Beach CECS 343 with Prof. Phuong Nguyen(Summer 2021)
  - All course material is ©PhuongNguyen

Apartment Rental System - Multiuser Edition v0.4
Team 6: Sterling Engle (lead)
        Jacob Sunia, Larry Delgado, and Matthew Chung

Python Class Ownership(*) and Roles:

Jacob:
1. UserInterface.py (done)
2. UserList.py (done)
3. main.py (done)
4. All JSON-related code (needs ExpenseRecords, RentRecords to work like TenantList)
5. UsersApartmentData.json data file design (done)
6. Integration testing, open and assign github repo issues (bugs)

Larry:
1. ExpenseInputScreen.py
2. ExpenseRecords.py
3. Expense.py
4. Fix and close assigned github repo issues (bugs)

Matthew:
1. RentInputScreen.py
2. RentRecords.py
3. RentRow.py
4. Fix and close assigned github repo issues (bugs)

Sterling:
1. TenantInputScreen.py (done)
2. TenantList.py (done)
3. Tenant.py (done)
4. LoginInputScreen.py (done)
5. AnnualReport.py (about to start)
6. Menu interface design (done)

Everyone:
1. Final system testing, open and assign github repo issues (bugs)
2. Revise final report CRC cards and class diagrams to match our actual code

(*) Class Ownership means you are primarily responsible for this class and will be initially assigned all of its issues. If you need help with an issue, assign it to an additional team member.

Coding Strategy for Larry and Matthew:

Please model your *InputScreen.py coding on TenantInputScreen.py. The same goes for TenantList.py and Tenant.py, although you don’t need to implement so many methods like I did. Note the changes I made to UserInterface.py to make it work correctly.

JSON notes for Larry and Matthew:

1. After a user logs in, you have to create ExpenseRecords and RentRecords objects and save them in UserInterface.py. See lines 73-78.
2. Follow how I handled the tenant list in UserInterface.py:105-106. You need to write a .get*Dict method in your *Records.py classes like I did for TenantList.py
