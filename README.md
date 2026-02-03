# 🧪 Testes Automatizados E2E - Sistema de Licenciamento Ambiental

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.15.2-green.svg)
![Pytest](https://img.shields.io/badge/pytest-7.4.3-orange.svg)

> **Projeto separado de testes E2E** para o Sistema de Licenciamento Ambiental  
> Automatiza testes end-to-end usando Selenium WebDriver e Pytest

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Executando os Testes](#-executando-os-testes)
- [Desenvolvendo Testes](#-desenvolvendo-testes)
- [CI/CD](#-cicd)
- [Troubleshooting](#-troubleshooting)
- [Contribuindo](#-contribuindo)

---

## 🎯 Visão Geral

Este projeto contém testes automatizados end-to-end (E2E) para o Sistema de Licenciamento Ambiental. Os testes validam o fluxo completo de cadastro de empreendimentos, desde o login até a finalização do cadastro.

### Características

- ✅ **Testes E2E completos** - Valida fluxos de ponta a ponta
- ✅ **Page Object Model** - Arquitetura organizada e manutenível
- ✅ **Auto-login** - Evita tela de login em cada teste
- ✅ **Screenshots em falhas** - Facilita debug de problemas
- ✅ **Relatórios HTML** - Visualização clara dos resultados
- ✅ **Configuração flexível** - Variáveis de ambiente para diferentes ambientes

### Fluxo Testado

```
Auto-Login → Menu Empreendimento → Novo Empreendimento →
Wizard (Imóvel → Dados Gerais → Atividades → Caracterização) →
Validação de Dados → Sucesso
```

---

## 📦 Pré-requisitos

### Software Necessário

#### Windows

```powershell
# Python 3.11+
# Baixar de: https://www.python.org/downloads/

# Google Chrome (versão atualizada)
# Baixar de: https://www.google.com/chrome/

# Git
# Baixar de: https://git-scm.com/download/win
```

#### Linux/Ubuntu

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
sudo apt install google-chrome-stable
sudo apt install git
```

### ChromeDriver

**IMPORTANTE:** A versão do ChromeDriver deve ser compatível com sua versão do Chrome.

### 🔒 Ambientes com Restrições de Internet

Se você está em um ambiente corporativo com restrições de acesso ao PyPI:
- ✅ Este projeto inclui uma pasta `wheels/` com todas as dependências
- ✅ Instalação 100% offline disponível
- 📖 Veja instruções completas em **[INSTALACAO_OFFLINE.md](INSTALACAO_OFFLINE.md)**

#### Verificar versão do Chrome

```powershell
# Windows PowerShell
(Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo.FileVersion

# Ou abrir Chrome e acessar: chrome://version
```

#### Instalar ChromeDriver

```powershell
# 1. Baixar versão compatível
# Site: https://googlechromelabs.github.io/chrome-for-testing/

# 2. Extrair para C:\chromedriver\
mkdir C:\chromedriver
# Copiar chromedriver.exe para C:\chromedriver\

# 3. Verificar instalação
C:\chromedriver\chromedriver.exe --version
# Saída esperada: ChromeDriver 144.x.xxxx.xxx
```

### Frontend e Backend Rodando

**IMPORTANTE:** O frontend e backend devem estar rodando em outro terminal/VSCode.

```bash
# Frontend deve estar em: http://localhost:5173
# Backend (opcional) em: http://localhost:8000
```

---

## 🚀 Instalação

### 1. Clonar Repositório

```bash
git clone https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e
```

### 2. Criar Ambiente Virtual

#### Windows

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se houver erro de política de execução:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux/Mac

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
# Instalar pacotes necessários
pip install -r requirements.txt

# Instalar o projeto em modo desenvolvimento (opcional)
pip install -e .
```

---

## ⚙️ Configuração

### 1. Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env com suas configurações
notepad .env  # Windows
nano .env     # Linux
```

### 2. Configurar .env

```env
# URLs do Sistema (ajustar conforme seu ambiente)
FRONTEND_URL=http://localhost:5173
BACKEND_URL=http://localhost:8000

# Auto-login (obter token do sistema)
AUTO_LOGIN_TOKEN=seu_token_aqui
AUTO_LOGIN_USER_ID=9948
AUTO_LOGIN_USER_NAME=TESTE DESENVOLVIMENTO

# ChromeDriver
CHROME_DRIVER_PATH=C:\chromedriver\chromedriver.exe
USE_WEBDRIVER_MANAGER=false

# Configurações de Teste
TEST_TIMEOUT=20
HEADLESS=false
SCREENSHOT_ON_FAIL=true
```

### 3. Verificar Configuração

```bash
# Verificar se Python está corretamente instalado
python --version
# Saída esperada: Python 3.11.x

# Verificar se pacotes foram instalados
pip list | grep selenium
pip list | grep pytest
```

---

## 📁 Estrutura do Projeto

```
licenciamento-ambiental-testes-e2e/
├── .git/                           # Controle de versão
├── .gitignore                      # Arquivos ignorados pelo Git
├── README.md                       # Este arquivo
├── requirements.txt                # Dependências Python
├── pytest.ini                      # Configuração do Pytest
├── setup.py                        # Setup do projeto
├── .env.example                    # Exemplo de variáveis de ambiente
├── .env                            # Variáveis de ambiente (não commitado)
│
├── src/                            # Código fonte
│   ├── __init__.py
│   ├── config/                     # Configurações
│   │   ├── __init__.py
│   │   ├── settings.py             # Configurações centralizadas
│   │   └── urls.py                 # URLs do sistema
│   │
│   ├── core/                       # Funcionalidades centrais
│   │   ├── __init__.py
│   │   ├── driver_manager.py      # Gerenciamento do WebDriver
│   │   ├── base_test.py            # Classe base para testes
│   │   └── orchestrator.py         # Orquestrador de testes
│   │
│   ├── pages/                      # Page Object Model
│   │   ├── __init__.py
│   │   ├── login_page.py           # Página de login
│   │   ├── empreendimento_page.py  # Página de empreendimentos
│   │   └── wizard/                 # Wizard de cadastro
│   │       ├── __init__.py
│   │       ├── imovel_step.py      # Etapa Imóvel
│   │       ├── dados_gerais_step.py
│   │       ├── atividades_step.py
│   │       └── caracterizacao_step.py
│   │
│   ├── utils/                      # Utilitários
│   │   ├── __init__.py
│   │   ├── json_helper.py          # Manipulação de JSON
│   │   ├── screenshot.py           # Captura de screenshots
│   │   └── wait_helper.py          # Helpers de espera
│   │
│   └── fixtures/                   # Dados de teste
│       ├── __init__.py
│       ├── empresas.json           # Dados de empresas
│       ├── imoveis.json            # Dados de imóveis
│       └── atividades.json         # Dados de atividades
│
├── tests/                          # Testes
│   ├── __init__.py
│   ├── conftest.py                 # Fixtures Pytest
│   ├── test_01_login.py            # Testes de login
│   ├── test_02_cadastro_empreendimento.py
│   └── integration/                # Testes de integração
│       └── test_fluxo_completo.py
│
├── reports/                        # Relatórios de execução
│   ├── html/                       # Relatórios HTML
│   ├── json/                       # Relatórios JSON
│   └── screenshots/                # Screenshots de erros
│
└── output/                         # Saídas dos testes
    └── *.json                      # JSONs gerados pelos testes
```

---

## 🏃 Executando os Testes

### Pré-requisitos de Execução

**ANTES DE EXECUTAR OS TESTES**, certifique-se de que:

1. ✅ Frontend está rodando em `http://localhost:5173`
2. ✅ Ambiente virtual está ativado (`venv`)
3. ✅ ChromeDriver está instalado e configurado
4. ✅ Arquivo `.env` está configurado

### Executar Todos os Testes

```bash
# Com pytest (recomendado)
pytest -v

# Com relatório HTML
pytest --html=reports/html/report.html --self-contained-html
```

### Executar Testes Específicos

```bash
# Executar apenas testes de login
pytest tests/test_01_login.py -v

# Executar apenas testes de integração
pytest tests/integration/ -v

# Executar testes com marcador específico
pytest -m smoke -v          # Testes de smoke
pytest -m e2e -v            # Testes E2E
pytest -m "not slow" -v     # Excluir testes lentos
```

### Executar com Opções Avançadas

```bash
# Executar em paralelo (mais rápido)
pytest -n 4 -v              # 4 processos paralelos

# Parar no primeiro erro
pytest -x

# Mostrar saída detalhada
pytest -v -s

# Executar último teste que falhou
pytest --lf
```

### Executar Modo Standalone

```bash
# Executar arquivo de teste diretamente
python tests/test_01_login.py
```

---

## 🛠️ Desenvolvendo Testes

### Criar Novo Teste

```python
"""
Teste 03 - Seu Teste
====================

Descrição do que o teste faz.
"""

import pytest
from src.pages.login_page import LoginPage


@pytest.mark.e2e
def test_seu_teste(driver, wait, auto_login_url):
    """
    Descrição do teste.
    
    Args:
        driver: Fixture do WebDriver
        wait: Fixture do WebDriverWait
        auto_login_url: Fixture com URL de auto-login
    """
    # Seu código de teste aqui
    login_page = LoginPage(driver, wait)
    assert login_page.auto_login()
    
    # ... mais asserções
```

### Criar Novo Page Object

```python
"""
Page Object - Nova Página
=========================

Representa a página X do sistema.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ..utils.wait_helper import WaitHelper


class NovaPage:
    """Page Object para a nova página."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
    
    # Locators
    BOTAO_ACAO = (By.XPATH, "//button[contains(., 'Ação')]")
    
    def realizar_acao(self) -> bool:
        """Realiza uma ação na página."""
        btn = WaitHelper.wait_for_element(
            self.driver, self.BOTAO_ACAO, condition='clickable'
        )
        btn.click()
        return True
```

### Usar Fixtures de Dados

```python
from src.utils.json_helper import JSONHelper
from pathlib import Path

# Carregar dados de teste
fixtures_dir = Path(__file__).parent.parent / "src" / "fixtures"
empresas = JSONHelper.load_json(fixtures_dir / "empresas.json")

# Usar dados
empresa_teste = empresas['empresa_01']
print(empresa_teste['razaoSocial'])
```

---

## 🔄 CI/CD

### GitHub Actions (Exemplo)

Criar arquivo `.github/workflows/tests.yml`:

```yaml
name: Testes E2E

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install Chrome
      run: |
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
        sudo apt-get update
        sudo apt-get install google-chrome-stable
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest -v --html=reports/html/report.html
    
    - name: Upload test results
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: test-results
        path: reports/
```

---

## 🐛 Troubleshooting

### Problema: ChromeDriver incompatível

```
SessionNotCreatedException: session not created: This version of ChromeDriver only supports Chrome version X
```

**Solução:**
1. Verificar versão do Chrome: `chrome://version`
2. Baixar ChromeDriver compatível: https://googlechromelabs.github.io/chrome-for-testing/
3. Atualizar `CHROME_DRIVER_PATH` no `.env`

### Problema: Frontend não está rodando

```
selenium.common.exceptions.WebDriverException: net::ERR_CONNECTION_REFUSED
```

**Solução:**
1. Verificar se frontend está rodando: `http://localhost:5173`
2. Iniciar frontend no projeto principal: `npm run dev`

### Problema: Elemento não encontrado

```
TimeoutException: Message: 
```

**Solução:**
1. Verificar se locator está correto
2. Aumentar timeout em `.env`: `TEST_TIMEOUT=30`
3. Verificar se página carregou completamente
4. Usar `driver.implicitly_wait(10)` ou `WebDriverWait`

### Problema: Módulo não encontrado

```
ModuleNotFoundError: No module named 'src'
```

**Solução:**
1. Ativar ambiente virtual: `.\venv\Scripts\Activate.ps1`
2. Instalar dependências: `pip install -r requirements.txt`
3. Instalar projeto: `pip install -e .`

---

## 🤝 Contribuindo

### Fluxo de Contribuição

1. Fork o projeto
2. Criar branch para feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: Amazing Feature'`)
4. Push para branch (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

### Padrões de Código

- Seguir PEP 8 para Python
- Usar docstrings em todas as funções e classes
- Escrever testes para novas funcionalidades
- Manter Page Objects atualizados

### Executar Linters

```bash
# Formatação de código
black src/ tests/

# Verificação de estilo
flake8 src/ tests/

# Verificação de tipos
mypy src/
```

---

## 📞 Suporte

- **Issues:** https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e/issues
- **Email:** contato@miltec.com.br
- **Documentação completa:** [PROJETO_TESTES_AUTOMATIZADOS_E2E.md](PROJETO_TESTES_AUTOMATIZADOS_E2E.md)

---

## 📝 Licença

Este projeto é proprietário da Miltec TI.

---

## 🎉 Status

**Última atualização:** 02/02/2026  
**Versão:** 1.0.0  
**Status:** ✅ Projeto configurado e pronto para uso

**Desenvolvido com** ❤️ **por Miltec TI**
