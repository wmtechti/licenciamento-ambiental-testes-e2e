"""
Configuração de Fixtures Pytest
================================

Define fixtures compartilhadas para todos os testes.
"""

import pytest
from pathlib import Path
import sys

# Adicionar src ao path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from src.core.driver_manager import DriverManager
from src.config.settings import settings


@pytest.fixture(scope="function")
def driver():
    """
    Fixture que fornece um driver do Chrome para cada teste.
    
    Yields:
        webdriver.Chrome: Instância do Chrome WebDriver
    """
    driver = DriverManager.create_driver()
    yield driver
    DriverManager.quit_driver(driver)


@pytest.fixture(scope="function")
def wait(driver):
    """
    Fixture que fornece um WebDriverWait.
    
    Args:
        driver: Fixture do driver
        
    Yields:
        WebDriverWait: Instância do WebDriverWait
    """
    yield DriverManager.create_wait(driver)


@pytest.fixture(scope="session")
def base_url():
    """
    Fixture que fornece a URL base do frontend.
    
    Returns:
        str: URL base
    """
    return settings.FRONTEND_URL


@pytest.fixture(scope="session")
def auto_login_url():
    """
    Fixture que fornece a URL de auto-login.
    
    Returns:
        str: URL de auto-login
    """
    return settings.AUTO_LOGIN_URL


@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """
    Fixture que captura screenshot em caso de falha.
    
    Args:
        request: Request do pytest
        driver: Fixture do driver
    """
    yield
    
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        from src.utils.screenshot import ScreenshotHelper
        test_name = request.node.name
        ScreenshotHelper.capture_on_error(driver, test_name, str(request.node.rep_call.longrepr))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook para capturar resultado do teste.
    
    Permite que a fixture screenshot_on_failure saiba se o teste falhou.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
