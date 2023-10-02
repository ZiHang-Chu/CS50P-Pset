months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                mm, dd, yyyy = date.strip().split("/")
            elif "," in date:
                mmdd, yyyy = date.strip().split(",")
                mm, dd = mmdd.split(" ")
                mm = months.index(mm) + 1
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
        except (AttributeError, ValueError, NameError, KeyError):
            pass
        else:
            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break


main()
