month_list = [
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


while True:
    try:
        anno = str(input('enter a date: ')).title()
        if "/" in anno:
            month, day, year = anno.split("/")
            if int(day) <= 31 and int(month) <= 12:
                break
            else:
                raise ValueError
        elif "," in anno:
            md, year = anno.split(", ")
            mnth, day = md.split(" ")
            if mnth in month_list:
                month = month_list.index(mnth) + 1
                if int(month) <= 12 and int(day) <= 31:
                    break
            else:
                raise KeyError
    except KeyError:
        print('please input a date')
    except ValueError:
        print('please input a date')


print(int(year), "-", f"{int(month):02}", "-", f"{int(day):02}", sep='')
