/*
CHALLENGES
1. **Hello World**: Create a simple contract that stores a string message set during deployment.
2. **Simple Storage**: Create a contract to store and retrieve an unsigned integer.
3. **Basic Counter**: Implement a counter that can be incremented and decremented.
4. **Boolean Flag**: Create a contract with a boolean flag that can be toggled.
5. **User Greeting**: Store and retrieve a personalized greeting for users.
*/

//SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/utils/Strings.sol";

pragma solidity ^0.8.2;

contract challengeOneThruFive{

    //State Variables
    string public hail;
    uint128 public count;
    uint128 public iter;
    bool public flag;
    mapping(address => string) public greeting;

    constructor(){

        hail = "Hail, Guildsman!";
        count = 2*2*2*2;
        iter = 0;
        flag = false;
        

    }

    function getHail() public view returns (string memory){

        return hail;

    }

    function getCount() public view returns (uint128){

        return count;

    }

    function getIter() public returns (uint128){

        iter += 1;
        return iter;

    }

    function getFlag() public returns (bool){

        if(iter % 2 == 0){

            flag = true;
            return flag;

        } else if (iter % 2 != 0){

            flag = false;
            return flag;

        }


    }

    function getAddress() public view returns (address){

        return msg.sender;


    }

    function greetPlayer() public returns (string memory){

        greeting[msg.sender] = string(abi.encodePacked("Greetings, ", Strings.toHexString(uint256(uint160(msg.sender)), 20), ", welcome to The Game!"));
        return greeting[msg.sender];

    }

    function exeAll() public returns (string memory){

        getHail();
        getCount();
        getIter();
        getFlag();
        getIter();
        getIter();
        getIter();
        getFlag();
        getAddress();
        greetPlayer();

    }

}
