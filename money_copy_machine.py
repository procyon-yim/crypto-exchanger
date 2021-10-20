from coin_exchanger import *

username, password = login('upbit.txt')
user = pyupbit.Upbit(username, password)

coins = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP', 'KRW-ADA', 'KRW-DOGE']  # list of coins to exchange
k = 0.5  # breakout coefficient. See Larry Williams's Volatility Breakout Strategy.
amount = get_amount(coins)
target_price = get_target_price(coins, k)
start_balance  = user.get_balance()
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
send_alarm('mail.txt', 'Current time is {2}, Current Balance is {0}KRW. Today\'s targets are {1}.'.format(int(start_balance), amount, now))

try:
    while True:  
        # This script must run 24/7
        now = datetime.datetime.now()

        if mid < now < mid + datetime.timedelta(seconds=10): 
            # Rebalances account every midnight (00:00)
            try:
                
                renew(user, user.get_balances())
                coins = ['KRW-BTC', 'KRW-ETH', 'KRW-XRP', 'KRW-ADA', 'KRW-DOGE']
                k = 0.5
                amount = get_amount(coins)
                target_price = get_target_price(coins, k)
                start_balance = user.get_balance()
                now = datetime.datetime.now()
                mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
                send_alarm('mail.txt', 'Current time is {2}, Current Balance is {0}KRW. Today\'s targets are {1}.'.format(int(start_balance), amount, now))

            except TypeError:
                send_alarm('mail.txt', 'JSONDecodeError. Terminating MCM.')
                break

            except Exception as e:
                send_alarm('mail.txt', 'An error occured during midnight process. {} Terminating MCM.'.format(e))
                break

        try:
            for coin in coins:
                current_price = pyupbit.get_current_price(coin)
                time.sleep(0.1)  # This is because you can call an Upbit API only 10 times a second

                if current_price >= target_price[coin]:
                    
                    # The bot will buy a currency if the current price is higher than the target price.
                    # target price = k (breakout coefficient, usually 0.5) times (yesterday's volatility)
                    qtty = amount[coin]
                    time.sleep(0.1)

                    if qtty == 0:
                        coins.remove(coin)

                    else:
                        user.buy_market_order(coin, start_balance * qtty)
                        time.sleep(0.1)
                        coins.remove(coin)

        except:
            try:
                for coin in coins:
                    current_price = pyupbit.get_current_price(coin)
                    time.sleep(0.5)

                    if current_price >= target_price[coin]:
                        qtty = amount[coin]
                        time.sleep(0.5)
                        if qtty == 0:
                            coins.remove(coin)
                        else:
                            user.buy_market_order(coin, start_balance * qtty)
                            time.sleep(0.5)
                            coins.remove(coin)

            except Exception as e:
                send_alarm('mail.txt', "An error occured while exchanging. {}. Terminating MCM.".format(e))
                break

        time.sleep(1)

except KeyboardInterrupt:
    print('keyboard interruption')
