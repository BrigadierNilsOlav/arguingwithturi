import random

insults = "stfu","your mum","thats not what your mum said last night","you bitch", "fuck you","invalid arguement","who","bugger off","for fuck sake","cunt","piece of shit","ya dog","dickhead","emo","you furry","filthy weeb","touch grass","do you think your funny"
print("welcome to arguing with turi simulator say hi to our good old friend")
exitapplication = "878464546546848648468454564521214886896456465"
while exitapplication == "878464546546848648468454564521214886896456465":
    insultchoice = random.choice(insults)
    answer = input()
    print(insultchoice)

    if insultchoice == "who":
        answerwho = input()
        print("asked")
        insultchoice = random.choice(insults)
        answer = input()
        print(insultchoice)

