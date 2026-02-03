"""
Page Object - Wizard Etapa Atividades
======================================

Representa a etapa de Atividades do wizard de novo empreendimento.
"""

import time
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ...utils.wait_helper import WaitHelper


class AtividadesStep:
    """Page Object para a etapa de Atividades do wizard."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a etapa de Atividades.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    STEP_TITLE = (By.XPATH, "//*[contains(text(), 'Atividades') or contains(text(), 'Selecione as atividades')]")
    
    # Botões
    BTN_ADICIONAR = (By.XPATH, "//button[contains(., 'Adicionar Atividade')]")
    BTN_PREENCHER = (By.XPATH, "//button[contains(., 'Preencher Dados')]")
    BTN_PROXIMO = (By.XPATH, "//button[contains(., 'Próximo')]")
    BTN_VOLTAR = (By.XPATH, "//button[contains(., 'Voltar')]")
    
    # Seção de atividades selecionadas
    SECAO_SELECIONADAS = (By.XPATH, "//*[contains(text(), 'Atividades Selecionadas')]")
    CARDS_ATIVIDADES = (By.XPATH, "//div[contains(@class, 'bg-gradient-to-r from-green-50')]")
    
    def is_visible(self) -> bool:
        """
        Verifica se a etapa está visível.
        
        Returns:
            bool: True se etapa está visível
        """
        try:
            # Timeout maior pois essa página pode demorar
            WaitHelper.wait_for_element(
                self.driver, self.BTN_ADICIONAR, 
                condition='clickable', timeout=60
            )
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
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PREENCHER, condition='clickable'
            )
            
            # Scroll até o botão
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
                btn
            )
            time.sleep(0.5)
            
            btn.click()
            time.sleep(2)  # Aguardar preenchimento automático
            
            print("✅ Dados preenchidos automaticamente")
            return True
            
        except Exception as e:
            print(f"⚠️ Botão 'Preencher Dados' não encontrado: {e}")
            print("⚠️ Continuando com método manual...")
            
            # Fallback: clicar em Adicionar Atividade
            try:
                btn_adicionar = WaitHelper.wait_for_element(
                    self.driver, self.BTN_ADICIONAR, condition='clickable'
                )
                btn_adicionar.click()
                time.sleep(1)
                print("✅ Botão 'Adicionar Atividade' clicado (fallback)")
                return False
            except:
                print("❌ Erro ao clicar em Adicionar Atividade")
                return False
    
    def validar_atividades_adicionadas(self) -> bool:
        """
        Valida se atividades foram adicionadas.
        
        Returns:
            bool: True se atividades encontradas
        """
        print("✅ Validando atividades adicionadas...")
        
        try:
            # Verificar seção "Atividades Selecionadas"
            WaitHelper.wait_for_element(
                self.driver, self.SECAO_SELECIONADAS, timeout=5
            )
            print("✓ Seção 'Atividades Selecionadas' encontrada")
            
            # Contar cards de atividades
            cards = self.driver.find_elements(*self.CARDS_ATIVIDADES)
            if len(cards) > 0:
                print(f"✓ {len(cards)} atividade(s) adicionada(s)")
                return True
            else:
                print("⚠️ Nenhuma atividade selecionada encontrada")
                return False
                
        except Exception as e:
            print(f"⚠️ Erro ao validar atividades: {e}")
            return False
    
    def validar_campos_numericos(self) -> bool:
        """
        Valida se campos numéricos foram preenchidos.
        
        Returns:
            bool: True se campos preenchidos
        """
        print("🔢 Validando campos numéricos...")
        
        try:
            campos = self.driver.find_elements(
                By.XPATH, 
                "//input[@type='number' and @value!='']"
            )
            if len(campos) > 0:
                print(f"✓ {len(campos)} campo(s) numérico(s) preenchido(s)")
                return True
            else:
                print("⚠️ Nenhum campo numérico preenchido")
                return False
        except Exception as e:
            print(f"⚠️ Erro ao validar campos: {e}")
            return False
    
    def click_proximo(self) -> bool:
        """
        Clica no botão Próximo.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("➡️ Clicando em 'Próximo'...")
        
        try:
            # Scroll para o final da página
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PROXIMO, condition='clickable'
            )
            btn.click()
            time.sleep(2)
            
            print("✅ Avançou para próxima etapa")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Próximo: {e}")
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
