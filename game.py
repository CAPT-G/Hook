"""
Casino Game

This module simulates an online casino game with user authentication and role-based access.
It includes classes and functions for playing casino games, managing user coins, and handling payouts.
"""
import random
import datetime
import os

class RandomNumberSelector:
    """
    A class to generate random numbers based on given odds.

    This class provides a mechanism to generate random numbers based on specified odds.

    Args:
        odds (int): The odds of selecting a number, represented as a percentage.
    """
    def __init__(self, odds):
        """
        Initialize a RandomNumberSelector instance with specified odds.

        This method initializes a RandomNumberSelector instance with the given odds.
        The odds represent the percentage likelihood of selecting a True value (number selected)
        when using the generate_number() method of the instance.

        Args:
            odds (int): The odds of selecting a number, represented as a percentage.

        Returns:
            None
        """
        self.odds = odds

    def generate_number(self):
        """
        Generate a random number based on the playable odds.

        This method generates a random number based on the playable odds of the casino game.
        The playable odds determine the likelihood of winning a game. If the generated number falls within the playable odds, the player wins; otherwise, they lose.

        Returns:
            bool: True if the number falls within playable odds (player wins), False otherwise.
        """
        if random.randint(1, 100) <= self.odds:
            return True
        else:
            return False

class CasinoGame:
    """
    Represents an online casino game.

    This class models an online casino game, including the user's coins, winnings, maximum payout,
    purchase amount, playable odds, and the ability to play games, cash out, and generate random numbers.

    Attributes:
        user_coins (int): The number of coins the user currently has.
        user_winnings (int): The total winnings accumulated by the user.
        max_payout (int): The maximum amount of winnings a user can accumulate.
        purchase_amount (int): The amount of coins required to play a game.
        playable_odds (int): The odds of winning a game, represented as a percentage.
        _number_selector (RandomNumberSelector): An instance of the RandomNumberSelector
                                                 class used to generate random numbers for games.
    """
    def __init__(self):
        """
        Initialize the CasinoGame instance.

        Initializes the attributes for the CasinoGame instance, including user coins, winnings,
        max payout, purchase amount, playable odds, and a random number selector.
        """
        self.user_coins = 200
        self.user_winnings = 0
        self.max_payout = 2000
        self.purchase_amount = 200
        self.playable_odds = 10
        self._number_selector = RandomNumberSelector(odds=self.playable_odds)
        self.player_username = None
        self.player_coins = 0
        self.last_checkin_date = None

    def set_player(self, username):
        """
        Set the current player and perform initialization tasks.

        This method sets the current player for the casino game and performs
        necessary initialization tasks, such as updating the player's last check-in date.

        Args:
            username (str): The username of the player.

        Returns:
            None
        """
        self.player_username = username
        self.player_coins = users.get(username, {}).get('coins', 0)
        self.last_checkin_date = None

    def generate_number(self):
        """
        Generate a random number based on the specified odds.

        This method generates a random number based on the specified odds of the
        RandomNumberSelector instance. The odds determine the likelihood of selecting
        a True value (number selected) or a False value (number not selected).

        Returns:
            bool: True if the number is selected, False otherwise.
        """
        if random.randint(1, 100) <= self.odds:
            return True
        else:
            return False
            
    def clear_screen():
        """
        Clear the console screen.

        This function clears the console screen to provide a cleaner interface
        for displaying menu options and information.

        Note:
            The method for clearing the console screen may vary depending on the
            operating system or development environment being used.

        Returns:
            None
        """
        # Clear the console screen (use appropriate method for your environment)
        os.system('clear')  # For Unix-like systems (Linux, macOS)
        # os.system('cls')  # For Windows

    def play_game(self):
        """
        Play a casino game and update player's coins and winnings.

        This method allows the player to play a casino game. The playable odds determine the
        likelihood of winning. If the player wins, their winnings increase by the purchase amount
        multiplied by a factor. If the player loses, their coins decrease by the purchase amount.

        Returns:
            None
        """
        if self.user_coins >= self.purchase_amount:
            if self._number_selector.generate_number():
                self.user_winnings += self.purchase_amount * 5
                self.user_coins -= self.purchase_amount
                if self.user_winnings > self.max_payout:
                    self.user_winnings -= self.max_payout
                print(f"Congratulations! You won {self.purchase_amount * 5} coins.")
            else:
                self.user_coins -= self.purchase_amount
                print("Better luck next time. You lost.")
        else:
            print("You don't have enough coins to play.")

    def cash_out(self):
        """
        Cash out player's winnings in exchange for coins.

        This method allows the player to cash out their winnings in exchange for coins.
        The player can only cash out if their winnings are greater than or equal to the
        required amount for cashing out. The cashed-out amount is deducted from the player's
        winnings and added to their coins.

        Returns:
            None
        """
        if self.user_winnings >= self.purchase_amount * 5:
            cash_out_amount = min(self.user_winnings, self.user_coins * 5)
            self.user_winnings -= cash_out_amount
            self.user_coins += cash_out_amount
            print(f"You cashed out {cash_out_amount} coins.")
        else:
            print("You don't have enough winnings to cash out.")

    def check_in(self):
        """
        Perform the daily check-in for the player.

        This method allows the player to perform a daily check-in to receive a bonus of coins.
        The player can only perform a check-in once every 24 hours. If the player hasn't performed
        a check-in in the last 24 hours, they receive a specified amount of coins as a bonus.

        Returns:
            bool: True if the check-in is successful, False if the check-in was performed
                  within the last 24 hours.
        """
        today = datetime.now().date()
        if self.last_checkin_date is None or today > self.last_checkin_date:
            self.player_coins += 100
            self.last_checkin_date = today
            print('Daily check-in successful! You received 100 coins.')
        else:
            print('You have already checked in today. Come back tomorrow.')

def game_menu(game):
    """
    Display the game menu and handle player game selections.

    This method presents a menu with options for playing different casino games.
    The player can choose from a variety of games to play. After the player plays a game,
    they are returned to the game menu to make another selection or return to the player menu.

    Returns:
        None
    """
    print('\nGame Menu:')
    print('1. Ding Ding King')
    print('2. Blackjack Attack')
    print('3. Spin To Win')
    print('4. Player Menu')

    while True:
        choice = input('Play or Go back: ')
        if choice == '1':
            play_ding_ding_king(game)
        elif choice == '2':
            play_blackjack_attack(game)
        elif choice == '3':
            play_spin_to_win(game)
        elif choice == '4':
            print('Returning to Player Menu')
            break
        else:
            print('Invalid choice. Please select a valid option.')

def play_ding_ding_king(game):
    print('Playing Ding Ding King...')
    # Implement the logic for the Ding Ding King game here

def play_blackjack_attack(game):
    print('Playing Blackjack Attack...')
    # Implement the logic for the Blackjack Attack game here

def play_spin_to_win(game):
    print('Playing Spin To Win...')
    # Implement the logic for the Spin To Win game here

def user_login(username, password):
    """
    Authenticate a player user's credentials.

    This method takes a username and password as input and checks if the provided
    credentials match any registered player user's information. If the provided
    credentials are valid for a player user, the method returns True; otherwise, it
    returns False.

    Args:
        username (str): The username of the player user.
        password (str): The password of the player user.

    Returns:
        bool: True if the provided credentials are valid for a player user, False otherwise.
    """
    if username in users and users[username]['password'] == password and users[username]['role'] == 'player':
        return True
    else:
        return False

def admin_login(username, password):
    """
    Authenticate an admin user's credentials.

    This method takes a username and password as input and checks if the provided
    credentials match any registered admin user's information. If the provided
    credentials are valid for an admin user, the method returns True; otherwise, it
    returns False.

    Args:
        username (str): The username of the admin user.
        password (str): The password of the admin user.

    Returns:
        bool: True if the provided credentials are valid for an admin user, False otherwise.
    """
    if username in users and users[username]['password'] == password and users[username]['role'] == 'admin':
        return True
    else:
        return False

def main_menu():
    """
    Display the main menu and handle user login options.

    This function presents a menu with options for user login (Admin or Player) and handles
    the corresponding actions based on the user's choice. It prompts the user for their choice
    and credentials, then directs them to the appropriate menu or displays an error message.

    Returns:
        None
    """
    print("\nMain Menu:")
    print("1. Admin Login")
    print("2. Player Login")
    print("3. Quit")
    choice = input()
    
    while True:
        choice = input("\nMain Menu:\n1. Admin Login\n2. Player Login\n3. Quit\n")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            if admin_login(admin_username, admin_password):
                clear_screen()  # Clear the screen after successful login
                admin_menu(admin_username)
            else:
                print("Invalid admin credentials.")

        elif choice == "2":
            player_username = input("Enter player username: ")
            player_password = input("Enter player password: ")
            if user_login(player_username, player_password):
                clear_screen()  # Clear the screen after successful login
                player_menu(player_username)
            else:
                print("Invalid player credentials.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
def admin_menu(username):
    """
    Display the admin menu and handle admin actions.

    This method presents a menu with options for an admin user, such as managing player coins,
    adjusting playable odds, and logging out. It handles the user's input and directs them to the
    appropriate actions. The admin user's username is passed as an argument to personalize the menu.

    Args:
        admin_username (str): The username of the admin user.

    Returns:
        None
    """
    print(f'Welcome, {username} (Administrator)!')
    game = CasinoGame()
    
    while True:
        print('\nAdmin Menu:')
        print('1. Manage Coins for Players')
        print('2. Adjust Playable Odds')
        print('3. Log Out')
        choice = input('Select an option: ')

        if choice == '1':
            manage_coins()
        elif choice == '2':
            new_odds = int(input("Enter new playable odds: "))
            game.playable_odds = new_odds
            print(f"Playable odds changed to {new_odds}%")
        elif choice == '3':
            print(f'Goodbye, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

def manage_coins():
    """
    Manage player coins.

    This method allows an admin user to manage the coins of a player. It prompts the admin
    for a player's username, an action (add/cashout), and the amount of coins. Based on the
    action, it either adds or cashes out the specified number of coins for the player.

    Args:
        player_username (str): The username of the player whose coins are being managed.

    Returns:
        None
    """
    username = input('Enter player username: ')
    if username in users and users[username]['role'] == 'player':
        action = input('Enter action (add/cashout): ')
        coins = int(input('Enter coins: '))
        if action == 'add':
            users[username]['coins'] += coins
            print(f'{coins} coins added to {username}.')
        elif action == 'cashout':
            if users[username]['coins'] >= coins:
                users[username]['coins'] -= coins
                print(f'{coins} coins cashed out from {username}.')
            else:
                print('Not enough coins to cash out.')
        else:
            print('Invalid action.')
    else:
        print(f'Player "{username}" is not a valid player.')

def main():
    """
    Start the Casino Game simulation.

    This function serves as the entry point of the Casino Game simulation. It displays
    the initial "Select Login!" message and presents the main menu to the user. The menu
    provides options for admin login, player login, or quitting the game.

    Returns:
        None
    """
    global current_datetime  # Declare the global variable to be modified
    current_datetime = datetime.datetime.now()  # Set the current datetime
    while True:
        choice = input("\nMain Menu:\n1. Admin Login\n2. Player Login\n3. Quit\n")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            if admin_login(admin_username, admin_password):
                clear_screen()  # Clear the screen after successful login
                admin_menu(admin_username)
            else:
                print("Invalid admin credentials.")

        elif choice == "2":
            player_username = input("Enter player username: ")
            player_password = input("Enter player password: ")
            if user_login(player_username, player_password):
                clear_screen()  # Clear the screen after successful login
                player_menu(player_username)
            else:
                print("Invalid player credentials.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
        main_menu()
def player_menu(username):
    """
    Display the player menu and handle player actions.

    This function presents a menu with options for the player, including playing games,
    adding coins, checking in for daily rewards, redeeming winnings, and checking out.
    It calls the appropriate methods based on the player's choice.

    Args:
        username (str): The username of the player user.

    Returns:
        None
    """
    game = CasinoGame()
    game.set_player(username)

    print(f'Welcome,{username} Coins {game.player_coins}!')
    while True:
        print('\nPlayer Menu:')
        print('1. Play Now')
        print('2. Re-Up')
        print('3. Check In')
        print('4. Redeem')
        print('5. Check Out')
        choice = input('Select an option: ')

        if choice == '1':
            game_menu(game)
        elif choice == '2':
            print('Win Big!')  # Placeholder message, add coin adding logic here
        elif choice == '3':
            game.last_checkin_date = datetime.datetime.now().date()  # Set last check-in date
            print("You've checked in for today.")
        elif choice == '4':
            print('Big Ballin!')  # Placeholder message, add winning redemption logic here
            break
        elif choice == '5':
            print(f'Thank you for playing, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')
def clear_screen():
    """
    Clear the console screen.

    This function uses system-specific commands to clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    """
    Entry point for the Casino Game simulation.

    This block of code is executed when the script is run directly (not imported as a module).
    It serves as the entry point for starting the Casino Game simulation. The main function
    is called to present the initial menu and handle user login options.

    Returns:
        None
    """
    users = {'admin': {'password': 'adminpass', 'role': 'admin'},
             'player': {'password': 'playerpass', 'role': 'player', 'coins': 100}}
    main()
