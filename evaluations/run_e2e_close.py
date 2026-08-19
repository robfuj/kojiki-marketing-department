#!/usr/bin/env python3
"""
PHASE 4 (closure): feed a simulated outcome and have the agent complete the
Learning Ledger (actual_result, variance, cause, learning, rule_update) so the
decision is fully closed — proving the "exceptions are learning" loop.
Reads the record from run-001, appends the closed-loop fields, re-validates.
"""
import json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(ROOT, "03-marketing", "evaluations", "run-001", "decision-record.json")
MKT = os.path.join(ROOT, "03-marketing")
VALIDATOR = os.path.join(MKT, "tools", "validate.py")
MODEL = "qwen2.5:14b"

def ollama_chat(system, user, temperature=0.2):
    payload = {"model": MODEL, "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": user}], "temperature": temperature, "stream": False}
    req = urllib.request.Request("http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())["message"]["content"]

rec = json.load(open(REC))
do = rec["decision_object"]; ll = rec["learning_ledger"]

sys_p = f"""You are the Marketing department agent (Kojiki Decision System). You made a decision
recorded as: {json.dumps(rec, indent=2)}.

Now the decision has played out. Simulated reality:
  - The GDPR-compliance-led messaging (Option A) launched. After 6 weeks: lead volume +38%,
    but qualified-MQL-to-SQL conversion was 9% vs 14% target. Sales flagged that German
    procurement requires TUV/certification proof, not just GDPR statements. Several enterprise
    deals stalled at legal review.

Complete the record: fill these fields with concrete values (no nulls):
  decision_object.actual_outcome, decision_object.learning_extracted, decision_object.rule_version (bump), decision_object.last_reviewed (2026-08-18)
  learning_ledger.actual_result, learning_ledger.variance, learning_ledger.cause, learning_ledger.learning, learning_ledger.rule_update
Output ONLY the complete JSON record (same two keys), no commentary."""

ans = ollama_chat(sys_p, "Close the loop now.", temperature=0.1)
m = re.search(r"\{.*\}", ans, re.DOTALL)
closed = json.loads(m.group(0))
out = os.path.join(ROOT, "03-marketing", "evaluations", "run-001", "decision-record-closed.json")
json.dump(closed, open(out, "w"), indent=2)
print("CLOSED-LOOP RECORD:")
print(json.dumps(closed, indent=2)[:2500])

res = subprocess.run([sys.executable, VALIDATOR, out], capture_output=True, text=True)
print("\nVALIDATION:", res.stdout.strip())
print(res.stderr.strip())

summary = json.load(open(os.path.join(ROOT, "03-marketing", "evaluations", "run-001", "summary.json")))
summary["loop_closed"] = "ALL VALID" in res.stdout
summary["learning_extracted"] = closed["decision_object"].get("learning_extracted")
json.dump(summary, open(os.path.join(ROOT, "03-marketing", "evaluations", "run-001", "summary.json"), "w"), indent=2)
print("\nFINAL SUMMARY:", json.dumps(summary, indent=2))
