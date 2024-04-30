from apps.app import db
from apps.auth.forms import SignUpForm
from apps.crud.models import User
from flask import Blueprint, render_template,url_for, redirect, request
from flask_login import login_user


auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            toyname=form.toyname.data,
            age=form.age.data,
            type=form.type.data,
            components=form.components.data,
            explain=form.explain.data,
            rental =form.rental.data,
        )
   

        db.session.add(user)
        db.session.commit()
        login_user(user) 
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("crud.users")
        return redirect(next_)
    return render_template("auth/signup.html", form=form)


