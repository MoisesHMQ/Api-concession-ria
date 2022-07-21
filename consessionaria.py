from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

comprador = []

@app.route("/cadastrar/compradores", methods=['POST'])
def cadastrar():
    cadastrar_compradores = request.json 
    for user in comprador:
        if user["email"] == cadastrar_compradores["email"]:  
            return {"Algo deu errado.":"Esse usuario ja existe."}
    cadastrar_compradores = {
        "id": str(uuid.uuid4()),
        "email": cadastrar_compradores["email"],
        "senha": cadastrar_compradores["senha"]
        }
    comprador.append(cadastrar_compradores)
    return jsonify(cadastrar_compradores)

@app.route("/login", methods=['POST'])
def logar():
    login = request.json
    for login in comprador:
        if login["email"] == login["email"] and login["senha"] == login["senha"]:
            return{"Status":"Logado."}
        else:
            return{"Status":"Usuario ou Senha Incorretos."}

@app.route("/todos/usuarios")
def usuarios():
    return jsonify(comprador)

@app.route("/excluir/usuarios", methods=['POST'])
def excluir_usuarios():
    excluir = request.json
    print(comprador)
    for dados in usuarios:
        if dados["id"] == excluir["id"]:
            comprador.remove(dados)
            return excluir

moto160 = []

@app.route("/160", methods=['POST'])
def moto():
    marca = request.json
    for modelo1 in moto160:
        if modelo1["moto"] == marca["moto"] and modelo1["marca"] == marca["marca"]:
            return {"status": "veiculo já cadastrado."}
    marca = {
        "chassi": str(uuid.uuid4()),
        "moto": marca["moto"],
        "cor":marca["cor"],
        "marca":marca["marca"]
        }
    moto160.append(marca)
    return jsonify(marca)

@app.route("/excluir/160", methods=['POST'])
def excluir_moto():
    delete = request.json
    print(moto160)
    for dell in moto160:
        if dell["chassi"] == delete["chassi"]:
            moto160.remove(dell)
            return delete

moto250 = []

@app.route("/250", methods=['POST'])
def motores():
    marca1 = request.json
    for modelo2 in moto250:
        if modelo2["moto"] == marca1["moto"] and modelo2["marca"] == marca1["marca"]:
            return {"status": "veiculo já cadastrado."}
    marca1 = {
        "chassi": str(uuid.uuid4()),
        "moto": marca1["moto"],
        "cor":marca1["cor"],
        "marca":marca1["marca"]
        }
    moto250.append(marca1)
    return jsonify(marca1)

@app.route("/excluir/250", methods=['POST'])
def excluir250():
    delete = request.json
    print(moto250)
    for dell in moto250:
        if dell["chassi"] == delete["chassi"]:
            moto250.remove(dell)
            return delete

moto300 = []

@app.route("/300", methods=['POST'])
def motores300():
    marca2 = request.json
    for modelo3 in moto300:
        if modelo3["moto"] == marca2["moto"] and modelo3["marca"] == marca2["marca"]:
            return {"status": "veiculo já cadastrado."}
    marca2= {
        "chassi": str(uuid.uuid4()),
        "moto": marca2["moto"],
        "cor":marca2["cor"],
        "marca":marca2["marca"]
        }
    moto300.append(marca2)
    return jsonify(marca2)

@app.route("/excluir/300", methods=['POST'])
def excluir300():
    delete = request.json
    print(moto300)
    for dell in moto300:
        if dell["chassi"] == delete["chassi"]:
            moto300.remove(dell)
            return delete


moto600 = []

@app.route("/600", methods=['POST'])
def motores600():
    marca3 = request.json
    for modelo4 in moto600:
        if modelo4["moto"] == marca3["moto"] and modelo4["marca"] == marca3["marca"]:
            return {"status": "veiculo já cadastrado."}
    marca3= {
        "chassi": str(uuid.uuid4()),
        "moto": marca3["moto"],
        "cor":marca3["cor"],
        "marca":marca3["marca"]
        }
    moto600.append(marca3)
    return jsonify(marca3)


@app.route("/excluir/600", methods=['POST'])
def excluir600():
    delete = request.json
    print(moto600)
    for dell in moto600:
        if dell["chassi"] == delete["chassi"]:
            moto600.remove(dell)
            return delete


moto1000 = []

@app.route("/1000", methods=['POST'])
def motores1000():
    marca4 = request.json
    for modelo5 in moto1000:
        if modelo5["moto"] == marca4["moto"] and modelo5["marca"] == marca4["marca"]:
            return {"status": "veiculo já cadastrado."}
    marca4= {
        "chassi": str(uuid.uuid4()),
        "moto": marca4["moto"],
        "cor":marca4["cor"],
        "marca":marca4["marca"]
        }
    moto1000.append(marca4)
    return jsonify(marca4)

@app.route("/excluir/1000", methods=['POST'])
def excluir1000():
    delete = request.json
    print(moto1000)
    for dell in moto1000:
        if dell["chassi"] == delete["chassi"]:
            moto1000.remove(dell)
            return delete

@app.route("/consecionaria")
def loja():
    return jsonify(moto160, moto250, moto300, moto600, moto1000)

app.run()

