// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FactorialContract {

    function calculateFactorial(uint256 n) public pure returns (uint256) {

        uint256 m = 1;


        if (n == 0){
            m = 1; //factorial of 0 is 1
        }

        for (uint256 i = n; i > 1; i--){
            m *= i;
        }
        return m;
     
    }
}
