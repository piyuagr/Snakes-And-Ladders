
1. getCompoundInterest function calculates interest using values of P, R, T (in years). An iterative implementation is used to calculate the Compound Interest, which is compounded annually. 

2. reqLoan function can bre used by anyone to request the Owner to settle his loan. The P, R, T entered is used to calculate the dues, and is added to a mapping. The function emits the Request event too.

3. getOwnerBalance function used MetaCoin contract's getBalance to implemenet it which is an example of inheritance.

4. viewDues function was made and only the owner can access this to view the amount of loan he owes to the input address, which is stored in the loans mapping. Making use of the modifier IsOwner.

5. settleDues function allows only the owner to settle the amount of loan he owes using MetaCoin's sendCoin function to settle dues.
