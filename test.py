from coinmarketcap import Market
from coin import Coin
import time
import sys


def main():
	coinmarketcap = Market()
	markets_coin = coinmarketcap.ticker(limit=20)

	coins = []
	for i in range(0,20):
		coins.append(Coin(name=markets_coin[i]['name'],
			accronym=markets_coin[i]['symbol'],
			in_usd=markets_coin[i]['price_usd'],
			available_supply=markets_coin[i]['available_supply'],
			total_supply=markets_coin[i]['total_supply']
			))

	print("\033c")
	for i in coins:
		sys.stdout.write(str(i))
	time.sleep(20)

	while(True):

		count_coin = 0
		markets_coin = coinmarketcap.ticker(limit=20)
		for i in coins:
			i.update(markets_coin[count_coin]['price_usd'])
			count_coin += 1

		print("\033c")
		for i in coins:
			sys.stdout.write(str(i))

		time.sleep(20)

if __name__ == '__main__':
	main()
