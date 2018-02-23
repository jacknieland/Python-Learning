import random
bases = ["tostada shell","soft tortilla","huarache","sope","taco"]
meats = ["carne asada","al pastor","carnitas","pollo asado", "barbacoa"]
toppings = ["lettuce","tomato","avocado","radish","pico","habenero","crema","onions","cilantro","roasted corn","cotija","queso fresco","black beans","refried beans","rice","roasted garlic"]
salsas = ["green","red","mezcla","death"]
flair = ["whole thing deep fried","doused in sauce and baked","served with tequila","doused in death sauce", "covered in cheese and baked", "turn the whole plate upside down over fries"]
meat_preference = 0
input_parameters = [1,2,3]
rand_val1 = random.sample(range(0,len(meats)),2)
rand_val2 = random.sample(range(0,len(toppings)),6)

print("Welcome to Jack's Mexican Food Generator 1.0!")
print("What are your meat preferences?")
input1 = int(raw_input("Press 1 for vegetarian, press 2 for omnivore, press 3 for EXRA MEATY: "))
if input1 in input_parameters:
	meat_preference = input1
else:
	print("You can't follow directions can you?")
print("Your base is " + str(bases[random.randint(0,len(bases)) - 1]))
if meat_preference == 2:
	print("Your meat is " + str(meats[random.randint(0,len(meats) - 1)]))
elif meat_preference == 1:
	print("You're eating veggies buddy")
elif meat_preference == 3:
	print("You're getting meaty with some " + meats[rand_val1[0]] + " and " + meats[rand_val1[1]])
else:
	print("IDK WTF you did")
	
print("Your toppings are " + toppings[rand_val2[0]] + ", " + toppings[rand_val2[1]] + ", " + toppings[rand_val2[2]] + ", " + toppings[rand_val2[3]] + ", " + toppings[rand_val2[4]] + ", and " + toppings[rand_val2[5]])
print("Your salsa is " + salsas[random.randint(0,len(salsas) - 1)] + " sauce.")
print("Your flair is " + flair[random.randint(0,len(flair) - 1)])

