import random
def welcome():

    for i in range(0,20):
        print("*\t",end="")
    print()
    print("*",end="")
    for i in range(0,19):
        print("\t",end="")
    print("*")
    print("*",end="")
    for i in range(0,19):
        print("\t",end="")
    print("*")
    print("*",end="")
    for i in range(0,8):
        print("\t",end="")
    print("Welcome",end="")
    for i in range(0,10):
        print("\t",end="")
    print("*")
    print("*",end="")
    for i in range(0,19):
        print("\t",end="")
    print("*")
    print("*",end="")
    for i in range(0,19):
        print("\t",end="")
    print("*")
    for i in range(0,20):
        print("*\t",end="")
    print()
    input("press any key to start:")
welcome()
print("\n"*100)
def mainmenu():
    print("1.Rock paper Scissor\n2.Cow and bulls\n3.Exit")
    ch=int(input("Enter your choice number:"))
    if ch==1:
         rockpaperscissormenu()
    elif ch==1:
         cowandbullsmenu()
    elif ch==3:
         exit()
    else:
        print("Invalid Cjoice!")
        mainmenu()
def rockpaperscissormenu():
    print("1.play\n2.rules\n3.Return to mainmenu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        rockpaperscissor()
    elif ch == 1:
        rockpaperscissorrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid Cjoice!")
        rockpaperscissorsmenu()
def cowandbullsmenu():
    print("1.play\n2.rules\n3.Return to mainmenu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        cowandbulls()
    elif ch == 1:
        cowandbullsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid Cjoice!")
        cowandbullsmenu()
def rockpaperscissor():
    print("WELCOME TO ROCK PAPER SCISSOR")
    print("you will be competing against the computer. That player score 5 points 1st will be declared the winner!")
    print("If your choice is rock, Please Enter 0")
    print("If your choice is Paper, Please Enter 1")
    print("If your choice is Scissor, Please Enter 2")
    print("If you want to exit, please Enter -1")
    user=0
    comp=0
    cnt=0
    choice=["rock","Paper","Scissor"]
    while(user<5 and comp<5 and cnt<25):
        cnt+=1
        u_ch=int(input("Enter your choice:"))
        if u_ch==-1:
            print("Thank you")
            break
        c_ch=random.choice([0,1,2])
        if u_ch==0 and u_ch==1:
            comp+=1
        elif u_ch==0 and u_ch==2:
            user+=1
        elif u_ch==1 and u_ch==0:
            user+=1
        elif u_ch==1 and u_ch==2:
            comp+=1
        elif u_ch==2 and u_ch==0:
            comp+=1
        elif u_ch==2 and u_ch==1:
            user+=1
        print("you",chc[u_ch])
        print("Computer",chc[u_ch])
        print("yours score:",user,"\tComputer's score:",comp)
    if(user>comp):
        print("Congratulations! you win")
    elif(comp>user):
        print("Oops!Sorry You Lose. Better luck Next time!")
    else:
        print("Match Draw")
    mainmenu()
def cowandbulls():
    words=["rate","fail","cake","sore","tear","calm","rige","time","face","swan"]
    rand=random.randrange(0,10)
    word=words[rand]
    cnt=0
    while(cnt<15):
         s=input("Enter string:")
        if s==("-1"):
            print("Thank you")
            return
        cow=0
        bulls=0
        chars=0
        for c in s:
            if c in word:
                chars+=1
        for i in range(0,4):
            if s [i]==word[i]:
                bulls+=1
        cow=chars-bulls
        print("cows",cow,"\tBulls",bulls,)
        if bulls==4:
            print("Congratulation You win!")
            mainmenu()
        cnt+=1
    print("oops, Sory better luck next time")
    mainmenu()

welcome()
print("\n"*100)
mainmenu()

