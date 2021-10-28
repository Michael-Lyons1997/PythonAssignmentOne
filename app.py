from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "homepage.html",
        title="Welcome!",
        heading="This is my homepage, please select the option to use",
    )


@app.get("/showpersonalpage")
def displayPersonal():
    return render_template(
        "personalPage.html", title="Personal Page", heading="This is a page about me",
    )


@app.get("/showCVpage")
def displayCV():
    return render_template("CV.html", title="CV Page", heading="This is my CV",)


@app.get("/showtechnologiespage")
def displayTechnologies():
    return render_template(
        "computingTechnologies.html",
        title="Computing Technology",
        heading="Please fill in this form",
    )


@app.get("/showTechSubpage1")
def displaySub1():
    return render_template(
        "computingTechnologiesSubpageOne.html",
        title="CV Page",
        heading="This is my CV",
    )


@app.get("/showTechSubpage2")
def displaySub2():
    return render_template(
        "computingTechnologiesSubpageTwo.html",
        title="CV Page",
        heading="This is my CV",
    )


@app.get("/showTechSubpage3")
def displaySub3():
    return render_template(
        "computingTechnologiesSubpageThree.html",
        title="CV Page",
        heading="This is my CV",
    )


@app.get("/showinterestspage")
def displayinterests():
    return render_template(
        "interests.html",
        title="Interests",
        heading="These are my non-computing related interests",
    )


@app.post("/processform")
def showPersonal():
    theEmail = request.form["email"]
    theMessage = request.form["message"]

    with open("comments.txt", "a") as f:
        print(f"{theEmail},{theMessage}", file=f)
    return render_template(
        "homepage.html",
        title="Welcome!",
        heading="This is my homepage, please select the option to use",
    )


if __name__ == "__main__":
    app.run(debug=True)
