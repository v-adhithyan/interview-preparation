# Strategy Pattern

- It is a pattern where different algorithms or procedures can be used to complete a task where algorithm or procedure will be specified at runtime.

- Example: billing of drinks in a pub during normal hour and happy bours. The billing strategy can be passed at the runtime.

## Example

```python
from abc import ABCMeta, abstractmethod


class BillingStrategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_price(self, price):
		pass


class HappyHour(BillingStrategy):

	def get_price(self, price):
		return price * 0.5


class NormalHour(BillingStrategy):

	def get_price(self, price):
		return price


class Customer(object):

	def __init__(self, billing_strategy):
		self.drinks = list()
		self.strategy = billing_strategy()

	def add(self, price, quantity):
		price = self.strategy.get_price(price * quantity)
		self.drinks.append(price)

	def print_bill(self):
		total_cost = sum(self.drinks)
		print(f"Total bill: {total_cost}")

def main():
	customer1 = Customer(billing_strategy=HappyHour)
	customer1.add(10, 5)

	customer1.strategy = NormalHour()
	customer1.add(5, 5)

	customer1.print_bill()

if __name__ == "__main__":
	main()
```