# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = scorer_1 +" "+ str(goal_0)+ ", " + scorer_2+ " "+str(goal_1) 
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
print(scorers)
print(report)

player = scorer_1
x = player.find(" ")
first_name = player[:x]
last_name = player[(x+1):]
last_name_len = len(last_name)
y = player[0]
name_short = f'{y}. {last_name}'
z = (len((first_name))-1)

chant = (first_name + "!") + ((" "+first_name + "!") * z)
good_chant = chant[-1] != " "

print(first_name)
print(last_name)
print(name_short)
print(last_name_len)
print(chant)
print(good_chant)

