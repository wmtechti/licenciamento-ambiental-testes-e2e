"""
Teste Debug - Inspecionar Dropdown de Tipo de Imóvel
=====================================================

Teste para investigar as opções reais do dropdown.
"""

import pytest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from src.utils.wait_helper import WaitHelper
from src.pages.login_page import LoginPage
from src.pages.empreendimento_page import EmpreendimentoPage

@pytest.mark.helper
def test_inspecionar_dropdown(driver, wait):
    """Inspeciona o dropdown para ver todas as opções disponíveis."""
    
    print("\n" + "="*60)
    print("  🔍 DEBUG - DROPDOWN TIPO DE IMÓVEL")
    print("="*60 + "\n")
    
    # Criar páginas
    login_page = LoginPage(driver, wait)
    emp_page = EmpreendimentoPage(driver, wait)
    
    # Auto-login e navegar
    print("1️⃣ Fazendo auto-login...")
    login_page.auto_login()
    
    print("2️⃣ Navegando para Novo Empreendimento...")
    emp_page.navigate_from_menu()
    emp_page.click_novo_empreendimento()
    
    time.sleep(3)
    
    print("\n3️⃣ Procurando dropdown...")
    
    try:
        SELECT_LOCATOR = (By.XPATH, "//select")
        
        select_element = WaitHelper.wait_for_element(
            driver, SELECT_LOCATOR, condition='visible', timeout=10
        )
        
        print("✅ Dropdown encontrado!\n")
        
        # Criar objeto Select
        select = Select(select_element)
        
        # Listar todas as opções
        print("📋 OPÇÕES DO DROPDOWN:")
        print("-" * 60)
        
        for i, option in enumerate(select.options):
            value = option.get_attribute('value')
            text = option.text
            print(f"{i}. Valor: '{value}' | Texto: '{text}'")
            print(f"   Repr bytes: {repr(text.encode('utf-8'))}")
        
        print("-" * 60)
        
        print("\n⏸️  Pressione ENTER para continuar...")
        input()
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        
        # Tentar listar todos os selects
        print("\n🔍 Procurando TODOS os <select> na página...")
        selects = driver.find_elements(By.TAG_NAME, "select")
        print(f"   Encontrados: {len(selects)} elementos <select>")
        
        for i, sel in enumerate(selects):
            print(f"\n   Select #{i+1}:")
            print(f"   - Visível: {sel.is_displayed()}")
            print(f"   - ID: {sel.get_attribute('id')}")
            print(f"   - Class: {sel.get_attribute('class')}")
            print(f"   - Name: {sel.get_attribute('name')}")
        
        print("\n⏸️  Pressione ENTER para fechar...")
        input()
