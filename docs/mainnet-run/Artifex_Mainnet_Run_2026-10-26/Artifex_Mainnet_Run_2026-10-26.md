# Artifex – Mainnet QA run, 2026-10-26

- **Scope:** short production route on the Stellar **public network** (steps a–g), with funding of the QA wallets beforehand. Positive cases only; no negative tests.
- **Site:** https://artifex.0xvera.com
- **Versions:** web 0.4.24 / api 0.17.4 for the a-propose step and steps c, d, e. web 0.4.25 / api 0.17.5 (certification-fee fix) for steps f, a-deposit/finalize, b and g.
- **Network:** Stellar Mainnet ("Public Global Stellar Network ; September 2015"). Freighter showed "Main Net" on every signature.
- **Verification:** every hash below was checked on Horizon mainnet (`/transactions/<hash>` and `/effects`). All of them are `successful: true`. Fees are Horizon `fee_charged`, not the Freighter maximum. Times are ledger close times in WET (Atlantic/Canary, UTC+0).

## Wallets

| Wallet | Role | Address |
|---|---|---|
| QA-1 | Artist | GCPGMC55DFBJBOPRXZ7MZ6ZJU5GLAJLB5DXNIQS3RNKIKKXZN3YCH3RL |
| QA-2 | Collector 1 (funder) | GAWH75XHCV5CE375EPEVKXG63SIKDLID5ULHDIY7WIPS2U2ZJLAYWBNJ |
| QA-3 | Collector 2 | GAJ7W5UPCR3ENU5CY4ELU2BNVWI7TZ54KH6APFCT5TIEZXSS6VDSXTHQ |
| QA-4 | (funded only) | GAJGJCAQFRQQX2PE4KYVC6STKIYBZZTNYN4BIVP73MSYNYJLW7ZCYT54 |
| QA-5 | Museum | GB7XRDD2A5AMOJVGMEZ4M7DIS3CSPQRP3FMRRPUDJ46XFGO4AFJ4QXFV |

Primary-sale payee for Torso II, Estudio en azul and Silencio blanco: `GAHZC…CMF5`. This is the issuer account, which the site excludes from distributions. Certification fee contract: `CBWJBOE3…J7Q2`.

## Transactions

| Step | Action | Wallet | Tx | Value moved | Fee charged (XLM) | Result |
|---|---|---|---|---|---|---|
| Funding | Create account QA-1 | QA-2 | [082bdfe1…2852](https://stellar.expert/explorer/public/tx/082bdfe1fd2a2f4e64ef307db2b1bc262b9f51f297a112b899a11fc73a122852) | 2.5 XLM QA-2 → QA-1 (account created) | 0.00001 | OK · ledger 65137136 · 2026-10-25 23:37:43 WET |
| Funding | Create account QA-3 | QA-2 | [972eec39…d6ce](https://stellar.expert/explorer/public/tx/972eec3986143f2c19df00c4801cf3b80c6b1484c0e9ba401fcb3fb9b8b8d6ce) | 2.5 XLM QA-2 → QA-3 (account created) | 0.00001 | OK · 65137157 · 23:39:28 WET |
| Funding | Create account QA-4 | QA-2 | [08a1cca0…efc7](https://stellar.expert/explorer/public/tx/08a1cca07f9294452e681a71cfbadc22258d2e9495b97e25e953abb021aaefc7) | 2.5 XLM QA-2 → QA-4 (account created) | 0.00001 | OK · 65137175 · 23:40:58 WET |
| Funding | Create account QA-5 | QA-2 | [863dc206…28fb](https://stellar.expert/explorer/public/tx/863dc2065eede0988b6e6bf327c9921651c058ef95b0eb65de72dd43c0a728fb) | 2.5 XLM QA-2 → QA-5 (account created) | 0.00001 | OK · 65137194 · 23:42:33 WET |
| Funding | USDC trustline (issuer GA5Z…KZVN) | QA-2 | [a9359cfc…c6e0](https://stellar.expert/explorer/public/tx/a9359cfc983db92cdf2d6ee71afc10f73f2314251b6ab6b53fd23dff6b78c6e0) | none (trustline created) | 0.00001 | OK · 65137210 · 23:43:53 WET |
| a | Register "Luz de Anaga" (living author, photo) + propose certification (= artist signature) | QA-1 | [ad9073f3…9b98](https://stellar.expert/explorer/public/tx/ad9073f3a8b28fb53babd0f191a1c963594cff00164f333cc94632b26fd39b98) | none (gas only) | 0.0892639 | OK · 65138173 · 2026-10-26 01:04:08 WET (web 0.4.24) |
| a | Deposit certification fee | QA-1 | [51f36e24…9735](https://stellar.expert/explorer/public/tx/51f36e2440d43c56bfcca37861ea3acfe5e0f447d695ef27b029ed51b2b99735) | 0.5 XLM QA-1 → fee contract CBWJBOE3…J7Q2 | 0.0438536 | OK · 65138482 · 01:29:53 WET |
| a | Finalize certification | QA-1 | [a652c807…21d7](https://stellar.expert/explorer/public/tx/a652c8079b09b68deff4b1918f781e50972259c452afee1efc028d0c374421d7) | none (consumes deposit) | 0.0006513 | OK · 65138489 · 01:30:28 WET · /verify: Certified, 1 signer, Finalized: Yes · Fee: Paid |
| b | Mint whole NFT (token 5) | QA-1 | [2369253e…4ad7](https://stellar.expert/explorer/public/tx/2369253e1d16fbfcfce9c6def95de2b4d49e3dfb1d63d734b4e43a2b0d3a4ad7) | none (gas only) | 0.0769792 | OK · 65138516 · 01:32:43 WET |
| b | List whole NFT at 1 XLM (sale 5) | QA-1 | [5f16c840…05fb](https://stellar.expert/explorer/public/tx/5f16c84081b221312b3df93cc3c0d8d0f832b4dc0bfeeec9bf9a30599c4d05fb) | none (escrow listing) | 0.0851479 | OK · 65138526 · 01:33:33 WET |
| b | Buy whole NFT | QA-3 | [f7d4a181…fe48](https://stellar.expert/explorer/public/tx/f7d4a18187babeafde8e7365b7d9d20e2b72b0800a491b25b8d565cea39cfe48) | 1 XLM QA-3 → QA-1 | 0.0019282 | OK · 65138546 · 01:35:13 WET · owner history QA-1 → QA-3 |
| c | Buy 3 u Torso II (offer 2) | QA-2 | [8479553c…cac1](https://stellar.expert/explorer/public/tx/8479553c49e110a6daeb4f7e3b0d50124039ff5516796fafda8a9855c1eccac1) | 0.3 XLM QA-2 → GAHZC…CMF5 | 0.0280989 | OK · 65138243 · 01:09:58 WET |
| c | Buy 1 u Estudio en azul (offer 1, Try it) | QA-2 | [20119cbe…8c3b](https://stellar.expert/explorer/public/tx/20119cbee97c15a38c4fe959c0d9ae6394ae1ba3512f800ffc961d1bb3028c3b) | 0.1 XLM QA-2 → GAHZC…CMF5 | 0.0280989 | OK · 65138257 · 01:11:08 WET |
| c | Buy 1 u Torso II (offer 2) | QA-3 | [b9f151c3…83b6](https://stellar.expert/explorer/public/tx/b9f151c32fd185310a4f5979e8f6828a0fcf0a9bb7b80f9b16a62cfc734883b6) | 0.1 XLM QA-3 → GAHZC…CMF5 | 0.0280989 | OK · 65138292 · 01:14:03 WET |
| c | Buy 1 u Estudio en azul (offer 1, Try it) | QA-3 | [ac35ea3b…083a](https://stellar.expert/explorer/public/tx/ac35ea3b66b4b0281fae7c0afd90752765a694f897a960c2a52e9b08cc25083a) | 0.1 XLM QA-3 → GAHZC…CMF5 | 0.0280989 | OK · 65138309 · 01:15:28 WET |
| d | Distribute 0.5 XLM on Torso II, pro-rata by units (3 u / 1 u) | QA-5 | [c28c7dce…a411](https://stellar.expert/explorer/public/tx/c28c7dce42b8ae00e4004cf9f4acc7449d7645fb5d06266629c49ac2e5d4a411) | 0.375 XLM QA-5 → QA-2; 0.125 XLM QA-5 → QA-3 | 0.0011735 | OK · 65138354 · 01:19:13 WET · 7500/2500 bps as previewed |
| e | Buy 1 u Silencio blanco in USDC (offer 5) | QA-2 | [cbe39243…4796](https://stellar.expert/explorer/public/tx/cbe3924319d0258ce7bc2ffde971d78b04b18e1a4998ecff28937bfdb15d4796) | 0.1 USDC QA-2 → GAHZC…CMF5 | 0.0281290 | OK · 65138388 · 01:22:03 WET |
| f | Second signature (cosign) "Puerto al alba" | QA-5 | [65a624c4…59da](https://stellar.expert/explorer/public/tx/65a624c454d33e230c43b754e62bbcd991799f39c942ef13dbcbc6c40aba59da) | none (gas only) | 0.0077570 | OK · 65138440 · 01:26:23 WET (web 0.4.25) |
| f | Finalize certification "Puerto al alba" | QA-5 | [806a9865…9fa6](https://stellar.expert/explorer/public/tx/806a9865511f18616559298361290345644630d5b957c0c69391be1d8d5b9fa6) | none (consumes the existing deposit) | 0.0007195 | OK · 65138449 · 01:27:08 WET · /verify: Certified, 2 signers, Fee: Paid |
| g | Public verification by QR of "Luz de Anaga", no wallet connected | — | no tx (read-only) | — | — | OK · /verify shows Certified, 1 signer, Finalized: Yes · Fee: Paid. QR decodes to https://artifex.0xvera.com/verify/8f0326d791c679433f71e3d1b3ba4837d9ff47f51e431ac6918a7c8c6ca282e6 (matches the printed URL; HTTP 200 without a wallet). |

**Total network fees charged:** 0.4480487 XLM across 19 transactions.

**Value moved:**
- Funding: 4 × 2.5 XLM.
- Certification fee: 0.5 XLM.
- Whole sale: 1 XLM.
- Unit purchases: 0.6 XLM.
- Distribution: 0.5 XLM.
- USDC purchase: 0.1 USDC.

## Findings

1. **Wrong certification fee on web 0.4.24 (fixed in 0.4.25).**
   - The deposit dialog asked for 5 XLM, which is the Testnet fee. The mainnet contract `fees()` is 0.5 XLM / 0.1 USDC.
   - The dialog was cancelled before signing, so nothing was sent.
   - On web 0.4.25 the dialog shows 0.5 XLM, and the deposit tx moved exactly 0.5 XLM.
   - Still: `stills/a-0424-cert-fee-5xlm-dialog-cancelled.png`.
2. **Finalize dialog shows a misleading amount.**
   - The dialog reads "Finalize certification (consumes fee deposit) / Amount: 0.5 XLM · Currency: XLM".
   - The transaction has no payment and only consumes the existing deposit. Horizon shows no XLM debit on either finalize: a652c807… (QA-1) and 806a9865… (QA-5).
3. **Layout shift after the deposit.**
   - After the deposit confirms, the page re-flows and "Refund deposit" lands under the cursor where "Finalize" was.
   - A click intended for Finalize opened the refund dialog instead. It was cancelled without signing, but a real user could request a refund by mistake.
4. **Whole-NFT listing shows unit text.**
   - While the whole sale of "Luz de Anaga" was active, the piece page showed "Secondary listing: 1 XLM · 10 units available", although the listing is a single whole NFT.
5. **Owner history already listed QA-2 before the purchase in step e.**
   - The owner history of "Silencio blanco" already showed QA-2 (`GAWH7…WBNJ`) before the step e purchase. This was not investigated.
6. **Confirm dialogs show raw base units.**
   - Example: "Amount: 10000000 · Currency: XLM" for a 1 XLM listing or purchase, and "1 u × 1000000 (XLM)" for 0.1 XLM per unit.
   - The values are correct on-chain but read as 10,000,000 XLM.
7. **/holdings has no per-wallet unit counts.**
   - /holdings shows only "Certified · 0.1 XLM · N owner(s)". The user cannot see how many units they hold. In this run QA-2 holds 3 u of Torso II and QA-3 holds 1 u.

## Clips

Screen recordings for steps a–g are published on YouTube (not stored in this repository). Local filenames used during the run: `clips/01-funding.mp4` … `clips/09-g-qr-verify.mp4`.

## Stills

| File | Shows |
|---|---|
| `stills/a-0424-cert-fee-5xlm-dialog-cancelled.png` | Finding 1 |
| `stills/m2a-verify.png` | Luz de Anaga certified |
| `stills/m2b-owner.png` | Owner history QA-1 → QA-3 |
| `stills/d-preview.webp` | Distribution preview |
| `stills/m2e-usdc-holdings.webp` | QA-2 holdings |
| `stills/m2f-verify.png` | Puerto al alba certified |
| `stills/m2g-qr-zoom.png` | QR |

Raw Horizon responses are in `horizon/`.
