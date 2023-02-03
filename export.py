import json

TXT_PATH = "rules.txt"
JSON_PATH = "export/rules.json"
MD_PATH = "export/rules.md"


def parse(text):
    res = text.split('---\n')
    rules: list = []
    for r in res:
        e = r.split('\n')
        rule: dict = {
            "title": e[0].rstrip(),
            "content": e[1].rstrip()
        }
        rules.append(rule)
    print(f"Parsed rules from {TXT_PATH}")
    return rules


def exportJson(rules: list):
    jsonStr = json.dumps(rules, indent=4)
    open(JSON_PATH, "w").write(jsonStr)
    print(f"Exported JSON to {JSON_PATH}")


def exportMd(rules: list):
    exp = ""
    i = 0
    for r in rules:
        exp += f"**§{i:02d} {r['title']}**\n{r['content']}\n\n"
        i += 1
    open(MD_PATH, "w").write(exp.rstrip())
    print(f"Exported Discord Markdown to {MD_PATH}")
    

with open("rules.txt", "r") as txt:
    rules = parse(txt.read())
    exportJson(rules)
    exportMd(rules)
