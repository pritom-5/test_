
print("hello there")
#<<<<<<< HEAD
print('this is also added to the new brunch')
# =======
x = [1,2,3,4]
total = 0
for i in x:
  total += i
  
print(total)
#>>>>>>> cf66058f8ec3167d3fb01492d4364e72c2e4e304

total_mult = 1

for i in x:
    total_mult *= i
    
print(total_mult)

print("let's see this works or not")
print('''
    This is in the master brunch and will be upped in the master of the origin not found in the new
''')