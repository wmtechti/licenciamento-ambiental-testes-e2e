# Contexto Completo do Projeto - Testes E2E Licenciamento Ambiental

## 📋 Visão Geral do Projeto

Este é um projeto **separado** de testes E2E automatizados para o sistema de Licenciamento Ambiental. Foi criado para rodar independentemente do frontend e backend, que executam em outras IDEs.

### URLs das Aplicações
- **Frontend:** http://localhost:5173 (rodando em outra IDE)
- **Backend:** http://localhost:8000 (rodando em outra IDE)
- **Repositório GitHub:** https://github.com/wmtechti/licenciamento-ambiental-testes-e2e

### Objetivo
Automatizar testes end-to-end do fluxo completo de cadastro de empreendimentos no sistema de licenciamento ambiental, utilizando Page Object Model e boas práticas de automação.

---

## 🛠️ Stack Tecnológica

- **Python:** 3.11.9
- **Selenium:** 4.15.2
- **ChromeDriver:** 144.0.7559.109
- **Pytest:** 7.4.3
- **Arquitetura:** Page Object Model (POM)
- **Sistema Operacional:** Windows

---

## 📦 Instalação e Configuração

### 1. Pré-requisitos
- Python 3.11.9 instalado
- Google Chrome instalado
- Git configurado
- Acesso ao frontend e backend rodando localmente

### 2. Setup Inicial

```powershell
# 1. Clonar o repositório
git clone https://github.com/wmtechti/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# 2. Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Se houver erro de ExecutionPolicy, execute:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Verificar instalação
python .\check_environment.ps1
```

### 3. Configuração do Ambiente (.env)

Criar arquivo `.env` na raiz do projeto:

```env
# URLs
FRONTEND_URL=http://localhost:5173
BACKEND_URL=http://localhost:8000

# Credenciais de Login
LOGIN_EMAIL=seu_email@exemplo.com
LOGIN_PASSWORD=sua_senha

# Token de Autenticação (obtido após login manual no frontend)
AUTH_TOKEN=seu_token_jwt_aqui

# Configurações do Chrome
HEADLESS=false
WINDOW_SIZE=1920,1080
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20

# Configurações de Screenshot
SCREENSHOT_ON_FAILURE=true
```

### 4. Obter Token de Autenticação

1. Abrir o frontend: http://localhost:5173
2. Fazer login manual
3. Abrir DevTools (F12) → Application → Local Storage
4. Copiar o valor da chave `sb-<projeto>-auth-token`
5. Colar no arquivo `.env` na variável `AUTH_TOKEN`

---

## 🏗️ Estrutura do Projeto

```
licenciamento-testes-e3e/
├── src/
│   ├── config/              # Configurações
│   │   ├── settings.py      # Configurações gerais
│   │   └── urls.py          # URLs do sistema
│   ├── core/                # Núcleo do framework
│   │   ├── driver_manager.py    # Gerenciador do WebDriver
│   │   ├── base_test.py         # Classe base para testes
│   │   └── orchestrator.py      # Orquestrador de testes
│   ├── pages/               # Page Objects
│   │   ├── login_page.py         # Página de login
│   │   ├── empreendimento_page.py  # Página de empreendimentos
│   │   └── wizard/               # Steps do wizard
│   │       ├── imovel_step.py           # Etapa 1: Imóvel
│   │       ├── dados_gerais_step.py     # Etapa 2: Dados Gerais
│   │       ├── atividades_step.py       # Etapa 3: Atividades
│   │       └── caracterizacao_step.py   # Etapa 4: Caracterização
│   ├── utils/               # Utilitários
│   │   ├── json_helper.py        # Manipulação de JSON
│   │   ├── screenshot.py         # Capturas de tela
│   │   ├── wait_helper.py        # Helpers de espera
│   │   └── json_collector.py     # Coleta de JSON do browser
│   └── fixtures/            # Dados de teste
│       ├── imoveis.json
│       ├── empresas.json
│       └── atividades.json
├── tests/                   # Testes
│   ├── conftest.py               # Fixtures do Pytest
│   ├── test_01_login.py          # Teste de login
│   ├── integration/
│   │   └── test_fluxo_completo.py  # Teste completo E2E
│   └── analisar/                   # Testes originais (referência)
├── docs/                    # Documentação
│   ├── ARCHITECTURE.md           # Arquitetura do projeto
│   ├── SETUP.md                  # Guia de instalação
│   ├── COMMANDS.md               # Comandos disponíveis
│   └── LOCATORS_GUIDE.md         # Guia de locators
├── reports/                 # Relatórios
│   ├── screenshots/
│   ├── html/
│   └── json/
├── output/                  # Saídas temporárias
├── .env                     # Variáveis de ambiente
├── .gitignore              
├── pytest.ini               # Configuração do Pytest
├── requirements.txt         # Dependências Python
└── README.md               # Documentação principal
```

---

## 🎯 Fluxo de Teste E2E Completo

O teste completo (`test_fluxo_completo.py`) executa as seguintes etapas:

### ETAPA 1: Auto-Login
- Injeta token JWT diretamente no localStorage
- Evita interação com tela de login
- Mais rápido e confiável

### ETAPA 2: Navegação
- Acessa menu "Empreendimento"
- Clica em "Novo Empreendimento"
- Abre o wizard de cadastro

### ETAPA 3: Cadastro de Imóvel
- Seleciona tipo de imóvel: **URBANO** (via dropdown `<select>`)
- Clica em "Preencher Dados" (botão roxo/verde)
- Salva o imóvel
- Avança para próxima etapa

### ETAPA 4: Dados Gerais
- Clica em "Preencher Dados" (auto-fill)
- Valida campos obrigatórios preenchidos
- Valida partícipe adicionado
- Avança para próxima etapa

### ETAPA 5: Atividades
- Clica em "Preencher Dados" (auto-fill)
- Valida atividades adicionadas
- Valida campos numéricos preenchidos
- Avança para próxima etapa

### ETAPA 6: Caracterização
- Clica em "Preencher Dados" (auto-fill)
- Valida respostas de caracterização
- Clica em "Finalizar"
- ✅ Cadastro concluído

**Tempo de execução:** ~52 segundos

---

## 💻 Comandos de Uso

```powershell
# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Executar todos os testes
pytest -v

# Executar teste de integração completo
pytest -m integration -v -s

# Executar teste de login
pytest tests/test_01_login.py -v

# Executar com output detalhado
pytest -v -s

# Executar testes específicos por marker
pytest -m smoke -v       # Testes smoke
pytest -m e2e -v         # Testes E2E
pytest -m helper -v      # Testes helper

# Gerar relatório HTML (após instalar pytest-html)
pytest --html=reports/html/report.html
```

---

## 🔧 Configurações Importantes

### Chrome Driver Manager
**Arquivo:** `src/core/driver_manager.py`

```python
# Configurações aplicadas:
- Download automático bloqueado (automatic_downloads: 2)
- Modo headless opcional via .env
- Window size configurável
- Waits implícitos e explícitos
- Suporte a devtools para injeção de token
```

### Pytest Configuration
**Arquivo:** `pytest.ini`

```ini
[pytest]
markers =
    e2e: Testes end-to-end completos
    smoke: Testes smoke (rápidos)
    integration: Testes de integração
    helper: Testes auxiliares (locators, debug)
```

### Auto-Login
**Implementado em:** `src/pages/login_page.py`

Utiliza Chrome DevTools Protocol para injetar token:
```python
driver.execute_cdp_cmd('Storage.setLocalStorageItems', {
    'storageId': {'origin': FRONTEND_URL},
    'items': [{'key': 'sb-<projeto>-auth-token', 'value': token}]
})
```

---

## 🐛 Problemas Resolvidos e Soluções

### 1. Erro de ExecutionPolicy no PowerShell
**Problema:** Scripts .ps1 bloqueados  
**Solução:**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Locators de Botões vs Dropdown
**Problema:** Tipo de imóvel era dropdown, não botões  
**Solução:** Usar `Select().select_by_value("URBANO")`
```python
from selenium.webdriver.support.ui import Select
select = Select(element)
select.select_by_value("URBANO")  # Usa value, não texto com emoji
```

### 3. Downloads Automáticos de JSON
**Problema:** Frontend baixava JSON a cada etapa concluída  
**Solução:** Bloquear downloads no Chrome
```python
prefs = {
    "download.prompt_for_download": False,
    "profile.default_content_setting_values.automatic_downloads": 2
}
options.add_experimental_option("prefs", prefs)
```

### 4. Credenciais Git Incorretas
**Problema:** Git usava usuário antigo (wmiltecti)  
**Solução:**
```powershell
# Limpar credenciais antigas
cmdkey /delete:LegacyGeneric:target=git:https://github.com

# Reconfigurar
git config --global user.name "wmtechti"
git config --global user.email "wmtechti@gmail.com"
```

---

## 📝 Padrões e Boas Práticas

### Page Object Model
- Cada página/etapa tem sua própria classe
- Locators definidos como constantes de classe
- Métodos representam ações do usuário
- Não há assertions dentro dos Page Objects

### Waits
- **Implicit Wait:** 10 segundos (padrão)
- **Explicit Wait:** 20 segundos (operações específicas)
- Uso de `WebDriverWait` para elementos dinâmicos
- Helpers de espera em `src/utils/wait_helper.py`

### Locators
- Preferência: `data-testid` > `id` > `class` > `xpath`
- XPath usado apenas quando necessário
- Textos visíveis evitados (podem conter emojis)
- Valores de atributos preferidos

### Exemplo de Locator com Dropdown:
```python
# ❌ Evitar (texto com emoji)
select.select_by_visible_text("🏙️ URBANO")

# ✅ Usar (value do option)
select.select_by_value("URBANO")
```

---

## 🎨 Características Específicas do Frontend

### Botões de Auto-Fill
- **Cor:** Roxo ou Verde
- **Texto:** "Preencher Dados"
- **Função:** Preenche automaticamente todos os campos da etapa
- **Presentes em:** Dados Gerais, Atividades, Caracterização

### Dropdown de Tipo de Imóvel
```html
<select>
  <option value="">Selecione</option>
  <option value="URBANO">🏙️ URBANO</option>
  <option value="RURAL">🌾 RURAL</option>
  <option value="LINEAR">🛤️ LINEAR</option>
</select>
```

### Botões de Navegação
- **"Salvar"**: Salva dados da etapa atual
- **"Próximo"**: Avança para próxima etapa (após salvar)
- **"Finalizar"**: Conclui o cadastro (última etapa)

---

## 📊 Estado Atual do Projeto

### ✅ Completado
- [x] Estrutura completa do projeto (40+ arquivos)
- [x] Configuração de ambiente (Python, Selenium, Pytest)
- [x] Core framework (DriverManager, BaseTest, Orchestrator)
- [x] Todos os Page Objects (Login, Empreendimento, 4 wizard steps)
- [x] Teste E2E completo funcionando (6 etapas)
- [x] Auto-login via token JWT
- [x] Bloqueio de downloads automáticos
- [x] Documentação completa
- [x] Git configurado e código no GitHub

### 🔄 Em Uso
- Ambiente virtual Python: `d:\projetos\licenciamento-testes-e3e\venv`
- ChromeDriver gerenciado automaticamente
- Testes executando em ~52 segundos

### 📌 Observações Importantes

1. **Arquivo .env NÃO está no Git**
   - Configurar manualmente em cada ambiente
   - Copiar de `.env.example` e preencher com dados reais

2. **Token JWT expira**
   - Renovar periodicamente
   - Sintoma: teste de login falha

3. **Frontend e Backend devem estar rodando**
   - Antes de executar os testes
   - Verificar URLs: http://localhost:5173 e http://localhost:8000

4. **ChromeDriver é gerenciado automaticamente**
   - Webdriver-manager faz download se necessário
   - Primeira execução pode demorar mais

---

## 🔜 Próximos Passos (Projeto Principal)

### Diferenças Esperadas no Projeto Principal
- ⚠️ **Dados de tela alterados** (nomes, labels, estrutura)
- ⚠️ **Regras de negócio modificadas**
- ⚠️ **Novos campos ou etapas podem ter sido adicionados**

### Para Adaptar ao Projeto Principal

1. **Atualizar Locators**
   - Inspecionar elementos no frontend real
   - Atualizar constantes nas classes Page Object
   - Usar `test_helper_locators.py` para debug

2. **Atualizar Fluxo de Negócio**
   - Verificar etapas do wizard
   - Confirmar botões de auto-fill
   - Validar campos obrigatórios

3. **Atualizar Fixtures**
   - Ajustar dados de teste em `src/fixtures/`
   - Garantir que JSON está atualizado

4. **Executar Testes Incrementalmente**
   ```powershell
   # Testar etapa por etapa
   pytest tests/test_01_login.py -v
   pytest tests/test_debug_dropdown.py -v
   # ... validar cada passo antes do fluxo completo
   ```

---

## 📞 Informações de Suporte

### Comandos Úteis de Debug

```powershell
# Verificar ambiente
python .\check_environment.ps1

# Verificar configuração Git
git config --global --list

# Verificar status do repositório
git status

# Ver histórico de commits
git log --oneline

# Executar teste com debug
pytest -v -s --pdb
```

### Arquivos de Referência
- **Testes originais:** `tests/analisar/` (código fornecido pelo usuário)
- **Teste atual:** `tests/integration/test_fluxo_completo.py`
- **Documentação:** `docs/` (ARCHITECTURE, COMMANDS, SETUP, LOCATORS_GUIDE)

---

## 🎓 Conceitos Importantes

### Page Object Model (POM)
Padrão de design que separa a lógica de localização de elementos da lógica de teste.

**Vantagens:**
- Manutenção facilitada (alteração em 1 lugar)
- Reutilização de código
- Testes mais legíveis

### Selenium Waits
- **Implicit:** Espera global para todos os elementos
- **Explicit:** Espera específica com condição
- **Fluent:** Espera com polling customizado

### Pytest Fixtures
Funções que fornecem dados/recursos para testes.
- **Escopo:** function, class, module, session
- **Autouse:** Executam automaticamente
- **Parametrize:** Geram múltiplos testes

---

## 📄 Licença

Este é um projeto interno para testes automatizados. Verifique políticas da empresa antes de compartilhar externamente.

---

## 📅 Histórico de Versões

### v1.0.0 - 02/02/2026
- ✅ Projeto inicial criado
- ✅ Estrutura completa implementada
- ✅ Teste E2E funcionando
- ✅ Documentação completa
- ✅ Código versionado no GitHub

---

**Última atualização:** 03/02/2026  
**Autor:** Desenvolvido com auxílio do GitHub Copilot  
**Repositório:** https://github.com/wmtechti/licenciamento-ambiental-testes-e2e
