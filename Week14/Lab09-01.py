'''Lab 09.01 - coinExchangeV2'''
import json
def coin_exchange(amount, coins :dict):
    '''coin exchange'''
    memo = {key:[key] for key in coins}
    for i in range(1, amount+1):
        found = False
        currbest = None
        for coin in memo:
            if coin <= i:
                coins_copy = coins.copy()
                found = True
                dif = i - coin
                if dif == 0:
                    currbest = [coin]
                    break
                past = memo[dif]
                if past is None or memo[coin] is None:
                    continue
                candidate = memo[coin]+past
                no_coin = False
                for num in candidate:
                    coins_copy[num] -= 1
                    if coins_copy[num] < 0:
                        no_coin = True
                        break
                if no_coin:
                    continue
                if (not currbest) or (len(candidate) <= len(currbest)):
                    currbest = candidate
        if found:
            memo[i] = currbest
        else:
            memo[i] = None
    # print(memo)
    return memo[amount]

def main():
    amount = int(input())
    coins = json.loads(input())
    coins = {int(x):coins[x] for x in coins}
    ans = coin_exchange(amount,coins)
    print(f"Amount: {amount}")
    if not ans:
        print("Can not exchange.")
        return
    print("Coin exchange result:")
    dct = {}
    for num in ans:
        dct[num] = dct.get(num,0)+1
    for key in sorted(coins, reverse=True):
        print(f"  {key} baht = {dct.get(key,0)} coins")
    print(f"Number of coins: {sum(dct.values())}")
main()
