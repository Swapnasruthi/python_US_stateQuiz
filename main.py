import turtle as t
import pandas
tim=t.Turtle()

screen=t.Screen()
image="blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()

guessed_states=[]
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed states",
                                    prompt="what's another state in us:").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        tim.penup()
        tim.hideturtle()
        state_details=data[data.state == answer_state]
        tim.goto(int(state_details.x),int(state_details.y))
        tim.write(answer_state)

screen.exitonclick()