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
    
    def __str__(self):   

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
    categories_stats = list()

    chart_width = len(categories) + 7

    def calculate_total_spend(categories):
        total = 0
        for cateogory in categories:
            for ledge in cateogory.ledger:
                if ledge["amount"] < 0:
                    total = total + (ledge["amount"] * -1)
        return total


    total = calculate_total_spend(categories)
    

    def generate_category_bar(category, percentage, first_category = False):
        category_bar = list()

        for char in range(100, -10, -10):
            if char > percentage:
                if first_category:
                    category_bar.append(" ")
                else:
                    category_bar.append("  ")
            else:
                if first_category:
                    category_bar.append("o")
                else:
                    category_bar.append(" o")

        return category_bar

    def poblate_categories_stats(categories, total):
        for index, category in enumerate(categories):
            category_total = 0
            name = category.name

            for ledge in category.ledger:
                if ledge["amount"] < 0:
                    category_total = category_total + (ledge["amount"] * -1)
            
            percentage_spent = int((category_total / total) * 100)

            if index == 0:
                category_bar = generate_category_bar(category, percentage_spent, True)
            else:
                category_bar = generate_category_bar(category, percentage_spent)

            category_stats = {"name": name, "category_bar": category_bar}

            categories_stats.append(category_stats)

    
    #Hard code legend margin
    legend = []
    for char in range(100, -10, -10):
        legend.append(f"{char}|")
    
    #Hard code horizonal line
    horizonal_line = ""
    for char in range(chart_width):
        horizonal_line = horizonal_line + "-"

    poblate_categories_stats(categories, total)

    chart = ""
    for index, number in enumerate(legend):
        categories_bar = ""
        for category in categories_stats:
            categories_bar = categories_bar + " " + category["category_bar"][index]
        if number == "100|":
            chart = chart + f"{number}{categories_bar}\n"
        elif number == "0|":
            chart = chart + f"  {number}{categories_bar}\n"
        else:
            chart = chart + f" {number}{categories_bar}\n"

    chart = chart + f"    {horizonal_line}"

    ##longest word?
    longest_category_name_lenght = len(categories[0].name)
    for category in categories:
        if len(category.name) > longest_category_name_lenght:
            longest_category_name_lenght = len(category.name)

    bottom_chart = ""
    for index in range(longest_category_name_lenght):
        name_bar = ""
        for category_number, category in enumerate(categories):
            name_len = len(category.name)
            if name_len > index:
                if category_number == 0:
                    name_bar = name_bar + f" {category.name[index]}"
                else:
                    name_bar = name_bar + f"  {category.name[index]}"
            else:
                if category_number == 0:
                    name_bar = name_bar + "  "
                else:
                    name_bar = name_bar + "   "
        bottom_chart = bottom_chart + f"    {name_bar}\n"

    bottom_chart = bottom_chart[:-1]
    chart = "Percentage spent by category\n" + chart + f"\n{bottom_chart}"
    return type(chart)