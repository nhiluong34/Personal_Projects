import turtle
from operator import truediv

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif" 
screen.addshape(image) # add new shape instead of traditional ones
turtle.shape(image)


all_states = pandas.read_csv("50_states.csv")

all_states_list = all_states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states_list:
            if state not in guessed_states:
                missing_states.append(state) # Create a list of missing states
        new_data = pandas.DataFrame(missing_states) # Save missing_states as csv
        new_data.to_csv("states_to_learn.csv") 
        break
    if answer_state in all_states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = all_states[all_states.state == answer_state] 
        t.goto(state_data.x.item(), state_data.y.item()) 
        t.write(answer_state)


