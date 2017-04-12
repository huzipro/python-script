import json
import os.path

def init():
  _load_items()

def items():
  global _items
  return _items

def products():
  global _products
  return _products

def locations():
  global _locations
  return _locations

def add_item(product_code, location_code):
  global _items
  _items.append((product_code, location_code))
  _save_items()

def remove_item(product_code, location_code):
  global _items
  for i in range(len(_items)):
    prod_code,loc_code = _items[i]
    if prod_code == product_code and loc_code == location_code:
      del _items[i]
      _save_items()
      return True
  return False

def set_products(products):
  global _products
  _products = products

def set_locations(locations):
  global _locations
  _locations = locations

def _load_items():
  global _items
  if os.path.exists("items.json"):
    f = open("items.json", "r")
    _items = json.loads(f.read())
    f.close()
  else:
    _items = []

def _save_items():
  global _items
  f = open("items.json", "w")
  f.write(json.dumps(_items))
  f.close()
