# -*- coding: utf-8 -*-
"""
Coleta a série REAL de interesse de busca do Google Trends (Brasil) para os
termos do debate educacional e salva em trends_data.json — a fonte da linha
do tempo do painel (index.html).

Cada termo é consultado em query própria, de modo que fica auto-normalizado
0–100 na sua própria série (senão o ENEM, muito maior, achataria o Pé-de-Meia).

Requer: pip install pytrends
Uso:    python fetch_trends.py
"""
import json, time
from pytrends.request import TrendReq

TERMS = ['Pé-de-Meia', 'ENEM', 'SISU']
TIMEFRAME = '2024-08-01 2025-07-31'   # 12 meses retrospectivos
GEO = 'BR'

def main():
    series = {}
    for t in TERMS:
        p = TrendReq(hl='pt-BR', tz=180)          # NÃO passar retries= (incompat. urllib3 novo)
        p.build_payload([t], timeframe=TIMEFRAME, geo=GEO)
        df = p.interest_over_time()
        series[t] = {ix.strftime('%Y-%m-%d'): int(v) for ix, v in df[t].items()}
        print(f'coletado: {t:12s} ({len(series[t])} semanas)')
        time.sleep(3)                              # evita rate-limit (429)

    dates = sorted(series[TERMS[0]].keys())
    rows = [{'date': d, **{t: series[t].get(d, 0) for t in TERMS}} for d in dates]
    out = {
        'source': 'Google Trends (geo=BR, pt-BR) — cada termo auto-normalizado 0–100 em query própria',
        'timeframe': TIMEFRAME.replace(' ', '..'),
        'terms': TERMS, 'granularity': 'weekly',
        'fetched': time.strftime('%Y-%m-%d'), 'data': rows,
    }
    with open('trends_data.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'salvo trends_data.json — {len(rows)} semanas')

if __name__ == '__main__':
    main()
