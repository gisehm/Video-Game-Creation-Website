from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

LESSONS = {
    1: {"title": "Step 1: Software Setup", "content": "Download Unity and Visual Studio Code."},
    2: {"title": "Step 2: Create Project", "content": "Create a 2D project in Unity."},
    3: {"title": "Step 3: Add Assets", "content": "Import assets into your game environment."},
    4: {"title": "Step 4: Animator Window", "content": "Use the Animator window to control animations."}
}

QUIZ = {
    1: {
        "question": "What is an asset?",
        "choices": ["Only code", "Any file used in a game", "Only images"],
        "answer": "Any file used in a game"
    },
    2: {
        "question": "Which window manages animations?",
        "choices": ["Scene Window", "Animator Window", "Project Window"],
        "answer": "Animator Window"
    }
}

user_data = {
    "answers": []
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start", methods=["POST"])
def start():
    user_data["answers"] = []
    return redirect(url_for("learn", num=1))

@app.route("/learn/<int:num>")
def learn(num):
    lesson = LESSONS.get(num)

    if not lesson:
        return redirect(url_for("quiz", num=1))

    return render_template("learn.html", lesson=lesson, num=num)

@app.route("/quiz/<int:num>", methods=["GET", "POST"])
def quiz(num):
    if request.method == "POST":
        user_data["answers"].append(request.form.get("answer"))
        return redirect(url_for("quiz", num=num + 1))

    if num not in QUIZ:
        return redirect(url_for("results"))

    return render_template("quiz.html", q=QUIZ[num], num=num, total=len(QUIZ))

@app.route("/results")
def results():
    score = 0

    for i, ans in enumerate(user_data["answers"]):
        if ans == QUIZ[i + 1]["answer"]:
            score += 1

    return render_template("results.html", score=score, total=len(QUIZ))

if __name__ == "__main__":
    app.run(debug=True)