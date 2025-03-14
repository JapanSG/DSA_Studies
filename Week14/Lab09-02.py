'''Lab 09.02 - KnapsackV2'''
import json
class Item:
    def __init__(self, name : str, value : int, weight : int):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"{self.name} -> {self.weight} kg -> {self.value} THB"

def get_best_price(items : list, limit :int):
    memo = []
    for i,item in enumerate(items):
        item :Item
        sacks = []
        for j in range(1, limit+1):
            if i-1 < 0:
                if item.weight <= j:
                    sacks.append([item])
                else:
                    sacks.append([])
                continue
            if item.weight < j:
                # print(j-item.weight-1)
                new_sack = memo[i-1][j-item.weight-1]+[item]
                # print(new_sack)
                if value_sum(memo[i-1][j-1]) < value_sum(new_sack):
                    sacks.append(new_sack)
                else:
                    sacks.append(memo[i-1][j-1])
            elif item.weight == j:
                if value_sum(memo[i-1][j-1]) < item.value:
                    sacks.append([item])
                else:
                    sacks.append(memo[i-1][j-1])
            else:
                sacks.append(memo[i-1][j-1])
        memo.append(sacks)
        # print(item.name)
        # for i,sack in enumerate(memo[i]):
        #     print(f"Weight={i+1}:{sack}")
        # print('')
    # for i,sack in enumerate(memo):
    #     print(f"{i+1} {sack}")
    return memo[-1][-1]

def value_sum(lis :list):
    total = 0
    for item in lis:
        total += item.value
    return total
def main():
    '''Driver Code'''
    data  =json.loads(input())
    items = [Item(name,value,weight) for name,value,weight in data]
    limit = int(input())
    result = sorted(get_best_price(items,limit), key = lambda x : x.name)
    print(f"Total: {value_sum(result)}")
    for item in result:
        print(item)
main()
