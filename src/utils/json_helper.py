"""
Helper para manipulação de JSON
================================

Funções auxiliares para trabalhar com dados JSON.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict


class JSONHelper:
    """Helper para manipulação de JSON."""
    
    @staticmethod
    def save_json(data: Dict[str, Any], filename: str, directory: Path = None) -> str:
        """
        Salva dados em arquivo JSON.
        
        Args:
            data: Dados a serem salvos
            filename: Nome do arquivo (sem extensão)
            directory: Diretório de destino
            
        Returns:
            str: Caminho do arquivo salvo
        """
        if directory is None:
            from ..config.settings import OUTPUT_DIR
            directory = OUTPUT_DIR
        
        # Adicionar timestamp ao nome se não tiver
        if not any(char.isdigit() for char in filename):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename}_{timestamp}"
        
        # Garantir extensão .json
        if not filename.endswith('.json'):
            filename = f"{filename}.json"
        
        filepath = directory / filename
        
        # Salvar arquivo
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return str(filepath)
    
    @staticmethod
    def load_json(filepath: str) -> Dict[str, Any]:
        """
        Carrega dados de arquivo JSON.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            dict: Dados carregados
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def merge_contexts(*contexts) -> Dict[str, Any]:
        """
        Mescla múltiplos contextos em um único dicionário.
        
        Args:
            *contexts: Contextos a serem mesclados
            
        Returns:
            dict: Contexto mesclado
        """
        merged = {}
        for context in contexts:
            if context and isinstance(context, dict):
                merged.update(context)
        return merged
    
    @staticmethod
    def add_metadata(data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Adiciona metadados ao JSON.
        
        Args:
            data: Dados originais
            **kwargs: Metadados adicionais
            
        Returns:
            dict: Dados com metadados
        """
        metadata = {
            'timestamp': datetime.now().isoformat(),
            'version': '1.0.0',
            **kwargs
        }
        
        return {
            'metadata': metadata,
            'data': data
        }
