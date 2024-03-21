import os
from pathlib import Path

base = "./gerbers/right"
for file in Path(base).iterdir():
    if file.name.startswith("xurp") and not file.is_dir():
        fp = file.name
        new_file = fp.replace("xurp", "duosync")
        new_file = os.path.join(base, new_file)
        fp = os.path.join(base, fp)
        os.rename(fp, new_file)
