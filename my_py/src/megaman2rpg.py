import time
while True:
    print("Now running Megaman 2 RPG edition...\n version 1.0.0 ")
    time.sleep(1)
    print("You are Megaman, created by Dr.Light to stop the evil forces of Dr.Wily.\n However, after you were created, Dr.Wily created 8 Robo Masters, each with a unique ability. \n You must stop them all and beat Dr.Wily.")
    time.sleep(2)
    print("Now entering stage select.")
    time.sleep(0.9)
    stage_select = input("There are 8 stages to choose from. \nAir Man, Bubble Man, Crash Man, Quick Man, Flash Man,\n Quick Man, Leaf Man, and Metal Man.\n Which stage do you choose?\n")
    stage_select = stage_select.lower()
    if stage_select == "Air Man":
        print("Now loading Air Man stage...\n Get your weapons ready...")
        print("A")