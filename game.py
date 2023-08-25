"""
Casino Game

This module simulates an online casino game with user authentication and role-based access.
It includes classes and functions for playing casino games, managing user coins, and handling payouts.
"""
import random
import time

class RandomNumberSelector:
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
        self.playable_odds = 5
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
                    self.user_winnings -= self.max_payout
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

    def adjust_playable_odds(self, new_odds):
        """
        Adjust the playable odds of the game.

        Args:
            new_odds (int): The new playable odds, represented as a percentage.
        """
        self.playable_odds = new_odds
        self._number_selector.odds = new_odds

def user_login(username, password, users):
    """
    Authenticate a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        users (dict): A dictionary containing user information.

    Returns:
        bool: True if the provided credentials are valid for a user, False otherwise.
    """
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False

def player_menu(username, users):
    """
    Display the player menu and handle player actions.

    Args:
        username (str): The username of the player user.
        users (dict): A dictionary containing user information.
    """
    game = CasinoGame()
    print(f'Welcome, {username} (Player)!')

    while True:
        print('\nPlayer Menu:')
        print('1. Play Game')
        print('2. Cash Out')
        print('3. Check-in')
        print('4. Log Out')
        choice = input('Select an option: ')

        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.cash_out()
        elif choice == '3':
            check_in(username, users)
        elif choice == '4':
            print(f'Goodbye, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

def admin_login(username, password, users):
    """
    Authenticate an admin user.

    Args:
        username (str): The username of the admin user.
        password (str): The password of the admin user.
        users (dict): A dictionary containing user information.

    Returns:
        bool: True if the provided credentials are valid for an admin user, False otherwise.
    """
    if username in users and users[username]['password'] == password and users[username]['role'] == 'admin':
        return True
    else:
        return False

def admin_menu(username, users):
    """
    Display the admin menu and handle admin actions.

    Args:
        username (str): The username of the admin user.
        users (dict): A dictionary containing user information.
    """
    game = CasinoGame()
    print(f'Welcome, {username} (Administrator)!')

    while True:
        print('\nAdmin Menu:')
        print('1. Manage Coins for Players')
        print('2. Adjust Playable Odds')
        print('3. Log Out')
        choice = input('Select an option: ')

        if choice == '1':
            manage_coins(users)
        elif choice == '2':
            new_odds = int(input("Enter new playable odds: "))
            game.adjust_playable_odds(new_odds)
            print(f"Playable odds changed to {new_odds}%")
        elif choice == '3':
            print(f'Goodbye, {username}!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

def manage_coins(users):
    """
    Manage player coins.

    Args:
        users (dict): A dictionary containing user information.
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
                print('Insufficient coins to cash out.')
        else:
            print('Invalid action.')
    else:
        print(f'Player "{username}" is not a valid player.')

def check_in(username, users):
    """
    Perform daily check-in for a player.

    Args:
        username (str): The username of the player.
        users (dict): A dictionary containing user information.
    """
    if users[username]['last_check_in'] == time.localtime().tm_yday:
        print("You've already checked in today.")
    else:
        users[username]['last_check_in'] = time.localtime().tm_yday
        users[username]['coins'] += 50
        print("You've checked in and received 50 coins.")

def register_user(users):
    """
    Register a new user.

    Args:
        users (dict): A dictionary containing user information.
    """
    new_username = input("Enter a new username: ")
    new_password = input("Enter a password: ")
    role = input("Enter role (admin/player): ")
    users[new_username] = {'password': new_password, 'role': role, 'coins': 200, 'last_check_in': -1}
    print(f"User {new_username} registered successfully.")

def main():
    print('Welcome to the Casino Game!')
    current_time = time.ctime()
    print(f'Current time: {current_time}')

    users = {
        'admin': {'password': 'adminpass', 'role': 'admin', 'coins': 9999999, 'last_check_in': -1},
        'player1': {'password': 'playerpass', 'role': 'player', 'coins': 200, 'last_check_in': -1}
    }

    while True:
        choice = input('Enter your choice (login/register/quit): ')

        if choice == 'login':
            user_type = input('Are you an admin or player? ').lower()
            user_username = input('Enter username: ')
            user_password = input('Enter password: ')

            if user_type == 'admin' and admin_login(user_username, user_password, users):
                admin_menu(user_username, users)
            elif user_type == 'player' and user_login(user_username, user_password, users):
                player_menu(user_username, users)
            else:
                print('Invalid credentials.')

        elif choice == 'register':
            register_user(users)

        elif choice == 'quit':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Please select a valid option.')

if __name__ == '__main__':
    main()
