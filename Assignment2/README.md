
1. getCompoundInterest : allows anyone to use it to calculate the amount of interest for given values of P, R, T (in years). Remember that solidity does not have a good support for floats though, so enter the rate as a whole number (like if the rate is 83%, enter 83). We are looking for an iterative implementation to calculate the Compound Interest, which is compounded annually, to test if you understood the applications of loops. This is an inefficient method though, and we'll come back to that later, but we want it to be iterative. A few blogs to clue you in to how to perform percentage based calculations with just integers have been provided in the template.

2. reqLoan function can bre used by anyone to request the Owner to settle his loan. The P, R, T entered is used to calculate the dues, and is added to a mapping. The function emits the Request event too.

3. getOwnerBalance: anyone can use it to get the amount of MetaCoins owned by the owner. make use of MetaCoin contract's getBalance to implement this, to get a taste of inheritance!

4. viewDues function was made and only the owner can access this to view the amount of loan he owes to the input address, which is stored in the loans mapping. Making use of the modifier IsOwner.

5. settleDues: only the owner can use this to settle the amount of loan he owes to the input address, use MetaCoin's sendCoin function to settle these dues, with appropriate checks for the return values from sendCoin. Also remember to set the amount owed to 0 or whatever remains if sendCoin runs succesfully!
