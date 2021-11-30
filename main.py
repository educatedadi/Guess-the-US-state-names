import pandas
import turtle
from write_name import WriteName

image = 'blank_states_img.gif'
file_data = pandas.read_csv('50_states.csv')

screen = turtle.Screen()
screen.title('Guess all the states of U.S.')
write_object = WriteName()

screen.addshape(image)
turtle.shape(image)

state_list = file_data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:

    user_input = (screen.textinput(f'{len(guessed_states)}/50', 'Enter another state name')).title()
    if user_input in state_list:
        state_df = file_data[file_data.state == user_input]
        x_coor = int(state_df['x'])
        y_coor = int(state_df['y'])
        write_object.write_on_screen(user_input, x_coor, y_coor)
        guessed_states.append(user_input)

    elif user_input == 'Exit':
        missing_state = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        to_learn_dict = {'States to learn': missing_state}
        to_learn_df = pandas.DataFrame.from_dict(to_learn_dict)
        to_learn_df.to_csv('States to learn.csv')
        break

screen.exitonclick()
