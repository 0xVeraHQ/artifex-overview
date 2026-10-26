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

### 23:10 — VPS cutover · wiring verified · seed wallets funded

Mainnet cutover executed on the VPS. Contract wiring verified; `finalize_cert` simulation OK. **Five** demo seed wallets funded with Circle USDC trustlines from the platform (public payments on [stellar.expert](https://stellar.expert/explorer/public/account/GCNSEGPV3MS36RO7TT4OE7UEVWLLVSOGDRHURZRUHPRKQRCJ2QC32Q3V)). Addresses in [WALLETS.md](WALLETS.md).

### 23:15 — Application cutover to mainnet in progress

Contracts live on mainnet; app cutover started.

### 23:40 — Application serving Stellar mainnet

| Check | Value |
| --- | --- |
| `/api/health` | `stellarNetwork: mainnet` |
| `/api/meta` | api **0.17.1** → **0.17.2**, `platformWallet` `GCNSEG…Q3V` |
| `/api/contracts/registry` | active **mainnet-v1** (tag `vps-deploy`) |

Overview docs list **mainnet first**; Testnet remains HackMeridian history.

### 00:25 (26 Oct) — Seed `hackathon-scale-15-v6-mainnet` · api 0.17.2

Lisbon night of the 25th into the early 26th. Live api **0.17.2** / web **0.4.22**.

| Item | Value |
| --- | --- |
| Pieces | **15** demo works on-chain |
| Certified | **7** |
| Pending second signature | **1** — Puerto al alba |
| Primary offers | **1–6** (3 XLM · 3 USDC) |
| Whole-work tokens listed | **1–4** |
| Secondary listing | **1** (Silencio blanco) |
| Roles | QA-1 artist, QA-4 connoisseur, QA-5 museum |
| Try it | **Estudio en azul** · offer **1** · **0.1 XLM** |

Catalog: [PIECES.md](PIECES.md). Contracts: [CONTRACTS.md](CONTRACTS.md).

### 00:40 (26 Oct) — Mainnet QA wallets activated

QA Freighter accounts funded on mainnet from **QA-2** (`GAWH75…WBNJ`), then QA-2 opened a Circle USDC trustline.

| Step | Account | Tx (public) |
| --- | --- | --- |
| Activate QA-1 | `GCPGMC…H3RL` | [082bdfe1fd…](https://stellar.expert/explorer/public/tx/082bdfe1fd2a2f4e64ef307db2b1bc262b9f51f297a112b899a11fc73a122852) |
| Activate QA-3 | `GAJ7W5…XTHQ` | [972eec3986…](https://stellar.expert/explorer/public/tx/972eec3986143f2c19df00c4801cf3b80c6b1484c0e9ba401fcb3fb9b8b8d6ce) |
| Activate QA-4 | `GAJGJC…YT54` | [08a1cca07f…](https://stellar.expert/explorer/public/tx/08a1cca07f9294452e681a71cfbadc22258d2e9495b97e25e953abb021aaefc7) |
| Activate QA-5 | `GB7XRD…QXFV` | [863dc2065e…](https://stellar.expert/explorer/public/tx/863dc2065eede0988b6e6bf327c9921651c058ef95b0eb65de72dd43c0a728fb) |
| QA-2 USDC trustline | `GAWH75…WBNJ` | [a9359cfc98…](https://stellar.expert/explorer/public/tx/a9359cfc983db92cdf2d6ee71afc10f73f2314251b6ab6b53fd23dff6b78c6e0) |

Mainnet smoke section in [QA.md](QA.md) is **PENDING** for product results.

### 00:45 (26 Oct) — Web mainnet adaptation in progress

Web UI being adapted so the network comes from the API (no Testnet banner). Still **in progress** (Testnet string still present on the live HTML at this tick).

### 00:46 (26 Oct) — Platform → QA-2 USDC top-up

Platform wallet sent **2 USDC** to QA-2 for smoke funding: [773640b8b5…](https://stellar.expert/explorer/public/tx/773640b8b5ce1cce6301a3855c321010fbdd3c8376eac2591e818e67aa1d23ba).

### 01:05 (26 Oct) — Orch pin api 0.17.3 / web 0.4.23

Harbor images published and cosign-verified; artifex-orch `versions.env` pinned (PR #36).

| Image | Tag | Digest |
| --- | --- | --- |
| artifex-api | **0.17.3** | `sha256:c879277194e9fcf8146adc86555047585826c66f55bab517b32fbeb85c1d2d0f` |
| artifex-web-ui | **0.4.23** | `sha256:1c2bc4e09c897b2be0d63b8e2e28174ee8530b0b21443ef03b4486fa179524f2` |

Live `/api/meta` still reports **0.17.2** at this tick (VPS pull pending). Mainnet smoke remains **PENDING**.

### 01:35 (26 Oct) — Live api 0.17.3 · web 0.4.24 (Mainnet UI)

VPS serving api **0.17.3**. Orch pin moved to web **0.4.24** (PR #37): runtime network from API + SSR Mainnet footer. Live HTML no longer shows Testnet; Mainnet string present.

| Check | Value |
| --- | --- |
| `/api/meta` | **0.17.3**, `stellarNetwork: mainnet`, passphrase / Horizon / explorer public |
| `/api/health` | same network meta as `/api/meta` |
| Web | **0.4.24** · `sha256:85bbb9769ca0fb20e8beed1ffac26ba3221ad53d7f102ff770d8ef702f9a3f5a` |

Seed catalog unchanged (15 · 7 certified · Puerto al alba pending second). Mainnet smoke still **PENDING**.

### 02:05 (26 Oct) — api 0.17.4 live · Mainnet smoke starts (Luz de Anaga)

Orch pin **api 0.17.4** (PR #39: web3 mainnet login from runtime `STELLAR_NETWORK`). Live `/api/meta` **0.17.4**. Digest `sha256:810d8b4ba0ad41ed31e0ecc52559764c0cb82181a18edab12deddf89680b15a6`.

QA-1 (`GCPGMC…H3RL`) registered **Luz de Anaga** (catalog now **16** works) and invoked `propose_cert`: [ad9073f3a8…](https://stellar.expert/explorer/public/tx/ad9073f3a8b28fb53babd0f191a1c963594cff00164f333cc94632b26fd39b98). Finalize / buy / distribute still open — Mainnet smoke **PENDING**.

### 02:35 (26 Oct) — api 0.17.5 / web 0.4.25 · smoke certify / buy / distribute

Orch PR #40 pins api **0.17.5** (`/fees/cert` from `fee_collector.fees()`) and web **0.4.25** (deposit dialog uses `/fees/cert`). Live `/api/meta` **0.17.5**.

| Image | Tag | Digest |
| --- | --- | --- |
| artifex-api | **0.17.5** | `sha256:bf16ae966a552c272ea9a38c76a915a4cf96a4aee606b267515198bd3673a7c2` |
| artifex-web-ui | **0.4.25** | `sha256:e7809d39c286e54c401999d4839910ce095c3e28fc33168bf6303c6565372a68` |

Mainnet smoke chain (public Horizon), still awaiting official QA verdict:

| Step | Who | Fn | Tx |
| --- | --- | --- | --- |
| Finalize cert | QA-1 | `finalize_cert` | [a652c8079b…](https://stellar.expert/explorer/public/tx/a652c8079b09b68deff4b1918f781e50972259c452afee1efc028d0c374421d7) |
| Mint whole | QA-1 | `mint` | [2369253e1d…](https://stellar.expert/explorer/public/tx/2369253e1d16fbfcfce9c6def95de2b4d49e3dfb1d63d734b4e43a2b0d3a4ad7) |
| List | QA-1 | `list_for_sale` | [5f16c84081…](https://stellar.expert/explorer/public/tx/5f16c84081b221312b3df93cc3c0d8d0f832b4dc0bfeeec9bf9a30599c4d05fb) |
| Buy sale | QA-3 | `buy_sale` | [f7d4a18187…](https://stellar.expert/explorer/public/tx/f7d4a18187babeafde8e7365b7d9d20e2b72b0800a491b25b8d565cea39cfe48) |
| Buy primary (seed) | QA-2 / QA-3 | `buy_primary` | e.g. [20119cbee9…](https://stellar.expert/explorer/public/tx/20119cbee97c15a38c4fe959c0d9ae6394ae1ba3512f800ffc961d1bb3028c3b) |
| Distribute | QA-5 | `distribute` | [c28c7dce42…](https://stellar.expert/explorer/public/tx/c28c7dce42b8ae00e4004cf9f4acc7449d7645fb5d06266629c49ac2e5d4a411) |

**Luz de Anaga** certified · whole token **5** · sold to QA-3. Catalog: **16** works · **9** certified (API). Mainnet smoke **PENDING** for official close-out.

### 07:45 (26 Oct) — Mainnet QA run a–g **PASS**

External Freighter black-box on Main Net closed. **19** Horizon-successful transactions · **0.448 XLM** total fees. Full table: [QA.md — Mainnet run (26/10/2026)](QA.md#mainnet-run-26102026).

| Step | Result |
| --- | --- |
| a | Living author **Luz de Anaga**: propose → deposit 0,5 XLM → finalize |
| b | Mint token **5**, list 1 XLM, QA-3 buys whole |
| c | Participations: Torso II + Estudio en azul (Try it) for QA-2 / QA-3 |
| d | QA-5 proportional distribute 0,5 XLM on Torso II |
| e | QA-2 buys Silencio blanco in **USDC** |
| f | QA-5 second signature + finalize **Puerto al alba** (2 signatures) |
| g | Public QR verify without wallet |

Night diary summary (25→26 Lisbon): VPS cutover · seed on-chain · web/login mainnet · fee from contract · QA a–g **PASS**. Seven non-blocking UI findings listed as Known issues → [ROADMAP.md](ROADMAP.md).

---

## Planned during the event (not yet dated)

- Delivery window closes **Monday 26 Oct 12:00 Lisbon**.
- Non-blocking UI polish after the Mainnet run (see [QA.md](QA.md#known-issues-non-blocking-ui)).
