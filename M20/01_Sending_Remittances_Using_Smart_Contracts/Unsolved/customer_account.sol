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
            address payable,
            bool,
            uint256,
            string memory,
            string memory
        )
    {
        return (
            owner,
            authorizedRecipient,
            isNewAccount,
            accountBalance,
            customerName,
            customerLastName
        );
    }

    function setInfo(
        address payable newOwner,
        address payable newAuthorizedRecipient,
        bool newAccountStatus,
        uint256 newAccountBalance,
        string memory newCustomerName,
        string memory newCustomerLastName
    ) public {
        owner = newOwner;
        authorizedRecipient = newAuthorizedRecipient;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }

    function sendRemittance(uint256 amount, address payable recipient) public {
        require(
            recipient == owner || recipient == authorizedRecipient,
            "The recipient address is not authorized!"
        );
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
