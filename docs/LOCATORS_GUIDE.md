# 🔍 Guia de Ajuste de Locators

## Por que ajustar?

Os **locators** (seletores) são os "endereços" que o Selenium usa para encontrar elementos na página. Cada aplicação tem HTML diferente, então você precisa ajustar os locators para corresponder ao seu frontend.

---

## 🛠️ Como Inspecionar Elementos

### Método 1: DevTools do Chrome

1. **Abra o frontend** no Chrome
2. **Abra DevTools**: `F12` ou `Ctrl+Shift+I`
3. **Ative o seletor**: Clique no ícone de seta 🔍 ou `Ctrl+Shift+C`
4. **Clique no elemento** que quer localizar
5. **No DevTools**, veja o HTML do elemento

### Método 2: Executar Teste e Pausar

```python
# No seu teste, adicione:
import pdb; pdb.set_trace()

# Ou usar input():
input("Pressione ENTER após inspecionar...")
```

---

## 📝 Tipos de Locators

### 1. Por ID (Mais confiável)
```python
# HTML: <button id="btn-novo">Novo</button>
(By.ID, "btn-novo")
```

### 2. Por XPATH (Mais flexível)
```python
# Texto exato
(By.XPATH, "//button[text()='Novo Empreendimento']")

# Texto contém
(By.XPATH, "//button[contains(., 'Novo')]")

# Por atributo
(By.XPATH, "//button[@data-testid='novo-btn']")

# Por classe
(By.XPATH, "//button[@class='btn-primary']")
```

### 3. Por CSS Selector
```python
# Por classe
(By.CSS_SELECTOR, ".btn-novo")

# Por ID
(By.CSS_SELECTOR, "#btn-novo")

# Combinado
(By.CSS_SELECTOR, "button.btn-primary[data-testid='novo']")
```

---

## 🎯 Exemplo Prático: Ajustar Botão "Urbano"

### Passo 1: Inspecionar o Elemento

No seu frontend, inspecione o botão "Urbano". Você verá algo como:

```html
<button 
  class="tipo-imovel-btn urbano"
  data-tipo="URBANO"
  onclick="selecionarTipo('urbano')"
>
  Urbano
</button>
```

### Passo 2: Escolher o Melhor Locator

Opções (em ordem de preferência):

```python
# Opção 1: Por data attribute (melhor se existir)
BTN_URBANO = (By.XPATH, "//button[@data-tipo='URBANO']")

# Opção 2: Por classe específica
BTN_URBANO = (By.CSS_SELECTOR, "button.urbano")

# Opção 3: Por texto
BTN_URBANO = (By.XPATH, "//button[contains(text(), 'Urbano')]")

# Opção 4: Por combinação de classe + texto
BTN_URBANO = (By.XPATH, "//button[contains(@class, 'tipo-imovel-btn') and contains(., 'Urbano')]")
```

### Passo 3: Atualizar no Page Object

Edite `src/pages/wizard/imovel_step.py`:

```python
class ImovelStep:
    # ANTES (genérico)
    BTN_URBANO = (By.XPATH, "//button[contains(., 'Urbano')]")
    
    # DEPOIS (específico para seu frontend)
    BTN_URBANO = (By.XPATH, "//button[@data-tipo='URBANO']")
```

---

## 🔍 Descobrir Locators do Seu Wizard

### Elementos que você precisa localizar:

#### 1. Etapa Imóvel
- [ ] Botão "Rural"
- [ ] Botão "Urbano"  
- [ ] Botão "Linear"
- [ ] Botão "Preencher"
- [ ] Botão "Próximo"
- [ ] Campos do formulário (nome, área, etc)

#### 2. Etapa Dados Gerais
- [ ] Campos do formulário
- [ ] Botão "Próximo"
- [ ] Botão "Voltar"

#### 3. Etapa Atividades
- [ ] Botão "Adicionar Atividade"
- [ ] Campos de busca/seleção de atividade
- [ ] Campo de quantidade
- [ ] Botão "Próximo"

#### 4. Etapa Caracterização
- [ ] Campos de caracterização
- [ ] Botão "Finalizar"

---

## 🧪 Teste os Locators no Console

No DevTools, aba Console, teste seus XPath:

```javascript
// Testar XPath
$x("//button[contains(., 'Urbano')]")

// Testar CSS Selector
$$("button.urbano")

// Se retornar elementos, o locator está correto!
```

---

## 📋 Template para Atualizar Locators

### Arquivo: `src/pages/wizard/imovel_step.py`

```python
class ImovelStep:
    """Page Object para a etapa de Imóvel do wizard."""
    
    # ============================================
    # ATUALIZE ESTES LOCATORS CONFORME SEU HTML
    # ============================================
    
    # Títulos e identificadores
    STEP_TITLE = (By.XPATH, "//*[contains(text(), 'Imóvel')]")
    
    # Botões de tipo de imóvel
    BTN_RURAL = (By.XPATH, "SEU_LOCATOR_AQUI")
    BTN_URBANO = (By.XPATH, "SEU_LOCATOR_AQUI")
    BTN_LINEAR = (By.XPATH, "SEU_LOCATOR_AQUI")
    
    # Botões de ação
    BTN_PREENCHER = (By.XPATH, "SEU_LOCATOR_AQUI")
    BTN_PROXIMO = (By.XPATH, "SEU_LOCATOR_AQUI")
    
    # Campos do formulário (se necessário)
    INPUT_NOME = (By.ID, "nomeImovel")  # Exemplo
    INPUT_AREA = (By.ID, "area")        # Exemplo
```

---

## 🚀 Workflow Recomendado

1. **Executar teste** com `pytest -v -s`
2. **Ver onde falha** (qual locator não foi encontrado)
3. **Abrir frontend** e inspecionar o elemento
4. **Descobrir o locator** correto
5. **Atualizar** no Page Object
6. **Re-executar** o teste
7. **Repetir** até todos os locators estarem corretos

---

## 💡 Dicas Importantes

### ✅ Boas Práticas

1. **Prefira IDs** - Mais estáveis
2. **Use data attributes** - `data-testid`, `data-test`, etc
3. **Evite classes CSS** - Mudam com redesigns
4. **Evite XPath complexos** - Frágeis e difíceis de manter

### ⚠️ Locators Frágeis (Evitar)

```python
# ❌ Muito específico (quebra fácil)
(By.XPATH, "/html/body/div[2]/div/div[3]/button[1]")

# ❌ Depende de estrutura
(By.XPATH, "//div/div/div/button")

# ❌ Índice fixo
(By.XPATH, "//button[1]")
```

### ✅ Locators Robustos (Preferir)

```python
# ✅ Por ID único
(By.ID, "novo-empreendimento-btn")

# ✅ Por data attribute
(By.XPATH, "//button[@data-testid='novo-empreendimento']")

# ✅ Por texto específico
(By.XPATH, "//button[text()='Novo Empreendimento']")

# ✅ Combinação inteligente
(By.XPATH, "//div[@class='wizard-step']//button[contains(., 'Próximo')]")
```

---

## 📞 Precisa de Ajuda?

1. Execute o teste e veja o erro
2. Inspeccione o elemento no Chrome DevTools
3. Teste o locator no console do navegador
4. Atualize no Page Object
5. Se ainda tiver dúvidas, compartilhe o HTML do elemento

---

## 🎯 Próximo Passo

Execute este comando para ver onde os locators precisam ser ajustados:

```powershell
pytest tests/integration/test_fluxo_completo.py -v -s
```

O teste mostrará exatamente qual locator falhou. Inspeccione esse elemento e atualize!
