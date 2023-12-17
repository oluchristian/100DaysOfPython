resources = \
    {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": 0.0
    }

ingredients = \
    {
        "espresso": {"water": 30, "milk": 100, "coffee": 18},
        "latte": {"water": 60, "milk": 120, "coffee": 30},
        "Cappuccino": {"water": 50, "milk": 100, "coffee": 24}
    }

money = \
    {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

coffee_prices = \
    {
        "latte": 2.5,
        "espresso": 2.0,
        "cappuccino": 1.5,
    }


def calculate_money(prompt):
    m_quarter = float(input("how many quarters?:"))
    m_dimes = float(input("how many dimes?:"))
    m_nickels = float(input("how many dimes?:"))
    m_pennies = float(input("how many pennies?:"))
    mul_quarter = money["quarters"] * m_quarter
    mul_dimes = money["dimes"] * m_dimes
    mul_nickels = money["nickels"] * m_nickels
    mul_pennies = money["pennies"] * m_pennies
    sum_money = mul_quarter + mul_dimes + mul_nickels + mul_pennies
    for key, value in coffee_prices.items():
        if key == prompt:
            change = sum_money - value
            resources["Money"] = change - resources["Money"]
            ingredient_quantities = ingredients[prompt]
            resources["Water"] -= ingredient_quantities["water"]
            resources["Milk"] -= ingredient_quantities["milk"]
            resources["Coffee"] -= ingredient_quantities["coffee"]
            if change > 0:
                print(f"Here is ${change:.2f} dollars in change")
                print(f"Here is your {prompt}. Enjoy!")
            return sum_money
    print("Sorry that's not enough money. Money refunded.")
    user_input()


def user_input():
    prompt = input("What would you like? espresso/latte/cappuccino:\n")
    if prompt not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid input.")
        user_input()
    elif prompt == "report":
        for key, values in resources.items():
            print(f"{key}: {values}")
        user_input()
    elif prompt == "off":
        return "off"
    else:
        for ingredient_needed, quantity in ingredients[prompt].items():
            if resources[ingredient_needed.capitalize()] < quantity:
                print(f"Not enough {ingredient_needed} to make {prompt}")
                return "off"
        return prompt


def coffee_machine():
    turn_on = True
    while turn_on:
        user_prompt = user_input()
        if user_prompt == "off":
            return
        calculate_money(user_prompt)


coffee_machine()
