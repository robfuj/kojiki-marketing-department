# 03 — Marketing

> Part of the **Kojiki Decision System**. This repo is the
> **Marketing** line. It references the shared ontology in
> [`00-kojiki-ontology`](https://github.com/robfuj/kojiki-ontology) for the
> canonical schemas, taxonomy, decision-rights, and handoff standards.

## Primary question
> How do we create qualified demand?

## Purpose
Understand audiences, create demand, position the organization, and measure response.

## Sub-functions
Brand, Product Marketing, Demand Generation, Growth, Content, Communications, Performance Marketing, Marketing Operations, Market Research

## Typical roles
CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager

## Inputs
Audience data, market research, product value, competitive signals, channel performance.

## Outputs
Positioning, campaigns, content, demand, leads, market insights.

## Learning focus
Audience behavior; messaging effectiveness; channel quality; conversion triggers; objections; market trends.

## Operating tree
```text
MARKET →
    SEGMENT →
    AUDIENCE →
    PROBLEM →
    POSITIONING →
    MESSAGE →
    CHANNEL →
    CAMPAIGN →
    RESPONSE →
    CONVERSION →
    ATTRIBUTION →
    LEARNING
```

## Decision states
```text
UNKNOWN AUDIENCE → IDENTIFIED → SEGMENTED → RESEARCHED → POSITIONED → ACTIVATED → ENGAGED → CONVERTING → RETAINING → EXPANDING
```

## Decision outputs
`Scale · Iterate · Reposition · Change Audience · Change Channel · Stop`

## Critical prompts (what this function thinks about)
> Who are we trying to influence?
> What do they currently believe?
> What do we want them to believe?
> What problem do they recognize?
> What problem don't they recognize?
> What triggers action?
> What prevents action?
> What alternatives are they considering?
> Why should they believe us?
> What evidence supports our positioning?
> Which message is working?
> Which message isn't?
> Which audience responds?
> Which audience doesn't?
> Which channel produces quality?
> What should we stop?
> What should we test next?
> What did the market teach us?

## Canonical record schema (docx Learning Ledger + Decision Object Fields)
Every decision in this line is recorded as:
- a **Decision Object** (docx S9) — see `schema/decision-object.json`
- a **Learning Ledger** entry (docx S7) — see `schema/learning-ledger.json`

and the agent must run the **Orientation Protocol** first (see `AGENT.md`).

## How to use
1. Read `AGENT.md` — the first-run Orientation Protocol.
2. Read `SCHEMA.md` — how this line maps to the universal schema.
3. Read `data/03-marketing.json` — the machine-readable spec.
4. See `data/example.json` — one fully worked decision (Decision Object + Ledger).
5. Use `decision-graph.mmd` — agent-decodable operating tree + state model.
6. Validate new records: `python3 tools/validate.py data/<name>.json`
