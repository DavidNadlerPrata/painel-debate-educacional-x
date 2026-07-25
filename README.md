# Painel — Inteligência Social no Debate Educacional no X

Painel de monitoramento (Capítulo 7) da tese de doutorado de **Leonardo Barchini** —
PPGGTD/UFT, orientação Prof. Dr. David Nadler Prata.

O painel materializa a tese: em monitoramento governamental orientado a eventos, a
**validade dos indicadores de posicionamento depende mais da especificação do alvo do
que da escolha do classificador**. O artefato central é a **Ficha de Especificação de
Alvo (FEA)**.

> **Versão publicada (raiz):** ancorada em **dados reais** — série do Google Trends e
> eventos-âncora com fonte citável.
> **Versão anterior:** o PoC com dados sintéticos permanece em [`/poc/`](poc/).

## O que é real e o que é estimativa

| Camada | Estatuto | Fonte |
|---|---|---|
| Série temporal / picos | **Real** | Google Trends (BR), via `pytrends` |
| Episódios, datas, eventos-âncora | **Real** | Fonte oficial/imprensa citada em cada ficha (link) |
| Posicionamento, deslocamento de alvo, tipologia, experimento fatorial | **Estimativa** | Dependem do corpus anotado (a construir); substituídos por medição real após a coleta do X (V-Tracker) e anotação |

O painel sinaliza a distinção com selos `real` / `estimado` em cada seção.

## Episódios reais (ancorados em picos reais do Trends)

| Episódio | Pico | Data | Fonte |
|---|---|---|---|
| ENEM 2024 — aplicação | ENEM=100 | 03–10/11/2024 | Agência Brasil |
| ENEM 2024 — resultado | ENEM=79 | 13/01/2025 | Agência Brasil |
| SISU 2025 — notas de corte e chamada regular | SISU=88–100 | 18–26/01/2025 | MEC |
| TCU × Pé-de-Meia — bloqueio e liberação (120 dias) | PdM=85 | 13/02/2025 | Portal TCU / Rádio Senado |
| Pé-de-Meia — pagamento da parcela de R$ 1.000 | PdM=100 | 25–27/02/2025 | Agência Gov / MEC |

Há ainda um **pico real em jul/2025** (Pé-de-Meia=69) exibido como *FEA pendente* —
detectado, mas ainda não caracterizado, refletindo o fluxo real de trabalho.

## Estrutura do repositório

- **`index.html`** — o painel (versão com dados reais). Autocontido; servido pelo GitHub Pages.
- **`trends_data.json`** — série real do Google Trends embutida no painel.
- **`fetch_trends.py`** — coletor da série real (requer `pip install pytrends`; `python fetch_trends.py`).
- **`gerar_proposta.py`** — gera o documento Word da proposta da PoC (requer `python-docx`).
- **`poc/`** — versão anterior do painel, com dados sintéticos.

## Nota metodológica

Google Trends mede **interesse de busca**, não menções no X — é um *proxy* real de atenção
pública, usado enquanto a coleta do X (V-Tracker) prevista na tese não é realizada. Os picos
de busca coincidem com os eventos-âncora reais, validando a lógica de detecção de episódios.

## Governança

Análise sempre agregada · vedado o perfilamento individual e qualquer inferência sobre pessoas
naturais identificáveis · minimização e pseudonimização desde a coleta · finalidade explícita
sob a LGPD. O painel diz o que o debate mostra sobre políticas, não sobre pessoas.
