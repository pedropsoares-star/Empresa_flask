const formulario = document.getElementById("loginForm");
const mensagem = document.getElementById("loginMensagem");

formulario.addEventListener("submit", async (event) => {
    event.preventDefault();

    mensagem.textContent = "Entrando no sistema...";
    mensagem.className = "mensagem";

    const dados = {
        email: document.getElementById("email").value.trim(),
        senha: document.getElementById("senha").value
    };

    try {
        const resposta = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();

        if (!resposta.ok) {
            throw new Error(resultado.erro || "Erro no login.");
        }

        mensagem.textContent = resultado.mensagem;
        mensagem.className = "mensagem sucesso";

        window.location.href = "/sistema";

    } catch (erro) {
        mensagem.textContent = "Erro: " + erro.message;
        mensagem.className = "mensagem erro";
    }
});
