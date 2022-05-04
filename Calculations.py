def profitOrLossFunction(textbox1,textbox2,textbox3):
    if textbox1.replace(".", "", 1).isdigit() == False or textbox2.replace(".", "", 1).isdigit() == False or textbox3.replace(".", "", 1).isdigit() == False:
        return "Invalid Entry"                              #returns invalid entry if at least one of the textboxes dont contain an int or float

    numShares = float(textbox1)
    purchasePrice = float(textbox2)
    sellPrice = float(textbox3)

    difference = abs(purchasePrice - sellPrice)
    amount = numShares * purchasePrice

    GainOrLoss = amount * (difference / purchasePrice)

    percentGainOrLoss = (difference / purchasePrice) * 100

    amount = round(amount, 4)
    GainOrLoss = round(GainOrLoss, 4)
    percentGainOrLoss = round(percentGainOrLoss, 2)

    percentGainOrLoss = "{:,}".format(percentGainOrLoss)

    if purchasePrice == sellPrice:
        return "You made no profit"

    elif purchasePrice < sellPrice:
        total = GainOrLoss + amount
        total = round(total, 4)
        total = "{:,}".format(total)
        amount = "{:,}".format(amount)
        GainOrLoss = "{:,}".format(GainOrLoss)


        return f"You initially invested ${amount}\nYou made: ${GainOrLoss} profit\nYou now have: ${total} in total \npercent gained: {percentGainOrLoss}%"


    elif purchasePrice > sellPrice:
        total = amount - GainOrLoss
        total = round(total, 4)
        total = "{:,}".format(total)
        amount = "{:,}".format(amount)
        GainOrLoss = "{:,}".format(GainOrLoss)


        return  f"You initially invested ${amount}\nYou Lost: ${GainOrLoss}\nYou now have: ${total} in total\npercent lost: {percentGainOrLoss}%"


def stockAverageFunction(input_list: list) -> str:
    """
    calculates the average of stocks 

    :param input_list: list contains 8 values. first 4 entries are the shares bought, last 4
    entries are the purchase price respective of the shares bought
    :return: String representing the stock average as well as the number of shares owned
    """


    for i in range(len(input_list)):
        if input_list[i].replace(".", "", 1).isdigit() == False:
            input_list[i] = 0
        else:
            input_list[i] = float(input_list[i])

    if input_list[4] == 0 and input_list[5] == 0 and  input_list[6] == 0 and input_list[7] == 0:
        return "Invalid"

    totalSharesBought = 0
    for i in range(0,4,1):
        totalSharesBought += input_list[i]

    for i in range(4):
        if input_list[i + 4] == 0:
            totalSharesBought-= input_list[i]

    totalAmountBought = 0

    for i in range(4):
        totalAmountBought += input_list[i] * input_list[i + 4]


    stockAveragePrice= totalAmountBought/totalSharesBought


    return "Total Shares: " + str(round(totalSharesBought,2)) +"\nAverage Cost: $"+ str(round(stockAveragePrice,3))


