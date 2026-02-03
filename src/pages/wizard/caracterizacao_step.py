"""
Page Object - Wizard Etapa Caracterização
==========================================

Representa a etapa de Caracterização do wizard de novo empreendimento.
"""

import time
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ...utils.wait_helper import WaitHelper


class CaracterizacaoStep:
    """Page Object para a etapa de Caracterização do wizard."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a etapa de Caracterização.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    STEP_TITLE = (By.XPATH, "//*[contains(text(), 'Caracterização Ambiental')]")
    
    # Botões
    BTN_PREENCHER = (By.XPATH, "//button[contains(., 'Preencher Dados')]")
    BTN_FINALIZAR = (By.XPATH, "//button[contains(., 'Finalizar')]")
    BTN_VOLTAR = (By.XPATH, "//button[contains(., 'Voltar')]")
    
    # Validações
    PERGUNTAS_RESPONDIDAS = (By.XPATH, "//button[contains(@class, 'bg-red') or contains(@class, 'bg-green-50')]")
    
    def is_visible(self) -> bool:
        """
        Verifica se a etapa está visível.
        
        Returns:
            bool: True se etapa está visível
        """
        try:
            # Scroll para o topo
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(0.5)
            
            WaitHelper.wait_for_element(self.driver, self.STEP_TITLE)
            return True
        except:
            return False
    
    def click_preencher_dados(self) -> bool:
        """
        Clica no botão Preencher Dados (auto-fill).
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("✨ Clicando em 'Preencher Dados' (auto-fill)...")
        
        try:
            # Scroll para o topo onde está o botão
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PREENCHER, condition='clickable'
            )
            btn.click()
            time.sleep(2)  # Aguardar preenchimento automático
            
            print("✅ Dados preenchidos automaticamente")
            return True
            
        except Exception as e:
            print(f"⚠️ Botão 'Preencher Dados' não encontrado: {e}")
            print("⚠️ Continuando sem auto-fill...")
            return False
    
    def validar_preenchimento(self) -> bool:
        """
        Valida se dados foram preenchidos.
        
        Returns:
            bool: True se preenchimento validado
        """
        print("✓ Validando preenchimento automático...")
        
        try:
            time.sleep(2)
            
            # Contar perguntas respondidas
            perguntas = self.driver.find_elements(*self.PERGUNTAS_RESPONDIDAS)
            total_perguntas = len(perguntas)
            
            if total_perguntas > 0:
                print(f"✓ {total_perguntas} perguntas respondidas automaticamente")
                return True
            else:
                print("⚠️ Nenhuma pergunta respondida detectada")
                return False
                
        except Exception as e:
            print(f"⚠️ Erro ao validar: {e}")
            return False
    
    def click_finalizar(self) -> bool:
        """
        Clica no botão Finalizar.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("✅ Clicando em 'Finalizar'...")
        
        try:
            # Scroll para o final da página
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_FINALIZAR, condition='clickable'
            )
            btn.click()
            time.sleep(2)
            
            print("✅ Cadastro finalizado!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Finalizar: {e}")
            return False
    
    def click_voltar(self) -> bool:
        """
        Clica no botão Voltar.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("⬅️ Clicando em 'Voltar'...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_VOLTAR, condition='clickable'
            )
            btn.click()
            time.sleep(2)
            
            print("✅ Voltou para etapa anterior")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Voltar: {e}")
            return False
