def dictinput():
    dict = {}
    n = int(input("Enter the amount of values that will be added to the dictionary: "))
    key = 1
    for x in range(0, n):
        key = str(input())
        value = int(input())
        dict[key] = value
    print(dict)
if __name__ == '__main__':
    dictinput()