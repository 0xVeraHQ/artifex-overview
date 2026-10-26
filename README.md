# Artifex

Provenance, certification, and funding for art — on Stellar.

Live app (**Stellar mainnet**): [https://artifex.0xvera.com](https://artifex.0xvera.com)

Artifex is built for **HackMeridian 2026**, track **Scale**. This repository (`0xVeraHQ/artifex-overview`) is the public presentation for judges. It has the product story, public mainnet identifiers (with Testnet history from the event), and the status of QA, releases, contracts, wallets, pieces, and the roadmap. Tables are generated from the real sources. Do not edit them by hand.

Judges do not need the private application repositories. Everything to understand and verify Artifex is here, with explorer links for on-chain evidence. The Soroban contracts are public (see below).

## What Artifex is

Artists need a simple path: certify a work with their wallet, then sell it whole or in participations on a public marketplace. Collectors need to check that certificate and settle a purchase on-chain, without a private PDF as the only proof.

Museums and foundations can raise financing against a work through participations **without moving the physical piece**. The four participation types are future sale, guaranteed repurchase, financing with a return, and exploitation rights.

As an additional capacity, works by deceased authors can be certified with two signatures (connoisseur plus heir, museum, or foundation), including digitization of a prior paper certificate.

Artifex puts certification and settlement on Stellar so anyone can open the transaction.

> **Note.** A participation is a contractual position in a work. It is not a claim that the holder owns the physical object. That distinction stays visible in the product. Legal review of participations remains on the [roadmap](ROADMAP.md).

## How it works

**Living artists.** The author certifies the work with one signature and a fee (5 XLM or 1 USDC), then lists a whole-work sale (digital or with a physical-delivery clause) or a participation offer on the marketplace. Payment and delivery of the NFT or of participation units happen in the same contract call.

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
| QA | PASS — APTO for mainnet (re-test api 0.16.23 / web 0.4.21–0.4.22) | [QA.md](QA.md) |
| Latest release | api 0.17.5, web 0.4.25, cosign verified | [RELEASES.md](RELEASES.md) |
| Active contracts | Mainnet live (mainnet-v1, tag vps-deploy); deploy 38 txs | [CONTRACTS.md](CONTRACTS.md) |
| Roadmap | HackMeridian in progress | [ROADMAP.md](ROADMAP.md) |

<!-- /GENERATED:status -->

Generated together with [QA.md](QA.md), [RELEASES.md](RELEASES.md), [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [ROADMAP.md](ROADMAP.md).

## Try it

1. Install [Freighter](https://www.freighter.app/) and set the network to **Public** (mainnet). Fund the account with real XLM.
2. Open [the app](https://artifex.0xvera.com), find **Estudio en azul** (offer titled **Try it**, **0.1 XLM**), and buy one unit.
3. Open the transaction on the [public explorer](https://stellar.expert/explorer/public) and confirm that the units arrived.

Full steps: [TRY-IT.md](TRY-IT.md). Catalog: [PIECES.md](PIECES.md).

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

- **Mainnet is live** (api **0.17.5** / web **0.4.25**, registry **mainnet-v1**): contracts deployed, VPS wiring verified, five seed wallets USDC-funded, seed **`hackathon-scale-15-v6-mainnet`** plus Mainnet-smoke fiche **Luz de Anaga** (certified · token **5** · sold to QA-3).
- Web takes network from the API (SSR Mainnet footer; no Testnet banner); deposit fees from `/fees/cert`.
- QA Freighter accounts activated on mainnet (QA-1/3/4/5 from QA-2; QA-2 USDC trustline + 2 USDC top-up). See [WALLETS.md](WALLETS.md) / [QA.md](QA.md).

**In progress:** mainnet product QA (Mainnet smoke **PENDING** in [QA.md](QA.md); certify / buy / distribute txs observed on-chain).

**Testnet (history):** development and external QA — four passes, validated cases **9 → 20 → 22 → 28**, then re-test **APTO for mainnet**. Details in [QA.md](QA.md) Cases (Testnet history).

Dated evidence: [HACKMERIDIAN.md](HACKMERIDIAN.md). Roadmap: [ROADMAP.md](ROADMAP.md).

The original application named OpenZeppelin contracts, Trustless Work escrow, and path payments. After conversations with judges and mentors, those three move to the longer [roadmap](ROADMAP.md) (phase 3).

## Known limitations

- Live network is Stellar **mainnet**. Testnet tables are history only ([PIECES.md](PIECES.md), [QA.md](QA.md)).
- Platform and validator are the same mainnet address today. Splitting them behind multisig is [phase 3](ROADMAP.md). See [WALLETS.md](WALLETS.md).
- Participations are not a legal opinion on title. Counsel review is [phase 3](ROADMAP.md).
- Signing is Freighter. Passkey smart wallet is [phase 1](ROADMAP.md); iOS / Android are [phase 2](ROADMAP.md).
- Mainnet smoke QA is **PENDING**; Testnet gate remains **PASS / APTO**.

## Team

- **Joel** — captain, technical.
- **Luis** — art expert, from a family of gallerists.

## Source code: smart contracts

The Soroban contracts are public:

- **[0xVeraHQ/artifex-contracts](https://github.com/0xVeraHQ/artifex-contracts)** — Rust / Soroban SDK sources, tags, and Wasm artifacts referenced from [CONTRACTS.md](CONTRACTS.md).

## Private implementation

These repositories stay private (application, UI, orchestration, internal docs):

- `artifex-api`
- `artifex-web-ui`
- `artifex-orch`
- `artifex-docs`

All of them are under the GitHub organization [0xVeraHQ](https://github.com/0xVeraHQ). This presentation repository does not contain their source, secrets, or host configuration.

A HackMeridian judge who needs read-only access to the private repos can open an issue on this repository titled **Read access for evaluation**, and include the GitHub usernames. Access is for the evaluation. The license is in [LICENSE](LICENSE): all rights reserved.
