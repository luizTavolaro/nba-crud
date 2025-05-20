from flask import Flask, request, jsonify
from controller.time_controller import TimeController

app = Flask(__name__)
controller = TimeController()

@app.route("/times", methods=["GET"])
def listar_times():
    times = controller.listar_times()
    return jsonify([t.to_dict() for t in times]), 200

@app.route("/times", methods=["POST"])
def criar_time():
    data = request.json
    controller.criar_time(data["id"], data["nome"], data["cidade"], data["dataFundacao"], data["tecnico"])
    return jsonify({"mensagem": "Time criado"}), 201

@app.route("/times/<int:id>", methods=["PUT"])
def atualizar_time(id):
    data = request.json
    controller.atualizar_time(id, data["nome"], data["cidade"], data["dataFundacao"], data["tecnico"])
    return jsonify({"mensagem": "Time atualizado"}), 200

@app.route("/times/<int:id>", methods=["DELETE"])
def deletar_time(id):
    controller.deletar_time(id)
    return jsonify({"mensagem": "Time deletado"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)