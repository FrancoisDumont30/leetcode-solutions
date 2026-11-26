"""Generate INDEX_SQL_PANDAS.md and INDEX_PYTHON3.md from the README table.
Sorted by difficulty (Easy, Medium, Hard), then problem id."""
import re
ORDER = {"Easy": 0, "Medium": 1, "Hard": 2}
rows = []
for line in open("README.md", encoding="utf-8"):
    m = re.match(r"\| (\d+) \| (\[.*?\]\(.*?\)) \| (\w+) \| (.*?) \| (.*?) \|$", line.strip())
    if m:
        rows.append((int(m[1]), m[2], m[3], [x.strip() for x in m[4].split(",")], m[5]))

def write(path, title, keep):
    sel = sorted((r for r in rows if keep(r[3])), key=lambda r: (ORDER[r[2]], r[0]))
    out = [f"# {title}", "", f"{len(sel)} problems, sorted by difficulty (Easy, Medium, Hard), then by id.", ""]
    for diff in ORDER:
        part = [r for r in sel if r[2] == diff]
        if not part:
            continue
        out += [f"## {diff} ({len(part)})", "", "| # | Problem | Languages | Last accepted |", "|---|---|---|---|"]
        out += [f"| {r[0]} | {r[1]} | {', '.join(r[3])} | {r[4]} |" for r in part]
        out.append("")
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return len(sel)

a = write("INDEX_SQL_PANDAS.md", "Index: SQL / Pandas", lambda l: "SQL" in l or "Pandas" in l)
b = write("INDEX_PYTHON3.md", "Index: Python3", lambda l: "Python3" in l)
print(a, b, len(rows))
