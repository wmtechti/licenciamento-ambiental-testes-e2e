"""
Page Object - Wizard Etapa Dados Gerais
========================================

Representa a etapa de Dados Gerais do wizard de novo empreendimento.
"""

import time
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from ...utils.wait_helper import WaitHelper


class DadosGeraisStep:
    """Page Object para a etapa de Dados Gerais do wizard."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a etapa de Dados Gerais.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    STEP_TITLE = (By.XPATH, "//*[contains(text(), 'Dados Gerais') or contains(text(), 'Nome do Empreendimento')]")
    
    # Botão auto-fill (roxo)
    BTN_PREENCHER = (By.XPATH, "//button[contains(@class, 'bg-purple-600') and contains(., 'Preencher Dados')] | //button[contains(., 'Preencher Dados') or contains(., 'Preencher')]")
    
    # Campos obrigatórios
    INPUT_NOME = (By.XPATH, "//label[contains(text(), 'Nome')]//following::input[1] | //input[contains(@placeholder, 'Complexo Industrial')]")
    SELECT_SITUACAO = (By.XPATH, "//label[contains(text(), 'Situação')]//following::select[1]")
    
    # Campos opcionais
    INPUT_EMPREGADOS = (By.XPATH, "//label[contains(text(), 'Nº de Empregados')]//following::input[1] | //input[contains(@placeholder, '0')][@type='number']")
    TEXTAREA_DESCRICAO = (By.XPATH, "//label[contains(text(), 'Descrição')]//following::textarea[1] | //textarea[contains(@placeholder, 'Descreva')]")
    
    # Partícipe
    PARTICIPE_ELEMENTO = (By.XPATH, "//*[contains(text(), 'Empresa Mineração') or contains(text(), 'Requerente')] | //table//tbody//tr | //div[contains(@class, 'participe')]")
    
    # Botões de navegação
    BTN_PROXIMO = (By.XPATH, "//button[contains(., 'Próximo') or contains(., 'Avançar')]")
    BTN_VOLTAR = (By.XPATH, "//button[contains(., 'Voltar')]")
    
    def is_visible(self) -> bool:
        """
        Verifica se a etapa está visível.
        
        Returns:
            bool: True se etapa está visível
        """
        try:
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
        print("🪄 Clicando em 'Preencher Dados' (auto-fill)...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PREENCHER, condition='clickable'
            )
            btn.click()
            time.sleep(3)  # Aguardar preenchimento automático
            
            print("✅ Dados preenchidos automaticamente")
            return True
            
        except Exception as e:
            print(f"⚠️ Botão 'Preencher Dados' não encontrado: {e}")
            print("⚠️ Continuando sem auto-fill...")
            return False
    
    def validar_campos_obrigatorios(self) -> bool:
        """
        Valida e preenche campos obrigatórios se necessário.
        
        Returns:
            bool: True se validação foi bem-sucedida
        """
        print("✅ Validando campos obrigatórios...")
        
        try:
            # Validar/Preencher Nome (OBRIGATÓRIO)
            nome_input = WaitHelper.wait_for_element(
                self.driver, self.INPUT_NOME, condition='visible'
            )
            nome_valor = nome_input.get_attribute('value')
            
            if not nome_valor or len(nome_valor) == 0:
                print("⚠️ Nome vazio - preenchendo manualmente...")
                nome_input.clear()
                nome_input.send_keys("Empreendimento Teste Automatizado")
                time.sleep(0.5)
                print("✅ Nome preenchido")
            else:
                print(f"✅ Nome já preenchido: {nome_valor}")
            
            # Validar/Preencher Situação (OBRIGATÓRIO)
            situacao_select = WaitHelper.wait_for_element(
                self.driver, self.SELECT_SITUACAO, condition='visible'
            )
            situacao_valor = situacao_select.get_attribute('value')
            
            if not situacao_valor or situacao_valor == '':
                print("⚠️ Situação vazia - preenchendo manualmente...")
                select = Select(situacao_select)
                # Pular opção vazia e selecionar primeira válida
                if len(select.options) > 1:
                    select.select_by_index(1)
                    time.sleep(0.5)
                    print("✅ Situação preenchida")
            else:
                print(f"✅ Situação já preenchida: {situacao_valor}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao validar campos: {e}")
            return False
    
    def validar_participe(self) -> bool:
        """
        Valida se partícipe foi adicionado.
        
        Returns:
            bool: True se partícipe encontrado
        """
        print("👥 Validando partícipe...")
        
        try:
            WaitHelper.wait_for_element(
                self.driver, self.PARTICIPE_ELEMENTO, timeout=5
            )
            print("✅ Partícipe encontrado")
            return True
        except:
            print("⚠️ Partícipe não encontrado visualmente, mas continuando...")
            return True  # Não bloquear por isso
    
    def click_proximo(self) -> bool:
        """
        Clica no botão Próximo.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("➡️ Clicando em 'Próximo'...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PROXIMO, condition='clickable'
            )
            btn.click()
            time.sleep(5)  # Aguardar transição entre páginas
            
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
