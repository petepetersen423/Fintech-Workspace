pragma solidity ^0.5.0;

// SPDX-License-Identifier: MIT

contract TradeController {
    uint256 previousPrice;
    string tradeType;

    function makeTrade(uint256 currentPrice, bool buyAnyway) public {
        if (currentPrice < previousPrice || buyAnyway) {
            tradeType = "Buy";
            previousPrice = currentPrice;
        } else if (currentPrice > previousPrice) {
            tradeType = "Sell";
            previousPrice = currentPrice;
        } else {
            tradeType = "Hold";
        }
    }
}
