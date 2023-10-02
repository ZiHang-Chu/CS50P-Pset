def main():
    grocery = {}
    while True:
        try:
            item = input().strip().upper()
            if item not in grocery:
                grocery[item] = 1
            else:
                grocery[item] += 1
        except EOFError:
            sort_list = sorted(grocery.items())
            for i in sort_list:
                print(i[1], i[0], sep=" ")
            break
        except KeyError:
            pass


main()
