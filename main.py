import os

TEXT = (
    "Somewhere a glacier is moving one inch.\n"
    "No one is waiting for it.\n"
    "The light touching you now left its star before anyone had a word for star, "
    "and it has not hurried once.\n"
    "Between the inch and the light, nothing is asked of you.\n"
    "Everything vast is slow."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
