import json, os, math
inp = os.environ.get("MAKEFUN_INPUT_DIR","/input")
out = os.environ.get("MAKEFUN_OUTPUT_DIR","/output")
os.makedirs(out, exist_ok=True)
task = json.load(open(os.path.join(inp,"task.json")))
hist = [json.loads(l) for l in open(os.path.join(inp,"history.ndjson")) if l.strip()]
last = hist[-1]["up_and_coming"]
# baseline: top10 as last chart order; probs: place k: 0.5 to game at k, 0.15 to neighbors
ids = [g["universe_id"] for g in last[:10]]
probs = []
for k in range(1,11):
    i = k-1
    probs.append({"universe_id": ids[i], "place": k, "p": 0.5})
    if i-1>=0: probs.append({"universe_id": ids[i-1], "place": k, "p": 0.15})
    if i+1<10: probs.append({"universe_id": ids[i+1], "place": k, "p": 0.15})
json.dump({"probabilities": probs, "top10": ids}, open(os.path.join(out,"forecast.json"),"w"))
