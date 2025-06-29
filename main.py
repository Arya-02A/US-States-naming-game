import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

gussed_states = []

while len(gussed_states) < 50:

    answer_state = screen.textinput(title=f"{len(gussed_states)}/50 states gussed", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in states_list:
        #     if state not in gussed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states_list if state not in gussed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        
    else:
        print(f"No State Named, {answer_state}")



screen.exitonclick()

