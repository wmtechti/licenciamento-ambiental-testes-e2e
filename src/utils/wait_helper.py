"""
Helper para esperas (waits)
============================

Funções auxiliares para esperar elementos e condições.
"""

from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ..config.settings import settings


class WaitHelper:
    """Helper para esperas no Selenium."""
    
    @staticmethod
    def wait_for_element(
        driver: webdriver.Chrome,
        locator: Tuple[By, str],
        timeout: int = None,
        condition: str = "presence"
    ):
        """
        Aguarda elemento estar disponível.
        
        Args:
            driver: Instância do WebDriver
            locator: Tupla (By, valor) do localizador
            timeout: Tempo máximo de espera
            condition: Tipo de condição (presence, visible, clickable)
            
        Returns:
            WebElement: Elemento encontrado
            
        Raises:
            TimeoutException: Se elemento não for encontrado
        """
        if timeout is None:
            timeout = settings.TEST_TIMEOUT
        
        wait = WebDriverWait(driver, timeout)
        
        conditions = {
            'presence': EC.presence_of_element_located,
            'visible': EC.visibility_of_element_located,
            'clickable': EC.element_to_be_clickable
        }
        
        condition_func = conditions.get(condition, EC.presence_of_element_located)
        
        return wait.until(condition_func(locator))
    
    @staticmethod
    def wait_for_text(
        driver: webdriver.Chrome,
        text: str,
        timeout: int = None
    ):
        """
        Aguarda texto aparecer na página.
        
        Args:
            driver: Instância do WebDriver
            text: Texto a procurar
            timeout: Tempo máximo de espera
            
        Returns:
            WebElement: Elemento com o texto
        """
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        return WaitHelper.wait_for_element(driver, locator, timeout, 'presence')
    
    @staticmethod
    def wait_for_url_contains(
        driver: webdriver.Chrome,
        url_part: str,
        timeout: int = None
    ) -> bool:
        """
        Aguarda URL conter parte específica.
        
        Args:
            driver: Instância do WebDriver
            url_part: Parte da URL a procurar
            timeout: Tempo máximo de espera
            
        Returns:
            bool: True se URL contém a parte
        """
        if timeout is None:
            timeout = settings.TEST_TIMEOUT
        
        wait = WebDriverWait(driver, timeout)
        
        try:
            wait.until(EC.url_contains(url_part))
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def wait_for_url_not_contains(
        driver: webdriver.Chrome,
        url_part: str,
        timeout: int = None
    ) -> bool:
        """
        Aguarda URL NÃO conter parte específica.
        
        Args:
            driver: Instância do WebDriver
            url_part: Parte da URL a evitar
            timeout: Tempo máximo de espera
            
        Returns:
            bool: True se URL não contém a parte
        """
        if timeout is None:
            timeout = settings.TEST_TIMEOUT
        
        wait = WebDriverWait(driver, timeout)
        
        try:
            wait.until_not(EC.url_contains(url_part))
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def wait_for_element_disappear(
        driver: webdriver.Chrome,
        locator: Tuple[By, str],
        timeout: int = None
    ) -> bool:
        """
        Aguarda elemento desaparecer.
        
        Args:
            driver: Instância do WebDriver
            locator: Tupla (By, valor) do localizador
            timeout: Tempo máximo de espera
            
        Returns:
            bool: True se elemento desapareceu
        """
        if timeout is None:
            timeout = settings.TEST_TIMEOUT
        
        wait = WebDriverWait(driver, timeout)
        
        try:
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
