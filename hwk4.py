# Kendra Ludwig (kel334)


def main():
    print("-----------------------------------------------------")
    print("\tWelcome to the Playfair Cipher Machine!")
    print("-----------------------------------------------------")
    menu()


# prints main menu and offers options
def menu():
    print("\t[ Main Menu ]\n")
    print("\tPlease make a selection")
    print("\t\t(e)ncryption")
    print("\t\t(d)ecryption")
    print("\t\t(c)redits")
    print("\t\t(q)uit")
    print("-----------------------------------------------------")
    selection = input("\tYour Selection: ").strip().lower()
    print("-----------------------------------------------------")
    # redirects input
    execution(selection)


# takes input and calls the proper function
def execution(selection):
    only_select = ['e', 'd', 'c', 'q']
    # inputs are restricted, will ask again if input is invalid
    while selection not in only_select:
        try:
            print("\tSorry, that is not an option!")
            print("\tPlease make a new selection.\n")
            selection = input("\tYour Selection: ").strip().lower()
            print()
            if selection in only_select:
                break
        except:
            pass # INTENTIONAL
    if selection == 'e':
        encryption()
    elif selection == 'd':
        decryption()
    elif selection == 'c':
        credits()
    elif selection == 'q':
        quit()


# encrypts the inputs
def encryption():
    print("\tYou have chosen encryption.")
    user_key = input("\tPlease enter your key: ").strip().upper()
    # takes input and alters it for playfair alpha
    key = user_key.replace('Q', 'K')
    key = key.replace('U', 'V')
    select = input("\tPlease enter a message: ")
    # takes input and alters it for playfair alpha
    select = select.strip().upper()
    select = select.replace('Q', 'K')
    select = select.replace('U', 'V')
    select = select.replace(' ', '')
    playfair = 'ABCDEFGHIJKLMNOPRSTVWXYZ '
    k = ""
    # takes encrypted message and makes it playfair compliant
    for char in key + playfair:
        if char not in k:
            k += char
    # creates grid for later reference
    grid = [k[0:5],k[5:10],k[10:15],k[15:20],k[20:25]]
    # tacks an X on the end if the input is odd
    if len(select) % 2 != 0:
        select += 'X'
    # finds neighboring duplicates and replaces one with X
    for i in range(len(select)):
        if select[i] == select[i - 1]:
            insert = select[i - 1]
            insert_x = i - 1
            select = select[:insert_x] + 'X' + select[insert_x + 1:]
    # splits altered input into digrams
    digram = [(select[i:i+2]) for i in range(0, len(select), 2)]
    encoded = []
    # begins encryption process
    for cipher in digram:
        for x in range(0, 5):
            for y in range(0, 5):
                # locates coordinates
                if cipher[0] == grid[x][y]:
                    row1 = x
                    col1 = y
                elif cipher[1] == grid[x][y]:
                    row2 = x
                    col2 = y
        # creates second variables for same values
        # to compare and swap as needed
        row01 = row1
        row02 = row2
        col01 = col1
        col02 = col2
        # horizontal encryption
        if row1 == row2:
            row01 += 1
            row02 += 1
            # checks for any out of bounds
            if row01 > 4:
                row01 = 0
            if row02 > 4:
                row02 = 0

        # vertical encryption
        elif col1 == col2:
            col01 += 1
            col02 += 1
            # checks for any out of bounds
            if col01 > 4:
                col01 = 0
            if col02 > 4:
                col02 = 0

        # diagonal encryption: keeps rows but swaps cols
        elif (row1 != row2) and (col1 != col2):
            row01 = row1
            col01 = col2
            row02 = row2
            col02 = col1

        # creates new coordinates
        char1 = grid[row01][col01]
        char2 = grid[row02][col02]
        # adds new coodrinates to encryption
        encoded.append(char1 + char2)

    # takes encoded list and turns it into a string for printing
    encrypted = ""
    for f in encoded:
        encrypted += f
    print("\tYour encrypted message is: ", encrypted)
    # returns to menu
    print("-----------------------------------------------------")
    menu()


# begins decryption proccess
def decryption():
    print("\tYou have chosen decryption.")
    user_key = input("\tPlease enter your key: ").strip().upper()
    # takes input and makes it playfair compliant
    key = user_key.replace('Q', 'K')
    key = key.replace('U', 'V')
    select = input("\tPlease enter an encrypted message: ")
    # takes encrypted message and makes it playfair compliant
    select = select.strip().upper()
    select = select.replace('Q', 'K')
    select = select.replace('U', 'V')
    select = select.replace(' ', '')
    playfair = 'ABCDEFGHIJKLMNOPRSTVWXYZ '
    k = ""
    # creates complete reference alphakey and removes possible duplicates
    for char in key + playfair:
        if char not in k:
            k += char
    # creates the grid
    grid = [k[0:5],k[5:10],k[10:15],k[15:20],k[20:25]]
    # splits encrypted message back into digrams
    digram = [(select[i:i+2]) for i in range(0, len(select), 2)]
    decoded = []
    # begins decryption process
    for cipher in digram:
        for x in range(0, 5):
            for y in range(0, 5):
                # locates coordinates
                if cipher[0] == grid[x][y]:
                    row1 = x
                    col1 = y
                elif cipher[1] == grid[x][y]:
                    row2 = x
                    col2 = y

        # creates second variables for same values
        # to compare and swap as needed
        row01 = row1
        row02 = row2
        col01 = col1
        col02 = col2
        # horizontal decryption
        if row1 == row2:
            row01 -= 1
            row02 -= 1
            # checks for any out of bounds
            if row01 < 0:
                row01 = 4
            if row02 < 0:
                row02 = 4

        # vertical decryption
        elif col1 == col2:
            col01 -= 1
            col02 -= 1
            # checks for any out of bounds
            if col01 < 0:
                col01 = 4
            if col02 < 0:
                col02 = 4

        # diagonal decryption
        elif (row1 != row2) and (col1 != col2):
            row01 = row1
            col01 = col2
            row02 = row2
            col02 = col1


        # creates new coordinates
        char1 = grid[row01][col01]
        char2 = grid[row02][col02]
        # adds new coodrinates to encryption
        decoded.append(char1 + char2)

    # takes decoded list and turns it into a string for printing
    decrypted = ""
    for f in decoded:
        decrypted += f
    print("\tYour deccrypted message is: ", decrypted)
    # returns to menu
    print("-----------------------------------------------------")
    menu()


# prints credits and returns to menu
def credits():
    print("\t[ Credits ]\n")
    print("\tThe Playfair Cipher Machine")
    print("\t\tCreated by Kendra Ludwig")
    print("-----------------------------------------------------")
    menu()


# thanks user and quits program
def quit():
    print("\tThank you for using this cipher!")
    print("\t\tQuitting in 3... 2... 1...")
    print("-----------------------------------------------------")


if __name__ == '__main__':
    main()
