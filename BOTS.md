# Bots of Marketing  (docx S5 candidate menu)

These are the **Major sub-functions** of Marketing from the spec. Each is a bot — a
child decision system that can be instantiated to do the actual work.

## Install flow (matches the Orientation Protocol)
1. **Orient** — the agent runs the Kojiki Orientation Protocol (name / industry /
   jurisdiction / siblings).
2. **Research** — the agent researches the field and decides which sub-functions this
   specific org needs.
3. **Install** — instantiate only the chosen bots:
   ```bash
   cd bots
   python3 install_bots.py brand growth performance-marketing
   ```
   (use the slugs listed below; omit args to install all). Each installed bot becomes a
   full decision system under `bots/<slug>/` with README + AGENT.md + schemas + a stub
   decision record, and registers under this department's group_id for handoffs.

Total candidates: 9.

- `brand` — **Brand**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `product-marketing` — **Product Marketing**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `demand-generation` — **Demand Generation**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `growth` — **Growth**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `content` — **Content**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `communications` — **Communications**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `performance-marketing` — **Performance Marketing**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `marketing-operations` — **Marketing Operations**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
- `market-research` — **Market Research**  ·  titles: CMO, VP Marketing, VP Growth, Brand Director, Growth Director, Product Marketing Director, Demand Generation Director, Marketing Manager
