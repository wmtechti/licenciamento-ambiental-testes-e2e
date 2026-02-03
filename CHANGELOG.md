# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2026-02-02

### Adicionado
- Estrutura inicial do projeto
- Page Object Model para login e empreendimentos
- Testes de login com auto-login via token
- Testes de navegação para novo empreendimento
- Configuração de ambiente via `.env`
- DriverManager para gerenciar WebDriver
- WaitHelper para esperas explícitas
- ScreenshotHelper para captura em falhas
- JSONHelper para manipulação de dados
- Fixtures de dados (empresas, imóveis, atividades)
- Configuração do Pytest com markers
- Geração de relatórios HTML
- Documentação completa (README, SETUP, ARCHITECTURE)
- Arquivo .gitignore configurado
- Requirements.txt com dependências
- Setup.py para instalação do projeto

### Configurado
- Pytest com markers personalizados (smoke, e2e, integration, slow)
- GitHub Actions ready (estrutura preparada)
- ChromeDriver configurável (local ou webdriver-manager)
- Screenshots automáticos em falhas
- Timeout configurável

### Documentado
- README.md completo com guia de uso
- SETUP.md com instruções passo a passo
- ARCHITECTURE.md explicando a arquitetura
- Docstrings em todas as classes e métodos
- Comentários em código complexo

## [Não Lançado]

### Planejado
- Testes para edição de empreendimentos
- Testes para exclusão de empreendimentos
- Testes de validação de campos
- Integração com banco de dados para validações
- Relatórios Allure
- Testes paralelos otimizados
- CI/CD completo no GitHub Actions
- Testes multi-browser (Firefox, Edge)
