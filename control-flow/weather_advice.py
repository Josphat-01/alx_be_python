weather = str(input("What is the weather like today? (sunny/rainy/cold): "))

sunny = "sunny"
cold = "cold"
rainy = "rainy"

if weather == sunny:
    print("Wear a T-shirt and sunglasses.")
elif weather == rainy:
    print("Don't forget your umbrella and a raincoat.")
elif weather == cold:
    print("Make sure you wear a warm coat and scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")