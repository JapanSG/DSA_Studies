'''Lab 09.03 - Longest Common Substring'''
def longest_substring(str1 :str, str2: str):
    memo = []
    longest = ""
    for i,char1 in enumerate(str1):
        row = []
        for j,char2 in enumerate(str2):
            if char1 == char2:
                if i-1 < 0 or j-1 < 0:
                    row.append(char2)
                else:
                    row.append(memo[i-1][j-1] + char2)
            else:
                row.append("")
            if len(row[-1]) > len(longest):
                longest = row[-1]
        memo.append(row)
    return longest

def main():
    str1 = input()
    str2 = input()
    result = longest_substring(str1,str2)
    if not result:
        print("No common substring.")
        return
    print(result)
    print(len(result))
main()
