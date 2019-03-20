#GUI app logic
import random
from tkinter import *
tv_shows = ['Game of Thrones','Friends','How I Met Your Mother','Breaking Bad','Narcos','Flash','Arrow','Big Bang Theory','Walking Dead','Agents Of Shield','Blue Planet 2',
            'Legion','The Grand Tour','Band Of Brothers','Westworld','Sherlock','The Punisher', 'True Detective', 'Daredevil','Luke Cage','Jessica Jones','Iron Fist','Stranger Things',
            'Rick and Morty', 'House of Cards', '13 Reasons Why','House MD', 'Castle','Doctor Who','Dexter','Suits']
score = 0
user_list=[]
time= 0
for i in range(1,11,1):
    choice = random.choice(tv_shows)
    user_list.append(choice)
    tv_shows.remove(choice)
print(user_list)


def jumble(word):   
    jum=" "
    while word:
        pos=random.randrange(len(word))
        jum +=word[pos]
        word=word[:pos]+word[(pos + 1):]
    return jum

def sen_jumble(w):
    l=[]
    for i in w:
        new = jumble(i)
        l.append(new)
    l=" ".join(l)
    return l

def start_game(event):
    timetaken()
    jumb_list = []
    global score
    for i in user_list:
        r1 = sen_jumble(i.split())
        jumb_list.append(r1)
        guess.focus_set()
    word.config(text = "Jumbled Word => " + str(jumb_list[score]))
    if guess.get().lower() == user_list[score].lower():
        score += 1
        score_display.config(text = str(score))
        try:
            word.config(text="Jumbled Word => " + str(jumb_list[score]))
        except IndexError:
            word.config(text="You Win!")
            score = 0
        guess.delete(0,END)
                
            
def timetaken():
   global time
   if time>=0:
      time += 1
      timeout.config(text = "Time : "+ str(time))
      timeout.after(1000, timetaken)

main = Tk()
main.title("Guess What")
main.geometry("550x300")

rules = Label(main, text="Guess the correct Tv-show name for the jumbled one shown",font = ('Times New Roman ',14),fg='Red')
rules.pack()

word = Label(main,font = ('Times New Roman bold', 14))
word.pack()

score_display = Label(main,font = ('Times New Roman bold', 13))
score_display.pack()

timeout = Label(main,font = ('Times New Roman', 13))
timeout.pack()

guess = Entry(main,font = ('Times New Roman', 13))
main.bind('<Return>',start_game)
guess.pack()
guess.focus_set()

main.mainloop()
               

