
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
    def __init__(self, odds):
        self.odds = odds
    
    def generate_number(self):
        if random.randint(1, 100) <= self.odds:
            return True
        else:
            return False

class CasinoGame:
    def __init__(self):
        self.user_coins = 200
        self.user_winnings = 0
        self.max_payout = 2000
        self.purchase_amount = 200
        self.playable_odds = 10
        self._number_selector = RandomNumberSelector(odds=self.playable_odds)
    
    def play_game(self):
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
        if self.user_winnings >= self.purchase_amount * 5:
            cash_out_amount = min(self.user_winnings, self.user_coins * 5)
            self.user_winnings -= cash_out_amount
            self.user_coins += cash_out_amount
            print(f"You cashed out {cash_out_amount} coins.")
        else:
            print("You don't have enough winnings to cash out.")

def admin_login(username, password):
    if username in users and users[username]['password'] == password and users[username]['role'] == 'admin':
        return True
    return False

def user_login(username, password):
    if username in users and users[username]['password'] == password and users[username]['role'] == 'player':
        return True
    return False

def main():
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
    if username in users and users[username]['role'] == 'player':
        users[username]['coins'] += amount

def cash_out_coins(username, amount):
    if username in users and users[username]['role'] == 'player' and users[username]['coins'] >= amount:
        users[username]['coins'] -= amount

def player_menu(username):
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
