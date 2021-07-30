import sys


def showSeats(seats):
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            print(seats[row][col], end=' ')
        print()
    yesOrNo = input("\nWould you like to enter another number? Y/N: ")
    if yesOrNo.lower() == "y":
        inputNumberToNavigate(seats)
    if yesOrNo.lower() == "n":
        sys.exit("Thank You For Using This Plane Reservation System")
    else:
        print("Enter Y/N")


def inputNumberToNavigate(seats):
    numberInput = input("Type number here: ")
    if numberInput == "1":
        showSeats(seats)
    else:
        print("Enter numbers 1, 2, 3, 4")
        inputNumberToNavigate(seats)


def startUp(seats):
    print("Welcome to the Python Plane Project")
    print("Input one of the following numbers below")
    print("1 -> view the seats available\n" +
          "2 -> Enter a seat number to reserve\n"
          "3 -> Search for a seat\n"
          "4 -> Exit\n")
    inputNumberToNavigate(seats)


def main():
    seats = [["A1", "B1", "C1", "D1", "E1", "F1"],
             ["A2", "B2", "C2", "D2", "E2", "F2"],
             ["A3", "B3", "C3", "D3", "E3", "F3"],
             ["A4", "B4", "C4", "D4", "E4", "F4"],
             ["A5", "B5", "C5", "D5", "E5", "F5"],
             ["A6", "B6", "C6", "D6", "E6", "F6"],
             ["A7", "B7", "C7", "D7", "E7", "F7"],
             ["A8", "B8", "C8", "D8", "E8", "F8"]
             ]
    startUp(seats)


if __name__ == "__main__":
    main()
