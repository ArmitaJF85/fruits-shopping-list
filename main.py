
def analyze_fruits(**fruits):
    count = len(fruits)
    total = sum(fruits.values())
    most_expensive = max(fruits,key = fruits.get)
    cheapest = min(fruits,key = fruits.get) 

    print(f"You have {count} fruits in your shopping list")
    print(f"The total cost of the shopping list is {total}")
    print(f"The most expensive fruit is {most_expensive} with the price of {fruits[most_expensive]}")
    print(f"The cheapest fruit is {cheapest} with the price of {fruits[cheapest]}")

def main():
        fruits = {}

        while True:
            line = input().strip()

            if line ==  "finish":
                break

            name, price = line.split()
            fruits[name] = int(price)

            analyze_fruits(**fruits)

if __name__ == "__main__":
    main()
