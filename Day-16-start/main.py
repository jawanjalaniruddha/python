# from turtle import Turtle, Screen
#
# sami = Turtle()
# print(sami)
#
# my_screen = Screen()
# print(my_screen.canvheight)

# sami.shape("turtle")
# sami.color("DeepPink1")
# sami.forward(100)
# print(sami.position())
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

print(table)