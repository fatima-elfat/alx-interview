#!/usr/bin/python3
"""
Task 0. Prime Game.

# print(primeNum(2))
# print("Winner: {}".format(isWinner(3, [4, 5, 1])))
# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
"""


def isPrimeNbr(n):
    """return 1 if prime

    Args:
        n (int): _description_

    Returns:
        float: _description_
    """
    if n > 1:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0


def isWinner(x, nums):
    """_summary_

    Args:
        x (int): the number of rounds
        nums (int): array of n

    Returns:
        str : name of the player that won the most rounds
    """
    winner = ''
    scores = {
        'Maria': 0,
        'Ben': 0
        }
    if x < 1 or not nums:
        return None
    for i in nums:
        primes = 0
        gameList = list(range(1, i + 1))
        for j in gameList:
            if isPrimeNbr(j):
                primes += 1
        if primes % 2 == 0:
            scores['Ben'] += 1
        else:
            scores['Maria'] += 1
    if scores['Maria'] > scores['Ben']:
        winner = 'Maria'
    elif scores['Maria'] == scores['Ben']:
        winner = None
    else:
        winner = 'Ben'
    return winner
