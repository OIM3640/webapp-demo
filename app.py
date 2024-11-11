from flask import Flask, flash, redirect, render_template, request, url_for

from calculator import NoRealRootsError, quadratic

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a random string for security


@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    """Render a page that says hello to the user."""
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template("404.html")


# @app.route("/solve", methods=["GET", "POST"])
# def solve():
#     """
#     Render a form to solve a quadratic equation if the request method is GET. If the request method is POST, solve the equation and render the result.
#     """
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
    """Render a form to solve a quadratic equation."""
    return render_template("solver_form.html")


@app.post("/solve")
def solve_post():
    """Solve a quadratic equation and render the result."""
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
    """Render a page with a list of grades."""
    students = [
        {"name": "John", "grade": 80},
        {"name": "Paul", "grade": 90},
        {"name": "George", "grade": 85},
        {"name": "Ringo", "grade": 95},
    ]
    return render_template("grades.html", grades=students)


if __name__ == "__main__":
    app.run(debug=True)
