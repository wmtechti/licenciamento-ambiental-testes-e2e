"""
Page Object - Página de Empreendimentos
========================================

Representa a página de listagem de empreendimentos.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ..config.urls import urls
from ..utils.wait_helper import WaitHelper


class EmpreendimentoPage:
    """Page Object para a página de empreendimentos."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a página de empreendimentos.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    MENU_EMPREENDIMENTO = (By.XPATH, "//button[contains(., 'Empreendimento')]")
    NOVO_EMPREENDIMENTO_BTN = (By.XPATH, "//button[contains(., 'Novo Empreendimento')]")
    PAGE_TITLE = (By.XPATH, "//*[contains(text(), 'Empreendimento')]")
    
    def navigate_from_menu(self) -> bool:
        """
        Navega para empreendimentos através do menu.
        
        Returns:
            bool: True se navegação foi bem-sucedida
        """
        print("📂 Navegando para menu Empreendimento...")
        
        # Clicar no menu
        menu_btn = WaitHelper.wait_for_element(
            self.driver, self.MENU_EMPREENDIMENTO, condition='clickable'
        )
        menu_btn.click()
        time.sleep(2)
        
        # Verificar se navegou
        try:
            WaitHelper.wait_for_element(self.driver, self.PAGE_TITLE)
            print("✅ Navegou para página de Empreendimentos")
            return True
        except:
            print("❌ Falha ao navegar para Empreendimentos")
            return False
    
    def click_novo_empreendimento(self) -> bool:
        """
        Clica no botão Novo Empreendimento.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("➕ Clicando em 'Novo Empreendimento'...")
        
        try:
            novo_btn = WaitHelper.wait_for_element(
                self.driver, self.NOVO_EMPREENDIMENTO_BTN, condition='clickable'
            )
            novo_btn.click()
            time.sleep(2)
            
            print("✅ Clicou em 'Novo Empreendimento'")
            return True
        except:
            print("❌ Falha ao clicar em 'Novo Empreendimento'")
            return False
    
    def wizard_is_open(self) -> bool:
        """
        Verifica se o wizard foi aberto.
        
        Returns:
            bool: True se wizard está aberto
        """
        wizard_title_locator = (By.XPATH, "//*[contains(text(), 'Novo Empreendimento')]")
        
        try:
            WaitHelper.wait_for_element(self.driver, wizard_title_locator)
            print("✅ Wizard aberto")
            return True
        except:
            print("❌ Wizard não foi aberto")
            return False
