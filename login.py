from flask import request, jsonify, render_template
from banco import conectar_banco


def registrar_rotas_login(app):
    @app.route("/")
    def login():
        return render_template("login.html")

    @app.route("/api/login", methods=["POST"])
    def fazer_login():
        dados = request.get_json(silent=True) or {}
        email = dados.get("email", "").strip()
        senha = dados.get("senha", "")

        if not email or not senha:
            return jsonify({"erro": "Informe o e-mail e a senha."}), 400

        conexao = None
        cursor = None

        try:
            conexao = conectar_banco()
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT id, nome, email, senha, ativo
                FROM usuario
                WHERE email = %s
            """
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()

            # Verifica primeiro se o usuário existe.
            if usuario is None:
                return jsonify({"erro": "E-mail ou senha inválidos."}), 401

            # Impede o acesso de contas desativadas.
            if not usuario["ativo"]:
                return jsonify({"erro": "Usuário desativado. Entre em contato com o administrador."}), 403

            # Compatível com o modelo atual, que compara senha em texto puro.
            # Para produção, armazene hash de senha e valide com Werkzeug.
            if senha != usuario["senha"]:
                return jsonify({"erro": "E-mail ou senha inválidos."}), 401

            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "usuario": {
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "email": usuario["email"]
                }
            }), 200

        except Exception as erro:
            print("Erro no login:", erro)
            return jsonify({"erro": "Erro interno no servidor. Confira o terminal."}), 500

        finally:
            if cursor is not None:
                cursor.close()
            if conexao is not None and conexao.is_connected():
                conexao.close()

    @app.route("/sistema")
    def sistema():
        return render_template("index.html")
