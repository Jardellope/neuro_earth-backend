from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API do Neuro Earth está no ar 🚀",
        "status": "online"
    })

@app.route("/visao")
def visao():
    return jsonify({
        "missao": "Transformar o futuro com tecnologia e sustentabilidade.",
        "objetivo": "Criar soluções inovadoras que conectam pessoas e o planeta."
    })

@app.route("/clima")
def clima():
    return jsonify({
        "alerta": "Monitorando dados climáticos em tempo real 🌍",
        "dados": {
            "temperatura": "25°C",
            "umidade": "60%",
            "qualidade_do_ar": "Boa"
        }
    })

@app.route("/impacto")
def impacto():
    return jsonify({
        "alerta": "Avaliando impacto ambiental 🌱",
        "dados": {
            "emissao_co2": "12 toneladas/dia",
            "economia_agua": "35 litros/dia",
            "energia_renovavel": "75%"
        }
    })

@app.route("/sustentabilidade")
def sustentabilidade():
    return jsonify({
        "alerta": "Projetos sustentáveis ativos ♻️",
        "projetos": [
            {"nome": "Energia Solar", "status": "Ativo"},
            {"nome": "Reciclagem Inteligente", "status": "Piloto"},
            {"nome": "Reflorestamento Urbano", "status": "Planejado"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)