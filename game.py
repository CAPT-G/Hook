Python

import random
import time

class RandomNumberSelector:
    def __init__(self, odds):
        """
        A class to generate random numbers based on given odds.

        This class provides a mechanism to generate random numbers based on specified odds.

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
    def __init__(self): # Initialize attributes here
        """
        Initialize the CasinoGame instance with default values.
        """
        self.user_coins = 200
        self.user_winnings = 0
        self.max_payout = 2000
        self.purchase_amount = 200
        self.playable_odds = 10
        self._number_selector = RandomNumberSelector(odds=self.playable_odds)
    def play_game(self): # Play game logic
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
    def cash_out(self): # Cash out logic
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
def username(user_dict, username):
    """
    Check if the provided username exists in the user dictionary.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username to check.

    Returns:
        bool: True if the username exists in the dictionary, False otherwise.
    """
    return username in user_dict
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
        return True
    else:
        return False
def cash_out_coins(user_dict, username, amount):
    """
    Cash out coins from a player's account.

    This function allows an admin user to cash out a specified amount of coins from a player's account.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username of the player.
        amount (int): The number of coins to be cashed out.

    Returns:
        bool: True if the cash out was successful, False otherwise.
    """
    if username in user_dict and user_dict[username]['role'] == 'player' and user_dict[username]['coins'] >= amount:
        user_dict[username]['coins'] -= amount
        return True
    return False
def add_coins(user_dict, username, amount):
    """
    Add coins to a player's account.

    This function allows an admin user to add a specified amount of coins to a player's account.

    Args:
        user_dict (dict): A dictionary containing user information.
        username (str): The username of the player.
        amount (int): The number of coins to be added.

    Returns:
        bool: True if the coins were added successfully, False otherwise.
    """
    if username in user_dict and user_dict[username]['role'] == 'player':
        user_dict[username]['coins'] += amount
        return True
    return False
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
        return True
    else:
        return False
def main():
    """
    The main function to run the Casino Game simulation.
    
    This function welcomes the user to the Casino Game, provides a menu to select a role
    (admin/player/quit), and directs the user to the appropriate menus based on their choice.
    """
    print('CAPT-G!')
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
def adjust_playable_odds(self, new_odds):
        """
        Adjust the playable odds for the casino games.

        This method allows an admin user to adjust the odds of winning a game.

        Args:
            new_odds (int): The new odds of winning a game, represented as a percentage.
        """
        self.playable_odds = new_odds
        self._number_selector.odds = new_odds
def admin_menu(username, game):
    """
    Display the admin menu and handle admin actions.
    
    This function presents a menu with options for an admin user, such as managing player coins,
    adjust playable odds and logging out.
    It handles the user's input and directs them to the appropriate actions.
    
    Args:
        username (str): The username of the admin user.
        game (CasinoGame): An instance of the CasinoGame class.
    """
    print(f'Welcome, {username} (Administrator)!')
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
    if username(user_dict, username):  # Use the function to check if the username exists
        if users[username]['role'] == 'player':
            action = input('Enter action (add/cashout): ')
            coins = int(input('Enter coins: '))
            if action == 'add':
                users[username]['coins'] += coins
                print(f'{coins} coins added to {username}.')
                add_coins(username, coins)
            elif action == 'cashout':
                cash_out_coins(username, coins)
            else:
                print('Invalid action.')
    else:
        print(f'Player "{username}" not found or not a valid player.')
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
    cashing out winnings, and logging out. It handles the user's input and directs them
    to the appropriate actions.
    
    Args:
        username (str): The username of the player user.
    """
    game = CasinoGame()  # Initialize the game instance
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
    main()  # Start the program execution by calling the main() function

    # Get user info for 'user1'
    user_info = get_user_info(users, 'user1')  # Replace 'user1' with the desired username
    if user_info:
        print(f"Username: {user_info['username']}")
        print(f"Role: {user_info['role']}")
        print(f"Coins: {user_info['coins']}")
    else:
        print("User not found.")
