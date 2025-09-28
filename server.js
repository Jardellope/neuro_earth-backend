const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const PORT = process.env.PORT || 5000;

// Middlewares
app.use(cors());
app.use(bodyParser.json());

// Rota principal
app.get("/", (req, res) => {
  res.send("🌍 API da Neuro Earth está rodando!");
});

// Rota de exemplo - visão da startup
app.get("/vision", (req, res) => {
  res.json({
    vision: "Um planeta digital onde pessoas, empresas e governos criam e interagem com agentes inteligentes, sustentáveis e globais."
  });
});

// Rota de contato
app.post("/contact", (req, res) => {
  const { name, email, message } = req.body;
  console.log("📩 Novo contato:", name, email, message);
  res.json({ success: true, msg: "Mensagem recebida com sucesso!" });
});

// Inicia servidor
app.listen(PORT, () => {
  console.log(`🚀 Servidor rodando na porta ${PORT}`);
});
