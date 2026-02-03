"""
Page Object - Página de Login
==============================

Representa a página de login do sistema.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ..config.urls import urls
from ..utils.wait_helper import WaitHelper


class LoginPage:
    """Page Object para a página de login."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a página de login.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Entrar')]")
    
    def navigate(self) -> None:
        """Navega para a página de login."""
        self.driver.get(urls.LOGIN)
    
    def auto_login(self) -> bool:
        """
        Realiza auto-login via URL com token.
        
        Returns:
            bool: True se login foi bem-sucedido
        """
        print("🔐 Realizando auto-login via token...")
        
        # Acessar URL com token
        self.driver.get(urls.AUTO_LOGIN)
        time.sleep(3)
        
        # Aguardar processamento
        WaitHelper.wait_for_url_not_contains(self.driver, 'login')
        
        # Verificar se está autenticado
        current_url = self.driver.current_url
        is_authenticated = 'login' not in current_url.lower() or '?' in current_url
        
        if is_authenticated:
            print("✅ Auto-login realizado com sucesso")
        else:
            print("❌ Falha no auto-login")
        
        return is_authenticated
    
    def login(self, username: str, password: str) -> bool:
        """
        Realiza login manual.
        
        Args:
            username: Nome de usuário
            password: Senha
            
        Returns:
            bool: True se login foi bem-sucedido
        """
        # Preencher campos
        username_field = WaitHelper.wait_for_element(
            self.driver, self.USERNAME_INPUT, condition='visible'
        )
        username_field.clear()
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        
        # Clicar em entrar
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        
        # Aguardar redirecionamento
        time.sleep(2)
        
        # Verificar se login foi bem-sucedido
        return 'login' not in self.driver.current_url.lower()
