import subprocess as s

while True:
    inp = input("> ")
    if inp.lower() == "help":
        print("""Commands:
              """)
        pass
    if inp.lower() == "wifi -s":
        inp = "netsh wlan show all"
    if inp.lower() == "wifi -sp":
        name = input("Wifi name: ")
        inp = f"netsh wlan show profile name={name} key=clear"
    try:
        out = s.run(inp.split(" "), stdout=s.PIPE)
        print(out.stdout.decode("utf-8"))
    except:
        print(f"An error occured with the provided input: {inp}")