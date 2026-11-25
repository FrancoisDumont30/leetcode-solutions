import json,re,os,subprocess,datetime
from bs4 import BeautifulSoup,NavigableString
o=json.load(open('/tmp/out.json')); best=json.load(open('/tmp/best.json')); subs=json.load(open('/tmp/subs.json'))
def md(n):
    if isinstance(n,NavigableString): return str(n)
    t=n.name; inner=''.join(md(c) for c in n.children)
    if t=='pre': return '\n```text\n'+n.get_text().strip('\n')+'\n```\n\n'
    if t=='code': return '`'+n.get_text()+'`'
    if t in('strong','b'): return '**'+inner.strip()+'**'
    if t in('em','i'): return '*'+inner.strip()+'*'
    if t=='p': 
        s=inner.strip(); return s+'\n\n' if s else ''
    if t=='li': return '- '+inner.strip()+'\n'
    if t in('ul','ol'): return inner+'\n'
    if t=='br': return '\n'
    if t=='sup': return '^'+inner
    if t=='sub': return '_'+inner
    if t=='img': return '![]('+(n.get('src') or '')+')'
    return inner
LANG={'mysql':('SQL','solution.sql'),'pythondata':('Pandas','solution_pandas.py'),'python3':('Python3','solution.py')}
probs={}
for slug,q in o['qs'].items():
    num=int(q['questionFrontendId']); d=f"problems/{num:04d}-{slug}"
    probs[slug]=dict(num=num,dir=d,q=q,sols=[])
for b in best:
    c=o['codes'][b['id']]; probs[b['slug']]['sols'].append((b['lang'],c['code'],int(b['ts'])))
os.makedirs('problems',exist_ok=True)
def run(*a): subprocess.run(a,check=True)
# commit 1 statements
for p in probs.values():
    q=p['q']; os.makedirs(p['dir'],exist_ok=True)
    text=md(BeautifulSoup(q['content'] or '','html.parser'))
    text=re.sub(r'\n{3,}','\n\n',text).replace('\xa0',' ').strip()
    tags=', '.join(t['name'] for t in q['topicTags'])
    open(p['dir']+'/README.md','w').write(f"# {p['num']}. {q['title'].strip()}\n\n**Difficulty:** {q['difficulty']}  \n**Topics:** {tags}  \n**Link:** https://leetcode.com/problems/{q['titleSlug'] if 'titleSlug' in q else [k for k,v in probs.items() if v is p][0]}/\n\n## Statement\n\n{text}\n\n*Problem statement and examples belong to LeetCode. Kept here for personal study only.*\n")
open('README.md','w').write("# leetcode-solutions\n\nPersonal LeetCode study notes. Index coming in a later commit.\n")
run('git','add','-A'); run('git','commit','-qm','Add problem statements and examples for 105 solved LeetCode problems')
for lang,cm in [('mysql','Add SQL (MySQL) solutions'),('pythondata','Add Pandas solutions'),('python3','Add Python3 solutions')]:
    n=0
    for p in probs.values():
        for l,code,ts in p['sols']:
            if l==lang:
                open(p['dir']+'/'+LANG[l][1],'w').write(code.rstrip()+'\n'); n+=1
    run('git','add','-A'); run('git','commit','-qm',f'{cm} ({n} files)')
# index
rows=[];cnt={}
for slug,p in sorted(probs.items(),key=lambda kv:kv[1]['num']):
    q=p['q']; langs=', '.join(sorted({LANG[l][0] for l,_,_ in p['sols']}))
    last=max([ts for _,_,ts in p['sols']]); date=datetime.datetime.utcfromtimestamp(last).strftime('%Y-%m-%d')
    cnt[q['difficulty']]=cnt.get(q['difficulty'],0)+1
    rows.append(f"| {p['num']} | [{q['title'].strip()}]({p['dir']}/README.md) | {q['difficulty']} | {langs} | {date} |")
r="# leetcode-solutions\n\nPersonal LeetCode study notes: my accepted solutions (SQL, Pandas, Python3) with the problem statements and examples.\n\n> Problem statements and examples belong to LeetCode (https://leetcode.com). This repository is private and kept for personal study only.\n\n"
r+=f"**{len(rows)} problems** ("+', '.join(f'{k}: {v}' for k,v in cnt.items())+"). Profile: https://leetcode.com/u/FD30/\n\nEach problem has a folder `problems/NNNN-slug/` with `README.md` (statement) and the solution file(s): `solution.sql` (MySQL), `solution_pandas.py` (Pandas), `solution.py` (Python3). The solution is the latest accepted submission per language. Date = last accepted submission (UTC).\n\n## Index\n\n| # | Problem | Difficulty | Languages | Last accepted |\n|---|---|---|---|---|\n"+'\n'.join(rows)+'\n'
open('README.md','w').write(r)
run('git','add','-A'); run('git','commit','-qm','Add README index (problem, difficulty, language, date)')
