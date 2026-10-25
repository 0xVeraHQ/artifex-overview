# HackMeridian 2026 — diary

Track: **Scale**. Team: Joel (captain, technical) and Luis (art expert).

Times are **Lisbon (WEST / UTC+1 in late October)**. Each entry records what landed during the event and the public evidence a judge can check. Pre-event product state is summarized in the README under *Before HackMeridian*.

---

## 2026-10-25 — Sunday

### 09:00 — Event start · production fixes begin

HackMeridian opens. Work starts on the production-readiness backlog agreed after mentor and judge conversations. The application had named OpenZeppelin, Trustless Work, and path payments; those three stay on the longer roadmap. The event priority is fixing Testnet sales flows, completing external QA, and launching on mainnet.

In progress from 09:00:

| Item | Intent | Evidence status |
| --- | --- | --- |
| Whole-work sale on contract version **v3** | List and buy an entire work on the new contract set | **PENDING** — v3 contract IDs are published in [CONTRACTS.md](CONTRACTS.md); the public API still serves **v2** until v3 is activated |
| USDC purchase fix | Primary / whole-work checkout in Circle Testnet USDC | **PENDING** — release after fix |
| Locked-unit recovery | Return units stuck from interrupted flows | **PENDING** — release after fix |
| Offer and listing indexing | Public marketplace index matches on-chain offers and listings | **PENDING** — indexer work in progress |
| Automatic distribution to holders | Run distribution under published terms | **PENDING** — QA case S-12 |
| Role permissions | Capabilities match on-chain roles for orgs with several member wallets | **PENDING** |
| Verification improvements | Signer list and QR verify for living / deceased / digitized certificates | **PENDING** — QA cases V-03, C-06–C-08 |

Baseline already public before this entry (Testnet):

- Live app: [https://artifex.0xvera.com](https://artifex.0xvera.com)
- Images: api **0.16.16**, web **0.4.16**, cosign verified — [RELEASES.md](RELEASES.md)
- Active contracts: version **v2**, contracts tag **v0.1.0** — [CONTRACTS.md](CONTRACTS.md)
- **15 demo artworks** — [PIECES.md](PIECES.md)
- External QA through pass 3: **22** validated, **4** blockers — [QA.md](QA.md)
- Contracts source: [artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts)

Next diary lines will attach release tags, digests, and explorer transaction links as each item lands. Fourth external QA pass runs after these corrections. Mainnet launch follows a clean Testnet state.

---

## Planned during the event (not yet dated)

- **Fourth external QA pass** — cases currently **PENDING** with reason `4th QA pass in progress` in [QA.md](QA.md).
- **Stellar mainnet launch** — Mainnet sections in [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [QA.md](QA.md) stay **PENDING** until real IDs and transactions exist.
