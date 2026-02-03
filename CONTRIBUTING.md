# Guia de Contribuição

Obrigado por considerar contribuir para este projeto! 🎉

## Como Contribuir

### Reportar Bugs

1. Verificar se o bug já não foi reportado em [Issues](https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e/issues)
2. Abrir nova issue com:
   - Título descritivo
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Versão do Chrome, Python, SO

### Sugerir Melhorias

1. Abrir issue com tag `enhancement`
2. Descrever a melhoria em detalhes
3. Explicar por que seria útil
4. Exemplos de uso (se possível)

### Contribuir com Código

#### 1. Fork e Clone

```bash
# Fork no GitHub
# Clone seu fork
git clone https://github.com/SEU-USUARIO/licenciamento-ambiental-testes-e2e.git
cd licenciamento-ambiental-testes-e2e

# Adicionar upstream
git remote add upstream https://github.com/wmiltecti/licenciamento-ambiental-testes-e2e.git
```

#### 2. Criar Branch

```bash
# Atualizar main
git checkout main
git pull upstream main

# Criar branch para feature
git checkout -b feature/nome-da-feature

# Ou para bugfix
git checkout -b fix/nome-do-bug
```

#### 3. Desenvolver

- Escrever código limpo e documentado
- Seguir padrões do projeto
- Adicionar testes para novas funcionalidades
- Atualizar documentação se necessário

#### 4. Testar

```bash
# Executar testes
pytest -v

# Verificar linting
flake8 src/ tests/

# Formatar código
black src/ tests/
```

#### 5. Commit

```bash
# Commits seguem padrão Conventional Commits
git add .
git commit -m "feat: adiciona nova funcionalidade X"
```

Tipos de commit:
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Manutenção

#### 6. Push e Pull Request

```bash
# Push para seu fork
git push origin feature/nome-da-feature

# Abrir PR no GitHub
# Descrever mudanças
# Referenciar issues relacionadas
```

## Padrões de Código

### Python

- Seguir [PEP 8](https://pep8.org/)
- Usar type hints
- Docstrings em todas as funções/classes
- Máximo 100 caracteres por linha

### Page Objects

```python
class NovaPage:
    """Descrição da página."""
    
    # Locators no topo
    BOTAO = (By.ID, "btn")
    
    def __init__(self, driver, wait):
        """Inicializa a página."""
        self.driver = driver
        self.wait = wait
    
    def metodo_acao(self) -> bool:
        """
        Descrição da ação.
        
        Returns:
            bool: True se sucesso
        """
        # Implementação
        return True
```

### Testes

```python
@pytest.mark.e2e
def test_nome_descritivo(driver, wait):
    """
    Descrição do que o teste valida.
    
    Args:
        driver: Fixture do WebDriver
        wait: Fixture do WebDriverWait
    """
    # Arrange (preparar)
    page = Page(driver, wait)
    
    # Act (executar)
    result = page.fazer_algo()
    
    # Assert (validar)
    assert result is True
```

## Estrutura de PR

### Título
- Claro e descritivo
- Seguir padrão de commits

### Descrição
```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Checklist
- [ ] Código segue os padrões do projeto
- [ ] Comentários adicionados em código complexo
- [ ] Documentação atualizada
- [ ] Testes adicionados/atualizados
- [ ] Todos os testes passam
- [ ] Sem warnings de linting

## Issues Relacionadas
Closes #123
```

## Code Review

### O que esperamos

- Código limpo e legível
- Testes abrangentes
- Documentação atualizada
- Sem código comentado
- Sem prints/debugs deixados

### Processo

1. Pelo menos 1 aprovação necessária
2. CI/CD deve passar
3. Resolver conversas antes do merge
4. Squash commits se necessário

## Dúvidas?

- Abrir issue com tag `question`
- Entrar em contato: contato@miltec.com.br

## Código de Conduta

- Ser respeitoso
- Aceitar críticas construtivas
- Focar no que é melhor para o projeto
- Mostrar empatia com outros contribuidores

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas
sob a mesma licença do projeto.
