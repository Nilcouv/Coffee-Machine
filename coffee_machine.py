class CoffeeMachine:
    def __init__(self, water=400, milk=540, bean=120, cup=9, cash=550):
        self.water = water
        self.milk = milk
        self.bean = bean
        self.cup = cup
        self.cash = cash

    # function tracking the answer
    def progress(self):
        while True:
            menu_answer = str(input("Write action (buy, fill, take, remaining, exit):\n"))
            # comparing the answer
            if menu_answer in ["buy", "Buy", "BUY"]:
                self.buy()
            elif menu_answer in ["fill", "Fill", "FILL"]:
                self.fill()
            elif menu_answer in ["take", "Take", "TAKE"]:
                self.take()
            elif menu_answer in ["remaining", "Remaining", "REMAINING"]:
                self.inventory()
            elif menu_answer in ["exit", "Exit", "EXIT"]:
                break
            else:
                print("Please, enter one of the five options!")

    # function showing the several coffee options
    def buy(self):
        coffee_loop = True

        # select the coffee type
        while coffee_loop:
            answer = ""
            try:
                answer = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
            except TypeError or ValueError:
                print("Please enter a number!\n")
            if answer == "1":
                self.espresso()
                coffee_loop = False
            elif answer == "2":
                self.latte()
                coffee_loop = False
            elif answer == "3":
                self.cappuccino()
                coffee_loop = False
            elif answer == "back":
                coffee_loop = False
            else:
                print("Please, select one of the three available choice!\n")

    # Espresso function - test the minimum number of available espresso and brew one if it is above 0
    def espresso(self):

        # calculating the minimum espresso available
        espresso_available = min(int(self.water / 250), int(self.bean / 16))

        # Testing if brewing an espresso is possible, and if so, actualize global variables
        if espresso_available > 0:
            print("I have enough resources to brew you a espresso!")
            print("Starts to brew you a espresso...")
            self.water -= 250
            self.bean -= 16
            self.cup -= 1
            self.cash += 4
            print("\[DONE\]\n Enjoy!")
        else:
            print("not enough ingredient available!")

    # Latte function - test the minimum number of available latte and brew one if it is above 0
    def latte(self):
        # calculating the minimum latte available
        latte_available = min(int(self.water / 350), int(self.milk / 75), int(self.bean / 20))

        # Testing if brewing an latte is possible, and if so, actualize global variables
        if latte_available > 0:
            print("I have enough resources to brew you a latte!")
            print("Starts to brew you a latte...")
            self.water -= 350
            self.milk-= 75
            self.bean -= 20
            self.cup -= 1
            self.cash += 7
            print("\[DONE\]\n Enjoy!")

        else:
            print("not enough ingredient available!")

    # Cappuccino function - test the minimum number of available cappuccino and brew one if it is above 0
    def cappuccino(self):
        # calculating the minimum cappuccino available
        cappuccino_available = min(int(self.water / 200), int(self.milk / 100), int(self.bean / 12))

        # Testing if brewing a cappuccino is possible, and if so, actualize global variables
        if cappuccino_available > 0:
            print("I have enough resources to brew you a cappuccino!")
            print("Starts to brew you a cappuccino...")
            self.water -= 200
            self.milk -= 100
            self.bean -= 12
            self.cup -= 1
            self.cash += 6
            print("\[DONE\]\n Enjoy!")

        else:
            print("not enough ingredient available!")

    # function refiling the coffee machine inventory
    def fill(self):
        # Water supply
        try:
            self.water += int(input("Write how many ml of water do you want to add:\n"))

        except TypeError or ValueError:
            print("Please enter a number")

        # Milk supply
        try:
            self.milk += int(input("Write how many ml of milk do you want to add:\n"))

        except TypeError or ValueError:
            print("Please enter a number")

        # Beans supply
        try:
            self.bean += int(input("Write how many grams of coffee beans do you want to add:\n"))

        except TypeError or ValueError:
            print("Please enter a number")

        # cups supply
        try:
            self.cup += int(input("Write how many disposable cups of coffee do you want to add:\n"))

        except TypeError or ValueError:
            print("Please enter a number")

    # function withdrawing the coffee machine money
    def take(self):
        print("I gave you $"+str(self.cash))
        self.cash = 0

    # function displaying the coffee machine inventory
    def inventory(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.bean, " of coffee beans")
        print(self.cup, " of disposable cups")
        print(self.cash, " of money")

machine = CoffeeMachine()
machine.progress()
