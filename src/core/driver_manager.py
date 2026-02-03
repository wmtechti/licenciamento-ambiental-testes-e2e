"""
Gerenciador do WebDriver
=========================

Centraliza a criação e configuração do WebDriver.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from ..config.settings import settings


class DriverManager:
    """Gerenciador do WebDriver."""
    
    @staticmethod
    def create_driver(headless: bool = None, maximize: bool = None) -> webdriver.Chrome:
        """
        Cria uma nova instância do Chrome WebDriver.
        
        Args:
            headless: Executar em modo headless (sem interface gráfica)
            maximize: Maximizar janela do navegador
            
        Returns:
            webdriver.Chrome: Instância do Chrome WebDriver
        """
        # Usar configurações padrão se não fornecidas
        if headless is None:
            headless = settings.HEADLESS
        if maximize is None:
            maximize = settings.MAXIMIZE_WINDOW
        
        # Configurar opções do Chrome
        options = Options()
        
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        
        if maximize:
            options.add_argument('--start-maximized')
        
        # Opções adicionais para estabilidade
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # Desabilitar downloads automáticos
        prefs = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "profile.default_content_setting_values.automatic_downloads": 2  # 2 = bloquear
        }
        options.add_experimental_option("prefs", prefs)
        
        # Criar serviço do ChromeDriver
        if settings.USE_WEBDRIVER_MANAGER:
            # Usar webdriver-manager (baixa versão correta automaticamente)
            service = Service(ChromeDriverManager().install())
        else:
            # Usar ChromeDriver local
            service = Service(settings.CHROME_DRIVER_PATH)
        
        # Criar driver
        driver = webdriver.Chrome(service=service, options=options)
        
        # Configurar timeout implícito
        driver.implicitly_wait(5)
        
        return driver
    
    @staticmethod
    def create_wait(driver: webdriver.Chrome, timeout: int = None) -> WebDriverWait:
        """
        Cria uma instância do WebDriverWait.
        
        Args:
            driver: Instância do WebDriver
            timeout: Tempo máximo de espera em segundos
            
        Returns:
            WebDriverWait: Instância do WebDriverWait
        """
        if timeout is None:
            timeout = settings.TEST_TIMEOUT
        
        return WebDriverWait(driver, timeout)
    
    @staticmethod
    def quit_driver(driver: webdriver.Chrome) -> None:
        """
        Fecha o navegador e libera recursos.
        
        Args:
            driver: Instância do WebDriver
        """
        if driver:
            try:
                driver.quit()
            except Exception:
                pass
