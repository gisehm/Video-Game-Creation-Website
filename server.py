from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "our_secret_key_:)!"

LESSONS = {
  1: {"title": "Step 1: SOFTWARE SETUP", "content": "Download Unity and Visual Studio Code.",
    "img1": "https://live.staticflickr.com/65535/55218872808_5db1e6bcbd.jpg", "img2": "https://live.staticflickr.com/65535/55217817002_04248170ea.jpg",
    "p1": "Before we jump in, make sure to create an account with and also download Unity, which is where we will be creating the actual video game. Along with Unity, also make sure to download Visual Studio Code, which is where we’ll be writing the code for the video game.",
    "p2": "For further instructions on this, there are many free tutorials to be found online about downloading both Unity and Visual Studio Code! If you’ve already completed these steps, feel free to press ‘NEXT’!"},
  2: {"title": "Step 2: CREATE A PROJECT", "content": "Create your 2D game!",
    "img1": "https://live.staticflickr.com/65535/55218872753_98de3ce1f5_b.jpg", "img2": "https://live.staticflickr.com/65535/55218715161_7262834cf9_c.jpg",
    "p1": "After downloading Unity and Visual Studio Code, open Unity and create your first project! When you first open the app, go to the ‘Projects’ section. Upon reaching ‘Projects’, press the ‘+ New Project’ button.",
    "p2": "To begin, let’s create a 2D game; feel free to name it whatever you prefer!",
    "p3": "After filling in the input, press the ‘+ Create project’ button to successfully create your first project!"},
  3: {"title": "Step 3: CONFIRM VS CODE USE", "content": "Ensure you're using VS Code!",
    "img1": "https://live.staticflickr.com/65535/55218969819_18fe474d77_c.jpg",
    "p1": "To ensure that you are using VS Code for the game scripts, do the following: ",
    "p2": "Windows: Go to Edit > Preferences. Mac: Go to Unity > Preferences.",
    "p3": "Then select ‘External Tools’ on the page that pops up. Ensure that your ‘External Script Editor’ is VS Code."},
  4: {"title": "Step 4: LEARNING THE COMPONENTS", "content": "Let’s get to know the environment!", 
    "img1": "https://live.staticflickr.com/65535/55218968639_3552734e07_z.jpg",
    "p1": "On the bottom, we can see the Project Window, which displays any and all assets that could potentially be included in a game.",
    "p2": "An asset is any file that is or can be used as a part of a game, including sprites, music, sound effects, and scripts.",
    "p3": "The Assets Folder is the folder in the Project Window that contains all assets that could be used in a Unity game."},
  6: {"title": "Step 5: ADDING ASSETS", "content": "Add assets to your game!", 
    "img1": "https://live.staticflickr.com/65535/55218715211_1011beb8d1_c.jpg", "img2": "https://live.staticflickr.com/65535/55218872738_b7f9767989_h.jpg?s=eyJpIjo1NTIxODg3MjczOCwiZSI6MTc3NjY3MTExMCwicyI6ImJlNmRhN2U2NWYyMWZkNDQ0YjcwOGQzZTU0MGEzYWIwYmNkZGZkMjQiLCJ2IjoxfQ",
    "p1": "In order to create a game, you will need assets, as discussed before. You can use whichever assets/asset package you like, but I will be using this free package, which you can download here from the Unity AssetStore!",
    "p2": "After downloading the package, go to ‘My Assets’ to find your assets and press ‘Open in Unity’ to add them to your project!"},
  7: {"title": "Step 6: ADDING ASSETS PT. 2", "content": "Add assets to your game!", 
    "img1": "https://live.staticflickr.com/65535/55218715131_e1549daa43_w.jpg", "img2": "https://live.staticflickr.com/65535/55217816937_ea167d1ecd_n.jpg",
    "p1": "After pressing this button, you will be brought to your project, where you must download and then import the package to actually see it within the Assets folder in your Project Window. When you reach this page, press ‘Import’ to successfully add your assets!",
    "p2": "After downloading and importing the package to your project, you should see it within your Assets folder, as shown on the left (SPUM)."},
  8: {"title": "Step 7: SETTING THE SCENE", "content": "Add GameObjects to your game!", 
    "img1": "https://live.staticflickr.com/65535/55219114155_b8b80ef5bc_c.jpg", "img2": "https://live.staticflickr.com/65535/55218872708_e6334cb0e2_n.jpg", "img3": "https://live.staticflickr.com/65535/55218968544_3b9fc4dda4.jpg",
    "p1": "Drag an asset from your Assets folder to the Scene Window. Rename it 'human'. The Scene Window enables the placement of all GameObjects that will be used in the game.",
    "p2": "On the right is the Inspector Window, which displays information about the currently selected GameObject, including its position and other components it has.",
    "p3": "A GameObject represents any object that can be placed directly in the Hierarchy or the Scene. On the left, we see the Hierarchy Window, which lists all GameObjects present in the scene."},
  10: {"title": "Step 8: USING THE ANIMATOR WINDOW", "content": "Use the animator window to set your animations!", 
    "img1": "https://live.staticflickr.com/65535/55218965348_f3580decdb.jpg", "img2": "https://live.staticflickr.com/65535/55218969639_f57ea2880e_w.jpg",
    "p1": "At this point, you have this character on screen, and if you press play, you may see some strange character animations popping up. To fix this, open the ‘Animator’ window, which can be seen at the top of the screen (Window > Animation > Animator).",
    "p2": "Press on ‘New Animation’ and go to the Inspector Window. Here, you can change the name to ‘Idle’ and change the Motion to ‘Astronaut_Idle’. The Astronaut should now stand still!"},
  11: {"title": "Step 9: USING THE ANIMATOR WINDOW PT. 2", "content": "Use the animator window to set your animations!", 
    "img1": "https://live.staticflickr.com/65535/55218968589_55c6fa2c0d_c.jpg", "img2": "https://live.staticflickr.com/65535/55218968514_4107db7a77_c.jpg", "img3": "https://live.staticflickr.com/65535/55218872663_6b0dcd96e8_c.jpg",
    "p1": "Drag the 'Astronaut_Jump' animation from the Project window to the Animator window.",
    "p2": "From here, go to the Parameters tab and create a 'Bool' object. Name it 'isJumping'.",
    "p3": "Make a transition leading from 'Idle' to 'Astronaut_Jump' and another transition leading from 'Astronaut_Jump' to 'Idle'."},
  12: {"title": "Step 10: PREPPING THE CHARACTER ANIMATION", "content": "Fix the character animation!", 
    "img1": "https://live.staticflickr.com/65535/55217818162_4500e43a29_z.jpg", "img2": "https://live.staticflickr.com/65535/55217818252_8c46ca31a2_n.jpg",
    "p1": "In the Inspector window of the arrow connecting 'Idle' to 'Astronaut_Jump', go to Conditions and press '+'. It should automatically show 'isJumping, true'.",
    "p2": "In the Inspector window of the arrow connecting 'Astronaut_Jump' to 'Idle', go to Conditions and press '+'. Change it to show 'isJumping, false'."},
  13: {"title": "Step 11: PREPPING THE CHARACTER ANIMATION PT. 2", "content": "Fix the character animation!", 
    "img1": "https://live.staticflickr.com/65535/55218968664_fa7660d6a9_w.jpg",
    "p1": "After this, you can go back to AstronautIdle. From here, press 'Add Component' and create a 'New script' named 'AstronautJump'.",
    "p2": "Also, ensure that it has an Animator where the Controller is AstronautIdle.",
    "p3": "Now, you can double-press the script ('AstronautJump') in order to access and begin editing it."},
  15: {"title": "Step 12: WRITING THE ANIMATION SCRIPT", "content": "Write the script to deploy the animation!", 
    "img1": "https://live.staticflickr.com/65535/55218969529_cdbd709ec3_c.jpg", "img2": "https://live.staticflickr.com/65535/55219114570_225ab7e01b_m.jpg", "img3": "https://live.staticflickr.com/65535/55217817387_639284417d_m.jpg",
    "p1": "This is what your script should look like! “void Start ()” will only run one time, when the game is first played. “void Update ()” will run over and over while the game is playing. When a line starts with //, it is a comment. Comments are like your “notes”. Writing comments will help others, and you, understand the code.",
    "p2": "When editing a script, if you made changes to a script but haven’t saved them yet, you will see a circle or * on the right side of the tab (as seen above)",
    "p3": "Once you’ve saved (command + S or Ctrl + S), this circle or * will be replaced by an x or disappear (as seen above)"},
  17: {"title": "Step 13: FINISH THE ANIMATION SCRIPT", "content": "Complete and save the script to deploy the animation!", 
    "img1": "https://live.staticflickr.com/65535/55219115110_bfff9d4915_m.jpg", "img2": "https://live.staticflickr.com/65535/55218716061_967576d2fe.jpg",
    "p1": "Put your cursor above void Start(){} and type: 'public Animator jump;'. Don’t forget the semicolon at the end of the line! If you forget, you will see a red squiggly line. That line means there’s an error in your code.",
    "p2": "Within void Update(){} write the code above. An if statement means “if ‘this’ is true, then do ‘that’”. Inside the ( ) is the condition, the trigger for the if statement. Inside the { } is the result, what happens when the condition is met.",
    "p3": "Input.GetKeyDown() lets the computer know that a key has been pressed down. KeyCode.__ is the specific key being pressed. Curly braces { } always show up in pairs; missing or misplacing them will cause errors. Make sure the if statement is inside the braces."},
  18: {"title": "Step 14: FINISH THE ANIMATION SCRIPT PT. 2", "content": "Complete and save the script to deploy the animation!", 
    "img3": "https://live.staticflickr.com/65535/55218716061_967576d2fe.jpg",
    "p1": "Input.GetKeyDown() lets the computer know that a key has been pressed down. KeyCode.__ is the specific key being pressed.",
    "p2": "Within void Update(){} write the following code: "},
  19: {"title": "Step 15: COMPLETE ANIMATION SCRIPT", "content": "Your code should look like this:", 
    "img1": "https://live.staticflickr.com/65535/55217817947_5197820229_c.jpg"},
  21: {"title": "Step 16: ERROR HANDLING", "content": "Fix possible errors!", 
    "img1": "https://live.staticflickr.com/65535/55218716056_ce121884ed_z.jpg", "img2": "https://live.staticflickr.com/65535/55219115100_76b7be8c6f.jpg",
    "p1": "Once you save your code and attempt to play your game, you may encounter an error with the use of “GetKeyDown”. This can be fixed by doing the following: Go to Edit > Project Settings > Player > Other Settings.",
    "p2": "From here, go to “Active Input Handling” and change it to “Both”. Your project will reload with this change, and afterwards, the error should go away."},
  22: {"title": "Step 17: FINALIZING THE ANIMATION", "content": "Add the final touches!", 
    "img1": "https://live.staticflickr.com/65535/55218873628_0d4d4889e0_z.jpg", "img2": "https://live.staticflickr.com/65535/55218969504_0f56357bba_n.jpg",
    "p1": "Upon completing the code and going back to Unity, go back to where your AstronautJump Script is, and you’ll notice a new slot with the name “Jump” has shown up. Press the circle to the right of it and press on AstronautIdle.",
    "p2": "You have now completed the code and set up to deploy your first animation. Now, if you click on the 'Play' button on the top of the screen and press the Spacebar, your astronaut should look as if they’re jumping! By pressing the 'Play' button that is at the top of the screen, you have officially entered the Game Window to see your game in action!",
    "p3": "CONGRATULATIONS! Press 'NEXT' to access the final quiz!"}
}

QUIZ = {
  1: {
    "img": "https://live.staticflickr.com/65535/55219115200_cfbecb3e67_c.jpg",
    "question": "What is normally found in the Assets folder?",
    "choices": ["Just the scripts/code for the game", "Any file that is or can be used as a part of a game", "Just the images for the game", "Images and audio"],
    "answer": "Any file that is or can be used as a part of a game"
  },
  2: {
    "img": "https://live.staticflickr.com/65535/55219114155_b8b80ef5bc_c.jpg",
    "question": "What are the four major parts of the Unity environment?",
    "choices": ["Asset Window, Game Window, Hierarchy Window, Inspector Window.", "Asset Window, Scene Window, Hierarchy Window, Information Window.", "Project Window, Game Window, Hierarchy Window, Inspector Window.", "Project Window, Scene Window, Hierarchy Window, Inspector Window."],
    "answer": "Project Window, Scene Window, Hierarchy Window, Inspector Window."
  },
  3: {
    "img": "https://live.staticflickr.com/65535/55219114155_b8b80ef5bc_c.jpg",
    "question": "How would you describe a GameObject?",
    "choices": ["It can be placed in the Hierarchy or Scene, and you can see its information in the Inspector Window.", "It can only be placed in the Scene, and you can see its information in the Hierarchy Window.", "It can only be placed in the Project Window, and you can see its information in the Scene Window.", "It can only be placed in the Hierarchy, and you can see its information in the Inspector Window."],
    "answer": "It can be placed in the Hierarchy or Scene, and you can see its information in the Inspector Window."
  },
  4: {
    "img": "https://live.staticflickr.com/65535/55218872663_6b0dcd96e8_c.jpg",
    "question": "What is the window used to manage the animations?",
    "choices": ["Animation Window", "Game Window", "Animator Window", "Layers Window"],
    "answer": "Animator Window"
  },
  5: {
    "img": "https://live.staticflickr.com/65535/55218872683_87606638da_c.jpg",
    "question": "What data type is used to tell if the character is jumping?",
    "choices": ["char", "bool", "float", "short"],
    "answer": "bool"
  },
  6: {
    "img": "https://live.staticflickr.com/65535/55218969529_cdbd709ec3_c.jpg",
    "question": "If you want an action to run more than once, you should place it in void Start()",
    "choices": ["True", "False"],
    "answer": "False"
  },
  7: {
    "img": "https://live.staticflickr.com/65535/55217817947_5197820229_c.jpg",
    "question": "Which of these if statements is invalid?",
    "choices": ["if (Input.GetKeyDown(KeyCode.D)){run.SetBool('isRunning', true);}", "if (Input.GetKeyDown(KeyCode.J));{jump.SetBool('isJumping', true);}", "if (Input.GetKeyDown(KeyCode.Space)){jump.SetBool('isJumping', false);}", "None of the above"],
    "answer": "if (Input.GetKeyDown(KeyCode.J));{jump.SetBool('isJumping', true);}"
  },
  8: {
    "img": "https://live.staticflickr.com/65535/55218969529_cdbd709ec3_c.jpg",
    "question": "What is the difference between void Start() and void Update()?",
    "choices": ["void Update() plays only once and void Start() plays over and over throughout the game", "void Start() plays only once and void Update() plays over and over throughout the game", "void Start() is ONLY for creating variables", "There is no difference"],
    "answer": "void Start() plays only once and void Update() plays over and over throughout the game"
  },
  9: {
    "img": "https://live.staticflickr.com/65535/55218716051_edcd274eed_w.jpg",
    "question": "What is the function of an ‘if’ statement?",
    "choices": ["A conditional which specifies that “if ‘this’ is true, then do ‘that’”", "A statement used to declare variables", "A conditional that constantly loops until it's true"],
    "answer": "A conditional which specifies that “if ‘this’ is true, then do ‘that’”"
  },
  10: {
    "img": "https://live.staticflickr.com/65535/55218969504_0f56357bba_n.jpg",
    "question": "What are the differences between the Scene Window and the Game Window (pictured above)?",
    "choices": ["You can fly around and zoom out the camera in the Game Window", "There is no difference", "The Scene Window displays what the player sees when actively playing", "The Scene Window is mostly used for editing the game while the Game Window is to test and view the game in action"],
    "answer": "The Scene Window is mostly used for editing the game while the Game Window is to test and view the game in action"
  },
  11: {
    "img": "https://live.staticflickr.com/65535/55227278988_175852a160.jpg",
    "question": "What is the name and function of this window?",
    "choices": ["Hierarchy Window which lists all GameObjects present in the scene", "Inspector Window which displays information about the currently selected GameObject", "Project Window which displays any and all assets that could potentially be included in a game", "Inspector Window which enables placement of all GameObjects that will be used in the game"],
    "answer": "Inspector Window which displays information about the currently selected GameObject"
  },
  12: {
    "img": "https://live.staticflickr.com/65535/55227360069_07532bf06c.jpg",
    "question": "What is the name and function of this window?",
    "choices": ["Hierarchy Window is to test and view the game in action", "Project Window which displays any and all assets that could potentially be included in a game", "Hierarchy Window which lists all GameObjects present in the scene", "Inspector Window which displays information about the currently selected GameObject"],
    "answer": "Hierarchy Window which lists all GameObjects present in the scene"
  }
}

QUIZSETS = {
  5: [1],
  9: [2, 3],
  14: [4, 5],
  16: [6],
  20: [7],
  23: [8, 9, 10, 11, 12]
}

user_data = {"answers": []}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/start", methods=["POST"])
def start():
  user_data["answers"] = []
  return redirect(url_for("learn", num=1))

@app.route("/learn/<int:num>")
def learn(num):
  if num in QUIZSETS:
    return redirect(url_for("quiz", curr=num, step=1))
  if num > 23:
    return redirect(url_for("results"))
  return render_template("learn.html", lesson=LESSONS[num], num=num)

@app.route("/quiz/<int:curr>/<int:step>", methods=["GET", "POST"])
def quiz(curr, step):
  Q_ids = QUIZSETS.get(curr, [])

  if step > len(Q_ids):
    return redirect(url_for("learn", num=curr+1))
  
  curr_Q_id = Q_ids[step - 1]

  if request.method == "POST":
    if "answers" not in session:
      session["answers"] = {}

    answer = request.form.get("answer")
    session["answers"][str(curr_Q_id)] = answer
    session.modified = True
    user_data["answers"].append(answer)
    return redirect(url_for("quiz", curr=curr, step=step+1))
    
  return render_template("quiz.html", q=QUIZ[curr_Q_id], curr=curr, step=step, num=curr_Q_id, total=len(QUIZ))

@app.route("/next/<int:curr>")
def next(curr):
  return redirect(url_for("learn", num=curr+1))

@app.route("/results")
def results():
  score = 0
  for i, ans in enumerate(user_data["answers"]):
    if ans == QUIZ[i+1]["answer"]:
      score += 1
  return render_template("results.html", score=score, total=len(QUIZ))

if __name__ == "__main__":
  app.run(debug=True)