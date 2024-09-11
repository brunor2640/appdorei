from flask import Flask

app = Flask (__name__)


#Criando a roda para um novo cliente
@app.route('/novocliente')
def criar_cliente():
    return("Estilo do Rei")

app.run(debug=True)


#Criando a roda para um novo agendamento
@app.route('/novoagendamento')
def criar_agendamento():
    return("Estilo do Rei")

app.run(debug=True)

#Criando a roda para um novo servico
@app.route("/novoservico")
def criar_serivo():
    return("Estilo do Rei")
app.run(debug=True)

#Criando a roda para a tela de login
@app.route("/login")
def index():
    return("Estilo do Rei")
app.run(debug=True)

@app.route("/logout")
def logout():
    return("Estilo do Rei")

app.run(debug=True)