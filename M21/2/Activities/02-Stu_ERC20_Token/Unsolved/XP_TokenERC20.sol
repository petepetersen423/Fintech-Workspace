pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract XP_Token is ERC20, ERC20Detailed {
    address payable owner;
    modifier onlyOwner() {
        require(msg.sender == owner, "You NEED PERMISSION!");
        _;
    }

    // @TODO: Pass the required parameters to `ERC20Detailed`
    constructor(uint256 initial_supply)
        public
        ERC20Detailed("XP_Token", "XPT", 18)
    {
        // @TODO: Set the owner to be `msg.sender`
        owner = msg.sender;
        // @TODO: Call the internal `_mint` function to give `initial_supply` to the `owner`
        _mint(owner, initial_supply);
    }

    // @TODO: Add the `onlyOwner` modifier to this function after `public`
    function mint(address recipient, uint256 amount) public onlyOwner {
        // @TODO: Call the internal `_mint` function and pass the `recipient`
        //and `amount` variables
        _mint(recipient, amount);
    }
}
