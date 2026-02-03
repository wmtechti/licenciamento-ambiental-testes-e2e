"""
Utilitário - Extração de JSON do Store
=======================================

Extrai dados do localStorage/store do navegador para validação.
"""

import json
from typing import Dict, Any, Optional
from datetime import datetime
from pathlib import Path


class JSONCollector:
    """Coleta e salva JSON do store do navegador."""
    
    def __init__(self, driver):
        """
        Inicializa o coletor.
        
        Args:
            driver: Instância do WebDriver
        """
        self.driver = driver
    
    def extrair_store(self) -> Optional[Dict[str, Any]]:
        """
        Extrai dados do store via localStorage.
        
        Returns:
            dict: Dados do store ou None se não encontrado
        """
        print("📊 Extraindo dados do store...")
        
        # Método 1: localStorage
        script_local = """
        try {
            const localData = localStorage.getItem('empreendimento-storage');
            if (localData) {
                return JSON.parse(localData);
            }
        } catch (e) {}
        return null;
        """
        
        # Método 2: sessionStorage
        script_session = """
        try {
            const sessionData = sessionStorage.getItem('empreendimento-storage');
            if (sessionData) {
                return JSON.parse(sessionData);
            }
        } catch (e) {}
        return null;
        """
        
        # Método 3: Window object (store global)
        script_window = """
        try {
            // Tentar diferentes variáveis globais
            if (window.store) return window.store.getState();
            if (window.__STORE__) return window.__STORE__;
            if (window.__ZUSTAND_STORES__) return window.__ZUSTAND_STORES__;
        } catch (e) {}
        return null;
        """
        
        # Tentar métodos em ordem
        metodos = [
            ("localStorage", script_local),
            ("sessionStorage", script_session),
            ("window store", script_window)
        ]
        
        for nome, script in metodos:
            try:
                store_data = self.driver.execute_script(script)
                
                if store_data:
                    print(f"✅ Store extraído com sucesso via {nome}!")
                    return store_data
                    
            except Exception as e:
                print(f"⚠️ Método {nome} falhou: {e}")
        
        print("⚠️ Store não encontrado em nenhum método")
        return None
    
    def salvar_json(self, data: Dict[str, Any], output_dir: str = "output") -> Optional[str]:
        """
        Salva JSON em arquivo.
        
        Args:
            data: Dados para salvar
            output_dir: Diretório de saída
            
        Returns:
            str: Caminho do arquivo salvo ou None
        """
        try:
            # Criar diretório
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            # Nome do arquivo com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"empreendimento_completo_{timestamp}.json"
            filepath = Path(output_dir) / filename
            
            # Salvar JSON formatado
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"💾 JSON salvo: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Erro ao salvar JSON: {e}")
            return None
    
    def exibir_estatisticas(self, data: Dict[str, Any]):
        """
        Exibe estatísticas dos dados coletados.
        
        Args:
            data: Dados para analisar
        """
        print("\n📈 Estatísticas dos Dados:")
        print("-" * 60)
        
        json_str = json.dumps(data, ensure_ascii=False)
        tamanho = len(json_str)
        
        print(f"  • Tamanho: {tamanho:,} bytes ({tamanho/1024:.2f} KB)")
        
        if isinstance(data, dict):
            print(f"  • Campos raiz: {len(data)}")
            
            # Contar campos do state se existir
            if 'state' in data:
                state = data['state']
                if isinstance(state, dict):
                    print(f"  • Campos do state: {len(state)}")
                    
                    # Listar seções principais
                    secoes = [k for k in state.keys() if not k.startswith('_')]
                    if secoes:
                        print(f"  • Seções: {', '.join(secoes[:5])}")
        
        print("-" * 60)
    
    def validar_estrutura(self, data: Dict[str, Any]) -> bool:
        """
        Valida se a estrutura do JSON está completa.
        
        Args:
            data: Dados para validar
            
        Returns:
            bool: True se estrutura válida
        """
        print("\n✓ Validando estrutura do JSON...")
        
        validacoes = []
        
        # Verificar se tem state
        if 'state' in data:
            validacoes.append(("State presente", True))
        else:
            validacoes.append(("State presente", False))
        
        # Se tiver state, verificar campos principais
        if 'state' in data and isinstance(data['state'], dict):
            state = data['state']
            
            # Validar imóvel
            tem_imovel = 'selectedProperty' in state or 'property' in state
            validacoes.append(("Imóvel cadastrado", tem_imovel))
            
            # Validar empreendimento
            tem_empreendimento = 'enterprise' in state or 'dados_gerais' in state
            validacoes.append(("Dados gerais preenchidos", tem_empreendimento))
            
            # Validar atividades
            tem_atividades = 'activities' in state or 'selectedActivities' in state
            validacoes.append(("Atividades cadastradas", tem_atividades))
        
        # Exibir resultados
        print()
        for nome, status in validacoes:
            icone = "✅" if status else "⚠️"
            print(f"  {icone} {nome}")
        
        # Retornar True se pelo menos metade validou
        total_ok = sum(1 for _, status in validacoes if status)
        return total_ok >= len(validacoes) / 2
