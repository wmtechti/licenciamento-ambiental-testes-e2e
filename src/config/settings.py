"""
Configurações Centralizadas do Projeto
=======================================

Gerencia todas as configurações do projeto usando variáveis de ambiente.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Diretórios do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / "src"
TESTS_DIR = BASE_DIR / "tests"
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

# Criar diretórios se não existirem
OUTPUT_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)
SCREENSHOTS_DIR.mkdir(exist_ok=True)


class Settings:
    """Configurações do projeto."""
    
    # URLs
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
    
    # Auto-login
    AUTO_LOGIN_TOKEN = os.getenv("AUTO_LOGIN_TOKEN", "")
    AUTO_LOGIN_USER_ID = os.getenv("AUTO_LOGIN_USER_ID", "9948")
    AUTO_LOGIN_USER_NAME = os.getenv("AUTO_LOGIN_USER_NAME", "TESTE DESENVOLVIMENTO")
    
    @property
    def AUTO_LOGIN_URL(self):
        """Gera URL de auto-login."""
        if os.getenv("AUTO_LOGIN_URL"):
            return os.getenv("AUTO_LOGIN_URL")
        
        import time
        timestamp = int(time.time() * 1000)
        return (
            f"{self.FRONTEND_URL}?"
            f"token={self.AUTO_LOGIN_TOKEN}&"
            f"nome={self.AUTO_LOGIN_USER_NAME}&"
            f"userId={self.AUTO_LOGIN_USER_ID}&"
            f"_t={timestamp}"
        )
    
    # ChromeDriver
    CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", r"C:\chromedriver\chromedriver.exe")
    USE_WEBDRIVER_MANAGER = os.getenv("USE_WEBDRIVER_MANAGER", "false").lower() == "true"
    
    # Configurações de Teste
    TEST_TIMEOUT = int(os.getenv("TEST_TIMEOUT", "20"))
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    MAXIMIZE_WINDOW = os.getenv("MAXIMIZE_WINDOW", "true").lower() == "true"
    SCREENSHOT_ON_FAIL = os.getenv("SCREENSHOT_ON_FAIL", "true").lower() == "true"
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = REPORTS_DIR / os.getenv("LOG_FILE", "test_execution.log")
    
    # Database (Opcional)
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")


# Instância global de configurações
settings = Settings()
