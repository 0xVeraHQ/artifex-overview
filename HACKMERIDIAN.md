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

**Contract v3 IDs (Testnet, active at the time):** see [CONTRACTS.md](CONTRACTS.md) historical rows. Source: [artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts) tag **v0.2.0**.

### 15:00 — Fourth external QA pass starts

Independent black-box QA begins against the reinstalled Testnet (api 0.16.20 / web 0.4.19 / registry v3).

### 17:45 — Fourth QA pass results (api 0.16.20 → 0.16.22)

Pass closed. Evolution of validated cases: **9 → 20 → 22 → 28**. On this pass: **28** validated, **7** open, **1** untested, **3** blockers.

Working end-to-end (with Testnet txs in [QA.md](QA.md) / annex A on [stellar.expert Testnet](https://stellar.expert/explorer/testnet)):

- Living-author certification (one signature) and deceased-author certification (two signatures)
- Public verification by QR
- Primary and secondary participations
- USDC purchase (secondary, Silencio blanco)
- Automatic distribution to holders

| Sample evidence | Tx (Testnet) |
| --- | --- |
| Living author finalize (C-02) | [26cfdc9fcc…](https://stellar.expert/explorer/testnet/tx/26cfdc9fcc33318ae18d2390c2bf5f4ba9b9e63eb7cc37a1cd0fc9b72b879444) |
| Museum second signature (C-05) | [fa565f9a3c…](https://stellar.expert/explorer/testnet/tx/fa565f9a3c5a28e270212da3eebe626bfd5af48244a3cb67fe68dce7a2c49621) |
| USDC secondary buy (S-10) | [4bfb943a1b…](https://stellar.expert/explorer/testnet/tx/4bfb943a1b1b7852c20325eb2deb905da9b89623516da8da21e0dcefd741455f) |
| Primary buy Try it (S-13) | [dae51abf3a…](https://stellar.expert/explorer/testnet/tx/dae51abf3ad34a818a2a58d4f56db5c4c9dc49e51cc371df8e90a3361244d683) |
| Automatic distribute (S-12 ran) | [4a6380f655…](https://stellar.expert/explorer/testnet/tx/4a6380f6555ae2f1e224308ba276bf62ae6d21a0aac2b6ca93d40f1e283e9ca9) |

**Blockers (whole-work buy from the UI):** S-02, S-04, S-05. Full case table: [QA.md](QA.md).

### 18:20 — Mainnet platform account created and funded

Public mainnet platform address created and funded. Circle USDC trustline opened on the public network.

| Item | Value |
| --- | --- |
| Platform (public) | `GCNSEGPV3MS36RO7TT4OE7UEVWLLVSOGDRHURZRUHPRKQRCJ2QC32Q3V` |
| USDC trustline tx | [a9df809b9748f309b720ff3aad0e86bc8c82c591af9dc085830326436b807118](https://stellar.expert/explorer/public/tx/a9df809b9748f309b720ff3aad0e86bc8c82c591af9dc085830326436b807118) |
| Contracts on mainnet | Not deployed yet — [WALLETS.md](WALLETS.md) Mainnet section |

### 19:05 — Release api 0.16.23 / web 0.4.21 · contract registry v4

Testnet updated to fix the three mainnet-gate themes from the 4th pass addendum:

| Fix | What changed |
| --- | --- |
| Living-author one-signature finalize | `cert_registry` redeployed (corrected) |
| Whole-work buy / cancel / resale | Active sale of the token; owner history accumulates |
| Distribution | Proportional to each holder’s units |

| Item | Value |
| --- | --- |
| api | **0.16.23** · digest `sha256:31bd6623cde7f67e85f0cc5cc43f19a49cabe10dbedde47292179f110786d876` |
| web | **0.4.21** · digest `sha256:eec0471fdb707759265ec11e8013ed218f190ae344b63f23779f85a9c005e527` |
| Active registry | **v4** · contracts tag **v0.2.1-living-author** |
| New `cert_registry` (v4) | `CDD2BYHRY7ZCMMHBRETM4X2EGVCTKMAGKNRWSCJYHOTLLCWYK2UZY4CC` |

Full IDs and cosign: [CONTRACTS.md](CONTRACTS.md), [RELEASES.md](RELEASES.md). Live `/api/meta` reports **0.16.23**; `/api/contracts/registry` serves **v4**.

### 19:10 — Re-test of the three blockers starts

Independent re-test of S-02, S-04, and S-05 (and the proportional-distribution check) against api **0.16.23** / web **0.4.21** / registry **v4**. Cases stay **PENDING** in [QA.md](QA.md) until the re-test reports. Result will be added here when it lands.

---

## Planned during the event (not yet dated)

- **Re-test result for the three blockers** — update [QA.md](QA.md) and this diary when the pass reports.
- **Stellar mainnet contract deploy** — Mainnet contract IDs in [CONTRACTS.md](CONTRACTS.md) stay empty until deploy; platform wallet is already public in [WALLETS.md](WALLETS.md).
