import re
import pandas as pd
from tkinter import filedialog
from numpy import vectorize
import warnings
import os
import sys
from tkinter import messagebox

first_part = """

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Arivadis

//@version=5
indicator("Trade Warehouse", overlay = true, max_bars_back = 400)
plot_table = input.bool(true, 'Show table')
color_last = input.color(defval = color.aqua, title = 'Color AVG last entry')
color_total = input.color(defval = color.rgb(14, 51, 218), title = 'Color AVG last entry')
tablea_color = input.color(defval = color.rgb(214, 218, 161), title = 'Main table')
pairs_col = input.color(defval = color.rgb(65, 130, 114), title = 'Pair column')


var current_pair = syminfo.ticker
var dust = 5 / close

type Trade
    string pair
    float price
    float amount
    int date
    bool buy


var trades_array = array.new<Trade>(0)
var pairs = array.new_string(0)

var avg_tot = array.new_float(0)
var amount_tot = array.new_float(0)
var usd_tot = array.new_float(0)

var avg_cur = array.new_float(0)
var amount_cur = array.new_float(0)
var usd_cur = array.new_float(0)

// Where  PAIR/PRICE/USDT/AMOUNT/TIMEBUY/IS_BUY
var bool_finished = false
if not bool_finished
"""
second_part = """
bool_finished := true

if array.size(trades_array) > 0
    for i = array.size(trades_array) - 1 to 0
        current_trade = array.get(trades_array, i)
        if current_trade.date < time
            if not array.includes(pairs, current_trade.pair)
                array.push(pairs, current_trade.pair)

                array.push(amount_tot, current_trade.amount)
                array.push(usd_tot, current_trade.amount * current_trade.price)
                array.push(avg_tot, current_trade.price)

                array.push(amount_cur, current_trade.amount)
                array.push(usd_cur, current_trade.amount * current_trade.price)
                array.push(avg_cur, current_trade.price)

                
            else
                index_of_pair = array.indexof(pairs, current_trade.pair)
                temp_amount_tot = array.get(amount_tot, index_of_pair)
                temp_usd_tot = array.get(usd_tot, index_of_pair)
                temp_amount_cur = array.get(amount_cur, index_of_pair)
                temp_usd_cur = array.get(usd_cur, index_of_pair)

                if current_trade.buy
                    
                    array.set(amount_tot, index_of_pair, current_trade.amount + temp_amount_tot)
                    array.set(usd_tot, index_of_pair, (current_trade.amount * current_trade.price) + temp_usd_tot)
                    array.set(avg_tot, index_of_pair, array.get(usd_tot,index_of_pair) /array.get(amount_tot,index_of_pair))
                    
                    array.set(amount_cur, index_of_pair, current_trade.amount + temp_amount_cur)
                    array.set(usd_cur, index_of_pair, (current_trade.amount * current_trade.price) + temp_usd_cur)
                    array.set(avg_cur,index_of_pair, array.get(usd_cur,index_of_pair) /array.get(amount_cur,index_of_pair))
                else
                    array.set(amount_tot, index_of_pair,temp_amount_tot - current_trade.amount)
                    array.set(usd_tot, index_of_pair, temp_usd_tot - (current_trade.amount * current_trade.price))
                    array.set(avg_tot, index_of_pair, array.get(usd_tot,index_of_pair) /array.get(amount_tot,index_of_pair))
                    
                    array.set(amount_cur, index_of_pair,temp_amount_cur - current_trade.amount)
                    array.set(usd_cur, index_of_pair, temp_usd_cur - (current_trade.amount * current_trade.price))
                    array.set(avg_cur,index_of_pair, array.get(usd_cur,index_of_pair) /array.get(amount_cur,index_of_pair))
                    if array.get(amount_cur, index_of_pair) < dust
                        array.set(amount_cur, index_of_pair, 0)
                        array.set(usd_cur, index_of_pair, 0)
                        array.set(avg_cur,index_of_pair, 0)

            array.remove(trades_array, i)
        else
            break




is_pair_in = array.includes(pairs, current_pair)
more_ = array.size(avg_cur) > 0 and array.size(pairs) > 0
plot_curr_pair = is_pair_in ? array.get(avg_cur,array.indexof(pairs,current_pair)) : na
plot(plot_curr_pair > 0  ? plot_curr_pair : na , "AVG price from Last entry", color = color_last, style = plot.style_linebr)
plot_curr_pair_total = is_pair_in ? array.get(avg_tot,array.indexof(pairs,current_pair)) : na
plot(plot_curr_pair_total > 0 ? plot_curr_pair_total : na, "AVG price Total", color = color_total, style = plot.style_linebr)


var unic_pairs = array.new_string()
if array.size(unic_pairs) == 0
    for i = array.size(trades_array) - 1 to 0
        current_trade = array.get(trades_array, i)
        if not array.includes(unic_pairs, current_trade.pair)
            array.push(unic_pairs, current_trade.pair)
var pairs_array_le = array.size(unic_pairs)
var testTable = table.new(position = position.bottom_right, columns = 7, rows = pairs_array_le , bgcolor = tablea_color, border_width = 0,frame_width = 0)

if barstate.isconfirmed and array.size(avg_tot) > 0 and plot_table
    for i = 0 to array.size(pairs) - 1
        pair_now = array.get(pairs, i)

        avg_now = array.get(avg_tot, i)
        tot_amount_now = array.get(amount_tot, i)
        tot_amount_now_usdt = array.get(usd_tot, i)


        avg_now_cur = array.get(avg_cur, i)
        amount_now_cur = array.get(amount_cur, i)
        amount_now_usdt_cur = array.get(usd_cur, i)
 
        table.cell(table_id = testTable, column = 0, row = i, text = pair_now, bgcolor=pairs_col)
        table.cell(table_id = testTable, column = 1, row = i, text = "Invested AVG price =>" + str.tostring(avg_now))
        table.cell(table_id = testTable, column = 2, row = i, text = "Invested amount =>" + str.tostring(tot_amount_now))
        table.cell(table_id = testTable, column = 3, row = i, text = "Invested USDT =>" + str.tostring(math.round(tot_amount_now_usdt, 2)))
        table.cell(table_id = testTable, column = 4, row = i, text = "Curr AVG price =>" + str.tostring(avg_now_cur))
        table.cell(table_id = testTable, column = 5, row = i, text = "Curr amount =>" + str.tostring(amount_now_cur))
        table.cell(table_id = testTable, column = 6, row = i, text = "Curr USDT =>" + str.tostring(math.round(amount_now_usdt_cur, 2)))





"""


def make_string(market, price, total, date, trade_type):
    buy_sell = 'true' if trade_type == 'BUY' else 'false'
    data = re.split(r"[-: ]", date)
    return f"    array.push(trades_array,Trade.new('{market}', {price}, {total},timestamp(syminfo.timezone, {data[0]}, {data[1]}, {data[2]}, {data[3]}), {buy_sell}))\n"


def open_index(ex_file) -> str:
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        file_ex = pd.read_csv(ex_file)
        file_ex = file_ex.sort_values(by='Date(UTC)', ascending=False)
        print(file_ex)
        file_ex['Executed'] = file_ex['Executed'].str.replace(r'[a-zA-Z,]', '', regex=True)
        print(file_ex['Executed'])


        # file_ex = file_ex.drop_duplicates(keep=False)
        file_ex['string'] = vectorize(make_string)(file_ex['Pair'], file_ex['Price'],
                                                   file_ex['Executed'], file_ex['Date(UTC)'], file_ex['Side'])
    return file_ex['string']


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("CSV",
                                                      "*.csv"),
                                                     ("Excel",
                                                      "*.xlsx*")
                                                     ))

    return filename


def concat(col):
    all_trades = ''
    all_trades += first_part
    counter = 0
    for now in col:
        all_trades += now
        counter += 1
        if counter > 50:
            all_trades += 'if not bool_finished \n'
            counter = 0
    all_trades += second_part
    return all_trades


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        df = open_index(browseFiles())
        with open(f'script.txt', 'w') as f:
            f.write(concat(df))
    except Exception as e:
        messagebox.showerror('', 'Something went wrong \nCheck Your exel file!!!')
        sys.exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
