
class Coin(object):

	def __init__(self, name, accronym, in_usd, available_supply, total_supply, nbr_coin=1):
		self.name = name
		self.accronym = accronym
		self.available_supply = available_supply
		self.total_supply = total_supply
		self.in_usd = in_usd
		self.nbr_coin = nbr_coin
		self.percentage = 0.0
		self.value_increased = 0

	def update(self, in_usd):
		if in_usd > self.in_usd:
			self.value_increased = 1
		elif in_usd < self.in_usd:
			self.value_increased = -1
		else:
			self.value_increased = 0
			self.percentage = 0.0

		if self.value_increased != 0:
			self.percentage = (100.0 * float(in_usd)) / float(self.in_usd)

		self.in_usd = in_usd

	def __str__(self):
		str_percentage = self.percentage
		if self.value_increased < 0:
			str_percentage = u'\u001b[31m-{0:.2f}\u001b[0m'.format(str_percentage)
		elif self.value_increased > 0:
			str_percentage = u'\u001b[32m+{0:.2f}\u001b[0m'.format(str_percentage)

		return '| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | \n'.format(self.name, self.accronym, self.nbr_coin, self.in_usd, str_percentage, self.available_supply, self.total_supply)

        def hello():
            print('hello World')
