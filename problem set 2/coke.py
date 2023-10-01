def main():
    valid_coins = [25, 10, 5]
    cost = 50
    tendered = 0

    while tendered < cost:
        print(f"Amount Due: {cost - tendered}")
        insert = int(input("Insert Coin: ").strip())
        if insert in valid_coins:
            tendered += insert
        else:
            continue
    print(f"Change Owed: {tendered - cost}")


main()
