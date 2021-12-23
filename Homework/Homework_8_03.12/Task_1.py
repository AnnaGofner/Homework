class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Right!'
                else:
                    return f'Wrong year!'
            else:
                return f'Wrong month!'
        else:
            return f'Wrong day!'

    def __str__(self):
        return f'Today is {Date.extract(self.day_month_year)}'


today = Date('15 - 12 - 2021')
print(today)
print(Date.valid(40, 12, 2021))
print(today.valid(15, 13, 2021))
print(Date.extract('11 - 09 - 2001'))
print(today.extract('15 - 03 - 1999'))
print(Date.valid(15, 12, 2021))
