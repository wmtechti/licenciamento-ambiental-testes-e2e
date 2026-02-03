# Arquitetura do Projeto de Testes E2E

## Visão Geral

Este projeto utiliza uma arquitetura baseada em **Page Object Model (POM)** combinada com **fixtures do Pytest** para criar testes E2E manuteníveis e escaláveis.

## Camadas da Arquitetura

```
┌─────────────────────────────────────┐
│         Testes (tests/)             │
│   - test_01_login.py                │
│   - test_02_cadastro.py             │
│   - integration/test_fluxo.py       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Page Objects (src/pages/)      │
│   - LoginPage                       │
│   - EmpreendimentoPage              │
│   - Wizard Steps                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Core & Utils (src/core/)       │
│   - DriverManager                   │
│   - BaseTest                        │
│   - WaitHelper                      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    Selenium WebDriver               │
└─────────────────────────────────────┘
```

## Componentes Principais

### 1. Tests (`tests/`)

Contém os testes propriamente ditos. Cada teste:
- Usa Page Objects para interagir com a UI
- Foca em validações de alto nível
- Não contém lógica de localização de elementos

**Exemplo:**
```python
def test_login(driver, wait):
    login_page = LoginPage(driver, wait)
    assert login_page.auto_login()
```

### 2. Page Objects (`src/pages/`)

Representa cada página/componente da aplicação:
- Encapsula locators (seletores)
- Fornece métodos de interação
- Esconde detalhes de implementação do Selenium

**Exemplo:**
```python
class LoginPage:
    USERNAME_INPUT = (By.ID, "username")
    
    def login(self, user, pwd):
        # Implementação...
```

### 3. Core (`src/core/`)

Funcionalidades centrais:
- **DriverManager**: Gerencia criação do WebDriver
- **BaseTest**: Classe base com funcionalidades comuns
- **Orchestrator**: Executa múltiplos testes em sequência

### 4. Utils (`src/utils/`)

Utilitários auxiliares:
- **WaitHelper**: Helpers para esperas
- **ScreenshotHelper**: Captura de screenshots
- **JSONHelper**: Manipulação de JSON

### 5. Config (`src/config/`)

Configurações:
- **Settings**: Carrega variáveis de ambiente
- **URLs**: Centraliza URLs do sistema

### 6. Fixtures (`src/fixtures/`)

Dados de teste em JSON:
- `empresas.json` - Dados de empresas
- `imoveis.json` - Dados de imóveis
- `atividades.json` - Dados de atividades

## Fluxo de Execução

### Execução de um Teste

```
1. Pytest carrega conftest.py
   └─ Define fixtures (driver, wait, etc)

2. Teste é iniciado
   └─ Fixtures são injetadas

3. Teste usa Page Objects
   └─ Page Objects usam WaitHelper
      └─ WaitHelper usa WebDriver

4. Teste faz asserções
   └─ Pytest valida resultados

5. Teardown
   └─ Screenshots (se falhou)
   └─ Fecha browser
   └─ Gera relatórios
```

### Fluxo de um Page Object

```python
# 1. Teste chama método do Page Object
login_page.auto_login()

# 2. Page Object localiza elemento
element = WaitHelper.wait_for_element(
    driver, LOGIN_BUTTON, condition='clickable'
)

# 3. Page Object interage
element.click()

# 4. Page Object valida resultado
return self.is_logged_in()
```

## Padrões Utilizados

### 1. Page Object Model

- Cada página = Uma classe
- Locators = Constantes de classe
- Ações = Métodos públicos

### 2. Dependency Injection (Fixtures)

```python
@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_something(driver):  # Injetado automaticamente
    # usar driver
```

### 3. Wait Pattern

Sempre usar waits explícitos:
```python
# ❌ Evitar
element = driver.find_element(By.ID, "btn")

# ✅ Preferir
element = WaitHelper.wait_for_element(
    driver, (By.ID, "btn"), condition='clickable'
)
```

### 4. Single Responsibility

Cada classe/método tem UMA responsabilidade:
- `DriverManager` → Criar drivers
- `LoginPage` → Interagir com login
- `WaitHelper` → Gerenciar esperas

## Vantagens desta Arquitetura

1. **Manutenibilidade**
   - Mudanças na UI afetam apenas Page Objects
   - Testes permanecem estáveis

2. **Reutilização**
   - Page Objects são compartilhados entre testes
   - Utils são genéricos

3. **Legibilidade**
   - Testes leem como casos de uso
   - Lógica complexa fica nos Page Objects

4. **Testabilidade**
   - Cada componente pode ser testado isoladamente
   - Mock de dependências é fácil

## Exemplo Completo

### Teste
```python
def test_cadastro_empreendimento(driver, wait):
    # Login
    login = LoginPage(driver, wait)
    login.auto_login()
    
    # Navegar
    emp = EmpreendimentoPage(driver, wait)
    emp.navigate_from_menu()
    emp.click_novo_empreendimento()
    
    # Wizard
    imovel = ImovelStep(driver, wait)
    imovel.select_tipo_imovel("URBANO")
    imovel.click_proximo()
    
    # Validar
    assert imovel.is_next_step_visible()
```

### Page Object
```python
class ImovelStep:
    BTN_URBANO = (By.XPATH, "//button[contains(., 'Urbano')]")
    
    def select_tipo_imovel(self, tipo):
        btn = WaitHelper.wait_for_element(
            self.driver, self.BTN_URBANO, 'clickable'
        )
        btn.click()
        return True
```

## Extensibilidade

Para adicionar novos recursos:

1. **Nova Página?** → Criar novo Page Object em `src/pages/`
2. **Novo Teste?** → Criar em `tests/`
3. **Nova Funcionalidade?** → Adicionar em `src/utils/` ou `src/core/`
4. **Novos Dados?** → Adicionar em `src/fixtures/`

## Referências

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
