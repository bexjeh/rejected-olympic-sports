import os

ENTRY = "50km Race Walk, in which one foot must stay on the ground at all times while the other rides a skateboard."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
