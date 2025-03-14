'''Shadow&Dragon ( Hard )'''
def kill_dragon(attk : int, hp : int, army_atk : list, army_hp : list, total_hp, army_num : int):
    '''return mana used'''
    least_mana = 1000000000000
    for i in range(army_num):
        atk_mana = hp-army_atk[i]
        if atk_mana < 0:
            atk_mana = 0
        hp_mana = attk + army_hp[i] - total_hp
        if hp_mana < 0:
            hp_mana = 0
        mana_used = atk_mana + hp_mana
        if mana_used < least_mana:
            least_mana = mana_used
    return least_mana

def main():
    '''Driver Code'''
    army_num = int(input())
    army_attk = [int(x) for x in input().split()]
    army_hp = [int(x) for x in input().split()]
    dragon_num = int(input())
    dragon_attk = [int(x) for x in input().split()]
    dragon_hp = [int(x) for x in input().split()]
    while len(dragon_hp) < dragon_num:
        dragon_hp.append(army_hp[len(dragon_attk)-1])
    total_hp = sum(army_hp)
    for i in range(dragon_num):
        print(kill_dragon(dragon_attk[i], dragon_hp[i], army_attk, army_hp, total_hp, army_num))
main()
