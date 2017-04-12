import datastorage

def prompt_for_action():
  while True:
    print()
    print("What would you like to do?")
    print()
    print(" A = add an item to the inventory.")
    print(" R = remove an item from the inventory.")
    print(" C = generate a report of the current inventory levels.")
    print(" O = generate a report of the inventory items to re-order.")
    print(" Q = quit.")
    print()
    action = input("> ").strip().upper()
    if action == "A": return "ADD"
    elif action == "R": return "REMOVE"
    elif action == "C": return "INVENTORY_REPORT"
    elif action == "O": return "REORDER_REPORT"
    elif action == "Q": return "QUIT"
    else:
      print("Unknown action!")

def prompt_for_product():
  while True:
    print()
    print("Select a product:")
    print()
    n = 1
    for code,description,desired_number in datastorage.products():
      print("{}. {} - {}".format(n, code, description))
      n = n + 1

    s = input("> ").strip()
    if s == "": return None

    try:
      n = int(s)
    except ValueError:
      n = -1

    if n < 1 or n > len(datastorage.products()):
      print("Invalid option: {}".format(s))
      continue

    product_code = datastorage.products()[n-1][0]
    return product_code

def prompt_for_location():
  while True:
    print()
    print("Select a location:")
    print()
    n = 1
    for code,description in datastorage.locations():
      print("{}. {} - {}".format(n, code, description))
      n = n + 1

      s = input("> ").strip()
      if s == "": return None
      try:
        n = int(s)
      except ValueError:
        n = -1

      if n < 1 or n > len(datastorage.locations()):
        print("Invalid option: {}".format(s))
        continue

      location_code = datastorage.locations()[n-1][0]
      return location_code

def show_report(report):
  print()
  for line in report:
    print(line)
print()

def show_error(err_msg):
  print()
  print(err_msg)
  print()

