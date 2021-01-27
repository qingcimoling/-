def rabbit(month):
    if month<=1:
        return 1
    else:
        return rabbit(month-1)+rabbit(month-2)

