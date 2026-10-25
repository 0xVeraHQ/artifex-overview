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

Production reinstalled on Testnet with the **15 demo artworks**. Public API served contract version **v3** (contracts tag **v0.2.0**). Whole-work sale, USDC fix, locked-unit recovery, indexing, automatic distribution, roles, verification, and public `llms.txt` / `robots.txt` / `sitemap.xml`. Evidence: [RELEASES.md](RELEASES.md), [CONTRACTS.md](CONTRACTS.md).

### 15:00 — Fourth external QA pass starts

Independent black-box QA against api 0.16.20 / web 0.4.19 / registry v3.

### 17:45 — Fourth QA pass results (api 0.16.20 → 0.16.22)

Pass closed. Evolution of validated cases: **9 → 20 → 22 → 28**. On this pass: **28** validated, **7** open, **1** untested, **3** blockers (S-02, S-04, S-05 — whole-work buy from the UI).

Working end-to-end: living-author and deceased-author certification, QR verify, primary/secondary participations, USDC purchase, automatic distribution. Sample txs in [QA.md](QA.md).

### 18:20 — Mainnet platform account created and funded

| Item | Value |
| --- | --- |
| Platform (public) | `GCNSEGPV3MS36RO7TT4OE7UEVWLLVSOGDRHURZRUHPRKQRCJ2QC32Q3V` |
| USDC trustline tx | [a9df809b9748f309…](https://stellar.expert/explorer/public/tx/a9df809b9748f309b720ff3aad0e86bc8c82c591af9dc085830326436b807118) |

### 19:05 — Release api 0.16.23 / web 0.4.21 · registry v4

Fixes for the three mainnet-gate themes: living-author one-signature `cert_registry`, whole-work buy/cancel/resale by active token sale with accumulated owner history, proportional distribution.

| Item | Value |
| --- | --- |
| api | **0.16.23** · `sha256:31bd6623…d876` |
| web | **0.4.21** · `sha256:eec0471f…e527` |
| Active registry | **v4** · tag **v0.2.1-living-author** |
| New `cert_registry` | `CDD2BYHRY7ZCMMHBRETM4X2EGVCTKMAGKNRWSCJYHOTLLCWYK2UZY4CC` |

### 19:10–20:11 — Re-test of the three blockers · **APTO for mainnet**

Independent re-test on api **0.16.23** / web **0.4.21–0.4.22** (Lisbon 18:10–19:11 session window in the QA clock; diary uses Lisbon). All three blockers corrected. External QA verdict: **APTO for mainnet**. Evolution: **9 → 20 → 22 → 28 → apto**.

| Check | Evidence (Testnet) |
| --- | --- |
| Cancel resale “Ventana norte” (sale 17) by QA-3 | [ef18d9b272…](https://stellar.expert/explorer/testnet/tx/ef18d9b27208580f46a47d8c7c92a0d9dae4ff51fd6308c7cee919a20c1a7542) |
| Buy “Marea de cobre” (token 24) by QA-2 · 2 owners | [59536ffc75…](https://stellar.expert/explorer/testnet/tx/59536ffc75242237b1283be22e47ecf931bdd2af975458d62bb1328a882ea183) |
| Living author one signature — “Brisa de Teno (QA w422)” finalize | [426463bdf5…](https://stellar.expert/explorer/testnet/tx/426463bdf506cecb33e2263231d8b66e6649ae8dafe45866897f36cc1d6c7692) |
| propose | [80445566ac…](https://stellar.expert/explorer/testnet/tx/80445566ac65716040bdcf3a5e0649199383d9cc7974f76b26ef98f8d04611af) |
| deposit | [373e88968e…](https://stellar.expert/explorer/testnet/tx/373e88968e9bdcc79469618c76e2b5dd1b45f5eb1eb5165759a9bab7a93196bd) |
| Proportional distribute “Torso II” (8 XLM QA-3 · 2 XLM QA-2) | [a7e1c35319…](https://stellar.expert/explorer/testnet/tx/a7e1c353199e72c95e468393e4b84124bc0c252469cc4b4b4a10e380794877ce) |

Cases **S-02**, **S-04**, **S-05**, **S-12** → **PASS** in [QA.md](QA.md). Journey steps 4, 5, and 7 cleared.

### 19:56 — web 0.4.22 (fee-consumer copy)

Harbor image **0.4.22** · digest `sha256:3463ddcbb6fdf620a0f7c9b78121fc593a5e99a9b7fde63802c298e0dc5c5ec5`, cosign verified. See [RELEASES.md](RELEASES.md).

### 21:54 — api 0.17.1 (mainnet support)

Harbor image **0.17.1** · digest `sha256:d0920748d3a11102ee70fdfc61b11a6aafcb7bb92a8621b48b88f6f87b63296f`, cosign verified. Orch `versions.env` points at api **0.17.1** / web **0.4.22**.

### 23:10 — Mainnet contracts deployed

Soroban contracts deployed on **Stellar mainnet** from platform `GCNSEG…Q3V` (**38** transactions, ~**88** XLM). Active `cert_registry` supports living-author single-signature finalize.

| Contract | Mainnet ID |
| --- | --- |
| Roles | `CBAG24ESXBYNKGC34VJZJ3XIL2ECCWJLPAK37IQIRQF5OBNZWUBKKELG` |
| Fee collector | `CBWJBOE3CESO5T2OZKLDASOFXAFQ4NAKWXZ26ZNYYWYI4E2VJCZJJ7Q2` |
| Connoisseur | `CAWJ56K3J6SOKUBTYDUKHPAU556KYYCWYUGQUTTHU7HH5UBNENWOPY5O` |
| Certificate registry | `CD4QIRNEXTEOXZGBI3JKKHMPS5IBDQACMZET6ZS2ID2GTPPC2FZMEZDG` |
| Whole-work NFT | `CCPE7A2HCTUUOIZSALBXYNEUU53COWMBFZEC6G3IIURBMHUNFWURYTEM` |
| Participation | `CAHS2BD7AI6U63C44VSE5EBVNBXQFZEOXDY4BNWDGNHKNQNWB4DBIU5D` |
| Marketplace | `CACYT65VWTZD5JM2PKRZCNYLMHVNYXBS7RNM3YXXSSI3IMNG5MHXXNY7` |
| Distribution | `CCBEWM4REV3LOK5XRZ5VIMAUY23Q4UBTPQBDAYBUHAVJNOVFQ7XRPHZU` |

Explorer: [stellar.expert public](https://stellar.expert/explorer/public). Full table: [CONTRACTS.md](CONTRACTS.md). Source IDs: artifex-orch `deployments/mainnet.json`.

### 23:15 — Application cutover to mainnet in progress

Contracts live on mainnet; app cutover started.

### 23:40 — Application serving Stellar mainnet

Public app cut over. Evidence:

| Check | Value |
| --- | --- |
| `/api/health` | `stellarNetwork: mainnet` |
| `/api/meta` | api **0.17.1**, `platformWallet` `GCNSEG…Q3V` |
| `/api/contracts/registry` | active **mainnet-v1** (tag `vps-deploy`) |
| `/api/pieces` | empty (`items: []`) — catalog pending seed/register |

Overview docs now list **mainnet first**; Testnet tables remain as HackMeridian history. [PIECES.md](PIECES.md) Mainnet section is LIVE with an empty catalog until works appear.

---

## Planned during the event (not yet dated)

- **Seed or register mainnet demo works** — fill [PIECES.md](PIECES.md) Mainnet rows and refresh [TRY-IT.md](TRY-IT.md) when a public mainnet buy path exists.
