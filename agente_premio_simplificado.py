"""
🎯 AGENTE SIMPLIFICADO - ANÁLISE POR PERCENTUAL DE PRÊMIO
Sistema de Decisão Automatizada baseado em Tabela de Percentuais

REGRAS:
- R$ 1M a R$ 5M    → Mínimo 7% de prêmio
- R$ 5M a R$ 10M   → Mínimo 6% de prêmio  
- Acima de R$ 10M  → Mínimo 5% de prêmio

Se o percentual oferecido for menor que o mínimo → NÃO PARTICIPA
"""

import json
from dataclasses import dataclass
from typing import Dict, List, Tuple
from datetime import datetime


@dataclass
class LicitacaoSimples:
    """Licitação simplificada focada em valores"""
    numero: str
    nome: str
    valor_total: float
    percentual_premio: float  # Percentual oferecido como prêmio para background
    

@dataclass
class ResultadoSimples:
    """Resultado da análise simplificada"""
    decisao: str  # "PARTICIPAR" ou "NAO_PARTICIPAR"
    faixa: str
    percentual_minimo_exigido: float
    percentual_oferecido: float
    valor_premio: float
    atende_criterio: bool
    diferenca_percentual: float
    motivo: str


class AgentePremioBR:
    """
    Agente simplificado que decide participação baseado APENAS em percentual de prêmio
    """
    
    # Tabela de percentuais mínimos por faixa
    TABELA_PERCENTUAIS = {
        "1M-5M": {"min": 1_000_000, "max": 5_000_000, "percentual_minimo": 7.0},
        "5M-10M": {"min": 5_000_000, "max": 10_000_000, "percentual_minimo": 6.0},
        "10M+": {"min": 10_000_000, "max": float('inf'), "percentual_minimo": 5.0}
    }
    
    def analisar_licitacao(self, licitacao: LicitacaoSimples) -> ResultadoSimples:
        """
        Executa análise simplificada baseada apenas em percentual
        """
        print(f"\n{'='*80}")
        print(f"🔍 ANÁLISE: {licitacao.numero}")
        print(f"{'='*80}")
        print(f"📋 Nome: {licitacao.nome}")
        print(f"💰 Valor Total: R$ {licitacao.valor_total:,.2f}")
        print(f"🎁 Percentual Oferecido: {licitacao.percentual_premio:.2f}%")
        
        # Identificar faixa
        faixa, faixa_config = self._identificar_faixa(licitacao.valor_total)
        percentual_minimo = faixa_config["percentual_minimo"]
        
        print(f"\n📊 Faixa Identificada: {faixa}")
        print(f"📏 Percentual Mínimo Exigido: {percentual_minimo:.2f}%")
        
        # Calcular valor do prêmio
        valor_premio = licitacao.valor_total * (licitacao.percentual_premio / 100)
        
        # Verificar se atende critério
        atende = licitacao.percentual_premio >= percentual_minimo
        diferenca = licitacao.percentual_premio - percentual_minimo
        
        print(f"\n💵 Valor do Prêmio: R$ {valor_premio:,.2f}")
        print(f"📈 Diferença: {diferenca:+.2f} pontos percentuais")
        
        # Decisão
        if atende:
            decisao = "PARTICIPAR"
            motivo = f"Percentual oferecido ({licitacao.percentual_premio:.2f}%) atende o mínimo exigido ({percentual_minimo:.2f}%)"
            print(f"\n✅ DECISÃO: {decisao}")
        else:
            decisao = "NAO_PARTICIPAR"
            motivo = f"Percentual oferecido ({licitacao.percentual_premio:.2f}%) está abaixo do mínimo exigido ({percentual_minimo:.2f}%)"
            print(f"\n❌ DECISÃO: {decisao}")
        
        print(f"💬 Motivo: {motivo}")
        
        return ResultadoSimples(
            decisao=decisao,
            faixa=faixa,
            percentual_minimo_exigido=percentual_minimo,
            percentual_oferecido=licitacao.percentual_premio,
            valor_premio=valor_premio,
            atende_criterio=atende,
            diferenca_percentual=diferenca,
            motivo=motivo
        )
    
    def _identificar_faixa(self, valor: float) -> Tuple[str, Dict]:
        """Identifica a faixa de valor e retorna configuração"""
        for faixa_nome, config in self.TABELA_PERCENTUAIS.items():
            if config["min"] <= valor < config["max"]:
                return faixa_nome, config
        # Fallback (não deve acontecer)
        return "10M+", self.TABELA_PERCENTUAIS["10M+"]
    
    def analisar_lote(self, licitacoes: List[LicitacaoSimples]) -> List[ResultadoSimples]:
        """Analisa múltiplas licitações"""
        resultados = []
        for lic in licitacoes:
            resultado = self.analisar_licitacao(lic)
            resultados.append(resultado)
            print("\n" + "-"*80)
        return resultados
    
    def gerar_relatorio_consolidado(self, resultados: List[ResultadoSimples]) -> Dict:
        """Gera relatório consolidado das análises"""
        total = len(resultados)
        aprovadas = sum(1 for r in resultados if r.decisao == "PARTICIPAR")
        rejeitadas = total - aprovadas
        
        valor_total_analise = sum(r.valor_premio for r in resultados if r.atende_criterio)
        
        por_faixa = {}
        for resultado in resultados:
            if resultado.faixa not in por_faixa:
                por_faixa[resultado.faixa] = {"total": 0, "aprovadas": 0, "rejeitadas": 0}
            por_faixa[resultado.faixa]["total"] += 1
            if resultado.decisao == "PARTICIPAR":
                por_faixa[resultado.faixa]["aprovadas"] += 1
            else:
                por_faixa[resultado.faixa]["rejeitadas"] += 1
        
        return {
            "total_analisado": total,
            "aprovadas": aprovadas,
            "rejeitadas": rejeitadas,
            "taxa_aprovacao": (aprovadas / total * 100) if total > 0 else 0,
            "valor_total_premios_aprovados": valor_total_analise,
            "por_faixa": por_faixa,
            "timestamp": datetime.now().isoformat()
        }


def criar_cenarios_teste():
    """Cria 4 cenários para cada faixa (12 cenários totais)"""
    
    cenarios = []
    
    # FAIXA 1: R$ 1M - R$ 5M (mínimo 7%)
    print("\n" + "🟦"*40)
    print("FAIXA 1: R$ 1M - R$ 5M (Mínimo 7%)")
    print("🟦"*40)
    
    cenarios.extend([
        LicitacaoSimples("LIC-001", "Sistema Municipal de Saúde", 2_000_000.00, 8.0),  # ✅ Acima
        LicitacaoSimples("LIC-002", "Portal de Transparência", 3_500_000.00, 7.0),    # ✅ Exato
        LicitacaoSimples("LIC-003", "App Mobile Cidadão", 4_200_000.00, 6.5),         # ❌ Abaixo
        LicitacaoSimples("LIC-004", "Gestão Escolar Digital", 1_800_000.00, 9.0),     # ✅ Muito acima
    ])
    
    # FAIXA 2: R$ 5M - R$ 10M (mínimo 6%)
    print("\n" + "🟩"*40)
    print("FAIXA 2: R$ 5M - R$ 10M (Mínimo 6%)")
    print("🟩"*40)
    
    cenarios.extend([
        LicitacaoSimples("LIC-005", "Modernização Infraestrutura TI", 6_500_000.00, 7.0),  # ✅ Acima
        LicitacaoSimples("LIC-006", "Sistema Integrado de Gestão", 8_000_000.00, 6.0),    # ✅ Exato
        LicitacaoSimples("LIC-007", "Cloud Migration Gov", 7_200_000.00, 5.5),            # ❌ Abaixo
        LicitacaoSimples("LIC-008", "Datacenter Estadual", 9_800_000.00, 6.5),            # ✅ Acima
    ])
    
    # FAIXA 3: Acima de R$ 10M (mínimo 5%)
    print("\n" + "🟪"*40)
    print("FAIXA 3: Acima de R$ 10M (Mínimo 5%)")
    print("🟪"*40)
    
    cenarios.extend([
        LicitacaoSimples("LIC-009", "Transformação Digital Estadual", 15_000_000.00, 6.0),  # ✅ Acima
        LicitacaoSimples("LIC-010", "Smart City Nacional", 25_000_000.00, 5.0),            # ✅ Exato
        LicitacaoSimples("LIC-011", "Blockchain Gov Federal", 18_000_000.00, 4.5),         # ❌ Abaixo
        LicitacaoSimples("LIC-012", "IA para Saúde Pública", 12_500_000.00, 5.5),          # ✅ Acima
    ])
    
    return cenarios


def imprimir_resumo_visual(resultados: List[ResultadoSimples]):
    """Imprime resumo visual dos resultados"""
    print("\n" + "="*80)
    print("📊 RESUMO VISUAL DAS ANÁLISES")
    print("="*80 + "\n")
    
    # Agrupar por faixa
    faixas = {}
    for r in resultados:
        if r.faixa not in faixas:
            faixas[r.faixa] = {"aprovadas": [], "rejeitadas": []}
        
        if r.decisao == "PARTICIPAR":
            faixas[r.faixa]["aprovadas"].append(r)
        else:
            faixas[r.faixa]["rejeitadas"].append(r)
    
    # Imprimir por faixa
    for faixa in ["1M-5M", "5M-10M", "10M+"]:
        if faixa in faixas:
            dados = faixas[faixa]
            total_faixa = len(dados["aprovadas"]) + len(dados["rejeitadas"])
            
            print(f"\n🏷️  FAIXA: {faixa}")
            print(f"   Total: {total_faixa} licitações")
            print(f"   ✅ Aprovadas: {len(dados['aprovadas'])}")
            print(f"   ❌ Rejeitadas: {len(dados['rejeitadas'])}")
            
            if dados["aprovadas"]:
                print(f"\n   ✅ Aprovadas:")
                for r in dados["aprovadas"]:
                    print(f"      • {r.percentual_oferecido:.2f}% → R$ {r.valor_premio:,.2f}")
            
            if dados["rejeitadas"]:
                print(f"\n   ❌ Rejeitadas:")
                for r in dados["rejeitadas"]:
                    print(f"      • {r.percentual_oferecido:.2f}% (faltam {abs(r.diferenca_percentual):.2f}pp)")


def main():
    """Função principal"""
    print("\n" + "="*80)
    print("🎯 AGENTE SIMPLIFICADO - ANÁLISE POR PERCENTUAL DE PRÊMIO")
    print("="*80)
    print("\n📋 TABELA DE PERCENTUAIS:")
    print("   • R$ 1M - R$ 5M    → Mínimo 7%")
    print("   • R$ 5M - R$ 10M   → Mínimo 6%")
    print("   • Acima de R$ 10M  → Mínimo 5%")
    print("\n" + "="*80)
    
    # Criar agente
    agente = AgentePremioBR()
    
    # Criar cenários
    cenarios = criar_cenarios_teste()
    
    # Analisar
    print("\n🚀 Iniciando análises...\n")
    resultados = agente.analisar_lote(cenarios)
    
    # Resumo visual
    imprimir_resumo_visual(resultados)
    
    # Relatório consolidado
    relatorio = agente.gerar_relatorio_consolidado(resultados)
    
    print("\n\n" + "="*80)
    print("📈 RELATÓRIO CONSOLIDADO")
    print("="*80)
    print(f"\n✅ Total Analisado: {relatorio['total_analisado']}")
    print(f"✅ Aprovadas: {relatorio['aprovadas']}")
    print(f"❌ Rejeitadas: {relatorio['rejeitadas']}")
    print(f"📊 Taxa de Aprovação: {relatorio['taxa_aprovacao']:.1f}%")
    print(f"💰 Valor Total em Prêmios (Aprovadas): R$ {relatorio['valor_total_premios_aprovados']:,.2f}")
    
    print("\n📊 Por Faixa:")
    for faixa, dados in relatorio['por_faixa'].items():
        print(f"\n   {faixa}:")
        print(f"      Total: {dados['total']}")
        print(f"      Aprovadas: {dados['aprovadas']}")
        print(f"      Rejeitadas: {dados['rejeitadas']}")
        taxa = (dados['aprovadas'] / dados['total'] * 100) if dados['total'] > 0 else 0
        print(f"      Taxa: {taxa:.1f}%")
    
    print("\n" + "="*80)
    print("✨ Análises concluídas!")
    print("="*80 + "\n")
    
    return resultados, relatorio


if __name__ == "__main__":
    resultados, relatorio = main()
