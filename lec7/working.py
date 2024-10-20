import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if match := re.search(
        r"^([0-9]{1,2}):?([0-5]{0,1}[0-9]{1})?\s{1}(AM{1}|PM{1})\sto\s([0-9]{1,2}):?([0-5]{0,1}[0-9]{1})?\s(AM{1}|PM{1})$", s):

        hour1 = int(match.group(1))     # 9
        min1 = match.group(2)           # 00
        ampm1 = str(match.group(3))     # AM
        hour2 = int(match.group(4))     # 5
        min2 = match.group(5)           # 00
        ampm2 = str(match.group(6))     # PM

        if 1 <= hour1 <= 12 and 1 <= hour2 <= 12:
            if ampm1 == 'AM':
                if hour1 == 12:
                    hour1 = 0
                if min1 == None:
                    min1 = 0
                elif 0 <= int(min1) <= 59:
                    min1 == min1
            elif ampm1 == 'PM':
                if hour1 != 12:
                    hour1 += 12
                if min1 == None:
                    min1 = 0
                elif 0 <= int(min1) <= 59:
                    min1 == min1

            if ampm2 == 'AM':
                if hour2 == 12:
                    hour2 = 0
                if min2 == None:
                    min2 = 0
                elif 0 <= int(min2) <= 59:
                    min2 == min2
            elif ampm2 == 'PM':
                if hour2 != 12:
                    hour2 += 12
                if min2 == None:
                    min2 = 0
                elif 0 <= int(min2) <= 59:
                    min2 == min2
                
        else:
            raise ValueError('input valid times')
    else:
        raise ValueError('input valid times')
    
    return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"


if __name__ == "__main__":
    main()

