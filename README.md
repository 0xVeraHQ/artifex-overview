# Artifex

**Live on Stellar Mainnet** — [https://artifex.0xvera.com](https://artifex.0xvera.com) (api **0.17.5** / web **0.4.25**).  
On-chain evidence: [stellar.expert/explorer/public](https://stellar.expert/explorer/public).

Provenance, certification, and funding for art — on Stellar.

Artifex is built for **HackMeridian 2026**, track **Scale**. This repository (`0xVeraHQ/artifex-overview`) is the public presentation for judges. It has the product story, public mainnet identifiers (with Testnet history from the event), and the status of QA, releases, contracts, wallets, pieces, and the roadmap. Tables are generated from the real sources. Do not edit them by hand.

Judges do not need the private application repositories. Everything to understand and verify Artifex is here, with explorer links for on-chain evidence. The Soroban contracts are public (see below).

## What Artifex is

Artists need a simple path: certify a work with their wallet, then sell it whole or in participations on a public marketplace. Collectors need to check that certificate and settle a purchase on-chain, without a private PDF as the only proof.

Museums and foundations can raise financing against a work through participations **without moving the physical piece**. The four participation types are future sale, guaranteed repurchase, financing with a return, and exploitation rights.

As an additional capacity, works by deceased authors can be certified with two signatures (connoisseur plus heir, museum, or foundation), including digitization of a prior paper certificate.

Artifex puts certification and settlement on Stellar so anyone can open the transaction.

> **Note.** A participation is a contractual position in a work. It is not a claim that the holder owns the physical object. That distinction stays visible in the product. Legal review of participations remains on the [roadmap](ROADMAP.md).

## How it works

**Living artists.** The author certifies the work with one signature and a fee (read live from the fee collector on mainnet), then lists a whole-work sale (digital or with a physical-delivery clause) or a participation offer on the marketplace. Payment and delivery of the NFT or of participation units happen in the same contract call.

**Museums and foundations.** An institution offers participation units in a work it holds, with a terms document, without transferring the physical object. Buyers can take the whole offer or part of it. Secondary listings can be filled in part or cancelled. Organizations operate with several member wallets and on-chain roles.

**Deceased authors (additional).** Two signatures are required: a connoisseur, and a second signature from the heir, a museum, or a foundation. The museum or foundation authorizes the connoisseur first. An existing paper certificate can be digitized; the document hash is stored on the fiche.

**Verification.** Anyone can open a QR code or a link and read the certificate, including who signed it. No wallet is required. A work that is not certified can still be listed, and the page marks it as not certified.

**Marketplace.** Primary and secondary sales are public. Prices are in XLM or in USDC.

## Architecture

The web app talks to an API. The API keeps the catalog, the fiches, and the documents, and it prepares the transactions. The buyer or the signer approves them in Freighter. Soroban contracts on Stellar hold roles, certificates, the whole-work NFT, participation offers, the secondary marketplace, distribution, and the certification fee. The public explorer is the receipt.

Component diagram and certification / sale flows: [docs/architecture.md](docs/architecture.md).

## Status

<!-- GENERATED:status -->
| Area | State | Document |
| --- | --- | --- |
| Network | Mainnet LIVE — artifex.0xvera.com | [stellar.expert/public](https://stellar.expert/explorer/public) |
| QA mainnet | PASS — Mainnet run a–g (26/10/2026) | [QA.md](QA.md#mainnet-run-26102026) |
| QA Testnet (history) | 4 passes · 9 → 20 → 22 → 28 validated · APTO | [QA.md](QA.md#pass-history-testnet) |
| Latest release | api 0.17.5, web 0.4.25, cosign verified | [RELEASES.md](RELEASES.md) |
| Active contracts | Mainnet LIVE (mainnet-v1, tag vps-deploy); deploy 38 txs | [CONTRACTS.md](CONTRACTS.md) |
| Roadmap | HackMeridian in progress | [ROADMAP.md](ROADMAP.md) |

<!-- /GENERATED:status -->

Generated together with [QA.md](QA.md), [RELEASES.md](RELEASES.md), [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [ROADMAP.md](ROADMAP.md).

## Try it

1. Install [Freighter](https://www.freighter.app/) and set the network to **Public** (mainnet). Fund the account with real XLM.
2. Open [the app](https://artifex.0xvera.com), find **Estudio en azul** (offer titled **Try it**, **0.1 XLM**), and buy one unit.
3. Open the transaction on the [public explorer](https://stellar.expert/explorer/public) and confirm that the units arrived.

Full steps: [TRY-IT.md](TRY-IT.md). Catalog: [PIECES.md](PIECES.md). Public verify example (Luz de Anaga): [verify link](https://artifex.0xvera.com/verify/8f0326d791c679433f71e3d1b3ba4837d9ff47f51e431ac6918a7c8c6ca282e6).

## Before HackMeridian

Already on Stellar Testnet before Sunday 25 October 2026 09:00 Lisbon:

- Product flows for living-artist certification and sales, museum/foundation participations, public QR verify, marketplace in XLM and USDC, multi-wallet organizations, and deceased-author certification as an additional capacity.
- Soroban contract versions **v1** and **v2** deployed; public API serving **v2** (contracts tag **v0.1.0**).
- Harbor images for API and web UI, signed keyless with cosign.
- **15 demo artworks** on-chain: **7 certified**, 10 for sale.
- External black-box QA: pass 1 (21 Oct) 9 validated / 11 blockers → pass 2 (22 Oct) 20 / 4 → pass 3 (23 Oct) 22 / 4.

Details: [CONTRACTS.md](CONTRACTS.md), [RELEASES.md](RELEASES.md), [PIECES.md](PIECES.md), [QA.md](QA.md).

## During HackMeridian

From Sunday 25 October 2026 09:00 Lisbon, the Scale track prioritizes production readiness and mainnet launch.

**Landed:**

- **Mainnet LIVE** (api **0.17.5** / web **0.4.25**, registry **mainnet-v1**): contracts deployed, VPS wiring verified, seed **`hackathon-scale-15-v6-mainnet`**, web network from the API (Mainnet footer, no Testnet banner), certification fee from `/fees/cert`.
- **Mainnet QA PASS** — Freighter black-box run **a–g** (26 Oct): living-author cert + whole sale (Luz de Anaga), participations + Try it, proportional distribute, USDC buy, deceased two-signature finalize (Puerto al alba), public QR verify. **19** successful txs · **0.448 XLM** fees. See [QA.md](QA.md#mainnet-run-26102026).
- Stills from the run: [docs/mainnet-run/…](docs/mainnet-run/Artifex_Mainnet_Run_2026-10-26/Artifex_Mainnet_Run_2026-10-26.md) (videos on YouTube, not in this repo).
- Testnet gate for the launch: four passes **9 → 20 → 22 → 28** validated, then re-test **APTO**.

**Testnet** remains development and QA history only.

Dated evidence: [HACKMERIDIAN.md](HACKMERIDIAN.md). Roadmap: [ROADMAP.md](ROADMAP.md).

The original application named OpenZeppelin contracts, Trustless Work escrow, and path payments. After conversations with judges and mentors, those three move to the longer [roadmap](ROADMAP.md) (phase 3).

## Known limitations

- Live network is Stellar **mainnet**. Testnet tables are history only ([PIECES.md](PIECES.md), [QA.md](QA.md)).
- Seven non-blocking UI findings from the Mainnet run are listed under [QA.md Known issues](QA.md#known-issues-non-blocking-ui) and tracked on the [roadmap](ROADMAP.md).
- Platform and validator are the same mainnet address today. Splitting them behind multisig is [phase 3](ROADMAP.md). See [WALLETS.md](WALLETS.md).
- Participations are not a legal opinion on title. Counsel review is [phase 3](ROADMAP.md).
- Signing is Freighter. Passkey smart wallet is [phase 1](ROADMAP.md); iOS / Android are [phase 2](ROADMAP.md).

## Public contracts

The Soroban contracts used by Artifex are public: [0xVeraHQ/artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts). Deployed mainnet IDs: [CONTRACTS.md](CONTRACTS.md).

## Private repositories

These repositories stay private (application, UI, orchestration, internal docs):

- artifex-api, artifex-web-ui, artifex-orch, and related ops repos.

Judges only need this overview repo and the public contracts repo.

## License

See [LICENSE](LICENSE).
