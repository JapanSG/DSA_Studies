'''Labs 08.01 - Coin Exchange'''
import json
def convert_key(data : dict):
    '''JSON'''
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount : int ,data : dict) -> dict:
    '''Coin Excahnge method'''
    coin_used = {10 : 0, 5 : 0, 2 : 0, 1 : 0}
    for coin in data:
        while data[coin] > 0 and amount - coin >= 0:
            data[coin] -= 1
            amount -= coin
            coin_used[coin] += 1
    if amount > 0:
        return None
    return coin_used

def main():
    total = int(input())
    data = convert_key(json.loads(input()))
    result = coin_exchange(total,data)
    print(f"Amount: {total}")
    if result == None:
        print("Coins are not enough.")
        return
    print("Coin exchange result:")
    coin_num = 0
    for coin, amount in result.items():
        coin_num += amount
        print(f"  {coin} baht = {amount} coins")
    print(f"Number of coins: {coin_num}")
main()