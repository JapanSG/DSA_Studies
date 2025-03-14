'''BubbleV2 ( Medium )'''
def run(track : list, info : list):
    memo = {0 : []}
    for i in range(1,len(track)):
        shortest = None
        if info[i] == " ":
            memo[i] = None
            continue
        for past in range(i-1, -1,-1):
            if memo[past] is None:
                continue
            candidate = memo[past].copy()
            # print(candidate, shortest)
            if int(info[past]) >= i-past:
                if shortest == None or len(shortest) > len(candidate + [i-past]):
                    shortest = candidate + [i-past]
                else:
                    continue
        memo[i] = shortest
    # print(memo)
    return memo[len(track)-1]
        
def main():
    '''Driver Code'''
    track = list(input())
    bubble_info = input().split()
    temp = []
    i = 0
    for space in track:
        if space == "o":
            temp.append(bubble_info[i])
            i += 1
        elif space == "^":
            temp.append("1")
        else:
            temp.append(space)
    bubble_info = temp
    result = run(track,bubble_info)
    if not result:
        print(-1)
    else:
        print(len(result))
main()
