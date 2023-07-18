sandwich_orders = ['a', 'b', 'c', 'd',]
finished_sandwiches = []
while sandwich_orders:
    made_sandwiches = sandwich_orders.pop()
    print(f"I made your {made_sandwiches} sandwich! ")
    finished_sandwiches.append(made_sandwiches)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

