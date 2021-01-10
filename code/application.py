import os
import languages

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///proximalingua.db")


survey_conservative = 0
survey_difficult = 0
survey_difference = 0
survey_logographic = 0
survey_popularity_us = 0
survey_popularity_world = 0
survey_analytic = 0
survey_shocking = 0
survey_diverse = 0
survey_efficient = 0

user_languages = {}


@app.route("/")
@login_required
def index():
    """Give an introduction"""

    return render_template("index.html")


number_of_languages = 0
@app.route("/number", methods=["GET", "POST"])
@login_required
def number():
    """Ask the user for the number of languages they speak"""

    if request.method == "POST":
        # Get the number of languages the user speaks
        global number_of_languages
        number_of_languages = int(request.form.get("number_of_languages"))

        if number_of_languages > 0:
            # If user speaks foreign languages, redirect to input page
            return redirect("/insert")

        else:
            # If they don't, start survey
            return redirect("/conservative")

    return render_template("number.html")


@app.route("/insert", methods=["GET", "POST"])
@login_required
def insert():
    """Input the languages"""

    if request.method == "POST":
        global user_languages

        for i in range(number_of_languages):
            # Add user inputs to dictionary of languages they speak
            user_languages[i] = request.form.get("language" + str(i))

        return redirect("/conservative")

    return render_template("insert.html", number=number_of_languages)


@app.route("/conservative", methods=["GET", "POST"])
@login_required
def conservative():
    """Questions for conservative metric"""

    if request.method == "POST":
        # Update survey conservative metric
        global survey_conservative
        survey_conservative = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/difficult")

    return render_template("conservative.html")


@app.route("/difficult", methods=["GET", "POST"])
@login_required
def difficult():
    """Questions for difficult metric"""

    if request.method == "POST":
        # Update survey difficult metric
        global survey_difficult
        survey_difficult = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/difference")

    return render_template("difficult.html")


@app.route("/difference", methods=["GET", "POST"])
@login_required
def different():
    """Questions for difference metric"""

    if request.method == "POST":
        # Update survey difference metric
        global survey_difference
        survey_difference = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/logographic")

    return render_template("difference.html")


@app.route("/logographic", methods=["GET", "POST"])
@login_required
def logographic():
    """Questions for logographic metric"""

    if request.method == "POST":
        # Update survey logographic metric
        global survey_logographic
        survey_logographic = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/popularus")

    return render_template("logographic.html")


@app.route("/popularus", methods=["GET", "POST"])
@login_required
def popularus():
    """Questions for popularity US metric"""

    if request.method == "POST":
        # Update survey popularity US metric
        global survey_popularity_us
        survey_popularity_us = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/popularworld")

    return render_template("popular_us.html")


@app.route("/popularworld", methods=["GET", "POST"])
@login_required
def popularworld():
    """Questions for popularity world metric"""

    if request.method == "POST":
        # Update survey popularity world metric
        global survey_popularity_world
        survey_popularity_world = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/analytic")

    return render_template("popular_world.html")


@app.route("/analytic", methods=["GET", "POST"])
@login_required
def analytic():
    """Questions for analytic metric"""

    if request.method == "POST":
        # Update survey analytic metric
        global survey_analytic
        survey_analytic = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/shocking")

    return render_template("analytic.html")


@app.route("/shocking", methods=["GET", "POST"])
@login_required
def shock():
    """Questions for shocking metric"""

    if request.method == "POST":
        # Update survey shocking metric
        global survey_shock
        survey_shock = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/diverse")

    return render_template("shocking.html")


@app.route("/diverse", methods=["GET", "POST"])
@login_required
def diverse():
    """Questions for diverse metric"""

    if request.method == "POST":
        # Update survey diverse metric
        global survey_diverse
        survey_diverse = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/efficient")

    return render_template("diverse.html")


@app.route("/efficient", methods=["GET", "POST"])
@login_required
def efficient():
    """Questions for efficient metric"""

    if request.method == "POST":
        # Update survey efficient metric
        global survey_efficient
        survey_efficient = (int(request.form.get("radio1")) + int(request.form.get("radio2")) + int(request.form.get("radio3")) + int(request.form.get("radio4")) + int(request.form.get("radio5"))) / 5.0

        # Advance to next metric
        return redirect("/results")

    return render_template("efficient.html")


# Capitalize first letter of every dictionary key
def _uppercase_for_dict_keys(lower_dict):
    upper_dict = {}
    for k, v in lower_dict.items():
        if isinstance(v, dict):
            v = _uppercase_for_dict_keys(v)
        upper_dict[k.capitalize()] = v
    return upper_dict


@app.route("/results", methods=["GET", "POST"])
@login_required
def results():
    """Show best languages for the user to learn next"""

    language_names = ["spanish", "chinese", "tagalog", "vietnamese", "arabic", "french", "korean", "russian", "german", "haitian", "hindi", "portuguese", "italian", "polish", "japanese", "persian", "gujarati", "telugu", "bengali", "urdu"]
    metrics = ["conservative", "difficult", "difference", "logographic", "popularity_us", "popularity_world", "analytic", "shocking", "diverse", "efficient"]
    survey_metrics = [survey_conservative, survey_difficult, survey_difference, survey_logographic, survey_popularity_us, survey_popularity_world, survey_analytic, survey_shocking, survey_diverse, survey_efficient]
    difference = {
        "spanish": 0,
        "chinese": 0,
        "tagalog": 0,
        "vietnamese": 0,
        "arabic": 0,
        "french": 0,
        "korean": 0,
        "russian": 0,
        "german": 0,
        "haitian": 0,
        "hindi": 0,
        "portuguese": 0,
        "italian": 0,
        "polish": 0,
        "japanese": 0,
        "persian": 0,
        "gujarati": 0,
        "telugu": 0,
        "bengali": 0,
        "urdu": 0
    }

    # Compare survey responses to each language
    for i in range(20):
        for j in range(10):
            difference_metric = abs(survey_metrics[j] - getattr(languages, language_names[i])[metrics[j]])
            difference[language_names[i]] += difference_metric

    # Compare previously learned langauges to the others
    if number_of_languages > 0:
        for i in range(number_of_languages):
            for j in range(20):
                for k in range (10):
                    difference_user = abs(getattr(languages, user_languages[i])[metrics[k]] - getattr(languages, language_names[j])[metrics[k]])
                    difference[language_names[j]] += difference_user / 10.0

    # Delete languages the user has already learned
    for i in range(number_of_languages):
        del difference[user_languages[i]]
        language_names.remove(user_languages[i])

    # Sort dictionary by the difference
    difference = dict(sorted(difference.items(), key=lambda item: item[1]))

    # Make the keys uppercase for display on Results page
    difference = _uppercase_for_dict_keys(difference)

    # Display results
    return render_template("results.html", difference=difference)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    else:

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("MISSING USERNAME", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("MISSING PASSWORD", 400)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("MISSING CONFIRMATION PASSWORD", 400)

        else:

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

            # Ensure username does not already exist
            if len(rows) > 0:
                return apology("USERNAME ALREADY EXISTS", 400)

            # Ensure password and confirmation of password match
            elif request.form.get("password") != request.form.get("confirmation"):
                return apology("PASSWORDS DON'T MATCH", 400)

            else:

                # Hash password for security
                password_hash = generate_password_hash(request.form.get("password"))

                # Store user's username and password hash in the users table
                db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), password_hash)

                # I REPEAT THIS HERE. SHOULD I BE ABLE TO WRITE IT ONLY ONCE?
                # Query database for username
                rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

                # Remember which user has logged in
                session["user_id"] = rows[0]["id"]

                # Redirect user to home page
                return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)