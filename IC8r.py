def main():
    filename = input('Please enter the name of the file: ')
    try:
        infile = open(filename, 'r')
        total = 0
        count = 0
        for x in infile:
            amount = float(x)
            total += amount
            count+=1
        infile = open(filename, 'r')
        numbers = infile.read()
        print('The numbers in the file are:', numbers)
        infile.close()
        print('There are',count,'numbers total')
        print('The sum of the numbers is:',total)
    except FileNotFoundError:
        print('File cannot be found')
    except IOError:
        print('An error occured trying to read file')
    except:
        print('error occured')
main()