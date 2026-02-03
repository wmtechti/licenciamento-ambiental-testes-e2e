# 🚀 Início Rápido - Testes E2E

## Setup em 5 Minutos

### 1️⃣ Pré-requisitos Rápidos

```powershell
# Verificar Python (deve ser 3.11+)
python --version

# Verificar Chrome instalado
# Abrir: chrome://version
```

### 2️⃣ Instalar ChromeDriver

```powershell
# Baixar da mesma versão do Chrome
# https://googlechromelabs.github.io/chrome-for-testing/

# Extrair para:
C:\chromedriver\chromedriver.exe
```

### 3️⃣ Setup do Projeto

```powershell
# Clonar
git clone https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# Criar venv
python -m venv venv

# Ativar venv
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
cp .env.example .env
notepad .env  # Editar se necessário
```

### 4️⃣ Executar Primeiro Teste

```powershell
# IMPORTANTE: Frontend deve estar rodando!
# Em outro terminal: npm run dev (no projeto principal)

# Executar teste
pytest tests/test_01_login.py -v -s
```

## ✅ Checklist Rápido

Antes de executar testes:

- [ ] Python 3.11+ instalado
- [ ] Chrome instalado
- [ ] ChromeDriver em C:\chromedriver\
- [ ] Projeto clonado
- [ ] Venv criado e ativado
- [ ] Dependências instaladas
- [ ] .env configurado
- [ ] **Frontend rodando em localhost:5173** ⭐

## 📚 Próximos Passos

1. Ler [README.md](README.md) completo
2. Ver [docs/SETUP.md](docs/SETUP.md) para detalhes
3. Explorar [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
4. Executar mais testes: `pytest -v`

## 🆘 Problemas?

### Frontend não está rodando
```powershell
# Em outro terminal
cd d:\code\python\github-dzabccvf
npm run dev
```

### ChromeDriver incompatível
```powershell
# Verificar versão do Chrome
chrome://version

# Baixar MESMA versão do ChromeDriver
# https://googlechromelabs.github.io/chrome-for-testing/
```

### Módulo não encontrado
```powershell
# Ativar venv
.\venv\Scripts\Activate.ps1

# Reinstalar
pip install -r requirements.txt
```

## 💡 Dica

Use VSCode com extensões:
- Python
- Pytest
- GitLens

Configuração recomendada no `.vscode/settings.json`:
```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black"
}
```

---

**Pronto para começar!** 🎉

Execute: `pytest -v` e veja a mágica acontecer! ✨
