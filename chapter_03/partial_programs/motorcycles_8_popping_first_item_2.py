motorcycles = ['honda', 'yamaha', 'suzuki']

wanted_bike = motorcycles.pop(0)

print(f"I'd like to buy a {wanted_bike.title()},"
      f" so now only {', '.join([bike.title() for bike in motorcycles])} are left in the store.")
