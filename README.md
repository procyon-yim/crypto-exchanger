# crypto-exchanger

This is a trading bot for cryptocurrencies exchange in South Korean exchange, Upbit. I make use of an already available API written by the Upbit.(https://github.com/procyon-yim/pyupbit)

**Prerequisites**
  You must have an account at Upbit (https://upbit.com/home), and an email address at www.naver.com

**About the Files**

  __coin_exchanger.py__ includes every method used in automated trading.

  **money_copy_machine.py** is the trading bot. Ideally this must be running 24/7.

  **reset.py** is sort of an emergency escape button. If you need to sell every cryptocurrencies and take them back as cash, you must run this file.

  **mail.txt** must include your email address, password. These are used to send you an alarm via email every 00:00.

  **upbit.txt** must include your API access details. These are used to access API and control your account via computer.
