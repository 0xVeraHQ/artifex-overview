# HackMeridian 2026 — diary

Track: **Scale**. Team: Joel (captain, technical) and Luis (art expert).

Times are **Lisbon (WEST / UTC+1 in late October)**. Each entry records what landed during the event and the public evidence a judge can check. Pre-event product state is summarized in the README under *Before HackMeridian*.

---

## 2026-10-25 — Sunday

### 09:00 — Event start · production fixes begin

HackMeridian opens. Work starts on the production-readiness backlog agreed after mentor and judge conversations. The application had named OpenZeppelin, Trustless Work, and path payments; those three stay on the longer roadmap. The event priority is fixing Testnet sales flows, completing external QA, and launching on mainnet.

Baseline already public before this entry (Testnet):

- Live app: [https://artifex.0xvera.com](https://artifex.0xvera.com)
- Images: api **0.16.16**, web **0.4.16**, cosign verified
- Active contracts: version **v2**, contracts tag **v0.1.0**
- **15 demo artworks**
- External QA through pass 3: **22** validated, **4** blockers
- Contracts source: [artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts)

### 14:45 — Release api 0.16.20 / web 0.4.19 · contract v3 live on Testnet

Production reinstalled on Testnet with the **15 demo artworks**. Public API now serves contract version **v3** (contracts tag **v0.2.0**).

| Item | Status | Evidence |
| --- | --- | --- |
| Whole-work sale on contract **v3** | Done in release | Active registry **v3**; whole-work NFT `CBEVANRZPBH4XJYGMWZUQMPZYAG2TIOYA6MRZGRNHJJNLSIUTRW3RAKT` — [CONTRACTS.md](CONTRACTS.md) |
| USDC purchase fix | Done in release | api **0.16.20** / web **0.4.19** — [RELEASES.md](RELEASES.md) |
| Locked-unit recovery | Done in release | Same release (marketplace `list_with_deposit` / recover) |
| Offer and listing indexing | Done in release | Marketplace index aligned with on-chain offers/listings; piece txs in [PIECES.md](PIECES.md) |
| Automatic distribution to holders | Done in release | Distribution contract `CCZMGEYTOCZ56L6U26ZS6KGWQ2NNUC3FNXFO5LDS6YQYJ5KP2DVGULFX` |
| Role permissions | Done in release | Same release |
| Verification improvements | Done in release | Same release |
| `llms.txt` / `robots.txt` / `sitemap.xml` | Live | https://artifex.0xvera.com/llms.txt · [/robots.txt](https://artifex.0xvera.com/robots.txt) · [/sitemap.xml](https://artifex.0xvera.com/sitemap.xml) |
| Demo catalog reseeded | Live | 15/15 titles on `/api/pieces`; meta version **0.16.20** |

**Images (cosign verified in GitHub Actions `docker-release`):**

| Image | Tag | Digest |
| --- | --- | --- |
| `registry.hosting1337.com/artifex/artifex-api` | 0.16.20 | `sha256:3cea2d8788a5777d2b30aee6d4114e5ca8e1cb9cf28203936dfcca312c1f0502` |
| `registry.hosting1337.com/artifex/artifex-web-ui` | 0.4.19 | `sha256:86baf41a8901fc63d7d497e0ad723b8fc6d12fc526f02b2d0735dd63971c4f92` |

**Contract v3 IDs (Testnet, active):** see [CONTRACTS.md](CONTRACTS.md). Source: [artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts) tag **v0.2.0**.

### 15:00 — Fourth external QA pass starts

Independent black-box QA begins against the reinstalled Testnet (api 0.16.20 / web 0.4.19 / registry v3). Cases still open remain **PENDING** in [QA.md](QA.md) with reason `4th QA pass in progress`.

---

## Planned during the event (not yet dated)

- **Fourth external QA pass results** — update [QA.md](QA.md) when the pass reports.
- **Stellar mainnet launch** — Mainnet sections in [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [QA.md](QA.md) stay **PENDING** until real IDs and transactions exist.
