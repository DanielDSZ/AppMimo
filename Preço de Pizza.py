menu = ['margherita', 'vegetable', 'pepperoni']

margherita = []
vegetables = ['peppers', 'mushrooms', 'onions']
pepperoni = ['peppers', 'chilli', 'salami']

ingredients = {
    'peppers': 0.8,
    'mushroons': 0.5,
    'onions': 0.6,
    'chilli': 0,
    'salami': 1.5
}

choice = vegetables

base_cost = 2.5
extra_cost = 0

for item in choice:
    extra_cost += ingredients[item]

total_cost = base_cost + extra_cost
print(total_cost)
