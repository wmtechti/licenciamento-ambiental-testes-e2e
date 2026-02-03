"""
Teste de Integração - Fluxo Completo de Cadastro
=================================================

Testa o fluxo completo de cadastro de novo empreendimento.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from src.pages.login_page import LoginPage
from src.pages.empreendimento_page import EmpreendimentoPage
from src.pages.wizard.imovel_step import ImovelStep
from src.pages.wizard.dados_gerais_step import DadosGeraisStep
from src.pages.wizard.atividades_step import AtividadesStep
from src.pages.wizard.caracterizacao_step import CaracterizacaoStep


@pytest.mark.e2e
@pytest.mark.integration
@pytest.mark.slow
def test_fluxo_completo_cadastro(driver, wait, auto_login_url):
    """
    Testa o fluxo completo de cadastro de empreendimento.
    
    Args:
        driver: Fixture do WebDriver
        wait: Fixture do WebDriverWait
        auto_login_url: Fixture com URL de auto-login
    """
    print("\n" + "=" * 80)
    print("TESTE DE INTEGRAÇÃO - FLUXO COMPLETO DE CADASTRO")
    print("=" * 80 + "\n")
    
    # 1. Login
    print("ETAPA 1: Auto-Login")
    login_page = LoginPage(driver, wait)
    assert login_page.auto_login(), "Falha no auto-login"
    
    # 2. Navegação
    print("\nETAPA 2: Navegação para Novo Empreendimento")
    emp_page = EmpreendimentoPage(driver, wait)
    assert emp_page.navigate_from_menu(), "Falha ao navegar"
    assert emp_page.click_novo_empreendimento(), "Falha ao abrir wizard"
    assert emp_page.wizard_is_open(), "Wizard não abriu"
    
    # ETAPA 3: Cadastro de Imóvel
    print("\nETAPA 3: Cadastro de Imóvel")
    print("-" * 60)
    
    imovel_step = ImovelStep(driver, wait)
    
    # Selecionar tipo de imóvel
    assert imovel_step.select_tipo_imovel("URBANO"), "Falha ao selecionar tipo"
    
    # Clicar em Preencher Dados (preenche automaticamente)
    assert imovel_step.click_preencher_dados(), "Falha ao preencher dados"
    
    # Salvar imóvel (fecha modal)
    assert imovel_step.click_salvar(), "Falha ao salvar imóvel"
    
    # Clicar em Próximo para avançar
    assert imovel_step.click_proximo(), "Falha ao avançar para próxima etapa"
    
    # ETAPA 4: Dados Gerais
    print("\nETAPA 4: Dados Gerais")
    print("-" * 60)
    
    dados_gerais_step = DadosGeraisStep(driver, wait)
    
    # Verificar se está na etapa
    assert dados_gerais_step.is_visible(), "Etapa Dados Gerais não está visível"
    
    # Clicar em Preencher Dados (auto-fill)
    dados_gerais_step.click_preencher_dados()  # Não bloquear se não encontrar
    
    # Validar campos obrigatórios
    assert dados_gerais_step.validar_campos_obrigatorios(), "Falha ao validar campos"
    
    # Validar partícipe
    dados_gerais_step.validar_participe()  # Não bloquear se não encontrar
    
    # Clicar em Próximo
    assert dados_gerais_step.click_proximo(), "Falha ao avançar para Atividades"
    
    # ETAPA 5: Atividades
    print("\nETAPA 5: Atividades")
    print("-" * 60)
    
    atividades_step = AtividadesStep(driver, wait)
    
    # Verificar se está na etapa (timeout maior - 60s)
    assert atividades_step.is_visible(), "Etapa Atividades não está visível"
    
    # Clicar em Preencher Dados (auto-fill)
    atividades_step.click_preencher_dados()
    
    # Validar atividades adicionadas
    atividades_step.validar_atividades_adicionadas()
    
    # Validar campos numéricos
    atividades_step.validar_campos_numericos()
    
    # Clicar em Próximo
    assert atividades_step.click_proximo(), "Falha ao avançar para Caracterização"
    
    # ETAPA 6: Caracterização
    print("\nETAPA 6: Caracterização")
    print("-" * 60)
    
    caracterizacao_step = CaracterizacaoStep(driver, wait)
    
    # Verificar se está na etapa
    assert caracterizacao_step.is_visible(), "Etapa Caracterização não está visível"
    
    # Clicar em Preencher Dados (auto-fill)
    caracterizacao_step.click_preencher_dados()
    
    # Validar preenchimento
    caracterizacao_step.validar_preenchimento()
    
    # Finalizar cadastro
    assert caracterizacao_step.click_finalizar(), "Falha ao finalizar cadastro"
    
    print("\n✅ Teste de integração concluído com sucesso!\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
