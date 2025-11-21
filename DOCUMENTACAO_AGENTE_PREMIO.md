# 🎯 AGENTE SIMPLIFICADO - ANÁLISE POR PERCENTUAL DE PRÊMIO

## 📋 DOCUMENTAÇÃO COMPLETA

---

## 🎯 1. OBJETIVO DO FLUXO

### Objetivo Principal
**Automatizar a decisão de participação em licitações baseada EXCLUSIVAMENTE no percentual de prêmio oferecido para equipes de background.**

### Objetivos Específicos
- ✅ Garantir que apenas licitações com percentual adequado sejam aprovadas
- ✅ Proteger a sustentabilidade financeira das equipes de suporte
- ✅ Eliminar análises subjetivas através de critérios objetivos e claros
- ✅ Acelerar o processo de triagem de oportunidades
- ✅ Padronizar decisões em toda a organização

### Meta de Negócio
Assegurar que **TODAS** as licitações aprovadas ofereçam remuneração mínima adequada para as equipes de background (RH, Financeiro, Jurídico, Admin, TI, Comercial, Suporte, Qualidade), independente do porte do projeto.

---

## 💡 2. PROBLEMA QUE O FLUXO RESOLVE

### Contexto do Problema

#### Problema 1: Subestimação de Custos de Background
Empresas frequentemente focam apenas nos custos técnicos diretos (desenvolvedores, infraestrutura) e **esquecem** ou **subestimam** os custos das equipes de suporte que viabilizam a operação.

**Impacto:**
- Projetos financeiramente inviáveis
- Equipes de background sobrecarregadas
- Alta rotatividade por baixa remuneração
- Qualidade de entrega comprometida

#### Problema 2: Análise Manual Demorada
Avaliar cada licitação manualmente para verificar se o prêmio oferecido é suficiente para remunerar as equipes de background consome tempo e é sujeito a erros.

**Impacto:**
- Decisões lentas (horas ou dias)
- Inconsistência entre analistas
- Oportunidades perdidas por demora

#### Problema 3: Falta de Critérios Objetivos
Sem uma tabela clara de percentuais mínimos por faixa de valor, decisões são tomadas "no feeling", gerando:

**Impacto:**
- Aprovação de licitações ruins
- Rejeição de licitações boas
- Discussões internas sobre critérios
- Dificuldade de justificar decisões

### Solução Proposta

O agente resolve estes problemas através de:

1. **Tabela Objetiva de Percentuais Mínimos**
   - Faixa 1M-5M: mínimo 7%
   - Faixa 5M-10M: mínimo 6%
   - Faixa 10M+: mínimo 5%

2. **Análise Automatizada em Segundos**
   - Entrada: Valor total + Percentual oferecido
   - Processamento: < 1 segundo
   - Saída: PARTICIPAR ou NÃO PARTICIPAR

3. **Decisões Consistentes e Rastreáveis**
   - Mesmos critérios sempre
   - Relatórios automáticos
   - Justificativas claras

---

## 🔄 3. ETAPAS DO FLUXO (BPMN)

### Visão Geral do Fluxo

```
START → Extrair Dados → Identificar Faixa → Obter % Mínimo → 
Gateway (% ≥ Mínimo?) → 
  ├─ SIM → Relatório Positivo → END (✅ PARTICIPAR)
  └─ NÃO → Relatório Negativo → END (❌ NÃO PARTICIPAR)
```

---

### ETAPA 1: Receber Nova Licitação

**O que acontece:**
- Sistema recebe notificação de nova licitação disponível
- Pode ser via integração com portais (ComprasNet, Transparência) ou entrada manual

**Entrada:**
- Número da licitação
- Nome/descrição
- Valor total do contrato
- Percentual de prêmio oferecido

**Saída:**
- Dados estruturados da licitação

**Tempo:** < 1 segundo

---

### ETAPA 2: Extrair Dados

**O que faz:**
Valida e estrutura os dados essenciais para análise:
- Valor total (em R$)
- Percentual de prêmio (em %)

**Validações:**
- Valor total > 0
- Percentual entre 0 e 100
- Dados numéricos válidos

**Exemplo:**
```json
{
  "numero": "LIC-2025-001",
  "nome": "Sistema Municipal de Saúde",
  "valor_total": 2000000.00,
  "percentual_premio": 8.0
}
```

**Tempo:** < 0.1 segundo

---

### ETAPA 3: Identificar Faixa de Valor

**O que faz:**
Classifica a licitação em uma das três faixas baseado no valor total:

| Valor Total | Faixa |
|-------------|-------|
| R$ 1M - R$ 5M | "1M-5M" |
| R$ 5M - R$ 10M | "5M-10M" |
| Acima de R$ 10M | "10M+" |

**Lógica:**
```python
if 1_000_000 <= valor < 5_000_000:
    faixa = "1M-5M"
elif 5_000_000 <= valor < 10_000_000:
    faixa = "5M-10M"
elif valor >= 10_000_000:
    faixa = "10M+"
```

**Exemplos:**
- R$ 2.000.000 → Faixa "1M-5M"
- R$ 7.200.000 → Faixa "5M-10M"
- R$ 15.000.000 → Faixa "10M+"

**Tempo:** < 0.01 segundo

---

### ETAPA 4: Obter Percentual Mínimo da Faixa

**O que faz:**
Consulta a tabela de percentuais mínimos e retorna o valor correspondente à faixa identificada.

**Tabela de Percentuais:**
```python
TABELA = {
    "1M-5M": 7.0,
    "5M-10M": 6.0,
    "10M+": 5.0
}
```

**Exemplo:**
- Faixa "1M-5M" → 7.0%
- Faixa "5M-10M" → 6.0%
- Faixa "10M+" → 5.0%

**Justificativa dos Percentuais:**

**Por que 7% para faixa 1M-5M?**
- Projetos menores têm custos fixos proporcionalmente maiores
- Menor economia de escala
- Maior risco relativo
- Necessidade de cobrir custos de setup e finalização

**Por que 6% para faixa 5M-10M?**
- Projetos médios já têm alguma economia de escala
- Custos fixos diluídos em valor maior
- Risco relativo menor

**Por que 5% para faixa 10M+?**
- Grandes projetos têm economia de escala significativa
- Custos fixos muito diluídos
- Volume permite margem menor ainda viável

**Tempo:** < 0.01 segundo

---

### ETAPA 5: GATEWAY - Verificar Percentual

**O que faz:**
Compara o percentual oferecido com o percentual mínimo exigido.

**Critério de Decisão:**
```
SE percentual_oferecido >= percentual_minimo:
    ENTÃO → Continua para Relatório Positivo
SENÃO:
    ENTÃO → Continua para Relatório Negativo
```

**Exemplos:**

✅ **Caso APROVADO:**
- Oferecido: 8.0% | Mínimo: 7.0% | 8.0 ≥ 7.0 → **SIM**

✅ **Caso APROVADO (exato):**
- Oferecido: 7.0% | Mínimo: 7.0% | 7.0 ≥ 7.0 → **SIM**

❌ **Caso REJEITADO:**
- Oferecido: 6.5% | Mínimo: 7.0% | 6.5 ≥ 7.0 → **NÃO**

**Cálculos Adicionais:**
- Valor do prêmio = valor_total × (percentual_oferecido / 100)
- Diferença = percentual_oferecido - percentual_minimo

**Tempo:** < 0.01 segundo

---

### ETAPA 6A: Gerar Relatório Positivo

**Quando acontece:**
Quando percentual oferecido ≥ percentual mínimo

**O que contém:**

```json
{
  "decisao": "PARTICIPAR",
  "faixa": "1M-5M",
  "percentual_minimo_exigido": 7.0,
  "percentual_oferecido": 8.0,
  "valor_premio": 160000.0,
  "atende_criterio": true,
  "diferenca_percentual": 1.0,
  "motivo": "Percentual oferecido (8.00%) atende o mínimo exigido (7.00%)"
}
```

**Próximos Passos Sugeridos:**
1. Alocar equipe de background
2. Iniciar preparação de proposta
3. Estimar recursos necessários
4. Definir cronograma

**Tempo:** < 0.1 segundo

---

### ETAPA 6B: Gerar Relatório Negativo

**Quando acontece:**
Quando percentual oferecido < percentual mínimo

**O que contém:**

```json
{
  "decisao": "NAO_PARTICIPAR",
  "faixa": "1M-5M",
  "percentual_minimo_exigido": 7.0,
  "percentual_oferecido": 6.5,
  "valor_premio": 273000.0,
  "atende_criterio": false,
  "diferenca_percentual": -0.5,
  "motivo": "Percentual oferecido (6.50%) está abaixo do mínimo exigido (7.00%)"
}
```

**Alternativas Sugeridas:**
1. Aguardar republicação com valor superior
2. Negociar aumento do percentual (se possível)
3. Buscar parceria para dividir custos
4. Focar em outras oportunidades

**Tempo:** < 0.1 segundo

---

### ETAPA 7: Decisão Final

**Saídas Possíveis:**

**✅ PARTICIPAR**
- Todos os critérios atendidos
- Relatório positivo gerado
- Sistema pode disparar workflow de participação
- Notificação para equipe responsável

**❌ NÃO PARTICIPAR**
- Critério não atendido
- Relatório negativo gerado
- Licitação arquivada ou marcada para revisão futura
- Notificação de rejeição

**Tempo Total do Fluxo:** < 1 segundo

---

## 📊 4. CENÁRIOS DEMONSTRATIVOS

### FAIXA 1: R$ 1M - R$ 5M (Mínimo 7%)

#### Cenário 1.1: APROVADO (Acima do Mínimo) ✅
```
Licitação: Sistema Municipal de Saúde
Valor Total: R$ 2.000.000
Percentual Oferecido: 8,0%
Percentual Mínimo: 7,0%
Valor do Prêmio: R$ 160.000
Diferença: +1,0pp
Decisão: PARTICIPAR
```

#### Cenário 1.2: APROVADO (Exatamente no Mínimo) ✅
```
Licitação: Portal de Transparência
Valor Total: R$ 3.500.000
Percentual Oferecido: 7,0%
Percentual Mínimo: 7,0%
Valor do Prêmio: R$ 245.000
Diferença: ±0,0pp
Decisão: PARTICIPAR
```

#### Cenário 1.3: REJEITADO (Abaixo do Mínimo) ❌
```
Licitação: App Mobile Cidadão
Valor Total: R$ 4.200.000
Percentual Oferecido: 6,5%
Percentual Mínimo: 7,0%
Valor do Prêmio: R$ 273.000
Diferença: -0,5pp
Decisão: NÃO PARTICIPAR
Motivo: Faltam 0,5 pontos percentuais
```

#### Cenário 1.4: APROVADO (Muito Acima) ✅
```
Licitação: Gestão Escolar Digital
Valor Total: R$ 1.800.000
Percentual Oferecido: 9,0%
Percentual Mínimo: 7,0%
Valor do Prêmio: R$ 162.000
Diferença: +2,0pp
Decisão: PARTICIPAR
```

---

### FAIXA 2: R$ 5M - R$ 10M (Mínimo 6%)

#### Cenário 2.1: APROVADO ✅
```
Licitação: Modernização Infraestrutura TI
Valor Total: R$ 6.500.000
Percentual Oferecido: 7,0%
Percentual Mínimo: 6,0%
Valor do Prêmio: R$ 455.000
Diferença: +1,0pp
Decisão: PARTICIPAR
```

#### Cenário 2.2: APROVADO (Exato) ✅
```
Licitação: Sistema Integrado de Gestão
Valor Total: R$ 8.000.000
Percentual Oferecido: 6,0%
Percentual Mínimo: 6,0%
Valor do Prêmio: R$ 480.000
Diferença: ±0,0pp
Decisão: PARTICIPAR
```

#### Cenário 2.3: REJEITADO ❌
```
Licitação: Cloud Migration Gov
Valor Total: R$ 7.200.000
Percentual Oferecido: 5,5%
Percentual Mínimo: 6,0%
Valor do Prêmio: R$ 396.000
Diferença: -0,5pp
Decisão: NÃO PARTICIPAR
```

#### Cenário 2.4: APROVADO ✅
```
Licitação: Datacenter Estadual
Valor Total: R$ 9.800.000
Percentual Oferecido: 6,5%
Percentual Mínimo: 6,0%
Valor do Prêmio: R$ 637.000
Diferença: +0,5pp
Decisão: PARTICIPAR
```

---

### FAIXA 3: Acima de R$ 10M (Mínimo 5%)

#### Cenário 3.1: APROVADO ✅
```
Licitação: Transformação Digital Estadual
Valor Total: R$ 15.000.000
Percentual Oferecido: 6,0%
Percentual Mínimo: 5,0%
Valor do Prêmio: R$ 900.000
Diferença: +1,0pp
Decisão: PARTICIPAR
```

#### Cenário 3.2: APROVADO (Exato) ✅
```
Licitação: Smart City Nacional
Valor Total: R$ 25.000.000
Percentual Oferecido: 5,0%
Percentual Mínimo: 5,0%
Valor do Prêmio: R$ 1.250.000
Diferença: ±0,0pp
Decisão: PARTICIPAR
```

#### Cenário 3.3: REJEITADO ❌
```
Licitação: Blockchain Gov Federal
Valor Total: R$ 18.000.000
Percentual Oferecido: 4,5%
Percentual Mínimo: 5,0%
Valor do Prêmio: R$ 810.000
Diferença: -0,5pp
Decisão: NÃO PARTICIPAR
```

#### Cenário 3.4: APROVADO ✅
```
Licitação: IA para Saúde Pública
Valor Total: R$ 12.500.000
Percentual Oferecido: 5,5%
Percentual Mínimo: 5,0%
Valor do Prêmio: R$ 687.500
Diferença: +0,5pp
Decisão: PARTICIPAR
```

---

## 📈 5. RESULTADOS CONSOLIDADOS

### Resumo Geral
- **Total Analisado:** 12 licitações
- **Aprovadas:** 9 (75%)
- **Rejeitadas:** 3 (25%)
- **Valor Total em Prêmios (Aprovadas):** R$ 4.976.500

### Por Faixa

#### Faixa 1M-5M
- Total: 4 licitações
- Aprovadas: 3 (75%)
- Rejeitadas: 1 (25%)
- Valor em Prêmios: R$ 567.000

#### Faixa 5M-10M
- Total: 4 licitações
- Aprovadas: 3 (75%)
- Rejeitadas: 1 (25%)
- Valor em Prêmios: R$ 1.572.000

#### Faixa 10M+
- Total: 4 licitações
- Aprovadas: 3 (75%)
- Rejeitadas: 1 (25%)
- Valor em Prêmios: R$ 2.837.500

---

## 🎓 6. CONCLUSÃO

### Vantagens do Sistema

1. **Simplicidade**
   - Apenas 2 dados necessários: valor + percentual
   - Decisão em < 1 segundo
   - Fácil de entender e explicar

2. **Objetividade**
   - Critérios claros e quantificáveis
   - Sem margem para interpretação
   - Decisões consistentes

3. **Proteção Financeira**
   - Garante sustentabilidade das equipes background
   - Evita projetos com margem insuficiente
   - Reduz risco de prejuízo

4. **Escalabilidade**
   - Pode analisar milhares de licitações
   - Sem custo adicional por análise
   - Processamento paralelo possível

5. **Rastreabilidade**
   - Todas as decisões registradas
   - Justificativas automáticas
   - Auditoria facilitada

### Limitações e Considerações

1. **Não considera complexidade técnica**
   - Licitações complexas podem precisar maior percentual
   - Sistema não avalia requisitos técnicos

2. **Percentuais fixos por faixa**
   - Não há granularidade dentro da faixa
   - R$ 1M e R$ 4,9M têm mesmo mínimo (7%)

3. **Não avalia outros riscos**
   - Prazo, localização, cliente, concorrência
   - Foco exclusivo em percentual de prêmio

### Recomendações de Uso

✅ **Use este agente quando:**
- Precisar de triagem rápida de muitas licitações
- Critério principal for viabilidade financeira
- Quiser padronizar decisões iniciais

⚠️ **Combine com análise adicional quando:**
- Licitação for estratégica (cliente importante)
- Houver requisitos técnicos complexos
- Valor for próximo aos limites das faixas

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Autor:** Sistema Automatizado LicitBrain
