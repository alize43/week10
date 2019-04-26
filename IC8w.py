import random
def random_number():
    number = random.randint(1, 500)
    return number
def main():
    try:
        random_amount = int(input('Please enter how many random numbers the file will hold: '))
        number_file = open('random', 'w')

        for x in range(1, 1 + random_amount):
            number = random_number()
            number_file.write(str(number) + '\n')
        number_file.close()
    except ValueError:
        print('Error: you must enter a number')





main()
