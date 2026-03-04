stock_price = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("Available Stocks:", list(stock_price.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_price:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = qty
        total_investment += stock_price[stock] * qty
    else:
        print("Stock not available!")

print("\nYour Portfolio:", portfolio)
print("Total Investment Value: $", total_investment)

save = input("Do you want to save result? (yes/no): ").lower()

if save == "yes":
    file_type = input("Save as txt or csv? ").lower()
    
    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Total Investment: " + str(total_investment))
        print("Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Total Investment," + str(total_investment))
        print("Saved as portfolio.csv")