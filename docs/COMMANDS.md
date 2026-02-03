# 📖 Guia de Comandos Úteis

## Setup Inicial

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
cp .env.example .env
```

## Executar Testes

### Básico

```powershell
# Todos os testes
pytest

# Com mais detalhes
pytest -v

# Com output detalhado
pytest -v -s

# Mostrar print statements
pytest -s
```

### Por Arquivo

```powershell
# Teste específico
pytest tests/test_01_login.py

# Diretório específico
pytest tests/integration/

# Função específica
pytest tests/test_01_login.py::test_login_e_navegacao
```

### Por Marcadores

```powershell
# Apenas testes smoke
pytest -m smoke

# Apenas testes E2E
pytest -m e2e

# Apenas testes de integração
pytest -m integration

# Excluir testes lentos
pytest -m "not slow"

# Combinar marcadores
pytest -m "smoke and not slow"
```

### Com Relatórios

```powershell
# Relatório HTML
pytest --html=reports/html/report.html --self-contained-html

# Abrir relatório
start reports/html/report.html

# Relatório com cobertura (se pytest-cov instalado)
pytest --cov=src --cov-report=html
```

### Opções Úteis

```powershell
# Parar no primeiro erro
pytest -x

# Parar após N falhas
pytest --maxfail=2

# Executar último teste que falhou
pytest --lf

# Executar testes que falharam e depois os outros
pytest --ff

# Modo verbose com timing
pytest -v --durations=10

# Executar testes em paralelo (4 processos)
pytest -n 4
```

## Verificação de Código

### Linting

```powershell
# Verificar estilo de código
flake8 src/ tests/

# Verificar com configuração customizada
flake8 src/ tests/ --max-line-length=100 --exclude=venv

# Verificar apenas src
flake8 src/
```

### Formatação

```powershell
# Formatar código
black src/ tests/

# Ver o que seria formatado (dry-run)
black --check src/ tests/

# Formatar apenas src
black src/
```

### Type Checking

```powershell
# Verificar tipos
mypy src/

# Com mais detalhes
mypy src/ --strict
```

## Gerenciamento de Dependências

```powershell
# Listar pacotes instalados
pip list

# Verificar se pacote está instalado
pip show selenium

# Instalar novo pacote
pip install nome-do-pacote

# Atualizar requirements.txt
pip freeze > requirements.txt

# Atualizar pacote
pip install --upgrade nome-do-pacote

# Desinstalar pacote
pip uninstall nome-do-pacote
```

## Git

```powershell
# Status
git status

# Adicionar arquivos
git add .

# Commit
git commit -m "feat: adiciona nova funcionalidade"

# Push
git push origin nome-da-branch

# Pull
git pull origin main

# Criar nova branch
git checkout -b feature/nova-feature

# Voltar para main
git checkout main

# Ver histórico
git log --oneline
```

## ChromeDriver

```powershell
# Verificar versão
C:\chromedriver\chromedriver.exe --version

# Verificar versão do Chrome
(Get-Item "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo.FileVersion
```

## Ambiente

```powershell
# Verificar Python
python --version

# Verificar pip
pip --version

# Ver variáveis de ambiente
Get-Content .env

# Editar .env
notepad .env
```

## Limpeza

```powershell
# Limpar cache do Python
Remove-Item -Recurse -Force __pycache__, .pytest_cache

# Limpar reports antigos
Remove-Item -Recurse -Force reports/html/*.html, reports/screenshots/*.png

# Limpar output antigo
Remove-Item -Recurse -Force output/*.json
```

## Debugging

```powershell
# Executar com debugger
pytest --pdb

# Parar em falha
pytest --pdb -x

# Verbose máximo
pytest -vv

# Mostrar fixtures disponíveis
pytest --fixtures

# Mostrar marcadores disponíveis
pytest --markers
```

## Scripts Customizados

```powershell
# Verificar ambiente
.\check_environment.ps1

# Executar teste específico (exemplo)
python tests/test_01_login.py
```

## VS Code

```powershell
# Abrir no VS Code
code .

# Abrir arquivo específico
code tests/test_01_login.py

# Abrir em nova janela
code . -n
```

## Atalhos Úteis

```powershell
# Criar alias temporários (na sessão atual)
Set-Alias pt pytest
Set-Alias act .\venv\Scripts\Activate.ps1

# Usar aliases
pt -v
act
```

## Comandos Completos Úteis

```powershell
# Setup completo do zero
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; cp .env.example .env

# Executar testes com relatório completo
pytest -v --html=reports/html/report.html --self-contained-html; start reports/html/report.html

# Limpar, verificar e executar
Remove-Item -Recurse -Force .pytest_cache; flake8 src/ tests/; black src/ tests/ --check; pytest -v

# Atualizar tudo
git pull; pip install --upgrade -r requirements.txt; pytest -v
```

## Dicas

- Use `tab` para autocompletar comandos
- Use `↑` e `↓` para navegar no histórico de comandos
- Use `Ctrl+C` para interromper execução
- Use `cls` para limpar o terminal
- Use `Get-Help comando` para ajuda sobre comandos PowerShell
