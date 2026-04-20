from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

LESSONS = {
    1: {"title": "Step 1: Software Setup", "content": "Download Unity and VS Code."},
    2: {"title": "Step 2: Create Project", "content": "Create a 2D Unity project."},
    3: {"title": "Step 3: Add Assets", "content": "Import assets into Unity."}
}

QUIZ = {
    1: {"question": "What is an asset?", "choices": ["Only code", "Any file used in a game", "Only images"], "answer": "Any file used in a game"},
    2: {"question": "Which window organizes files?", "choices": ["Scene", "Project", "Game"], "answer": "Project"},
    3: {"question": "What controls animations?", "choices": ["Animator", "Hierarchy", "Inspector"], "answer": "Animator"}
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
    if num not in LESSONS:
        return redirect(url_for("quiz", num=1))
    return render_template("learn.html", lesson=LESSONS[num], num=num)

@app.route("/quiz/<int:num>", methods=["GET","POST"])
def quiz(num):
    if request.method == "POST":
        user_data["answers"].append(request.form.get("answer"))
        return redirect(url_for("quiz", num=num+1))

    if num not in QUIZ:
        return redirect(url_for("results"))

    return render_template("quiz.html", q=QUIZ[num], num=num, total=len(QUIZ))

@app.route("/results")
def results():
    score = 0
    for i, ans in enumerate(user_data["answers"]):
        if ans == QUIZ[i+1]["answer"]:
            score += 1
    return render_template("results.html", score=score, total=len(QUIZ))

if __name__ == "__main__":
    app.run(debug=True)