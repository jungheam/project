from apps.crud.forms import UserForm
from apps.app import db
from apps.crud.models import User
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
@login_required
def sql():
    db.session.query(User).all()
    return "콘솔 로그를 확인해 주세요"

@crud.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    form = UserForm()
    
    if form.validate_on_submit():
        user = User(
            toyname=form.toyname.data,
            age=form.age.data,
            components=form.components.data,
            explain=form.explain.data,
            rental =form.rental.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)

@crud.route("/users/<user_id>", methods=["GET", "POST" ])
@login_required
def edit_user(user_id):
    form = UserForm()

    user = User.query.filter_by(number=user_id).first()

    if form.validate_on_submit():
        user.toyname = form.toyname.data
        user.age = form.age.data
        user.components = form.components.data
        user.explain = form.explain.data
        user.rental = form.rental.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
          
    return render_template("crud/edit.html", user=user, form=form)
    


@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user=User.query.filter_by(number=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))

