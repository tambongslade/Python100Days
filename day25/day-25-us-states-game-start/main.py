import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
screen.setup(700, 600)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_complete = False
correct = 0
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
newState = []
for state in states:
    newState.append(state.lower())

print(newState)


def logic():
    global correct

    for states in newState:
        if answer_state == states:
            index = newState.index(states)
            x = x_cor[index]
            y = y_cor[index]
            print(x)
            print(answer_state)
            turtle.penup()
            turtle.goto(x, y)
            turtle.write(answer_state, align="center", )
            turtle.goto(0, 0)
            screen.update()
            correct += 1


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()
logic()
passedQuestions = []

while not game_is_complete:
    answer_state = screen.textinput(title=f"{correct}/50 Guessed", prompt="What's another state's name?").lower()
    if answer_state == "exit":

        missingStates = [state for state in newState if state not in passedQuestions]

        dF=pandas.DataFrame(missingStates)
        dF.to_csv("Missing_state.csv")

        break
    else:
        logic()
#States to lear


