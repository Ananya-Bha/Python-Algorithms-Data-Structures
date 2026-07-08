#animals
animal_1="blue jellyfish"
animal_2="green lizard"
animal_3="red crab"
animal_4="yellow chick"
animal_5="purple unicorn"

#Colours
k = "\033[30m"  # black
r = "\033[31m"  # red
g = "\033[32m"  # green
y = "\033[33m"  # yellow
b = "\033[34m"  # blue
p = "\033[35m"  # purple
c = "\033[36m"  # cyan
w = "\033[37m"  # white
reset = "\033[0m"  # reset text back to normal

#Background Colours
kb = "\033[40m"  # black
rb = "\033[41m"  # red
gb = "\033[42m"  # green
yb = "\033[43m"  # yellow
bb = "\033[44m"  # blue
pb = "\033[45m"  # purple
cb = "\033[46m"  # cyan
wb = "\033[47m"  # white

#styles
bold = "\033[1m" 
faint = "\033[2m"     
underline = "\033[4m"
invert = "\033[7m"

'''
Challenge_1 =f"""
{invert}{bold}A Day at the Zoo{reset}

One day,I went to the zoo, where I saw a {b}{bold}{underline}{animal_1}{reset}🪼,a {g}{bold}{underline}{animal_2}{reset}🦎, a {r}{bold}{underline}{animal_3}{reset}🦀, a {y}{bold}{underline}{animal_4}{reset}🐥, and a {p}{bold}{underline}{animal_5}{reset}🦄.

I was amazed. I thought to myself,{faint}"Wow, I've never seen all these animals in a zoo before!"{reset}

My favourite animal was the {gb}{bold}{underline}{animal_2}🦎{reset}."""
print(Challenge_1)
'''

Challenge_2= f"""
{b}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■{r} ■{b} ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ {r}■ ■ ■ {b}■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ {r}■ ■ ■ ■ ■ {b}■ ■ ■ ■ ■
■ ■ ■ ■{r} ■ ■ ■ ■ ■ ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■ ■ ■ ■ ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■ ■ ■ ■ ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■ ■ ■ ■ ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■{w} ■ ■ ■{y} ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■{w} ■ ■ ■{y} ■ ■ {b}■ ■ ■ ■
■ ■ ■ ■{y} ■ ■{w} ■ ■ ■{y} ■ ■ {b}■ ■ ■ ■
{g}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
"""
print(Challenge_2)
