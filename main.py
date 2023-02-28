# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_scorer="Ruud Gullit"
second_scorer="Marco Van Basten"
print(first_scorer)
goal_0=32
goal_1=54
scorers=first_scorer + " " +(str(goal_0))+','+second_scorer + " " +(str(goal_1))
print(scorers)
report=f'Ruud Gullit scored in the {goal_0}nd minute \n Marco Van Basten scored in the {goal_1}th minute'
print(report)
player='Jan. Wouters'
print(player[0:3])
print(player.find('Jan'))
first_name=(player[0:3])
print(player.find('Wouters'))
print(player[5:12])
last_name=(player[5:12])
last_name_len=len(last_name)
print(last_name_len)
name_short=player[0]+'.' + " " +player[5:12]
print(name_short)
chant= (first_name + '!')*len(first_name)
print(chant)
good_chant=chant[:12]!=" "
print(good_chant)