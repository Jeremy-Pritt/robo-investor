import requests
import json
import time
import os
import datetime

# create a function that performs mean reversion strategy


def meanReversionStrategy(prices):
    # create a function for finding the average over 5 values to help calculate
    # average 5 day price
    def average_5_days(day1, day2, day3, day4, day5):
        count = 5
        total = day1 + day2 + day3 + day4 + day5
        average = total / count
        return average

    # initialize variables for program
    current_price = 0
    avg_price = 0
    first_buy = 0
    buy = -1
    sell = 0
    profit = 0
    total_profit = 0
    owns_stock = False
    buy_sell_message = ""

    # print title for output
    print("-- Mean Reversion Strategy --")

    # loop through each value in the list of prices
    for index, value in enumerate(prices):
        current_price = value
        if index > 4:
            # find the average 5 day price
            avg_price = average_5_days(prices[index - 5], prices[index - 4],
                                       prices[index - 3], prices[index - 2], prices[index - 1])

            # buys and prints result if the stock is worth less than moving
            # average *.98; store the 1st buy
            if current_price < avg_price * .98 and owns_stock == False:
                if buy == -1:
                    first_buy = current_price
                buy = current_price
                owns_stock = True
                print("buy at:", round(buy, 2))

            # sells and prints result if the stock is worth more than moving
            # average * 1.02; also prints profit and keeps track of total profit
            elif current_price > avg_price * 1.02 and owns_stock == True:
                sell = current_price
                print("sell at:", round(sell, 2))
                profit = sell - buy
                total_profit = total_profit + profit
                owns_stock = False
                print("trade profit:", round(profit, 2))

        # stores string describing whether you should buy or sell on the current day, if applicable
        if index == len(prices) - 1:
            if current_price < avg_price * .98 and owns_stock == True:
                buy_sell_message = "You should BUY this stock today!"
            elif current_price > avg_price * 1.02 and owns_stock == False:
                buy_sell_message = "You should SELL this stock today!"
            else:
                continue

    # find percentage return
    percent_return = (total_profit / first_buy) * 100

    # round results to 2 decimal spaces
    total_profit = round(total_profit, 2)
    percent_return = round(percent_return, 2)
    first_buy = round(first_buy, 2)

    # print total profit, first buy, and percentage return
    print("------------------------------------------------")
    print("Total profit: " + str(total_profit))
    print("First buy: " + str(first_buy))
    print("Percentage return: " + str(percent_return) + " %")
    print(buy_sell_message)
    print()

    # put total profit and percentage return into a list to be returned
    summary_list = [total_profit, percent_return]
    return summary_list
# ------------------ end of mean reversion function -----------------------------

# create a function that performs a simple moving strategy


def simpleMovingAverageStrategy(prices):
    # create a function for finding the average over 5 values to help calculate
    # average 5 day price
    def average_5_days(day1, day2, day3, day4, day5):
        count = 5
        total = day1 + day2 + day3 + day4 + day5
        average = total / count
        return average

    # initialize variables for program
    current_price = 0
    avg_price = 0
    first_buy = 0
    buy = -1
    sell = 0
    profit = 0
    total_profit = 0
    owns_stock = False
    buy_sell_message = ""

    # print title for output
    print("-- Simple Moving Average Strategy --")

    # loop through each value in the list of prices
    for index, value in enumerate(prices):
        current_price = value
        if index > 4:
            # find the average 5 day price
            avg_price = average_5_days(prices[index - 5], prices[index - 4],
                                       prices[index - 3], prices[index - 2], prices[index - 1])

            # buys and prints result if stock is worth more than moving average;
            # store the 1st buy
            if current_price > avg_price and owns_stock == False:
                if buy == -1:
                    first_buy = current_price
                buy = current_price
                owns_stock = True
                print("buy at:", round(buy, 2))

            # sells and prints result if stock is worth less than moving average;
            # also prints profit and keeps track of total profit
            elif current_price < avg_price and owns_stock == True:
                sell = current_price
                print("sell at:", round(sell, 2))
                profit = sell - buy
                total_profit = total_profit + profit
                owns_stock = False
                print("trade profit:", round(profit, 2))

        # stores string describing whether you should buy or sell on the current day, if applicable
        if index == len(prices) - 1:
            if current_price > avg_price and owns_stock == True:
                buy_sell_message = "You should BUY this stock today!"
            elif current_price < avg_price and owns_stock == False:
                buy_sell_message = "You should SELL this stock today!"
            else:
                continue

    # find percentage return
    percent_return = (total_profit / first_buy) * 100

    # round results to 2 decimal spaces
    total_profit = round(total_profit, 2)
    percent_return = round(percent_return, 2)
    first_buy = round(first_buy, 2)

    # print total profit, first buy, and percentage return
    print("------------------------------------------------")
    print("Total profit: " + str(total_profit))
    print("First buy: " + str(first_buy))
    print("Percentage return: " + str(percent_return) + " %")
    print(buy_sell_message)
    print()

    # put total profit and percentage return into a list to be returned
    # put total profit and percentage return into a list to be returned
    summary_list = [total_profit, percent_return]
    return summary_list
# ------------------ end of simple moving strategy function ---------------------

# create a function that performs bollinger bands strategy


def bollinger(prices):
    # create a function for finding the average over 5 values to help calculate
    # average 5 day price
    def average_5_days(day1, day2, day3, day4, day5):
        count = 5
        total = day1 + day2 + day3 + day4 + day5
        average = total / count
        return average

    # initialize variables for program
    current_price = 0
    avg_price = 0
    first_buy = 0
    buy = -1
    sell = 0
    profit = 0
    total_profit = 0
    owns_stock = False
    buy_sell_message = ""

    # print title for output
    print("-- Bollinger Strategy --")

    # loop through each value in the list of prices
    for index, value in enumerate(prices):
        current_price = value
        if index > 4:
            # find the average 5 day price
            avg_price = average_5_days(prices[index - 5], prices[index - 4],
                                       prices[index - 3], prices[index - 2], prices[index - 1])

            # buys and prints result if stock is worth more than moving average * 1.05;
            # store the 1st buy
            if current_price > avg_price * 1.05 and owns_stock == False:
                if buy == -1:
                    first_buy = current_price
                buy = current_price
                owns_stock = True
                print("buy at:", round(buy, 2))

            # sells and prints result if stock is worth less than moving average * .95;
            # also prints profit and keeps track of total profit
            elif current_price < avg_price * .95 and owns_stock == True:
                sell = current_price
                print("sell at:", round(sell, 2))
                profit = sell - buy
                total_profit = total_profit + profit
                owns_stock = False
                print("trade profit:", round(profit, 2))

        # stores string describing whether you should buy or sell on the current day, if applicable
        if index == len(prices) - 1:
            # assign the appropriate buy_sell_message depending on if the price meets certain criteria for bollinger bands
            if current_price > avg_price * 1.05 and owns_stock == True:
                buy_sell_message = "You should BUY this stock today!"
            elif current_price < avg_price * .95 and owns_stock == False:
                buy_sell_message = "You should SELL this stock today!"
            else:
                continue

    # find percentage return
    percent_return = (total_profit / first_buy) * 100

    # round results to 2 decimal spaces
    total_profit = round(total_profit, 2)
    percent_return = round(percent_return, 2)
    first_buy = round(first_buy, 2)

    # print total profit, first buy, and percentage return
    print("------------------------------------------------")
    print("Total profit: " + str(total_profit))
    print("First buy: " + str(first_buy))
    print("Percentage return: " + str(percent_return) + " %")
    print(buy_sell_message)

    # put total profit and percentage return into a list to be returned
    # put total profit and percentage return into a list to be returned
    summary_list = [total_profit, percent_return]
    return summary_list
# --------------------- end of bollinger bands function -------------------------

# create a function for saving dictionary to json file in Cloud9


def saveResults(my_dict, name_of_json_file):
    file_name = name_of_json_file + ".json"
    json.dump(my_dict, open(file_name, "w"))
# -----------------end of saveResults function ---------------------------------


# create a function that takes a list of tickers and retrieves data from web
# api and converts to csv files; allow for adding new data
def create_or_append_data(tickers_list):
    # loop through each ticker in the tickers list
    for ticker in tickers_list:
        # clean the tickers list to support the alphavantage url format
        ticker = ticker.upper().strip()

        # create the URL
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
            ticker + '&outputsize=full&apikey=LW2A0A0SG8LFDIYM'
        # get the json web api data
        request = requests.get(url)
        # wait 12 seconds between requests because alphavantage only allows 5
        # requests per minute
        time.sleep(12)

        # load into dictionary
        ticker_dict = json.loads(request.text)

        # find the keys that we need to extract from the json file
        key1 = "Time Series (Daily)"
        key2 = "4. close"

        # check if the file already exists and only needs updated/appended to
        # rather than recreated
        if os.path.exists("csv_files/" + ticker + ".csv"):
            # find the last date to help with adding new data after this date
            csv_file = open(
                "csv_files/" + ticker + ".csv", "r")
            lines = csv_file.readlines()
            last_date = lines[-1].split(",")[0]

            # find the new lines that need to be added to the data; break when
            # the last date is reached
            new_lines = []
            for date in ticker_dict[key1]:
                if date == last_date:
                    break
                new_lines.append(
                    date + "," + ticker_dict[key1][date][key2]+"\n")

            # reverse the order of the new lines and add them
            new_lines = new_lines[::-1]
            csv_file = open(
                "csv_files/" + ticker + ".csv", "a")
            csv_file.writelines(new_lines)
            csv_file.close()

        else:
            # create the csv file
            csv_file = open(
                ticker + ".csv", "w")
            write_lines = []

            # load the csv file with the date and closing price
            for date in ticker_dict[key1]:
                write_lines.append(
                    date + "," + ticker_dict[key1][date][key2]+"\n")
            # reverse the order of the lines
            write_lines = write_lines[::-1]
            csv_file.writelines(write_lines)
            csv_file.close()

# --------------------------end of api to csv function---------------------------

# create a function to run an analysis of 3 diffferent trading strategies
# given a list of tickers; perform the analysis on data from the past year only;
# store results into a dictionary and save
# to json file


def run_analysis(tickers_list):

    # create an empty dictionary to store results from analysis
    results = {}

    # run the function to create or append data from a web api and convert to a csv file
    create_or_append_data(tickers_list)

    # get the date 1 year prior to today and assign to variable starting_date
    years = 1
    days_per_year = 365.24
    current_date = datetime.datetime.now().date()
    starting_date = current_date - \
        datetime.timedelta(days=(years*days_per_year))

    # loop through each ticker in the ticker list; make sure the ticker matches
    # required formatting
    for index, ticker in enumerate(tickers_list):
        ticker = ticker.upper().strip()

        # create a list from csv data to only return prices from today through the starting date
        prices = []
        csv_file = open(
            "csv_files/" + ticker + ".csv", "r")
        lines = csv_file.readlines()
        for i in reversed(range(len(lines))):
            if datetime.datetime.strptime(lines[i].split(",")[0], '%Y-%m-%d').date() >= starting_date:
                prices.append(float(lines[i].split(",")[1]))
            else:
                break

        # load prices from the ticker file and store them in the results dictionary
        # with the key "<ticker>_prices"
        name = ticker
        name_prices = name + "_prices"
        results[name_prices] = prices

        # call meanReversionStrategy(prices) and store the profit and returns
        # in the results dictionary with the keys "<ticker>_mr_profit" and
        # "<ticker>_mr_returns"
        mean_reversion_strat = meanReversionStrategy(prices)
        mrs_Profit = mean_reversion_strat[0]
        mrs_PercentReturn = mean_reversion_strat[1]
        mrs_Profit_Name = name + "_mr_profit"
        mrs_PercentReturn_Name = name + "_mr_returns"
        results[mrs_Profit_Name] = mrs_Profit
        results[mrs_PercentReturn_Name] = mrs_PercentReturn

        # call simpleMovingAverageStrategy(prices) and store the profit and returns
        # in the results dictionary with the keys "<ticker>_sma_profit" and
        # "<ticker>_sma_returns"
        simple_strat = simpleMovingAverageStrategy(prices)
        sma_Profit = simple_strat[0]
        sma_PercentReturn = simple_strat[1]
        sma_Profit_Name = name + "_sma_profit"
        sma_PercentReturn_Name = name + "_sma_returns"
        results[sma_Profit_Name] = sma_Profit
        results[sma_PercentReturn_Name] = sma_PercentReturn

        # call bollinger(prices) and store the profit and returns
        # in the results dictionary with the keys "<ticker>_boll_profit" and
        # "<ticker>_boll_returns"
        boll_strat = bollinger(prices)
        boll_Profit = boll_strat[0]
        boll_PercentReturn = boll_strat[1]
        boll_Profit_Name = name + "_boll_profit"
        boll_PercentReturn_Name = name + "_boll_returns"
        results[boll_Profit_Name] = boll_Profit
        results[boll_PercentReturn_Name] = boll_PercentReturn

    # loop through the results dictionary to find the most effective approach
    # and stock combo
    # initiate variables
    highest_profit = -1000000000
    best_strategy = ""

    # loop through each key and value in the dictionary
    for i in results.items():
        # discard the prices and rate of return and focus on profit
        if "profit" in i[0]:
            # find the highest profit and return the strategy
            if i[1] > highest_profit:
                highest_profit = i[1]
                best_strategy = i[0]

    # format the best strategy by separating by underscore and returning
    # the first two indices in the list
    best_strategy = best_strategy.upper().split("_")[0:2]

    # put the list back into a string
    winner = ""
    for i in best_strategy:
        winner += i + " "

    # add results to dictionary
    results["Best Stock/Strat and Profit"] = [winner, highest_profit]

    # save the results dictionary to a json file using the saveResults function
    # the first argument is the name of the dictionary and the second argument is
    # what name to save the json file as; return dictionary
    saveResults(results, "results")
    return results
# ---------------------- end of run_analysis function----------------------------


# list of tickers to get data from
# "amzn", "burl", "dis", "nflx", "gme", "goog", "tsla", "wmt"]
tickers_list = ["aapl", "adbe"]
run_analysis(tickers_list)

# use this line of code to make sure to view end of output
input("press enter to continue")
