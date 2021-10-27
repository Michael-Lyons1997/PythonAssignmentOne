from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("homepage.html", title="Welcome!", heading="This is my homepage, please select the option to use",)



@app.get("/showpersonalpage")
def displayPersonal():
    """
        Retrieve the form.html file from the hard drive, and send it to the browser
    """
    return render_template("personalPage.html", title="Personal Page", heading="This is a page about me",)

@app.get("/showCVpage")
def displayCV():
    """
        Retrieve the form.html file from the hard drive, and send it to the browser
    """
    return render_template("CV.html", title="CV Page", heading="This is my CV",)

@app.get("/showtechnologiespage")
def displayTechnologies():
    """
        Retrieve the form.html file from the hard drive, and send it to the browser
    """
    return render_template("computingTechnologies.html", title="Computing Technology", heading="Please fill in this form",)

@app.get("/showinterestspage")
def displayinterests():
    """
        Retrieve the form.html file from the hard drive, and send it to the browser
    """
    return render_template("interests.html", title="Interests", heading="These are my non-computing related interests",)

@app.post("/processform")
def showPersonal():
    """
        retrieve the data from the html form, then save it to a disk file, then respond to the waiting browser.

        the following are expected: first, last, DOB
    """
    theEmail = request.form["email"]
    theMessage = request.form["message"]

    with open("comments.txt", "a") as f:
        print(f"{theEmail},{theMessage}", file=f)
    return render_template("homepage.html", title="Welcome!", heading="This is my homepage, please select the option to use",)


if __name__ == "__main__":
    app.run(debug=True)
