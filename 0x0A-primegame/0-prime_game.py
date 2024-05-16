#!/usr/bin/python3
"""
Task 0. Prime Game.

# print(primeNum(2))
# print("Winner: {}".format(isWinner(3, [4, 5, 1])))
# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
"""


def nextPlayer(current):
    """_summary_

    Args:
        current (_type_): _description_

    Returns:
        _type_: _description_
    """
    players = {
        1: 'Maria',
        2: 'Ben'
        }
    lent = len(players)
    for k in players:
        if players[k] == current:
            if k == lent:
                return players[1]
            else:
                return players[k + 1]


def primeNum(n):
    """gives the value of prime number or -1

    Args:
        n (int): _description_

    Returns:
        float: _description_
    """
    if n > 1:
        for i in range(2, (n//2)+1):
            if (n % i) == 0:
                return -1
        else:
            return n
    else:
        return -1


def isWinner(x, nums):
    """_summary_

    Args:
        x (int): the number of rounds
        nums (int): array of n

    Returns:
        str : name of the player that won the most rounds
    """
    prime = -1
    winner = ''
    scores = {
        'Maria': 0,
        'Ben': 0
        }
    if x < 1 or not nums:
        return None
    while (x != 0):
        for i in nums:
            player = 'Maria'
            # print(x, ' round:', i, 'pleyer', player)
            if i == 0:
                scores[nextPlayer(player)] += 1
            else:
                gameList = list(range(1, i + 1))
                # print(gameList, player)
                if gameList == [1]:
                    # winner = pla
                    # print(player)
                    scores[nextPlayer(player)] += 1
                    # player = nextPlayer(player)
                while (gameList != [1]):
                    for j in gameList:
                        prime = primeNum(j)
                        if (prime != -1):
                            for k in gameList:
                                if k % prime == 0:
                                    gameList = set(gameList)
                                    gameList.discard(k)
                                    gameList = list(gameList)
                            break
                    # print(player, "choose ", prime, "list  ", gameList)
                    if gameList == [1]:
                        # winner = player
                        scores[player] += 1
                    # print(scores)
                    player = nextPlayer(player)
            x -= 1
    # print(scores)
    if scores['Maria'] > scores['Ben']:
        winner = 'Maria'
    elif scores['Maria'] == scores['Ben']:
        winner = None
    else:
        winner = 'Ben'
    return winner
