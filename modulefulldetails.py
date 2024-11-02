#This is a script to get all the details of a module


# from contextlib import contextmanager

# print(dir(contextmanager))

# import contextlib
# print(dir(contextlib))

import inspect
import importlib

module_name = input("Enter the module to check: ")

# Dynamically import the module using importlib
try:
    module = importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"Module '{module_name}' not found.")
else:
    # Get a list of all items in the module
    items = dir(module)

    # Loop through each item and check its type
    for item_name in items:
        item = getattr(module, item_name)  # Get the actual item
        if inspect.isclass(item):
            print(f"{item_name} is a class")
        elif inspect.isfunction(item):
            print(f"{item_name} is a function")
        elif inspect.ismodule(item):
            print(f"{item_name} is a module")
        else:
            print(f"{item_name} is of type {type(item)}")

