import turtle

screen = turtle.Screen()
screen.title("Colourful Turtle Drawing")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]

for i in range(36):
  pen.color(colors[i % len(colors)])

  for j in range(4):
    pen.forward(100 + i * 2)
    pen.right(90)
    pen.right(10)

turtle.done()

print("Question Answering Bot")

question = input("Ask me something: ")

if question == "hku":
  print ("Bot: HKU stands for The University of Hong Kong.")

elif question == "robot":
  print ("Bot: A robot is a machine.")

elif question == "jetson":
  print ("Bot: Jetson Nano is an AI computer.")

elif question == "ai":
  print ("Bot: AI means Artificial Intelligence.")

elif question == "human":
  print ("Bot: A human is a person.")

else:
  print ("Bot: Sorry I don’t understand.")
