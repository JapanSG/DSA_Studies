'''Exercise 07.02 - Runner'''
def calc_time(spd: int, distance : int) -> float:
    return distance/spd
def find_winner(player_lis : list, start_dis) -> list:
    '''Return the index of the player who will win the race'''
    winner_index = -1
    winner_data = [1,0]
    for i,(spd,distance) in enumerate(player_lis):
        time = calc_time(spd, start_dis - distance)
        winner_time = calc_time(winner_data[0], start_dis - winner_data[1])
        if (time < winner_time) or (time == winner_time and spd > winner_data[0]):
            winner_data = [spd,distance]
            winner_index = i
    return winner_index
def main():
    '''Driver Code'''
    distance = float(input())
    player_num = int(input())
    player_lis = [[int(num) for num in input().split()] for _ in range(player_num)]
    print(find_winner(player_lis,distance)+1)
main()
