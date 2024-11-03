from flask import Flask, flash, redirect, render_template, request, url_for

from calculator import NoRealRootsError, quadratic

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a random string for security


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# @app.route("/solve", methods=["GET", "POST"])
# def solve():
#     if request.method == "POST":
#         a = float(request.form["a"])
#         b = float(request.form["b"])
#         c = float(request.form["c"])
#         roots = quadratic(a, b, c)

#         if roots:
#             return render_template(
#                 "solver_result.html",
#                 a=a,
#                 b=b,
#                 c=c,
#                 root_1=roots[0],
#                 root_2=roots[1],
#             )
#         else:
#             return render_template("solver_form.html")
#     return render_template("solver_form.html")


@app.get("/solve")
def solve_get():
    return render_template("solver_form.html")


@app.post("/solve")
def solve_post():
    try:
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
        c = float(request.form.get("c"))
    except ValueError:
        flash("Please enter valid numbers for coefficients.", "error")
        return redirect(url_for("solve_get"))

    try:
        roots = quadratic(a, b, c)
        return render_template(
            "solver_result.html",
            a=a,
            b=b,
            c=c,
            root_1=roots[0],
            root_2=roots[1],
        )
    except NoRealRootsError:
        flash("This equation does not have real number solution.", "error")
        return redirect(url_for("solve_get"))
    except ValueError as e:
        flash(str(e), "error")
        return redirect(url_for("solve_get"))


@app.route("/grade")
def show_grades():
    persons = [
        {"name": "John", "grade": 80},
        {"name": "Paul", "grade": 90},
        {"name": "George", "grade": 85},
        {"name": "Ringo", "grade": 95},
    ]
    return render_template("grades.html", grades=persons)


if __name__ == "__main__":
    app.run(debug=True)
