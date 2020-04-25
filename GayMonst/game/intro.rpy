define pov = Character("[povname]")

label intro:
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "assbutt"

    pov "My name is [povname]!"
