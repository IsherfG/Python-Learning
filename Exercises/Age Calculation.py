import datetime

current_year = datetime.date.today().year
birth_year_str = input('what year were you born? - ')
birth_year = int(birth_year_str)


def fun():
    return current_year - birth_year;


if birth_year < current_year:
    print(fun())


else:
    print('error')
