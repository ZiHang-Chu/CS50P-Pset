# meal schedule
schedule = [
    {"meal": "breakfast time", "start hour": 7, "end hour": 8},
    {"meal": "lunch time", "start hour": 12, "end hour": 13},
    {"meal": "dinner time", "start hour": 18, "end hour": 19},
]


def main():
    time = input("What time is it? ")
    time = convert(time)

    for dict1 in schedule:
        if dict1["start hour"] <= time <= dict1["end hour"]:
            print(dict1["meal"])
        else:
            continue


def convert(time):
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60)
    return t


if __name__ == "__main__":
    main()
