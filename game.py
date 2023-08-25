"""
Casino Game

This module simulates an online casino game with user authentication and role-based access.
It includes classes and functions for playing casino games, managing user coins, and handling payouts.
"""
import random
import time
from datetime import datetime, timedelta
class RandomNumberSelector:
    def __init__(self, length):
        """
        A class to generate a sequence of random numbers.

        Args:
            length (int): The length of the sequence.
        """
        self.length = length
def generate_sequence(self):
        """
        Generate a sequence of random numbers.

        Returns:
            list: A list of random numbers in the specified range.
        """
        sequence = [random.randint(0, 9) for _ in range(self.length)]
        return sequence
def __init__(self, odds):
        """
        A class to generate random numbers based on given odds.

        Args:
            odds (int): The odds of selecting a number, represented as a percentage.
        """
        self.odds = odds
def generate_number(self):
        """
        Generate a random number based on the specified odds.

        Returns:
            bool: True if the number is selected, False otherwise.
        """
        if random.randint(1, 100) <= self.odds:
            return True
        else:
            return False

class CasinoGame:
def __init__(self):
        """
        A class representing an online casino game.

        Attributes:
            user_coins (int): The number of coins the user currently has.
            user_winnings (int): The total winnings accumulated by the user.
            max_payout (int): The maximum amount of winnings a user can accumulate.
            purchase_amount (int): The amount of coins required to play a game.
            playable_odds (int): The odds of winning a game, represented as a percentage.
            _number_selector (RandomNumberSelector): An instance of the RandomNumberSelector
                                                     class used to generate random numbers for games.
        """
        self.user_coins = 200
        self.user_winnings = 0
        self.max_payout = 2000
        self.purchase_amount = 200
        self.playable_odds = 10
        self._number_selector = RandomNumberSelector(odds=self.playable_odds)
def generate_number(self):
        """
        Generate a random number based on the specified odds.
        
        Returns:
            bool: True if the number is selected, False otherwise.
        """
        if random.randint(1, 100) <= self.odds:
            return True
        else:
            return False
def cash_out_coins(user_dict, username, coins):
    """
    Cash out player's winnings.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username of the player.
        coins (int): The amount of coins to cash out.

    Returns:
        bool: True if the cash-out was successful, False otherwise.
    """
    if username in user_dict and user_dict[username]['role'] == 'player':
        if user_dict[username]['coins'] >= coins:
            user_dict[username]['coins'] -= coins
            return True
        else:
            print(f"{username} doesn't have enough coins to cash out.")
    else:
        print(f"Invalid username or not a player: {username}")
    return False
def play_game(self):
    """
    Play a casino game.

    Plays a game based on the specified odds and updates user coins and winnings accordingly.
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
def add_coins(user_dict, username, coins):
    """
    Add coins to a player's account.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username of the player.
        coins (int): The amount of coins to add.

    Returns:
        bool: True if the coins were added successfully, False otherwise.
    """
    if username in user_dict and user_dict[username]['role'] == 'player':
        user_dict[username]['coins'] += coins
        return True
    else:
        print(f"Invalid username or not a player: {username}")
    return False
def cash_out(self):
        """
        Cash out user winnings.

        Allows the user to cash out their winnings in exchange for coins.
        """
        if self.user_winnings >= self.purchase_amount * 5:
            cash_out_amount = min(self.user_winnings, self.user_coins * 5)
            self.user_winnings -= cash_out_amount
            self.user_coins += cash_out_amount
            print(f"You cashed out {cash_out_amount} coins.")
        else:
            print("You don't have enough winnings to cash out.")

def main_menu(self):
        """
        Display the main menu and handle user actions.

        This method presents a menu with options for a user, such as playing a game,
        cashing out winnings, and quitting. It handles the user's input and directs them
        to the appropriate actions.
        """
        while True:
            print("\nMain Menu:")
            print("1. Play Game")
            print("2. Cash Out")
            print("3. Quit")
            choice = input("Select an option: ")

            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.cash_out()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
users = {'admin': {'password': 'adminpass', 'role': 'admin'},
    'player': {'password': 'playerpass', 'role': 'player'}}

def admin_menu(username):
    """
    Display the admin menu and handle admin actions.
    
    This function presents a menu with options for an admin user, such as managing player coins,
    adjust playable odds, and logging out. It handles the user's input and directs them to the
    appropriate actions.
    
    Args:
        username (str): The username of the admin user.
    """
    print(f'Welcome, {username} (Administrator)!')
    game = CasinoGame()  # Initialize the game instance

    while True:
        print('\nAdmin Menu:')
        print('1. Manage Coins for Players')
        print('2. Adjust Playable Odds')
        print('3. Log Out')
        choice = input('Select an option: ')

        if choice == '1':
            player_username = input('Enter player username: ')
            manage_coins(player_username)
        elif choice == '2':
            new_odds = int(input("Enter new playable odds: "))
            game.adjust_playable_odds(new_odds)  # Call the method to adjust playable odds
            print(f"Playable odds changed to {new_odds}%")
        elif choice == '3':
            print(f'Goodbye, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

def manage_coins():
    """
    Manage player coins.
    
    This function allows an admin user to manage the coins of a player. It prompts the admin
    for a player's username, an action (add/cashout), and the amount of coins. Based on the
    action, it either adds or cashes out the specified number of coins for the player.
    """
    username = input('Enter player username: ')
    if username in users:  # Use the function to check if the username exists
        if users[username]['role'] == 'player':
            action = input('Enter action (add/cashout): ')
            coins = int(input('Enter coins: '))
            if action == 'add':
                add_coins(users, username, coins)  # Call the add_coins function
                print(f'{coins} coins added to {username}.')
            elif action == 'cashout':
                cash_out_coins(users, username, coins)  # Call the cash_out_coins function
                print(f'{coins} coins cashed out from {username}.')
            else:
                print('Invalid action.')
        else:
            print(f'Player "{username}" is not a valid player.')
    else:
        print(f'Player "{username}" not found.')

def user_login(username, password):
    """
    Authenticate a player user.

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
    Authenticate an admin user.

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

def player_menu(username):
    """
    Display the player menu and handle player actions.

    Args:
        username (str): The username of the player user.
    """
    game = CasinoGame()
    print(f'Welcome, {username} (Player)!')
    while True:
        print('\nPlayer Menu:')
        print('1. Play Game')
        print('2. Cash Out')
        print('3. Log Out')
        choice = input('Select an option: ')
        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.cash_out()
        elif choice == '3':
            print(f'Goodbye, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')
def get_user_info(user_dict, username):
    """
    Get user information from the user dictionary.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username to retrieve information for.

    Returns:
        dict: User information dictionary if the username exists, None otherwise.
    """
    if username in user_dict:
        return user_dict[username]
    else:
        return None
def main():
     """
    The main function to run the Casino Game simulation.

    This function welcomes the user to the Casino Game, provides a menu to select a role
    (admin/player/quit), and directs the user to the appropriate menus based on their choice.
    """
print('Welcome to the Casino Game!')
current_time = time.ctime()
print(f'Current time: {current_time}')
while True:
            choice = input('Enter your role (admin/player/quit): ')
            if choice == 'admin':
                admin_username = input('Enter admin username: ')
                admin_password = input('Enter admin password: ')
            if admin_login(admin_username, admin_password):
                admin_menu(admin_username)
            else:
                print('Invalid admin credentials.')
            if choice == 'player':
                player_username = input('Enter player username: ')
                player_password = input('Enter player password: ')
            if user_login(player_username, player_password):
                player_menu(player_username)
            else:
                print('Invalid player credentials.')
            if choice == 'quit':
                print('Goodbye!')
            break
        else:
    print('Invalid choice. Please select a valid role.')

if __name__ == '__main__':
    main()  # Start the program execution by calling the main() function

# Get user info for 'user1'
user_info = get_user_info(users, 'user1')  # Replace 'user1' with the desired username
if user_info:
    print(f"Username: {user_info['username']}")
    print(f"Role: {user_info['role']}")
    print(f"Coins: {user_info['coins']}")
else:
    print("User not found.")
