if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        s = list(map(str, input()))
        even_str = ''
        odd_str = ''

        for j in range(len(s)):
            if j % 2 == 0:
                even_str += str(s[j])
            else:
                odd_str += str(s[j])
        print(even_str, "  ", odd_str)
