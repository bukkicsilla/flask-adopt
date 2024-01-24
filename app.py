from flask import Flask, render_template, redirect, flash, url_for
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "Animals are adorable."
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://klkleurq:bjcINq77AmyQQWxmWjg0P3Y4UNcSbjb9@drona.db.elephantsql.com/klkleurq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
#db.create_all()
with app.app_context():
  db.create_all()

#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    """List of all pets."""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a new pet."""
    form = AddPetForm()
    if form.validate_on_submit():
        #name = form.name.data
        #species =  form.species.data
        #photo_url = form.photo_url.data
        #age = form.age.data
        #notes = form.notes.data
        #pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        #getting the data as a dicctionary
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        print("PET", data)
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} added.")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('home'))

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
