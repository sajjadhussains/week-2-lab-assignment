import pyjokes


def listen():
    return input("tell me anything,i will deliver you a joke.if you don't want to listen,say quit to stop me: ")
def decide():
    jokes = pyjokes.get_joke()
    return jokes

while True:  
    command=listen()
    if(command=="quit"):
        break
    else:
        print(decide())

