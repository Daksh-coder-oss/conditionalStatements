buyingPrice=int(input("Please enter the buying price"))
selling_price=int(input("Please enter the selling price"))

if buyingPrice>selling_price:
    print("You got a loss")

else:
    print("You have a profit",selling_price-buyingPrice)