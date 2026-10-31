print("\nProblem9\n")
# a

def electricity_bill(kwh):
    if kwh < 0:
        return None
    
    if kwh <= 50:
        cost = kwh * 480

    elif kwh <= 200:
        cost = (50 * 480) + (kwh - 50) * 610

    else:
        cost = (50 * 480) + (150 * 610) + (kwh - 200) * 730

    total = (cost + 2000) * 1.10
    return round(total)

# b
print("\nElectricity Bill Table")

values = [0, 35, 50, 120, 200, 350]

for kwh in values:
    bill = electricity_bill(kwh)
    usd =  bill / 4100

    print(f"{kwh} kWh = {bill:,} riel ≈ ${usd:.2f}")           # :,  :  7366 -> 7,366

# c
kwh = float(input("Enter your monthly consumption (kwh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid Consumption!!!")
else:
    print(f"Your electricity bill: {bill:,} riel.")
    print(f"USD: ${bill / 4100:.2f}")
    print("Thank You!!!\n")