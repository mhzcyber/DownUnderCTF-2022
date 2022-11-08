pragma solidity ^0.8.0;

import "./SolveMe.sol";

contract CallFun{
    SolveMe public solvemeAddress;
    constructor(SolveMe _solvemeAddress) public{
        solvemeAddress = (_solvemeAddress);

    }
    function attack() public{
        solvemeAddress.solveChallenge();
    }
}