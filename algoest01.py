import binance
import matplotlib.pyplot as plt
import pickle
import time

# carica il modello di machine learning
model = pickle.load(open("eth_model.pkl", "rb"))

# definisci la soglia di acquisto e vendita
THRESHOLD_BUY = 0.5
THRESHOLD_SELL = 0.5

# utilizza l'API di Binance per ottenere informazioni sull'account
client = binance.Client(api_key=API_KEY, api_secret=API_SECRET)
account = client.futures_balance()

# estrai il saldo in denaro e il numero di ETH dalle informazioni dell'account
cash = account['totalCash']
eth_balance = account['ETH']['available']

def invest(client, cash, eth_balance):
    i = 0
    while True:
        # ottieni il prezzo corrente di ETH
        eth_price = float(client.futures_ticker_24hr(symbol='ETHUSDT')['lastPrice'])
        # normalizza il prezzo corrente
        max_price = max(closing_prices)
        min_price = min(closing_prices)
        normalized_price = (eth_price - min_price) / (max_price - min_price)
        # otteni la previsione del modello per il prossimo minuto
        prediction = model.predict([[normalized_price]])[0]
        # acquista ETH quando la previsione è positiva e il prezzo è inferiore a una soglia specifica
        if prediction > 0 and eth_price < THRESHOLD_BUY:
            # acquista tutto il denaro disponibile in ETH
            eth_balance += cash / eth_price
            cash = 0
            # specifica gli ordini di stop loss e take profit
            stop_loss = eth_price * 0.95
            take_profit = eth_price * 1.05
            # imposta l'ordine di acquisto
            order = client.futures_order(
                symbol='ETHUSDT',
                side=binance.enums.SIDE_BUY,
                quantity=eth_balance,
                stopPrice=stop_loss,
                takeProfitPrice=take_profit,
                type=binance.enums.ORDER_TYPE_STOP_LOSS_TAKE_PROFIT,
                timeInForce=binance.enums.TIME_IN_FORCE_GTC
            )
            # aggiorna il saldo in denaro e il numero di ETH in base all'ordine eseguito
            eth_balance = order['executedQty']
            cash = order['cummulativeQuoteQty']
# vendi ETH quando la previsione è negativa e il prezzo è superiore a una soglia specifica
elif prediction < 0 and eth_price > THRESHOLD_SELL:
# specifica gli ordini di stop loss e take profit
stop_loss = eth_price * 1.05
take_profit = eth_price * 0.95
# imposta l'ordine di vendita
order = client.futures_order(
symbol='ETHUSDT',
side=binance.enums.SIDE_SELL,
quantity=eth_balance,
stopPrice=stop_loss,
takeProfitPrice=take_profit,
type=binance.enums.ORDER_TYPE_STOP_LOSS_TAKE_PROFIT,
timeInForce=binance.enums.TIME_IN_FORCE_GTC
)
# aggiorna il saldo in denaro e il numero di ETH in base all'ordine eseguito
eth_balance = order['executedQty']
cash = order['cummulativeQuoteQty']
# visualizza i grafici di denaro e ETH ogni 10 minuti
if i % 10 == 0:
plt.plot(cash)
plt.plot(eth_balance)
plt.show()
# attendi 1 minuto prima di eseguire nuovamente l'algoritmo
time.sleep(60)

esegui l'algoritmo di trading
invest(client, cash, eth_balance)
vendi ETH quando la previsione è negativa e il prezzo è superiore a una soglia specifica
elif prediction < 0 and eth_price > THRESHOLD_SELL:
# specifica gli ordini di stop loss e take profit
stop_loss = eth_price * 1.05
take_profit = eth_price * 0.95
# imposta l'ordine di vendita
order = client.futures_order(
symbol='ETHUSDT',
side=binance.enums.SIDE_SELL,
quantity=eth_balance,
stopPrice=stop_loss,
takeProfitPrice=take_profit,
type=binance.enums.ORDER_TYPE_STOP_LOSS_TAKE_PROFIT,
timeInForce=binance.enums.TIME_IN_FORCE_GTC
)
# aggiorna il saldo in denaro e il numero di ETH in base all'ordine eseguito
eth_balance = order['executedQty']
cash = order['cummulativeQuoteQty']

visualizza i grafici di denaro e ETH ogni 10 minuti
if i % 10 == 0:
plt.plot(cash)
plt.plot(eth_balance)
plt.show()

attendi 1 minuto prima di eseguire nuovamente l'algoritmo
time.sleep(60)

esegui l'algoritmo di trading
invest(client, cash, eth_balance)

