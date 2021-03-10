import sys

def error():
	print("Errore argomenti !!")
	print("Inserisci un valido arogmento:")
	print("Primo argomento : \n\t-c : Call\n\t -p : Put")
	print("Secondo argomento:\n\t-s : Sold \n\t-b : Bought")
	print("Terzo argomento : Trader price")
	print("Quarto argomento : Spot")
	print("Quinto argomento : Strike")
	print("ES:\n python3 payoff.py -c -b 10 10 10")
	exit()

#print("Arguments"+str(sys.argv))

if sys.argv[1] == '-c':
	type = 1
elif sys.argv[1] == '-p':
	type = 2
else:
	error()

if sys.argv[2] == '-s':
	isSold = True
elif sys.argv[2] == '-b':
	isSold = False
else:
	error()


try:
	trader_price = float(sys.argv[3])
	spot = float(sys.argv[4])
	strike = float(sys.argv[5])
except:
	error()

#print(isSold)
############### Check #######################


if int(type) == 1 :								#Call
	if isSold:
		#print("CALL SOLD")									#Sold
		if spot >strike :
			print(trader_price-spot+strike)
		else:
			print(trader_price)
	else:
		#print("CALL BOUGHT")					#Bought
		if spot>strike:
			print(spot-strike-trader_price)
		else:
			print(-trader_price)
else:									#Put
	if isSold:
		#print("PUT CALL")						#Sold
		if spot<strike:
			print(trader_price-strike+spot)
		else:
			print(trader_price)
	else:
		#print("PUT BOUGHT")					#Bought
		if spot<strike:
			print(strike-spot-trader_price)
		else:
			print(-trader_price)
