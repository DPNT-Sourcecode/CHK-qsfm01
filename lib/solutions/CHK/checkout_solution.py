import numpy as np
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        # counter dictionary of all items 
        items = Counter(skus)
        prices = [50,30,20,15,40,10]

        # check item validity
        valid_items = ['A', 'B', 'C', 'D', 'E', 'F']
        for item in items.keys():
            if item not in valid_items:
                return -1
        
        ## above could be combined into this if efficiency is required on huge lists + loops optimized
        ## for a smaller list like this I have favoured readability of the code to maintain
        # calculate cost of each item and total
        total = 0 
        for idx, item in enumerate(valid_items):
            quantity = items[item]
            price = prices[idx]
            # instructions for A
            if item == 'A':
                #cost = quantity%3*price + int(quantity/3)*130
                # implementing cost variations between 3 and 5 products
                cost_var_1 = quantity%3*price + int(quantity/3)*130
                cost_var_2 = quantity%5*price + int(quantity/5)*200
                # incase amount bought is a multiple of 8
                if (quantity-5)>=0 and ((quantity-5)-3)>=0:
                    cost_var_3 = quantity%8*price + int(quantity/5)*200 + int((quantity-5)/3)*130
                    # return min of three options to favour customer
                    cost = min(cost_var_1, cost_var_2, cost_var_3)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1, cost_var_2)     
            # instructions for B
            elif item == 'B':
                # calculate if any B are free from 2Es
                B_free_quan = int(items["E"]/2)
                quantity -= B_free_quan
                quantity = int(np.maximum(0, quantity))
                cost = quantity%2*price + int(quantity/2)*45
            # instructions for F 
            elif item =='F':
                if quantity>=3:
                    cost = int(quantity/3)*2*price + quantity%3*price
                else: 
                    cost = quantity*price

            # instructions for H 
            elif item == 'H':
                # implementing cost variations between 5 and 10 products
                cost_var_1 = quantity%5*price + int(quantity/5)*45
                cost_var_2 = quantity%10*price + int(quantity/10)*80
                # incase amount bought is a multiple of 15
                if (quantity-10)>=0 and ((quantity-10)-5)>=0:
                    cost_var_3 = quantity%15*price + int(quantity/10)*200 + int((quantity-10)/5)*130
                    # return min of three options to favour customer
                    cost = min(cost_var_1, cost_var_2, cost_var_3)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1, cost_var_2)     
            # instructions for K 
            elif item == 'K':
                # calculate if any K are free from 2Ks
                cost = quantity%2*price + int(quantity/2)*150 
            # instructions for M 
            elif item == 'M':
                # calculate if any B are free from 2Es
                M_free_quan = int(items["N"]/3)
                quantity -= M_free_quan
                quantity = int(np.maximum(0, quantity))
                cost = quantity*price
            elif item == 'P':
                # calculate if any B are free from 2Es
                cost = quantity%5*price + int(quantity/5)*200                     
            elif item == 'Q':
                # calculate if any B are free from 2Es                    
                Q_free_quan = int(items["R"]/3)
                quantity -= Q_free_quan
                quantity = int(np.maximum(0, quantity))    
                cost = quantity%3*price + int(quantity/3)*80 
            # instructions for U 
            elif item =='U':
                if quantity>=4:
                    cost = int(quantity/4)*3*price + quantity%4*price  
            # instructions for V
            if item == 'V':
                # implementing cost variations between 3 and 5 products
                cost_var_1 = quantity%2*price + int(quantity/2)*90
                cost_var_2 = quantity%3*price + int(quantity/3)*130
                # incase amount bought is a multiple of 8
                if (quantity-3)>=0 and ((quantity-3)-2)>=0:
                    cost_var_3 = quantity%5*price + int(quantity/3)*130 + int((quantity-3)/2)*90
                    # return min of three options to favour customer
                    cost = min(cost_var_1, cost_var_2, cost_var_3)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1, cost_var_2) 

            # others
            else:
                cost = quantity*price
            total += cost

        return total

    except:
        raise NotImplementedError()

