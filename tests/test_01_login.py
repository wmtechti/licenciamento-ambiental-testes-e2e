"""
Teste 01 - Login e Navegação
=============================

Testa o fluxo de auto-login e navegação até o wizard de novo empreendimento.
"""

import pytest
import sys
from pathlib import Path

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from src.pages.login_page import LoginPage
from src.pages.empreendimento_page import EmpreendimentoPage


@pytest.mark.e2e
@pytest.mark.smoke
def test_login_e_navegacao(driver, wait, auto_login_url):
    """
    Testa auto-login e navegação até wizard de novo empreendimento.
    
    Args:
        driver: Fixture do WebDriver
        wait: Fixture do WebDriverWait
        auto_login_url: Fixture com URL de auto-login
    """
    print("\n" + "=" * 80)
    print("TESTE 01 - LOGIN E NAVEGAÇÃO ATÉ NOVO EMPREENDIMENTO")
    print("=" * 80 + "\n")
    
    # Login
    login_page = LoginPage(driver, wait)
    assert login_page.auto_login(), "Falha no auto-login"
    
    # Navegação
    emp_page = EmpreendimentoPage(driver, wait)
    assert emp_page.navigate_from_menu(), "Falha ao navegar para Empreendimentos"
    assert emp_page.click_novo_empreendimento(), "Falha ao clicar em Novo Empreendimento"
    assert emp_page.wizard_is_open(), "Wizard não foi aberto"
    
    print("\n✅ Teste concluído com sucesso!\n")


if __name__ == "__main__":
    # Permite executar o teste diretamente
    pytest.main([__file__, "-v", "-s"])
