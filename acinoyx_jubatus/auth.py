from flask import Blueprint, render_template, request, flash 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET' 'POST'])
def login():
    return render_template('login.html')

@auth.route('/', methods=['GET' 'POST'])
def logout():
    return '<p>Logout</p>'

@auth.route('/registro', methods=['GET' 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form.get('correo')
        nombreCompleto = request.form.get('nombreCompleto')
        edad = request.form.get('edad')
        contrasena = request.form.get('contrasena')

        if len(nombreCompleto) < 2:
            flash('Su nombre debe tener mas de una letra.', category='error')
            pass
        elif len(correo) < 4:
            flash('Su correo debe tener mas de 3 caracteres.', category='error')
            pass
        elif (len(edad) < 18) and (len(edad) > 100):
            flash('Debe ser de 18 años o menor que 100 años', category='error')
            pass
        elif len(contrasena) < 8:
            flash('Password must be at least 7', category='error')
            pass
    return render_template('registro.html')
    




