"""
Classe Base para Testes
========================

Fornece funcionalidades comuns para todos os testes.
"""

import time
from typing import Optional
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from .driver_manager import DriverManager
from ..config.settings import settings, SCREENSHOTS_DIR


class BaseTest:
    """Classe base para todos os testes."""
    
    def __init__(self):
        """Inicializa o teste."""
        self.driver: Optional[webdriver.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
    
    def setup(self, driver: Optional[webdriver.Chrome] = None) -> None:
        """
        Configura o teste.
        
        Args:
            driver: Driver existente (opcional)
        """
        if driver:
            self.driver = driver
        else:
            self.driver = DriverManager.create_driver()
        
        self.wait = DriverManager.create_wait(self.driver)
    
    def teardown(self, close_driver: bool = True) -> None:
        """
        Finaliza o teste.
        
        Args:
            close_driver: Se deve fechar o navegador
        """
        if close_driver and self.driver:
            DriverManager.quit_driver(self.driver)
            self.driver = None
            self.wait = None
    
    def take_screenshot(self, name: str = None) -> str:
        """
        Captura screenshot da tela atual.
        
        Args:
            name: Nome do arquivo (sem extensão)
            
        Returns:
            str: Caminho do arquivo salvo
        """
        if not self.driver:
            return ""
        
        if not name:
            name = f"screenshot_{int(time.time())}"
        
        filepath = SCREENSHOTS_DIR / f"{name}.png"
        self.driver.save_screenshot(str(filepath))
        
        return str(filepath)
    
    def go_to_url(self, url: str) -> None:
        """
        Navega para uma URL.
        
        Args:
            url: URL de destino
        """
        if self.driver:
            self.driver.get(url)
    
    def get_current_url(self) -> str:
        """
        Retorna a URL atual.
        
        Returns:
            str: URL atual
        """
        if self.driver:
            return self.driver.current_url
        return ""
    
    def wait_seconds(self, seconds: float) -> None:
        """
        Aguarda um tempo específico.
        
        Args:
            seconds: Segundos para aguardar
        """
        time.sleep(seconds)
