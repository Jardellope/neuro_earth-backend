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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
