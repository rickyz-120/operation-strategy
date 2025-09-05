# 🚀 Guia COMPLETO — WiseRoutes (Flask)

> Documento único com **passo a passo** e **comandos de terminal** para clonar, configurar, rodar e versionar o projeto em **Windows**.

---------------------------------------------------------------------

## 0) Requisitos (instalar antes)

- **Git** → https://git-scm.com/downloads  
  - No Windows, mantenha habilitado: **Git Credential Manager**.
- **VS Code** → https://code.visualstudio.com/Download  
  Extensões recomendadas: *Python* (Microsoft), *Pylance*, *Jinja*.
- **Python 3.11 (recomendado)** → https://www.python.org/downloads/release/python-3119/  
  > Use **3.11.x**. Evite 3.13 por enquanto (numpy/pandas podem falhar).

---------------------------------------------------------------------

## 1) Clonar o repositório e abrir no VS Code

### Windows (PowerShell)
```powershell
cd C:\Users\SEU_USUARIO\Documents
git clone https://github.com/rickyz-120/operation-strategy.git
cd operation-strategy
code .

---------------------------------------------------------------------

## 2) Criar ambiente virtual

python --version
# deve exibir Python 3.11.x

python -m venv .venv
.\.venv\Scripts\activate
# prompt ficará parecido com: (.venv) PS C:\...\operation-strategy>

---------------------------------------------------------------------

## 3) Atualizar pip e instalar dependências

# venv precisa estar ATIVO
python -m pip install --upgrade pip
 pip install -r requirements.txt    (Se falhar em numpy/pandas, verifique se está usando Python 3.11.)

---------------------------------------------------------------------

## 4) Selecionar o Python do venv no VS Code (importante)

VS Code → Ctrl/Cmd + Shift + P → "Python: Select Interpreter" → escolha o interpretador dentro de .venv
(Windows: .venv\Scripts\python.exe | macOS/Linux: .venv/bin/python)

---------------------------------------------------------------------

## 5) Executar a aplicação

Modo simples (python)
python app.py
# Acesse no navegador: http://127.0.0.1:5000

Modo Flask CLI (hot reload)
# Windows PowerShell
$env:FLASK_APP="app.py"
$env:FLASK_ENV="development"
flask run
# macOS / Linux
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Porta alternativa:
flask run --port 5001

# Parar a app:
# Ctrl + C

---------------------------------------------------------------------

## 6) Criar/garantir .gitignore (mantém o repositório limpo)
Conteúdo recomendado do .gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
.venv/
venv/

# Configs locais
.env

# VS Code
.vscode/

# macOS / Windows
.DS_Store
Thumbs.db

Criar (se ainda não existir)
# Windows
echo # Python > .gitignore
# macOS/Linux
echo "# Python" > .gitignore

# Abra e cole o conteúdo acima

---------------------------------------------------------------------

## 7) Configurar usuário do Git (uma vez por máquina)
git config --global user.name "SEU_USUARIO_GITHUB"
git config --global user.email "seuemail@exemplo.com"
git config --list

---------------------------------------------------------------------

## 8) Commit e Push
git status
git add .
git commit -m "Minha alteração"
git push


Se for o primeiro push/branch:

git branch -M main
git push -u origin main

Autenticação no push

Se a janela do Git Credential Manager abrir preta no Windows:

Instale/atualize Microsoft Edge WebView2 Runtime.

Alternativas ao GCM:

Token Pessoal (PAT)
GitHub → Settings → Developer settings → Tokens (classic) → Generate token com escopo repo.
No prompt de senha, cole o token.

SSH

# gerar chave
ssh-keygen -t ed25519 -C "seuemail@exemplo.com"
# Windows PowerShell
eval $(ssh-agent -s)
ssh-add $env:USERPROFILE\.ssh\id_ed25519
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
# macOS/Linux
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub


Adicione a chave pública em: GitHub → Settings → SSH and GPG keys → New SSH key
Troque o remoto para SSH:

git remote set-url origin git@github.com:rickyz-120/operation-strategy.git

---------------------------------------------------------------------

## 9) Estrutura do projeto (referência)
operation-strategy/
├─ app.py
├─ requirements.txt
├─ README.md
├─ COMO_EXECUTAR.md
├─ data/
│  └─ synthetic_data.py
├─ static/
│  ├─ css/style.css
│  └─ js/main.js
├─ templates/
│  ├─ base.html
│  ├─ dashboard.html
│  ├─ map.html
│  ├─ drivers.html
│  ├─ vehicles.html
│  ├─ costs.html
│  ├─ reports.html
│  └─ weather.html
└─ .venv/                (IGNORADO pelo Git)

---------------------------------------------------------------------

## 10) Solução de problemas rápidos
1) ModuleNotFoundError: No module named 'flask'
   → Ative o venv e rode: pip install -r requirements.txt

2) pip lento/travando
   → python -m pip install --upgrade pip
   → pip install -r requirements.txt --no-cache-dir

3) Erro ao instalar numpy/pandas no Windows
   → Use Python 3.11 (não 3.13) e recrie o venv

4) Abriu 127.0.0.1:xxxxx/?code=...
   → É do Git Credential Manager; ignore. Sua app roda em http://127.0.0.1:5000

5) Porta 5000 ocupada
   → flask run --port 5001

6) PowerShell bloqueou ativação do venv
   → Set-ExecutionPolicy -Scope CurrentUser RemoteSigned (como admin) e ative de novo

---------------------------------------------------------------------

## 11) Comandos úteis (cola-e-usa)
# Clonar e abrir
git clone https://github.com/rickyz-120/operation-strategy.git
cd operation-strategy
code .

# venv (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# venv (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Dependências
python -m pip install --upgrade pip
 pip install -r requirements.txt

# Executar
python app.py
# ou:
# Windows
$env:FLASK_APP="app.py"; $env:FLASK_ENV="development"; flask run
# macOS/Linux
export FLASK_APP=app.py; export FLASK_ENV=development; flask run

# Git básico
git status
git add .
git commit -m "mensagem"
git push

# Ajustar remoto para SSH (opcional)
git remote set-url origin git@github.com:rickyz-120/operation-strategy.git


