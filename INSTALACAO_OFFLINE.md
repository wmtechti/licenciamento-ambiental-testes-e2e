# 📦 Instalação Offline com Wheels

Este guia explica como instalar as dependências do projeto em ambientes com **restrições de acesso à internet** (sem acesso ao PyPI).

---

## 📋 Pré-requisitos

- Python 3.11.9 instalado
- Pasta `wheels/` com todos os arquivos `.whl` (já incluída no projeto)
- Acesso ao diretório do projeto

---

## 🚀 Instalação Passo a Passo

### 1. Clonar o Repositório

```powershell
# Via Git (se tiver acesso)
git clone https://github.com/wmtechti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# OU copiar a pasta completa do projeto manualmente
```

### 2. Criar Ambiente Virtual

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se houver erro de ExecutionPolicy:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Instalar Dependências Offline

**Opção 1: Instalar tudo de uma vez**
```powershell
pip install --no-index --find-links=wheels -r requirements.txt
```

**Opção 2: Instalar todos os wheels da pasta**
```powershell
pip install --no-index --find-links=wheels wheels/*.whl
```

**Opção 3: Instalar pacotes específicos**
```powershell
# Principais pacotes
pip install --no-index --find-links=wheels selenium pytest webdriver-manager python-dotenv
```

---

## 📦 Conteúdo da Pasta wheels/

A pasta `wheels/` contém **65 arquivos .whl** com todas as dependências necessárias:

### Principais Pacotes
- `selenium-4.15.2` - Automação web
- `pytest-7.4.3` - Framework de testes
- `webdriver-manager-4.0.1` - Gerenciador do ChromeDriver
- `python-dotenv-1.0.0` - Variáveis de ambiente
- `requests-2.31.0` - Cliente HTTP
- `supabase-2.0.3` - Cliente Supabase

### Ferramentas de Desenvolvimento
- `black-23.12.1` - Formatador de código
- `flake8-7.0.0` - Linter
- `mypy-1.8.0` - Type checker
- `pytest-html-4.1.1` - Relatórios HTML
- `pytest-xdist-3.5.0` - Execução paralela
- `allure-pytest-2.13.2` - Relatórios Allure

### Dependências Transitivas
Todas as dependências indiretas também estão incluídas (attrs, certifi, httpx, pydantic, etc.)

---

## ✅ Verificação da Instalação

```powershell
# Verificar versão do Python
python --version
# Deve mostrar: Python 3.11.9

# Verificar pacotes instalados
pip list

# Verificar ambiente completo
python check_environment.ps1
```

**Saída esperada do check_environment.ps1:**
```
========================================
  VERIFICAÇÃO DE AMBIENTE
========================================

✓ Python 3.11.9
✓ Selenium 4.15.2
✓ Pytest 7.4.3
✓ WebDriver Manager 4.0.1
✓ Python-dotenv 1.0.0
✓ Supabase 2.0.3
✓ Requests 2.31.0

========================================
  AMBIENTE OK!
========================================
```

---

## 🔧 Solução de Problemas

### Erro: "No matching distribution found"
**Problema:** Algum pacote não está na pasta wheels/  
**Solução:**
```powershell
# Baixar pacote específico (em ambiente com internet)
pip download nome-do-pacote -d wheels

# Depois copiar a pasta wheels/ para o ambiente offline
```

### Erro: "Platform mismatch"
**Problema:** Wheels foram baixados para plataforma diferente  
**Solução:** Os wheels atuais são para Windows (win_amd64) e Python 3.11. Se precisar de outra plataforma:
```powershell
# Linux
pip download -r requirements.txt -d wheels --platform manylinux2014_x86_64 --python-version 311 --only-binary=:all:

# macOS
pip download -r requirements.txt -d wheels --platform macosx_11_0_x86_64 --python-version 311 --only-binary=:all:
```

### Erro: "ExecutionPolicy"
**Problema:** PowerShell bloqueia execução de scripts  
**Solução:**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📝 Atualizar Wheels (em ambiente com internet)

Se precisar atualizar ou adicionar novos pacotes:

```powershell
# 1. Atualizar requirements.txt com novos pacotes

# 2. Baixar todos os wheels novamente
pip download -r requirements.txt -d wheels

# 3. Verificar wheels baixados
dir wheels

# 4. Fazer commit e push
git add wheels/
git commit -m "chore: atualiza wheels para instalação offline"
git push
```

---

## 🎯 Workflow Completo na Estação da Empresa

### Primeira Vez
```powershell
# 1. Clonar projeto
git clone https://github.com/wmtechti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# 2. Criar e ativar venv
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Instalar dependências OFFLINE
pip install --no-index --find-links=wheels -r requirements.txt

# 4. Configurar .env
copy .env.example .env
# Editar .env com suas credenciais e token

# 5. Verificar instalação
python check_environment.ps1

# 6. Executar testes
pytest -m integration -v
```

### Próximas Vezes
```powershell
# 1. Navegar para o projeto
cd licenciamento-ambiental-testes-e2e

# 2. Ativar ambiente
.\venv\Scripts\Activate.ps1

# 3. Atualizar código (se necessário)
git pull

# 4. Executar testes
pytest -m integration -v
```

---

## 📊 Comparação: Online vs Offline

| Aspecto | Instalação Online | Instalação Offline |
|---------|-------------------|-------------------|
| **Comando** | `pip install -r requirements.txt` | `pip install --no-index --find-links=wheels -r requirements.txt` |
| **Requer internet** | ✅ Sim | ❌ Não |
| **Velocidade** | Depende da conexão | Muito rápido |
| **Espaço em disco** | ~50MB (cache) | ~80MB (wheels/ + instalado) |
| **Dependências** | Baixa do PyPI | Usa wheels/ localmente |

---

## 🔐 Segurança

- ✅ **Vantagens:** 
  - Não precisa acessar PyPI (rede externa)
  - Versões fixas e testadas
  - Instalação reproduzível
  
- ⚠️ **Atenção:**
  - Wheels não são verificados contra PyPI
  - Manter wheels/ atualizados com patches de segurança
  - Revisar dependências periodicamente

---

## 📦 Tamanho Total

```
Pasta wheels/: ~78 MB
Contém: 65 arquivos .whl
```

---

## 🆘 Suporte

Se encontrar problemas na instalação offline:

1. Verificar que todos os wheels estão na pasta
2. Confirmar versão do Python (3.11.9)
3. Limpar cache do pip: `pip cache purge`
4. Reinstalar do zero: deletar `venv/` e repetir processo

---

## 📚 Referências

- [Pip Offline Installation](https://pip.pypa.io/en/stable/cli/pip_install/#install-no-index)
- [Python Wheels](https://pythonwheels.com/)
- [Pip Download](https://pip.pypa.io/en/stable/cli/pip_download/)

---

**Última atualização:** 03/02/2026  
**Versão:** 1.0.0  
**Python:** 3.11.9  
**Plataforma:** Windows (win_amd64)
