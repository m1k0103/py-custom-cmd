import subprocess as s

while True:
    inp = input("> ")
    if inp.lower() == "help":
        print("""Commands: 
              """) # not finished this help command
        pass
    if inp.lower() == "wifi -s": # for windows only
        inp = "netsh wlan show all"
    if inp.lower() == "wifi -sp": # for windows only
        name = input("Wifi name: ")
        inp = f"netsh wlan show profile name={name} key=clear"
    try:
        out = s.run(inp.split(" "), stdout=s.PIPE) # runs the command and saves output
        print(out.stdout.decode("utf-8")) # decodes and prints the output
    except:
        print(f"An error occured with the provided input: {inp}") # error message and provides what the user inputted.