def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 300             # euros
    NORMAL_COMMISSION = 7.5 # %
    BONUS_COMMISSION = 14   # %
    i = 0

    while i < len(sales):
        if sales[i] >= 300:
            sales[i] = 0.14 * sales[i]
        else:
            sales[i] = 0.075 * sales[i]
        i = i + 1
    summa = 0
    for sale in sales:
        print("{:.2f} eur".format(sale))
        summa = summa + sale
    print("Total commissions {:.2f} eur".format(summa))


main()