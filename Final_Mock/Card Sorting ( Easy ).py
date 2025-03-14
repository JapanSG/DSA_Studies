'''Card Sorting ( Easy )'''
import json
def bubble(lis : list, key = None):
    for _ in range(len(lis)):
        swapped = False
        for i in range(len(lis)-1):
            if key(lis[i]) < key(lis[i+1]):
                swapped = True
                lis[i], lis[i+1] = lis[i+1], lis[i]
        if not swapped:
            return

def get_player(player_num):
    player_list = []
    for _ in range(player_num):
        player = json.loads(input())
        lis = player[1]
        bubble(lis, key = lambda x : (x[-1], x[0] == "K", x[0] == "Q", x[0] == "J", len(x[0:-1]) , x[0] != "A", x[0]))
        player_list.append(player)
    return player_list

def get_point(lis):
    total = 0
    for card in lis:
        if card == "2C" or card == "QS":
            total += 50
        elif "A" in card:
            total += 15
        elif "K" in card or "10" in card or "Q" in card or "J" in card:
            total += 10
        else:
            total += 5
    return total

def main():
    '''Driver Code'''
    player_num = int(input())
    hand_size = int(input())
    player_list = get_player(player_num)
    bubble(player_list, key = lambda x : (get_point(x[1]), x[0]))
    for player in player_list:
        print(f"{player[0]} -> {get_point(player[1])} -> {player[1]}")

if __name__ == "__main__":
    main()
