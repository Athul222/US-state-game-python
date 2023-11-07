import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)


data = pandas.read_csv("./us-states-game-start/50_states.csv")
all_states = data.state.to_list()
gussed_state = []

while len(gussed_state) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50 States Correct", prompt="What's the another states name?").title()
    if answer_state == "Exit":
        
        # if answer_state == "Exit":
        #     missing_states = []
        #     for state in all_states:
        #         if state not in gussed_state:
        #             missing_states.append(state)
        missing_states = [state for state in all_states if state not in gussed_state] # Above code is shortened using list comprehension.
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_missing_states.csv")
        break
    
    if answer_state in all_states:
        gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) # or state.data.state.item()

     