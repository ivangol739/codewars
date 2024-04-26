tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
#print(tasks.split(','))

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
new_list = ', '.join(crypto_list)
#print(new_list)

world = " earth "
#print(world.strip())
#print(world.strip(' '))
#print(world.lstrip())
#print(world.rstrip())

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
#print(len(poem))

name = 'Ivan'
#print(f"My name - {name}")

song = """When an eel grabs your arm, 
And it causes great harm,
That's - a moray!"""

razstr = song.split()
for i in razstr:
  if i.startswith('m'):
    print(i.capitalize())

questions = [
  "We don't serve strings around here. Are you a string?",
  "What is said on Father's Day in the forest?",
  "What makes the sound 'Sis! Boom! Bah!'?"

]
answers = [
  "An exploding sheep.",
  "No, I'm a frayed knot.",
  "'Pop!' goes the weasel."
]

for i in range(len(questions)):
  print("Q: ", questions[i])
  print("A ", answers[i])