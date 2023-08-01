from datetime import datetime
import random
from matplotlib import pyplot as plt
from decimal import Decimal

current_time = datetime.now()
print(current_time)

random_list = []
for number in range(101):
  random_list.append(random.randint(1, 100))

random_number = random.choice(random_list)
print(random_number)

# Add your code below:
numbers_a = range(1,13)
numbers_b = random.sample(range(0,1000),12)
print(numbers_b)
plt.plot(numbers_a, numbers_b)
#plt.show()

# Fix the floating point math below:
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)