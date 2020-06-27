def one():
    print(95)
def two():
    print(85)
def three():
    print(75)
def four():
    print(65)
def five():
    print(50)
def default():
    print('Invalid Input default case')


def switch_average(case):
    switch = {
        'A': one,
        'B': two,
        'C': three,
        'D': four,
        'F': five
    }
    functionToCall = switch.get(case, default)
    functionToCall()

if __name__ == '__main__':
    switch_average('A')
    switch_average('E')
