import json
import sys

file_ours = sys.argv[2]
file_theirs = sys.argv[3]

with open(file_ours, 'r') as f:
    ours = json.load(f)
with open(file_theirs, 'r') as f:
    theirs = json.load(f)

chips_ours = ours.get("AllCustomChipNames", [])
chips_theirs = theirs.get("AllCustomChipNames", [])
ours["AllCustomChipNames"] = list(set(chips_ours + chips_theirs))

with open(file_ours, 'w') as f:
    json.dump(ours, f, indent=4)
