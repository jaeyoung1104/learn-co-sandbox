nested_list = [1, [2, [4, [5, [6]], 3]]]
number_six = None

# 2. Sort the cats list in alphabetical order

cats = ['Maine Coon', 'Tabby', 'Siamese', 'Garfield', 'Sylvester']

# 3. Look up a new string or list method and explain how it work

dogs = ['Scooby', 'Scrappy', 'Clifford', 'Pickles', 'Floyd']
animal = None
cats_jrs = []
for i in cats: 
  cats_jrs.append(i + " Jrs")
print(cats_jrs)
pets_array = []
for i in [0,1,2,3,4]:
  pets_array.append(cats[i] + " " + dogs[i])
print(pets_array)

more_cats = ['Horatio', 'Whiskers', 'Chesire']
for i in more_cats:
  cats.append(i)
print(cats)
variable = sorted(cats,keys=lambda element: element[2])
