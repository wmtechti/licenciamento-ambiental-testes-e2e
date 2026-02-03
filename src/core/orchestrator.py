"""
Orquestrador Genérico de Testes
================================

Gerencia a execução sequencial de múltiplos testes.
"""

import time
from datetime import datetime
from typing import List, Dict, Callable, Any, Optional
from selenium import webdriver

from .driver_manager import DriverManager


class TestOrchestrator:
    """Orquestra a execução de testes em sequência."""
    
    def __init__(self, name: str = "Test Suite"):
        """
        Inicializa o orquestrador.
        
        Args:
            name: Nome da suíte de testes
        """
        self.name = name
        self.tests: List[Dict[str, Any]] = []
        self.results: List[Dict[str, Any]] = []
        self.driver: Optional[webdriver.Chrome] = None
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
    
    def add_test(
        self,
        name: str,
        function: Callable,
        active: bool = True,
        description: str = ""
    ) -> None:
        """
        Adiciona um teste à lista de execução.
        
        Args:
            name: Nome do teste
            function: Função a ser executada
            active: Se o teste está ativo
            description: Descrição do teste
        """
        self.tests.append({
            'name': name,
            'function': function,
            'active': active,
            'description': description,
            'status': 'pending'
        })
    
    def run_all(self, close_on_success: bool = True) -> bool:
        """
        Executa todos os testes em sequência.
        
        Args:
            close_on_success: Fechar navegador se todos os testes passarem
            
        Returns:
            bool: True se todos os testes passaram
        """
        self._print_header()
        
        self.start_time = time.time()
        previous_context = None
        all_passed = True
        
        for idx, test in enumerate(self.tests, 1):
            if not test['active']:
                print(f"⏭️  Teste {idx} - {test['name']}: DESATIVADO\n")
                test['status'] = 'disabled'
                continue
            
            print(f"\n{'=' * 100}")
            print(f"▶️  EXECUTANDO TESTE {idx}/{len(self.tests)}: {test['name']}")
            if test['description']:
                print(f"   {test['description']}")
            print(f"{'=' * 100}\n")
            
            try:
                # Primeiro teste não recebe driver
                if idx == 1:
                    context = test['function']()
                else:
                    # Testes subsequentes recebem driver e contexto
                    context = test['function'](
                        driver_existente=self.driver,
                        contexto_anterior=previous_context
                    )
                
                # Salvar driver para próximos testes
                if context and 'driver' in context:
                    self.driver = context['driver']
                
                # Verificar se teste passou
                if context and context.get('erro'):
                    print(f"❌ Teste {idx} - {test['name']}: FALHOU")
                    print(f"   Erro: {context['erro']}\n")
                    test['status'] = 'failed'
                    test['error'] = context['erro']
                    all_passed = False
                    break
                else:
                    print(f"✅ Teste {idx} - {test['name']}: SUCESSO\n")
                    test['status'] = 'passed'
                    previous_context = context
                    
            except Exception as e:
                print(f"❌ Teste {idx} - {test['name']}: EXCEÇÃO")
                print(f"   Erro: {e}\n")
                test['status'] = 'error'
                test['error'] = str(e)
                all_passed = False
                break
        
        self.end_time = time.time()
        self._print_report()
        
        # Fechar navegador se necessário
        if self.driver:
            if all_passed and close_on_success:
                print("\n✅ Todos os testes passaram! Fechando navegador automaticamente...")
                time.sleep(2)
                DriverManager.quit_driver(self.driver)
                print("🔒 Navegador fechado\n")
            elif not all_passed:
                print("\n❌ Houve erros. Navegador mantido aberto para debug.\n")
        
        return all_passed
    
    def _print_header(self) -> None:
        """Imprime cabeçalho da execução."""
        print("=" * 100)
        print(f"{self.name:^100}")
        print("=" * 100)
        print(f"\n📅 Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"📋 Total de testes: {len([t for t in self.tests if t['active']])}")
        print("\n" + "=" * 100 + "\n")
    
    def _print_report(self) -> None:
        """Imprime relatório final."""
        total_time = self.end_time - self.start_time if self.end_time else 0
        
        print("\n" + "=" * 100)
        print(f"{'RELATÓRIO FINAL':^100}")
        print("=" * 100)
        
        print(f"\n⏱️  Tempo total: {total_time:.2f}s")
        
        # Contadores
        passed = sum(1 for t in self.tests if t['status'] == 'passed')
        failed = sum(1 for t in self.tests if t['status'] == 'failed')
        error = sum(1 for t in self.tests if t['status'] == 'error')
        disabled = sum(1 for t in self.tests if t['status'] == 'disabled')
        pending = sum(1 for t in self.tests if t['status'] == 'pending')
        
        print(f"📊 Resumo:")
        print(f"   ✅ Sucesso: {passed}")
        print(f"   ❌ Falha: {failed}")
        print(f"   💥 Erro: {error}")
        print(f"   ⏭️  Desativado: {disabled}")
        print(f"   ⏸️  Pendente: {pending}")
        
        print("\n" + "-" * 100)
        print("\n📋 Detalhes:")
        
        status_emoji = {
            'passed': '✅',
            'failed': '❌',
            'error': '💥',
            'disabled': '⏭️',
            'pending': '⏸️'
        }
        
        for idx, test in enumerate(self.tests, 1):
            emoji = status_emoji.get(test['status'], '❓')
            print(f"   {idx}. {emoji} {test['name']}: {test['status'].upper()}")
            if test.get('error'):
                print(f"      ↳ Erro: {test['error']}")
        
        print("\n" + "=" * 100)
        
        if failed > 0 or error > 0:
            print("\n❌ EXECUÇÃO FALHOU - Corrija os erros antes de prosseguir\n")
        else:
            print("\n🎉 TODOS OS TESTES EXECUTADOS COM SUCESSO!\n")
        
        print("=" * 100 + "\n")
