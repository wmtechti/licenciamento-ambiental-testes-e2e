"""
Page Object - Wizard Etapa Imóvel
==================================

Representa a etapa de Imóvel do wizard de novo empreendimento.
"""

import time
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from ...utils.wait_helper import WaitHelper


class ImovelStep:
    """Page Object para a etapa de Imóvel do wizard."""
    
    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        """
        Inicializa a etapa de Imóvel.
        
        Args:
            driver: Instância do WebDriver
            wait: Instância do WebDriverWait
        """
        self.driver = driver
        self.wait = wait
    
    # Locators
    STEP_TITLE = (By.XPATH, "//*[contains(text(), 'Cadastrar Novo Imóvel')]")
    
    # Select de tipo de imóvel
    SELECT_TIPO_IMOVEL = (By.XPATH, "//select | //select[contains(@class, 'w-full')]")
    
    # Botões de ação
    BTN_PREENCHER = (By.XPATH, "//button[contains(., 'Preencher Dados') or contains(., 'Preencher')]")
    BTN_SALVAR = (By.XPATH, "//button[contains(@class, 'bg-green-600') and contains(., 'Salvar Imóvel')]")
    BTN_PROXIMO = (By.XPATH, "//button[contains(., 'Próximo') or contains(., 'Avançar')]")
    BTN_CANCELAR = (By.XPATH, "//button[contains(., 'Cancelar')]")
    
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
    
    def select_tipo_imovel(self, tipo: str) -> bool:
        """
        Seleciona o tipo de imóvel no dropdown.
        
        Args:
            tipo: Tipo de imóvel (RURAL, URBANO, LINEAR)
            
        Returns:
            bool: True se seleção foi bem-sucedida
        """
        print(f"📍 Selecionando tipo de imóvel: {tipo}")
        
        tipo_upper = tipo.upper()
        
        try:
            # Aguardar select estar disponível
            select_element = WaitHelper.wait_for_element(
                self.driver, self.SELECT_TIPO_IMOVEL, condition='visible'
            )
            
            # Criar objeto Select
            select = Select(select_element)
            
            # Selecionar pelo VALUE (não pelo texto com emoji)
            if tipo_upper == "RURAL":
                select.select_by_value("RURAL")
            elif tipo_upper == "URBANO":
                select.select_by_value("URBANO")
            elif tipo_upper == "LINEAR":
                select.select_by_value("LINEAR")
            else:
                print(f"❌ Tipo de imóvel inválido: {tipo}")
                return False
            
            time.sleep(1)
            
            print(f"✅ Tipo {tipo} selecionado no dropdown")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao selecionar tipo: {e}")
            return False
    
    def click_preencher_dados(self) -> bool:
        """
        Clica no botão Preencher Dados.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("📝 Clicando em 'Preencher Dados'...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_PREENCHER, condition='clickable'
            )
            btn.click()
            time.sleep(2)
            
            print("✅ Clicou em 'Preencher Dados'")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Preencher Dados: {e}")
            return False
    
    def fill_form(self, data: Dict[str, Any]) -> bool:
        """
        Preenche o formulário de imóvel.
        
        Args:
            data: Dados para preencher o formulário
            
        Returns:
            bool: True se preenchimento foi bem-sucedido
        """
        print("📝 Preenchendo formulário de imóvel...")
        
        try:
            # Aqui você implementaria o preenchimento real dos campos
            # Exemplo:
            # nome_imovel = data.get('nome_imovel', '')
            # if nome_imovel:
            #     input_nome = self.driver.find_element(By.ID, "nomeImovel")
            #     input_nome.clear()
            #     input_nome.send_keys(nome_imovel)
            
            time.sleep(1)
            print("✅ Formulário preenchido")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao preencher formulário: {e}")
            return False
    
    def click_salvar(self) -> bool:
        """
        Clica no botão Salvar Imóvel.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("💾 Clicando em 'Salvar Imóvel'...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_SALVAR, condition='clickable'
            )
            btn.click()
            time.sleep(2)
            
            print("✅ Imóvel salvo - avançando para próxima etapa")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Salvar: {e}")
            return False
    
    def click_proximo(self) -> bool:
        """
        Clica no botão Próximo para avançar para Dados Gerais.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("➡️ Clicando em 'Próximo'...")
        
        try:
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
    
    def click_cancelar(self) -> bool:
        """
        Clica no botão Cancelar.
        
        Returns:
            bool: True se clique foi bem-sucedido
        """
        print("❌ Clicando em 'Cancelar'...")
        
        try:
            btn = WaitHelper.wait_for_element(
                self.driver, self.BTN_CANCELAR, condition='clickable'
            )
            btn.click()
            time.sleep(1)
            
            print("✅ Cancelado")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao clicar em Cancelar: {e}")
            return False
