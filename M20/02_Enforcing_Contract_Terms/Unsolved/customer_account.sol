/*

Enforcing Contract Terms
------------------------
In this activity, you’ll use the `require` function to enhance the `sendRemittance` function of the `CustomerAccount` contract that you created in the previous lesson.

Instructions
------------
1. Open the Remix IDE. Either paste the code from the starter file into a new Solidity file or open the `customer_account.sol` file that you created earlier.

2. Define an `address payable` variable named `authorizedRecipient`. 
  This Ethereum address will represent a third-party account that’s authorized to receive 
  withdrawal payments.

3. To allow the account owner to receive withdrawal payments at their Ethereum address, 
change the `owner` variable to become `payable`.

4. Modify the type of the `newOwner` variable in the `setInfo` function to `address payable`.
 This will avoid compilation errors from the change that you made to the `owner` variable.

5. Change the `sendRemmitance` function by adding a `require` function. 
This `require` function will enforce the rule that only the account owner 
or the authorized recipient can receive ether from the contract balance.

6. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

*/

pragma solidity ^0.5.0;

contract CustomerAccount {
    address payable owner;
    bool isNewAccount;
    uint256 public accountBalance;
    string customerName;
    string customerLastName;
    address payable authorizedRecipient;

    function getInfo()
        public
        view
        returns (
            address,
            bool,
            uint256,
            string memory,
            string memory
        )
    {
        return (
            owner,
            isNewAccount,
            accountBalance,
            customerName,
            customerLastName
        );
    }

    function setInfo(
        address payable newOwner,
        bool newAccountStatus,
        uint256 newAccountBalance,
        string memory newCustomerName,
        string memory newCustomerLastName
    ) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }

    function sendRemittance(uint256 amount, address payable recipient) public {
        require(
            recipient == owner || recipient == authorizedRecipient,
            "Only the owner or the authorized recipient can receive ether"
        );
        {
            return recipient.transfer(amount);
        }
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
