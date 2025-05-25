from flask import Flask, request, jsonify
from controller.time_controller import TimeController

app = Flask(__name__)
controller = TimeController()

@app.route("/times", methods=["GET"])
def listar_times():
    print("[GET] /times - Requisição recebida")
    times = controller.listar_times()
    print(f"[GET] Retornando {len(times)} time(s)")
    return jsonify([t.to_dict() for t in times]), 200

@app.route("/times", methods=["POST"])
def criar_time():
    data = request.json
    print("[POST] /times - Dados recebidos:", data)
    controller.criar_time(data["id"], data["nome"], data["cidade"], data["dataFundacao"], data["tecnico"])
    print("[POST] Time criado com sucesso")
    return jsonify({"mensagem": "Time criado"}), 201

@app.route("/times/<int:id>", methods=["PUT"])
def atualizar_time(id):
    data = request.json
    print(f"[PUT] /times/{id} - Dados recebidos:", data)
    controller.atualizar_time(id, data["nome"], data["cidade"], data["dataFundacao"], data["tecnico"])
    print(f"[PUT] Time {id} atualizado com sucesso")
    return jsonify({"mensagem": "Time atualizado"}), 200

@app.route("/times/<int:id>", methods=["DELETE"])
def deletar_time(id):
    print(f"[DELETE] /times/{id} - Requisição recebida")
    controller.deletar_time(id)
    print(f"[DELETE] Time {id} deletado com sucesso")
    return jsonify({"mensagem": "Time deletado"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=30000, host="0.0.0.0")
