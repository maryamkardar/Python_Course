# main_script.py

import sys
sys.path.append('/home/pythonProject3/my_modules')  # Add the path to your custom module
# C:\Users\Maryam Hosseini\Desktop\New folder\pythonProject3

import my_custom_module  # Import the custom module

# Use the functions from the custom module
greeting = my_custom_module.greet("Alice")
sum_result = my_custom_module.add(5, 3)

print(greeting)  # Output: Hello, Alice!
print(f"The sum is: {sum_result}")  # Output: The sum is: 8
