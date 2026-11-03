"""Draft a q-<科目>.tsv from the site's public index (https://tiku.ptsfu.org/index.json.gz).

Usage: python3 -I derive_index.py index.json.gz _src/_index/units-<科目>.tsv <科目> > draft.tsv

Rules (checked against build_practice_set on 2026-11-03):
- 台大/交大/清大, 民國 100–107, paper category 軟體 (資料結構, 演算法) or 數學 (離散數學, 線性代數).
- unit_keys keep labels of the category's own subjects; labels of non-main subjects
  (程式語言, 工程數學, 資料庫…) become "<科目>§label" when that key is in the units file;
  labels of main subjects from the other category are dropped.
The draft is NOT authoritative: verify with build_practice_set(exclude_ids=<all draft ids>)
(must return 0 questions; any it returns must be added) and a small sample
(exclude all but ~10 ids; the rows returned must equal the draft rows).
離散數學 needed 36 extra 軟體-paper questions found this way.
"""
import gzip,json,sys
d=json.load(gzip.open(sys.argv[1])); subj=sys.argv[3]
keys=[l.split('\t')[0] for l in open(sys.argv[2]) if l.strip()]
bare={}
for k in keys: bare.setdefault(k.split('§',1)[-1],[]).append(k)
lab={}
for u in d['units']: lab.setdefault(u['l'],set()).add(u['s'])
CAT={'資料結構':'軟體','演算法':'軟體','離散數學':'數學','線性代數':'數學'}
MAIN={'軟體':{'資料結構','演算法'},'數學':{'離散數學','線性代數'}}
def ukeys(i):
    out=[]
    for x in i['u']:
        ss=lab.get(x,set())
        if ss & MAIN[CAT[subj]]: out.append(x)
        elif x in bare: out.append(bare[x][0])
    return out
rows={}
for i in d['items']:
    if i['s'] not in('台大','交大','清大') or not 100<=int(i['y'])<=107: continue
    if i['c']!=CAT[subj]: continue
    if not any(x in bare for x in i['u']) : continue
    rows[i['i']]='|'.join([i['i'],i['y'],i['s'],i['j'],i['q'],';'.join(ukeys(i))])
for k,v in rows.items(): print(v)
