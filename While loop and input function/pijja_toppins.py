prompt = ("Enter thr pijja toppins")
prompt += ("\n Enter 'quit' to quit: ")

while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(f"your {message.title()} is added to pijja")
