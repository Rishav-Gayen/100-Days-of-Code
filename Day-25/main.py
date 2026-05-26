import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

img_file_name = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(img_file_name)

turtle.shape(img_file_name)
game_is_on = True

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

while game_is_on:
    if len(guessed_states) == len(states_list):
        game_is_on = False
        turtle.TK.messagebox.showinfo(title="You won!", message="You have guessed all states! Congratulations!")
    else:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states_list)} guessed correct", prompt="What's another state's name?: (Type quit to quit) ")
        answer_state = answer_state.title().strip()

        if answer_state in guessed_states:
            turtle.TK.messagebox.showinfo(title="Guessed", message=f"You have already guessed {answer_state}")
            continue

        elif answer_state in states_list:

            coordinates_list = data[['x', 'y']].loc[data['state'] == answer_state]
            x_coord = coordinates_list['x'].to_list()[0]
            y_coord = coordinates_list['y'].to_list()[0]

            writer.goto(x_coord, y_coord)
            writer.write(f"{answer_state}")
            guessed_states.append(answer_state)
            
        elif answer_state.lower() == "quit":
            game_is_on = False

        else:
            turtle.TK.messagebox.showinfo(title="Message", message="Wrong guess! Try again.")

missed_data = {
    "state": [state for state in states_list if state not in guessed_states]
}

missed_data = pd.DataFrame(missed_data)
missed_data.to_csv('states_to_learn.csv')

screen.exitonclick()