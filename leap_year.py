def check_user_input(year):
    while True:
        try:
            year = int(year)
        except:
            print("invalid input!")
        else:
            return year
def check_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year!")
        return 0
    else:
        print(year, "is not a leap year!")
        return  -1

def main():
    year = int(input("Specify a year: "))
    year = check_user_input(year)
    check_leap_year(year)

if __name__ == "__main__":
    main()