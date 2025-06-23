def computepay(h, r):
    
    if h > 40:
        sol = (h-40)*1.5*r + 40*r
    else:
        sol =h*r
        
    return sol

hrs = float(input("Enter Hours:"))
rte = float(input("Enter Rate:"))

p = computepay(hrs, rte)
print("Pay", p)