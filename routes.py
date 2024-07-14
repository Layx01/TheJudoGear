from flask import Flask, render_template, redirect, url_for, flash
from extensions import create_app, db
from forms import SignUpForm, LogInForm
from models import User
from flask_login import login_user, logout_user
from flask_wtf.csrf import CSRFProtect

app = create_app()
csrf = CSRFProtect(app)

app = create_app()

products_top_home = [
    {
        "image": "static/images/mizuno.png",
        "name": "Mizuno Judogi",
        "text": "International Judo Federation approved",
        "price": "80$",
        "id": "0"
    },
    {
        "image": "static/images/adidas.png",
        "name": "Adidas Judogi",
        "text": "International Judo Federation approved",
        "price": "170$",
        "id": "1"
    },
    {
        "image": "static/images/greenhill.png",
        "name": "Green Hill Judogi",
        "text": "International Judo Federation approved",
        "price": "120$",
        "id": "2"
    }
]
products_top = [
    {
        "image": "images/mizuno.png",
        "name": "Mizuno Judogi",
        "text": "International Judo Federation approved",
        "price": "80$",
        "id": "0"
    },
    {
        "image": "images/adidas.png",
        "name": "Adidas Judogi",
        "text": "International Judo Federation approved",
        "price": "170$",
        "id": "1"
    },
    {
        "image": "images/greenhill.png",
        "name": "Green Hill Judogi",
        "text": "International Judo Federation approved",
        "price": "120$",
        "id": "2"
    }
]

products_bottom = [
    {
        "image": "static/images/mizuno/product-blue.png",
        "name": "Mizuno belt",
        "text": "International Judo Federation approved",
        "price": "15$",
        "id": "0"
    },
    {
        "image": "static/images/adidas/product-black.png",
        "name": "Adidas belt",
        "text": "International Judo Federation approved",
        "price": "25$",
        "id": "1"
    },
    {
        "image": "static/images/kusakura/product-white.png",
        "name": "KuSakura belt",
        "text": "International Judo Federation approved",
        "price": "30$",
        "id": "2"
    }
]

@app.route("/")
def home():
    return render_template("index.html", products_bottom=products_bottom, products_top_home=products_top_home)


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("This email is already registered.", "danger")
            print("Email already registered")  # Debugging line
            return render_template("register.html", form=form)

        if form.password.data != form.confirm_password.data:
            flash("Passwords do not match.", "danger")
            print("Passwords do not match")  # Debugging line
            return render_template("register.html", form=form)

        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        role="user")
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('home'))
    
    return render_template("register.html", form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect("/")

@app.route("/product/<int:product_id>")
def product(product_id):
    if product_id >= 0 and product_id < len(products_top):
        product = products_top[product_id]
        return render_template("product_kimono.html", product=product)
    else:
        return render_template("error.html")

@app.route("/mizuno")
def mizuno():
    return render_template("mizuno_belts.html")

@app.route("/adidas")
def adidas():
    return render_template("adidas_belts.html")

@app.route("/kusakura")
def kusakura():
    return render_template("kusakura_belts.html")


