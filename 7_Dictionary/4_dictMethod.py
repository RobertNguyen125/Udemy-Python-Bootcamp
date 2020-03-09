# .clear()
# .copy()

d = dict(a=1,b=2,c=3)
c = d.copy()
print(c)
print(c is d)
# .fromkeys(): create k,v pair from comma separated values
print({}.fromkeys('a','b')) #k:a, v:b
print({}.fromkeys(['email'],'unknown'))
print({}.fromkeys('a',[1,2,3,4,5]))

new_users = {}.fromkeys(['name', 'score', 'email', 'profile'], 'unknown')
print(new_users)
new_users = {}.fromkeys(['phone'],'unknown')
print(new_users) # this wont change

new_users = {}.fromkeys('phone', 'unknown') # w/o the list for keys, it will iterate over the string
print(new_users)

new_users = {}.fromkeys(range(1,10),'unknown')
print(new_users)

game_properties = ["current_score", "high_score", "number_of_lives",
                "items_in_inventory", "power_ups", "ammo", "enemies_on_screen",
                "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_result = {}.fromkeys(game_properties, 0)
print(initial_result)
# .get()

# .pop()
me = {'name':'Duc', 'age':28, 'hobby':'gym'}
me.pop('name')
print(me) # name is removed

# .popitem(): randomly remove a k,v pair
me = {'name':'Duc', 'age':28, 'hobby':'gym'}
me.popitem()
print(me)

# .update()
first =dict(a=1,b=2,c=3,d=4,e=5)
second =dict(f=6)
second.update(first) # f will be intact and update() will add first to the second
print(second)
second['a'] = 'amazing'
print(second)
second.update(first) # this will override the updated values
print(second)


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')
