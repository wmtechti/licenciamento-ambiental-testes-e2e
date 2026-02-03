# Guia de Setup - Testes E2E

## Setup Passo a Passo

### 1. Pré-requisitos

#### Verificar Python

```powershell
python --version
# Deve ser 3.11 ou superior
```

Se não tiver Python 3.11+, baixar de: https://www.python.org/downloads/

#### Verificar Chrome

```powershell
# Abrir Chrome e ir para chrome://version
# Verificar a versão completa (ex: 144.0.6367.60)
```

### 2. Instalar ChromeDriver

```powershell
# 1. Acessar: https://googlechromelabs.github.io/chrome-for-testing/
# 2. Buscar pela MESMA versão do seu Chrome
# 3. Baixar chromedriver-win64.zip
# 4. Extrair para C:\chromedriver\
# 5. Testar:

C:\chromedriver\chromedriver.exe --version
```

### 3. Clonar e Configurar Projeto

```powershell
# Clonar repositório
git clone https://github.com/wmtechti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se der erro de política de execução:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

### 3.1. Instalação de Dependências

**Opção 1: Instalação Online (com acesso à internet)**

```powershell
pip install -r requirements.txt
```

**Opção 2: Instalação Offline (ambiente com restrições)**

Se você está em ambiente corporativo sem acesso ao PyPI:

```powershell
# Usar wheels incluídos no projeto
pip install --no-index --find-links=wheels -r requirements.txt
```

📖 **Documentação completa:** [INSTALACAO_OFFLINE.md](../INSTALACAO_OFFLINE.md)

**Verificar instalação:**

```powershell
python check_environment.ps1

# Instalar dependências
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

```powershell
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env
notepad .env
```

Configurar:
- `FRONTEND_URL` - URL do frontend (padrão: http://localhost:5173)
- `CHROME_DRIVER_PATH` - Caminho do ChromeDriver
- `AUTO_LOGIN_TOKEN` - Token de autenticação

### 5. Verificar Setup

```powershell
# Verificar instalação
python -c "import selenium; print('Selenium OK')"
python -c "import pytest; print('Pytest OK')"

# Verificar ChromeDriver
C:\chromedriver\chromedriver.exe --version
```

### 6. Executar Primeiro Teste

```powershell
# IMPORTANTE: Frontend deve estar rodando em localhost:5173

# Executar teste simples
pytest tests/test_01_login.py -v -s
```

## Troubleshooting de Setup

### Erro: python não é reconhecido

**Solução:** Adicionar Python ao PATH do Windows

1. Buscar "Variáveis de Ambiente" no Windows
2. Editar PATH do usuário
3. Adicionar: `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311`
4. Reiniciar terminal

### Erro: ChromeDriver incompatível

**Solução:** Baixar versão exata do Chrome

1. Verificar versão: `chrome://version`
2. Baixar ChromeDriver da MESMA versão
3. Atualizar `.env` com caminho correto

### Erro: ModuleNotFoundError

**Solução:** Ambiente virtual não ativado

```powershell
# Ativar venv
.\venv\Scripts\Activate.ps1

# Reinstalar dependências
pip install -r requirements.txt
```

### Erro: Frontend não está rodando

**Solução:** Iniciar frontend no outro terminal

```powershell
# Em outro terminal/VSCode
cd d:\code\python\github-dzabccvf
npm install
npm run dev
```

## Checklist de Setup

- [ ] Python 3.11+ instalado
- [ ] Google Chrome instalado
- [ ] ChromeDriver baixado e configurado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas
- [ ] Arquivo .env configurado
- [ ] Frontend rodando em localhost:5173
- [ ] Primeiro teste executado com sucesso

## Próximos Passos

Após setup completo:

1. Ler [README.md](../README.md) para entender estrutura
2. Ver exemplos em `tests/`
3. Explorar Page Objects em `src/pages/`
4. Criar seus próprios testes

## Suporte

Problemas no setup? Abrir issue: https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e/issues
