# TradingView_Tradings_warehouse
This is Pinescript script to help You keep your trades in the right order, for your SPOT and BUY&HOLD activity.
![Example](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/73b2a04b-1778-430e-94ed-98576298a527)


Link to add the script.



As Binance(and other) exchange provides limted data storage(to get statistical data), You have to keep your SPOT trades somewhere to have idea where is your AVG price,
how much was invested and how is deep your wallet was before You get into crypto/stock investing. For this semi-automated process you can use 
this script.
All You have to do is:
1. Add the Pinescript script named Trade_warehouse into Pine editor and save
2. Download converter excel file or python zip(and extract).
![Screenshot from 2023-08-30 19-04-43](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/3c4aaf1e-40f0-41e5-a02b-b5eda160fcf5)

3. If You do want to use excel - see how to convert your trades using sample.
   After You downloaded your trades(https://www.binance.com/en/support/faq/how-to-download-spot-trading-transaction-history-statement-e4ff64f2533f4d23a0b3f8f17f510eab) for needed period(it is better to download every asset from the first trade, or from 0 owned amount,thus You
   won't sell more than have bought), push to the red columns You trades from column data to column fee. Every next column in script has its formula.
   Just use this formulas for every next trade to have script written trade(Green column). Copy green column, past into script(like it shown in
   the main script).![Excel_before](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/6552afa1-1f8e-4e70-b1c6-ab88f47bdb26)
![Excel_before_2](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/7f0f956e-fd76-4c77-a115-2f41553da8fd)
![Excel_before_3](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/25c70f26-d900-4ad2-a5a3-b99bfa31ec45)

4. For python script everything is much easier. Just extract zip, make shortcut to file \dist\main, run, choose the file with You trades - get
   .txt file with your trades to push to the script
![short_cut](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/0980b3bb-5291-4479-ae8c-ecdc9cd41c11)

![short_cut 2](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/8ab11589-eb3b-43f3-accc-08979eb5dafb)


5. Make sure You past your trades in the right place in script!
![Pine_trades](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/64c8ef36-bf61-4b46-89da-4e1b16ce1fe3)

After You passed all steps - You have the script working.

 
