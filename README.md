# Empresa Flask — versão revisada

## Como executar no Windows / VS Code

Abra o terminal na pasta que contém `app.py` e execute:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install flask mysql-connector-python
python app.py
```

Depois abra http://127.0.0.1:5000 no navegador.

## Antes de testar
- Confira em `banco.py` o nome do banco, usuário e senha do MySQL.
- Confirme que existe a tabela `usuario` com as colunas `id`, `nome`, `email`, `senha` e `ativo`.
- Esta versão mantém a comparação de senha em texto puro para combinar com a estrutura existente. Para uso real, altere para hash de senha.
- A rota `/sistema` ainda não exige sessão de autenticação.
- Os CRUDs de empresas e funcionários não estão implementados: os arquivos Python correspondentes não estavam no ZIP e os HTML estavam vazios.
