"""
Helper para captura de screenshots
===================================

Funções auxiliares para captura e gerenciamento de screenshots.
"""

import time
from pathlib import Path
from selenium import webdriver
from datetime import datetime

from ..config.settings import SCREENSHOTS_DIR


class ScreenshotHelper:
    """Helper para captura de screenshots."""
    
    @staticmethod
    def capture(
        driver: webdriver.Chrome,
        name: str = None,
        prefix: str = "screenshot",
        directory: Path = None
    ) -> str:
        """
        Captura screenshot da tela atual.
        
        Args:
            driver: Instância do WebDriver
            name: Nome específico do arquivo
            prefix: Prefixo do nome do arquivo
            directory: Diretório de destino
            
        Returns:
            str: Caminho do arquivo salvo
        """
        if directory is None:
            directory = SCREENSHOTS_DIR
        
        # Criar diretório se não existir
        directory.mkdir(parents=True, exist_ok=True)
        
        # Gerar nome do arquivo
        if name:
            filename = name
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{prefix}_{timestamp}"
        
        # Garantir extensão .png
        if not filename.endswith('.png'):
            filename = f"{filename}.png"
        
        filepath = directory / filename
        
        # Capturar screenshot
        driver.save_screenshot(str(filepath))
        
        return str(filepath)
    
    @staticmethod
    def capture_on_error(
        driver: webdriver.Chrome,
        test_name: str,
        error_message: str = ""
    ) -> str:
        """
        Captura screenshot em caso de erro.
        
        Args:
            driver: Instância do WebDriver
            test_name: Nome do teste
            error_message: Mensagem de erro
            
        Returns:
            str: Caminho do arquivo salvo
        """
        timestamp = int(time.time())
        name = f"erro_{test_name}_{timestamp}"
        
        filepath = ScreenshotHelper.capture(driver, name=name, prefix="erro")
        
        print(f"📸 Screenshot de erro salvo: {filepath}")
        if error_message:
            print(f"   Erro: {error_message}")
        
        return filepath
    
    @staticmethod
    def capture_step(
        driver: webdriver.Chrome,
        test_name: str,
        step_number: int,
        step_name: str = ""
    ) -> str:
        """
        Captura screenshot de uma etapa do teste.
        
        Args:
            driver: Instância do WebDriver
            test_name: Nome do teste
            step_number: Número da etapa
            step_name: Nome da etapa
            
        Returns:
            str: Caminho do arquivo salvo
        """
        name = f"{test_name}_step{step_number:02d}"
        if step_name:
            name = f"{name}_{step_name}"
        
        return ScreenshotHelper.capture(driver, name=name, prefix="step")
