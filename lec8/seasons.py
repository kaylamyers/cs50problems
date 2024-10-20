from datetime import date
import sys
import inflect

p = inflect.engine()

class DOB:
    def __init__(self, date):
        self.date = date
    def __sub__(self, input):
        return self.date - input.date

def main():
    print(minutes(input('Date of Birth: ')))

def minutes(dateInput):
    try:
        today = date.today()
        year, month, day = str(dateInput).split('-')
        cal = date(int(year), int(month), int(day))
        #timeDiff = today.__sub__(cal)
        timeDiff = today - cal
        mins = int(timeDiff.total_seconds()/60) # conversion to minutes
        num2word = p.number_to_words(mins)
        dob = num2word.replace(' and ', ' ').capitalize()

        return f'{dob} minutes'

    except ValueError:
        sys.exit('invalid date')


if __name__ == "__main__":
    main()
