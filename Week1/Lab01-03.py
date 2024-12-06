'''Lab 01.03 - SwapVar'''

def convert_string_to_tuples(text_in):
    '''Convert str to tuple'''
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

def main():
    '''Driver Code'''
    a,b = convert_string_to_tuples(input())
    print(f"{float(b),float(a)}")

if __name__ == "__main__":
    main()
