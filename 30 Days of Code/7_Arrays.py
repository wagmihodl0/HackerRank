if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rev_str = ''

    for i in range(n-1, -1, -1):
        rev_str += str(arr[i]) + ' '

    print(rev_str.rstrip())
