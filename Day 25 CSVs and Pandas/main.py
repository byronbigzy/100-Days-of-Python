import turtle
import pandas

screen = turtle.Screen()
screen.screensize(491, 725)
image = r"Day 25 CSVs and Pandas\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

path = r"Day 25 CSVs and Pandas\50_states.csv"
states_csv = pandas.read_csv(path)
data = pandas.DataFrame(data=states_csv)

state_list = data.state.to_list()
guessed_asnwers = []
score = 0

while len(guessed_asnwers) < 50:
    player_guess = screen.textinput(title=f"Guess the State. {score}/50", prompt="What's the name of another state?").title()
    guessed_asnwers.append(player_guess)

    if player_guess == "Exit":
        missing_states = [state for state in state_list if state not in guessed_asnwers]
        # missing_states = []
        # for state in state_list:
        #     if state not in guessed_asnwers:
        #         missing_states.append(state)
        
        df = pandas.DataFrame(missing_states)
        df.to_csv("States_to_learn.csv")
        break
    if player_guess.lower() in (s.lower() for s in state_list):
        state_data = data[data.state == player_guess]
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        label.goto(state_data.x.item(), state_data.y.item())
        label.write(state_data.state.item())
        score += 1
