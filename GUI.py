#GUI app logic
import random
from tkinter import *
tv_shows = ['Game of Thrones','Friends','How I Met Your Mother','Breaking Bad','Narcos','Flash','Arrow','Big Bang Theory','Walking Dead','Agents Of Shield','Blue Planet 2',
            'Legion','The Grand Tour','Band Of Brothers','Westworld','Sherlock','The Punisher', 'True Detective', 'Daredevil','Luke Cage','Jessica Jones','Iron Fist','Stranger Things',
            'Rick and Morty', 'House of Cards', '13 Reasons Why','House MD', 'Castle','Doctor Who','Dexter','Suits']
score = 0
user_list=[]
jumb_list=[]
time= 0
for i in range(1,10,1):
    user_list.append(random.choice(tv_shows))
print(user_list)


def jumble(word):   
    jum=" "
    while word:
        pos=random.randrange(len(word))
        jum +=word[pos]
        word=word[:pos]+word[(pos + 1):]
    return jum
    
u=str(user_list[random.randrange(0,9)]) #need to remove later

def sen_jumble(w):
    l=[]
    for i in w:
        new = jumble(i)
        #print("new=",new)
        l.append(new)
        #print("l=",l)
    l=" ".join(l)
    #print(l)
    return l
#print("Chosen show=>",u)
#print("Final result=>", sen_jumble(u.split()))



#define a function
#loop to make a jumbled list
#loop to print and match the jumbled word to the gusess made
#display point and time taken

def start_game(event):
    timetaken()
    global jumb_list
    global score
    for i in user_list:
        r1 = sen_jumble(i.split())
        jumb_list.append(r1)
        guess.focus_set()
    if time>0:
        for i in range(len(jumb_list)):
            word.config(text = "Jumbled Word=" + str(jumb_list[i]))
            if guess.get().lower() == user_list[i].lower():
                score+=1
                score_display.config(text = str(score))
                guess.delete(0,END)
            else:
                score+=0
                score_display.config(text = str(score))
            
def timetaken():
   global time
   if time>=0:
      time += 1
      timetaken.config(text = "Time : "+ str(time))
      timetaken.after(1000, timetaken)

main = Tk()
main.title("Guess What")
main.geometry("375x200")

rules = Label(main, text="Guess the correct Tv-show name for the jumbled one shown")
rules.pack()

word = Label(main)
word.pack()

score_display = Label(main)
score_display.pack()

timeout = Label(main)
timeout.pack()

guess = Entry(main)
main.bind('<Return>',start_game)
guess.pack()
guess.focus_set()

main.mainloop()
               

