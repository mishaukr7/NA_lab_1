import trajectory
from matplotlib import pyplot as plt


def main():
    while True:
        try:
            x0 = float(input('Input x0: '))
            break
        except ValueError:
            print("ERROR. Value must be float type! Try again...")
    while True:
        try:
            y0 = float(input('Input y0: '))
            break
        except ValueError:
            print("ERROR. Value must be float type! Try again...")

    while True:
        try:
            n = int(input('Input the number of iterations: '))
            break
        except ValueError:
            print("ERROR. Value must be integer type! Try again...")
    while True:
        try:
            flag_alpha = float(input('\'0\' - coefficient alpha = 0.001\n'
                                    '\'1\' - coefficient calculated first method\n'
                                    '\'2\' - coefficient calculated second method\n'
                                    'Enter mode selection the coefficient: '))
            if flag_alpha == 0 or flag_alpha == 1 or flag_alpha == 2:
                break
            else:
                print('You can enter only \'0\' or \'1\' or \'2\'. Try again... ')
        except ValueError:
            print('ERROR. Value must be float type! Try again..."')
    x, y = trajectory.get_trajectory(x0, y0, n, flag_alpha)
    plt.plot(x, y)
    plt.show()
    return x, y


main()
