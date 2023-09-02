# TradingView_Tradings_warehouse
This is Pinescript script to help You keep your trades in the right order, for your SPOT and BUY&HOLD activity.
![Example](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/73b2a04b-1778-430e-94ed-98576298a527)

Download python .exe script to convert excel trades into pine script => follow the instruction, please.




As Binance(and other) exchange provides limted data storage(to get statistical data), You have to keep your SPOT trades somewhere to have an idea where is your AVG price,
how much was invested and how deep your wallet was before You get into crypto/stock investing. For this semi-automated process you can use 
this script.
All You have to do is:
1. Download your trades from exchange. If there are several csv files - merge it into the one csv file.
2. Download converter excel file or python zip(and extract).
[Download](https://drive.google.com/file/d/15LT54f2LxsGPcPjit-xhqPMIPsoACf2R/view?usp=sharing)
or this (run main shortcut after export files into some folder) [Download](https://drive.google.com/file/d/1BrEKVurnvEyw6cUThL_k9BZU73xQwjrU/view?usp=sharing)
4. If You do want to use excel - see how to convert your trades using sample.
   After You downloaded your trades(https://www.binance.com/en/support/faq/how-to-download-spot-trading-transaction-history-statement-e4ff64f2533f4d23a0b3f8f17f510eab) for needed period(it is better to download every asset from the first trade, or from 0 owned amount,thus You
   won't sell more than have bought), push to the red columns You trades from column data to column fee. Every next column in script has its formula.
   Just use this formulas for every next trade to have script written trade(Green column). Copy green column, past into script(like it shown in
   the main script).![Excel_before](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/6552afa1-1f8e-4e70-b1c6-ab88f47bdb26)
![Excel_before_2](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/7f0f956e-fd76-4c77-a115-2f41553da8fd)
![Excel_before_3](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/25c70f26-d900-4ad2-a5a3-b99bfa31ec45)

5. For python script everything is much easier. Just download =>
[Download](https://drive.google.com/file/d/15LT54f2LxsGPcPjit-xhqPMIPsoACf2R/view?usp=sharing)
or this (run main shortcut after export files into some folder) [Download](https://drive.google.com/file/d/1BrEKVurnvEyw6cUThL_k9BZU73xQwjrU/view?usp=sharing)
extract zip => run script => browse file with trades => copy the script from .txt generated file => past into pine editor => add to the chart.

You system can show that this file can contain malware => sorry, I have no possibility to get certification for every script I have, so just skip warning.
You have the right not to believe me, in which case you can install python and run main.py script in console(main.py can be checked by low_skill_coder for malwares)
![Снимок экрана 2023-09-02 175024](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/45bb167a-0ce4-41ab-8a05-8cb14a08abf9)

![Снимок экрана 2023-09-02 174845](https://github.com/Arivadis/TradingView_Tradings_warehouse/assets/105313584/56bdc22e-7994-4603-99ef-d2b66506ce00)

Warning!!!

This script has no idea about your side currency deposits, so if You got Your BTC or EUR or .. from another wallet and sold later - it can break your statistical data. Add this transfer manually(see examples inside script)


Press Like this git and tradingview script if it helped You!



