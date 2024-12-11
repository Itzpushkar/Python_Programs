from time import * 
import random as r

def mistake(para, userInput):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != userInput[i]:
                error = error + 1
        except:
            error = error + 1
    return error 

def timeTaken(s_time, e_time, userInput):
    time_taken = e_time - s_time
    time_Round = round(timeTaken,2)
    speed = len(userInput)/time_Round
    return round(speed)

check = ["On a bright and sunny morning, Emily decided to take a walk through the park near her house. The air was crisp, and the trees swayed gently in the breeze", "As she strolled along the winding path, she spotted a family of ducks swimming in the pond. Their fluffy yellow chicks followed closely behind, quacking happily.", "Emily smiled and continued on her way, enjoying the peace and tranquility of the park. Suddenly, she heard a rustling noise in the bushes nearby."]

test = r.choice(check)
print("~~~~~~~~~Typing Speed Test~~~~~~~~~")
print(test)
print()
print()
startTime=time()
testInput=input("Enter:")
endTime=time()

print("Speed to complete give para:", timeTaken(startTime,endTime,testInput), "Words per second")
print("Errors in given test:", mistake(test, testInput))