# 🎬 PRIMEIROS PASSOS - LEIA ISTO PRIMEIRO!

## 👋 Bem-vindo ao Projeto de Testes E2E!

Este arquivo contém **instruções essenciais** para iniciar o projeto pela primeira vez.

---

## ⚡ Início Ultra-Rápido (3 Passos)

### 1️⃣ Setup do Ambiente

```powershell
# Abra PowerShell neste diretório e execute:

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

### 2️⃣ Configurar Variáveis

```powershell
# Copiar arquivo de configuração
cp .env.example .env

# Editar configurações (IMPORTANTE!)
notepad .env
```

**Configurações mínimas necessárias:**
- `CHROME_DRIVER_PATH=C:\chromedriver\chromedriver.exe`
- `FRONTEND_URL=http://localhost:5173`

### 3️⃣ Verificar e Executar

```powershell
# Verificar se tudo está OK
.\check_environment.ps1

# IMPORTANTE: Frontend deve estar rodando!
# Abra outro terminal e inicie o frontend

# Executar primeiro teste
pytest tests/test_01_login.py -v -s
```

---

## 📚 Documentação Disponível

1. **[README.md](README.md)** - Documentação completa do projeto
2. **[QUICKSTART.md](QUICKSTART.md)** - Guia de início rápido
3. **[docs/SETUP.md](docs/SETUP.md)** - Setup detalhado passo a passo
4. **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Arquitetura do projeto
5. **[docs/COMMANDS.md](docs/COMMANDS.md)** - Comandos úteis
6. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Sumário do que foi criado

---

## ⚠️ IMPORTANTE - Antes de Executar Testes

### ✅ Checklist Obrigatório

- [ ] **Python 3.11+** instalado
- [ ] **Google Chrome** instalado
- [ ] **ChromeDriver** baixado e em `C:\chromedriver\`
- [ ] **Ambiente virtual** criado e ativado (`venv`)
- [ ] **Dependências** instaladas (`pip install -r requirements.txt`)
- [ ] **Arquivo .env** criado e configurado
- [ ] **Frontend rodando** em `http://localhost:5173` ⭐⭐⭐

### 🔴 O Erro Mais Comum

**Erro:** `WebDriverException: net::ERR_CONNECTION_REFUSED`

**Causa:** Frontend não está rodando!

**Solução:**
```powershell
# Em OUTRO terminal/VSCode (projeto principal do frontend)
cd d:\code\python\github-dzabccvf
npm run dev
```

---

## 🚀 Fluxo de Trabalho Recomendado

### Terminal 1: Frontend
```powershell
# Projeto principal (frontend)
cd d:\code\python\github-dzabccvf
npm run dev
# Deixar rodando
```

### Terminal 2: Testes
```powershell
# Projeto de testes
cd d:\projetos\licenciamento-testes-e3e
.\venv\Scripts\Activate.ps1
pytest -v
```

---

## 🎯 Seus Primeiros Testes

### Teste 1: Verificar Ambiente
```powershell
.\check_environment.ps1
```

### Teste 2: Login Simples
```powershell
pytest tests/test_01_login.py -v -s
```

### Teste 3: Fluxo Completo
```powershell
pytest tests/integration/test_fluxo_completo.py -v -s
```

### Teste 4: Todos os Testes
```powershell
pytest -v
```

---

## 🐛 Troubleshooting Rápido

### Problema: "python não é reconhecido"
```powershell
# Adicionar Python ao PATH ou usar caminho completo
C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311\python.exe -m venv venv
```

### Problema: "Activate.ps1 não pode ser carregado"
```powershell
# Alterar política de execução
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: "ModuleNotFoundError"
```powershell
# Certifique-se de que venv está ativado
.\venv\Scripts\Activate.ps1
# Reinstalar dependências
pip install -r requirements.txt
```

### Problema: "ChromeDriver incompatível"
```powershell
# Verificar versão do Chrome
chrome://version (no navegador)

# Baixar MESMA versão em:
# https://googlechromelabs.github.io/chrome-for-testing/
```

---

## 🎓 Aprendendo o Projeto

### Ordem Recomendada de Leitura

1. ✅ Este arquivo (START_HERE.md) - Você está aqui!
2. 📖 [QUICKSTART.md](QUICKSTART.md) - Setup em 5 minutos
3. 📖 [README.md](README.md) - Documentação completa
4. 📖 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - Entender estrutura
5. 📖 [docs/COMMANDS.md](docs/COMMANDS.md) - Comandos úteis
6. 💻 Explorar `tests/` - Ver exemplos de testes
7. 💻 Explorar `src/pages/` - Ver Page Objects
8. 💻 Criar seus próprios testes!

---

## 💡 Dicas Importantes

### ✨ Boas Práticas

1. **Sempre ativar venv** antes de trabalhar
2. **Manter frontend rodando** durante os testes
3. **Usar `-v -s`** para ver detalhes dos testes
4. **Consultar logs** quando algo falha
5. **Screenshots** são salvos em `reports/screenshots/` quando há erro

### 🎯 Comandos que Você Vai Usar Muito

```powershell
# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Executar testes
pytest -v

# Executar com relatório
pytest --html=reports/html/report.html --self-contained-html

# Verificar ambiente
.\check_environment.ps1
```

---

## 🆘 Precisa de Ajuda?

1. **Ler documentação:** Maioria das dúvidas está documentada
2. **Verificar environment:** `.\check_environment.ps1`
3. **Ver comandos úteis:** [docs/COMMANDS.md](docs/COMMANDS.md)
4. **Abrir issue:** GitHub Issues (se aplicável)
5. **Contato:** contato@miltec.com.br

---

## ✅ Você Está Pronto Quando...

- [ ] Ambiente virtual está criado e ativado
- [ ] Dependências instaladas sem erros
- [ ] Arquivo .env configurado
- [ ] ChromeDriver funcionando
- [ ] Frontend rodando em localhost:5173
- [ ] Script `check_environment.ps1` passou sem erros
- [ ] Primeiro teste executou com sucesso

---

## 🎉 Próximo Passo

**Depois de configurar tudo:**

1. Leia o [README.md](README.md) completo
2. Execute `pytest -v` e veja a mágica acontecer! ✨
3. Explore os exemplos em `tests/`
4. Comece a criar seus próprios testes!

---

**Boa sorte com os testes!** 🚀

Se você chegou até aqui, você está no caminho certo! 👏

---

*Última atualização: 02/02/2026 - v1.0.0*
