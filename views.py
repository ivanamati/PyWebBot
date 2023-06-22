from flask import Blueprint, render_template, request, flash, redirect, url_for,session, jsonify
from digital_asisstent import get_the_answer

views = Blueprint(__name__,"views")


####################################################
# ROUTES za new index.html
@views.route("/start")
def index():
    # ovime sam dobila da se sve prethodne flash poruke maknu s prozora
    # prilikom povratka na pocetni prozor za unos
    message = session.pop('_flashes', None)

    # flash funkcija omogućuje generiranje poruka koje se mogu prikazati korisnicima kada se izvrši određena akcija, 
    # poput slanja obrasca ili prijave u sustav. 
    flash("Hi, i'm your personal digital asisstent.\n how may i help you?")
    return render_template("index.html", name="Ivana",message=message)


@views.route("/greet", methods=["POST","GET"])
def greet():
    # ovime dohvaćamo input usera
    # unos varijable u zagradama treba odgovarati 
    # name inputu u html dokumentu (<input type="text" name="name_input">)
    # -> request.form['name_input']
    input_from_user = request.form['pitanje']

    # flash pozdravna poruka 
    flash("this is your input "+ str(input_from_user))

    digital_asisstant_answer =  get_the_answer(str(input_from_user))

    return render_template("answer.html",input_text= input_from_user, odgovor = digital_asisstant_answer)



####################################################
# ROUTES za prosli index.html
# @views.route("/")
# def home():
#     return render_template("index.html", name = "PyRats")

# ovako pristupamo ako predamo u url username
# @views.route("/profile/<username>")
# def profile(username):
#     return render_template("index.html", name=username)

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    #return render_template("index.html", name=name)
    return render_template("profile.html")

# how to return json
@views.route("/json")
def get_json():
    return jsonify({'name':'ivana', 'age':38})

# ovako pristupimo jsonu pomocu route
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# redirect to a home page
@views.route("/go-to-home")
def go_to_home():
    # ovdje u zagradi nakon views. pisemo ime funkcije na koju stranicu zelimo otici
    return redirect(url_for("views.home"))

# redirect to a json page
@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))

