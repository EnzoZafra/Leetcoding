def my_bisect(a, x):
    start = 0
    end = len(a) - 1
    
    while start < end:
        mid = (end + start) // 2
        midNum = a[mid]
        
        if midNum > x:
            end = mid
        elif midNum <= x:
            start = mid + 1
    
    return start

def findCombinations(jeans, shoes, skirts, tops, budget):
    if budget == 0:
        return 0
    
    # combine two two arrays, add each pairs
    jeans_shoes = []
    skirts_tops = []
    
    for jean in jeans:
        for shoe in shoes:
            jeans_shoes.append(jean + shoe)
            
    for skirt in skirts:
        for top in tops:
            skirts_tops.append(skirt + top)
    
    ans = 0
    for jean_shoe in jeans_shoes:
        money_left = budget - jean_shoe
        ans += my_bisect(skirts_tops, money_left) 
    
    return ans
    
    
# Question:
# A customer wants to buy a pair of jeans, a pair of shoes, a skirt, and a top but has a limited budget in dollars. Given different pricing options for each product, determine how many options our customer has to buy 1 of each product. You cannot spend more money than the budgeted amount.

# The customer must buy shoes for 4 dollars since there is only one option. This leaves 6 dollars to spend on the other 3 items. Combinations of prices paid for jeans, skirts, and tops respectively that add up to 6 dollars or less are [2, 2, 2], [2, 2, 1], [3, 2, 1], [2, 3, 1].  There are 4 ways the customer can purchase all 4 items.

priceOfJeans = [2, 3]
priceOfShoes = [4]
priceOfSkirts = [2, 3]
priceOfTops = [1, 2]
budgeted = 10 

combinations = findCombinations(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted)
print(combinations)
