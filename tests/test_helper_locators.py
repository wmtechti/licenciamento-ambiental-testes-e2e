"""
Teste Helper - Descobrir Locators
==================================

Este teste abre o wizard e pausa para você inspecionar os elementos.
Use este teste para descobrir os locators corretos do seu frontend.
"""

import pytest
import sys
from pathlib import Path
import time

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from src.pages.login_page import LoginPage
from src.pages.empreendimento_page import EmpreendimentoPage


@pytest.mark.helper
def test_descobrir_locators(driver, wait, auto_login_url):
    """
    Abre o wizard e pausa para você descobrir os locators.
    
    COMO USAR:
    1. Execute: pytest tests/test_helper_locators.py -v -s
    2. O navegador abrirá e pausará
    3. Inspecione os elementos usando F12 (DevTools)
    4. Anote os IDs, classes, XPaths
    5. Pressione ENTER para fechar
    
    Args:
        driver: Fixture do WebDriver
        wait: Fixture do WebDriverWait
        auto_login_url: Fixture com URL de auto-login
    """
    print("\n" + "=" * 80)
    print("🔍 HELPER - DESCOBRIR LOCATORS DO WIZARD")
    print("=" * 80 + "\n")
    
    # 1. Login
    print("PASSO 1: Fazendo login...")
    login_page = LoginPage(driver, wait)
    assert login_page.auto_login(), "Falha no auto-login"
    print("✅ Login OK\n")
    
    # 2. Navegação
    print("PASSO 2: Abrindo wizard...")
    emp_page = EmpreendimentoPage(driver, wait)
    assert emp_page.navigate_from_menu(), "Falha ao navegar"
    assert emp_page.click_novo_empreendimento(), "Falha ao abrir wizard"
    assert emp_page.wizard_is_open(), "Wizard não abriu"
    print("✅ Wizard aberto\n")
    
    # 3. PAUSA para inspeção
    print("=" * 80)
    print("🛑 TESTE PAUSADO - INSPECIONE OS ELEMENTOS")
    print("=" * 80)
    print("\n📋 INSTRUÇÕES:")
    print("1. Abra o DevTools: F12")
    print("2. Clique no ícone de seletor (🔍) ou Ctrl+Shift+C")
    print("3. Clique nos elementos do wizard para ver o HTML")
    print("4. Anote os locators (IDs, classes, XPaths, data-attributes)")
    print("\n🎯 ELEMENTOS PARA LOCALIZAR:")
    print("   - Botão 'Rural'")
    print("   - Botão 'Urbano'")
    print("   - Botão 'Linear'")
    print("   - Botão 'Preencher'")
    print("   - Botão 'Próximo'")
    print("   - Campos do formulário (se visíveis)")
    print("\n💡 DICA: Prefira elementos com:")
    print("   - IDs únicos (id='...')")
    print("   - Data attributes (data-testid='...', data-test='...')")
    print("   - Classes específicas")
    print("\n" + "=" * 80)
    
    # Aguardar usuário inspecionar
    input("\n▶️  Pressione ENTER quando terminar de inspecionar...\n")
    
    print("\n✅ Inspeção concluída!")
    print("\n📝 PRÓXIMOS PASSOS:")
    print("1. Edite: src/pages/wizard/imovel_step.py")
    print("2. Atualize os locators com os valores descobertos")
    print("3. Execute: pytest tests/test_01_login.py -v -s")
    print("\n📖 Guia completo: docs/LOCATORS_GUIDE.md")
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "-m", "helper"])
