from flask import render_template, request
import requests
from app import app
from .forms import LoginForm

@app.route('/')
def hello():
   return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    return f'Hello! {name}'

@app.route('/login', methods = ['GET','POST'])
def login():
    loginForm = LoginForm()
    if request.method == 'POST' and loginForm.validate_on_submit():
        email = loginForm.email.data
        password = loginForm.password.data 
        return f'{email} {password}'
    return render_template('login.html', form = 'loginForm')

def pokemon_info(my_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{my_pokemon}'

    response = requests.get(url)

    if response.ok:
        data = response.json()
        poke_dict = {
        'name' :  data['name'],
        'id' : data['id'], 
        'ability' : data['abilities'][0]['ability']['name'],
        'sprite': data['sprites']['front_default']
        }
    print(poke_dict)
    return poke_dict
       
print(pokemon_info(66))

@app.route('/pokemon', methods = ['GET','POST'])
def pokemon():
    if request.method == 'POST':
        pokemon_name_id = request.form.get('pokemon_name_id')
        #print(pokemon_info(pokemon_name_id))
        return pokemon_info(pokemon_name_id) #f'Searched for {pokemon_name_id}'
    return render_template('pokemon.html')




