pragma solidity ^0.5.0;

// SPDX-License-Identifier: MIT

contract BankAccount {

    function withdraw(
        uint amount, 
        address payable recipient
        ) public {
        return recipient.transfer(amount);

    function() public payable {};

    function() external payable {};

}   
