class Category:
    balance = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + amount
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": (amount * -1), "description": description})
            self.balance = self.balance - amount
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        return self.get_balance() >= amount
    
    def __str__(self):   #TO DO

        result = f'{self.name.center(30, "*")}\n'
        total = 0
        for lodge in self.ledger:
            description = lodge["description"][0:23]
            amount = lodge["amount"]
            total = total + amount
            lodge_string = '{:23}{:7.2f}\n'.format(description, amount)
            result = result + lodge_string
        total_line = 'Total: {:.2f}'.format(total)
        result = result + total_line
        return result


def create_spend_chart(categories):
    return True

'''
food = Category("Food")
bar = Category("dog")

food.deposit(200, "deposit")
bar.deposit(4500, "more than twenty three words I think")
food.transfer(100, bar)

print(food)
print(bar)
'''