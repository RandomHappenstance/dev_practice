""" Coin Change

This problem comes from a video in the interviewing.io youtube channel.

The problem is described as:
    You are a cash register software and given an amount of change to 
    return, determine how many of each coin you have to give back.

"""

# Lets say that I have to return 33 cents.

def return_change(amount):
    coin_types = (25, 10, 5, 1)
    
    change = {"25" : 0,
              "10" : 0,
              "5" : 0,
              "1" : 0 }

    while amount != 0:
        if amount > 25:
            change['25'] += 1
            amount -= 25
        elif amount > 10:
            change['10'] += 1
            amount -= 10
        elif amount > 5:
            change['5'] += 1
            amount -= 5
        elif amount >= 1:
            change['1'] += 1       
            amount -= 1
    return change

if __name__ == "__main__":
    change_amount = 33 # 33 cents
    change = return_change(change_amount)
    print("Amount to return is: ")
    print(change)
    print(change_amount)

