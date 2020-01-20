import os


def check_input():
    i = str(input())
    if len(i) > 0:
        return i
    else:
        return None


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'temp.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    li = []
    n = int(input())
    d = dict(input().split() for _ in range(n))
    inp = check_input()

    while inp != None:
        li.append(inp)
        inp = check_input()

    for i in range(len(li)):
        if li[i] in d:
            fptr.write(li[i] + '=' + d[li[i]] + '\n')
        else:
            fptr.write(str("Not found") + '\n')

    fptr.close()
