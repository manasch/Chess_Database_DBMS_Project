from pathlib import Path

current = Path.cwd().resolve()

insert = "insert into opening values\n"

for i in (current.parent / "db").iterdir():
    if i.suffix == ".tsv":
        with open(i) as f:
            f.readline()
            a = f.readlines()
            for o in a:
                p = o.strip().split('\t')
                insert += f"(\"{p[0]}\", \"{p[1]}\", \"{p[2]}\"),\n"

with open('temp.sql', 'w') as f:
    f.write(insert)
