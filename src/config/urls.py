"""
URLs do Sistema
===============

Centraliza todas as URLs e rotas do sistema.
"""

from .settings import settings


class URLs:
    """Gerenciador de URLs do sistema."""
    
    # Base URLs
    FRONTEND = settings.FRONTEND_URL
    BACKEND = settings.BACKEND_URL
    
    # Auto-login
    AUTO_LOGIN = settings.AUTO_LOGIN_URL
    
    # Frontend Routes
    DASHBOARD = f"{FRONTEND}/dashboard"
    LOGIN = f"{FRONTEND}/login"
    
    # Empreendimentos
    EMPREENDIMENTOS = f"{FRONTEND}/empreendimentos"
    NOVO_EMPREENDIMENTO = f"{FRONTEND}/empreendimentos/novo"
    
    # Backend API Routes
    API_V1 = f"{BACKEND}/api/v1"
    
    # Propriedades
    API_PROPERTIES = f"{API_V1}/properties"
    
    @staticmethod
    def get_property(property_id: int) -> str:
        """URL para obter propriedade específica."""
        return f"{URLs.API_PROPERTIES}/{property_id}"
    
    # Empreendimentos
    API_ENTERPRISES = f"{API_V1}/enterprises"
    
    @staticmethod
    def get_enterprise(enterprise_id: int) -> str:
        """URL para obter empreendimento específico."""
        return f"{URLs.API_ENTERPRISES}/{enterprise_id}"
    
    @staticmethod
    def get_enterprise_activities(enterprise_id: int) -> str:
        """URL para obter atividades do empreendimento."""
        return f"{URLs.API_ENTERPRISES}/{enterprise_id}/activities"
    
    @staticmethod
    def get_enterprise_characterization(enterprise_id: int) -> str:
        """URL para obter caracterização do empreendimento."""
        return f"{URLs.API_ENTERPRISES}/{enterprise_id}/characterization"


# Instância global de URLs
urls = URLs()
