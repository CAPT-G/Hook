"""
Casino Game

This module simulates an online casino game with user authentication and role-based access.
It includes classes and functions for playing casino games, managing user coins, and handling payouts.
"""

import random
import time

users = {
    'admin': {
        'password': 'admin123',
        'role': 'admin',
        'coins': 0
    },
    'user1': {
        'password': 'password1',
        'role': 'player',
        'coins': 200,
        'last_daily_check_in': None
    }
}

class RandomNumberSelector:
 """
    A class to generate random numbers based on given odds.
    
    This class provides a mechanism to generate random numbers based on specified odds.
    
    Args:
        odds (int): The odds of selecting a number, represented as a percentage.
        
    Attributes:
        odds (int): The odds of selecting a number, represented as a percentage.
        """
def __init__(self, odds):
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
    """
    A class representing an online casino game.

    This class provides functionality for playing casino games, managing user coins,
    and handling payouts.

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
        Initialize the CasinoGame instance with default values.
        """
        self.user_coins = 200
        self.user_winnings = 0
        self.max_payout = 2000
        self.purchase_amount = 200
        self.playable_odds = 10
        self._number_selector = RandomNumberSelector(odds=self.playable_odds)
    
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
                    self.user_winnings = self.max_payout
                print(f"Congratulations! You won {self.purchase_amount * 5} coins.")
            else:
                self.user_coins -= self.purchase_amount
                print("Better luck next time. You lost.")
        else:
            print("You don't have enough coins to play.")
    
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

def admin_login(username, password):
   """
    Authenticate an admin user.

    This function checks if the provided username and password match an admin user's credentials.

    Args:
        username (str): The username of the admin user.
        password (str): The password of the admin user.

    Returns:
        bool: True if the provided credentials are valid for an admin user, False otherwise.
    """
   if username in users and users[username]['password'] == password and users[username]['role'] == 'admin':
        return True; return False

def user_login(username, password):
 """
    Authenticate a player user.

    This function checks if the provided username and password match a player user's credentials.

    Args:
        username (str): The username of the player user.
        password (str): The password of the player user.

    Returns:
        bool: True if the provided credentials are valid for a player user, False otherwise.
    """
 if username in users and users[username]['password'] == password and users[username]['role'] == 'player':
        return True; return False

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
        elif choice == 'player':
            player_username = input('Enter player username: ')
            player_password = input('Enter player password: ')
            if user_login(player_username, player_password):
                player_menu(player_username)
            else:
                print('Invalid player credentials.')
        elif choice == 'quit':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please select a valid role.')

def admin_menu(username):
 """
    Display the admin menu and handle admin actions.
    
    This function presents a menu with options for an admin user, such as managing player coins
    and logging out. It handles the user's input and directs them to the appropriate actions.
    
    Args:
        username (str): The username of the admin user.
    """
 print(f'Welcome, {username} (Administrator)!')
 while True:
        print('\nAdmin Menu:')
        print('1. Manage Coins for Players')
        print('2. Log Out')
        choice = input('Select an option: ')
        if choice == '1':
            manage_coins()
        elif choice == '2':
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
 player_username = input('Enter player username: ')
 action = input('Enter action (add/cashout): ')
 coins = int(input('Enter coins: '))
 if action == 'add':
        add_coins(player_username, coins)
        print(f'{coins} coins added to {player_username}.')
 elif action == 'cashout':
        cash_out_coins(player_username, coins)
        print(f'{coins} coins cashed out from {player_username}.')
 else:
        print('Invalid action.')

def add_coins(username, amount):
 """
    Add coins to a player's account.
    
    This function allows an admin user to add a specified amount of coins to a player's account.
    
    Args:
        username (str): The username of the player.
        amount (int): The number of coins to be added.
    """
 if username in users and users[username]['role'] == 'player':
        users[username]['coins'] += amount

def cash_out_coins(username, amount):
 """
    Cash out coins from a player's account.
    
    This function allows an admin user to cash out a specified amount of coins from a player's account.
    
    Args:
        username (str): The username of the player.
        amount (int): The number of coins to be cashed out.
    """
 if username in users and users[username]['role'] == 'player' and users[username]['coins'] >= amount:
        users[username]['coins'] -= amount

def player_menu(username):
    """
    Display the player menu and handle player actions.
    This function presents a menu with options for a player user, such as playing a game,
    cashing out winnings, and logging out. It handles the the user's input and directs them
    to the appropriate actions.
    Args:
        username (str): The user name of the player.
    Returns
        none
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

if __name__ == '__main__':
    main()
