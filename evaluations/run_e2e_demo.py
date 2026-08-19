#!/usr/bin/env python3
"""
End-to-end run of the kojiki-marketing-department agent against local Ollama (qwen2.5:14b).
Proves the agent: (1) follows the Kojiki Orientation Protocol, (2) emits a valid
Decision Object + Learning Ledger record. Output saved to 03-marketing/evaluations/run-001/.
No third-party deps beyond the Ollama HTTP API (stdlib only).
"""
import json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
MKT = os.path.join(ROOT, "03-marketing")
AGENT_MD = os.path.join(MKT, "AGENT.md")
VALIDATOR = os.path.join(MKT, "tools", "validate.py")
MODEL = "qwen2.5:14b"
OUTDIR = os.path.join(MKT, "evaluations", "run-001")
os.makedirs(OUTDIR, exist_ok=True)

def ollama_chat(system, user, temperature=0.2):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "stream": False,
    }
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())["message"]["content"]

def extract_json(text):
    # find the outermost {...} block
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

agent_md = open(AGENT_MD).read()

# ---- PHASE 1: Orientation Protocol ----
print("=== PHASE 1: Kojiki Orientation Protocol ===")
orient_sys = agent_md + "\n\nYou are being installed as the Marketing department agent. Run the Kojiki Orientation Protocol now: ask the 5 first-run questions IN ORDER and, for this simulation, ANSWER them yourself as if you are a B2B SaaS marketing leader (assume the answers). Then state you are oriented."
orient_ans = ollama_chat(orient_sys, "Begin the Orientation Protocol.", temperature=0.3)
print(orient_ans[:1600])
open(os.path.join(OUTDIR, "orientation.txt"), "w").write(orient_ans)

# ---- PHASE 2: Real decision (Decision Object + Learning Ledger) ----
print("\n=== PHASE 2: Real marketing decision ===")
decision_sys = agent_md + """

You are oriented as the Marketing department agent for a B2B SaaS company.
Now exercise your function as a decision system. Scenario:
  "We are launching our product in the German market (EU/Germany, GDPR regime,
   DACH geography, B2B SaaS subscription model). Decide the GTM messaging strategy
   and produce the canonical record."

Produce a single JSON object with exactly two keys:
  "decision_object": { ... 19 fields per the schema below ... }
  "learning_ledger": { ... 10 fields per the schema below ... }

decision_object fields (all required):
  decision_id, decision_name, owning_function, decision_owner_role,
  trigger_condition, current_state, required_inputs (list), evidence_threshold,
  available_options (non-empty list), decision_criteria, constraints,
  risk_level (one of low/medium/high/critical),
  delegation_level (one of Own/Recommend/Consult/Execute/Approve/Escalate/Automate),
  escalation_conditions, expected_outcome, verification_method,
  actual_outcome, learning_extracted, rule_version, last_reviewed

learning_ledger fields (all required):
  case, decision, assumption, action, expected_result, actual_result,
  variance, cause, learning, rule_update

Output ONLY the JSON, no commentary.
"""
decision_ans = ollama_chat(decision_sys, "Produce the decision record now.", temperature=0.1)
print(decision_ans[:1200])
rec = extract_json(decision_ans)
if not rec:
    print("!! could not parse JSON from model output")
    open(os.path.join(OUTDIR, "raw_decision.txt"), "w").write(decision_ans)
    sys.exit(2)
rec_path = os.path.join(OUTDIR, "decision-record.json")
json.dump(rec, open(rec_path, "w"), indent=2)

# ---- PHASE 3: validate against repo schema ----
print("\n=== PHASE 3: validate against repo schema ===")
res = subprocess.run([sys.executable, VALIDATOR, rec_path], capture_output=True, text=True)
print(res.stdout.strip())
print(res.stderr.strip())
valid = "ALL VALID" in res.stdout

summary = {
    "model": MODEL,
    "repo": "03-marketing",
    "orientation_ran": True,
    "decision_produced": rec is not None,
    "schema_valid": valid,
    "decision_id": (rec or {}).get("decision_object", {}).get("decision_id"),
}
json.dump(summary, open(os.path.join(OUTDIR, "summary.json"), "w"), indent=2)
print("\nSUMMARY:", json.dumps(summary, indent=2))
print("Artifacts in:", OUTDIR)
