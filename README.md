# Artifex

Provenance, certification, and funding for art — on Stellar.

Live app (Testnet): [https://artifex.0xvera.com](https://artifex.0xvera.com)

Artifex is built for **HackMeridian 2026**, track **Scale**. This repository (`0xVeraHQ/artifex-overview`) is the public presentation. It has no source code. It has the product story, public Testnet identifiers, and the status of QA, releases, contracts, wallets, pieces, and the roadmap. Tables are generated from the real sources. Do not edit them by hand.

Judges will not have access to the private implementation repositories. Everything needed to understand and verify Artifex is here, with links to [Stellar Expert](https://stellar.expert/explorer/testnet).

## What Artifex is

Galleries, museums, and foundations need a record that travels with the work: who made it, who certified it, and, when they choose, a way to fund it without pretending that a token is the legal title.

Two problems sit on top of each other. A certificate that lives only in a folder cannot be checked by the next buyer. A sale that is only a private invoice cannot show, in public, that the payment and the delivery happened together. Artifex puts both on Stellar, where anyone can open the transaction.

A participation is a contractual position in a work (a future sale, a guaranteed repurchase, financing with a return, or exploitation rights). It is not a claim that the holder owns the physical object. That distinction stays visible in the product. Legal review of participations remains on the [roadmap](ROADMAP.md).

## How it works

**Certification.** A living author certifies a work with one signature and a fee (5 XLM or 1 USDC). A deceased author needs two signatures: a connoisseur, and a second signature from the heir, a museum, or a foundation. The museum or foundation authorizes the connoisseur first. An existing paper certificate can be digitized, with the document hash stored on the fiche.

**Verification.** Anyone can open a QR code or a link and read the certificate, including who signed it. No wallet is required. A work that is not certified can still be listed, and the page marks it as not certified.

**Whole work.** The owner sells the entire work. The sale is digital, or it includes a physical-delivery clause. The delivery form is off-chain. The payment and the change of ownership are on-chain.

**Participations.** Museums and foundations offer units in a work. There are four types: future sale, guaranteed repurchase, financing with a return, and exploitation rights. Each offer carries a terms document. A buyer can take the whole offer or part of it. The payment and the delivery of units happen in the same contract call.

**Marketplace.** Primary sales and secondary listings are public. A secondary listing can be filled in part, and the seller can cancel what remains. Prices are in XLM or in USDC.

**Organizations.** Museums and foundations operate with several member wallets under one organization, with roles enforced on-chain and in the product.

## Architecture

The web app talks to an API. The API keeps the catalog, the fiches, and the documents, and it prepares the transactions. The buyer or the signer approves them in Freighter. Soroban contracts on Stellar hold roles, certificates, the whole-work NFT, participation offers, the secondary marketplace, distribution, and the certification fee. Stellar Expert is the public receipt.

Component diagram and certification / sale flows (Mermaid): [docs/architecture.md](docs/architecture.md).

## Status

<!-- GENERATED:status -->
| Area | State | Document |
| --- | --- | --- |
| QA | PENDING — 4th QA pass in progress | [QA.md](QA.md) |
| Latest release | api 0.16.16, web 0.4.16, cosign verified | [RELEASES.md](RELEASES.md) |
| Active contracts | Registry v2 on Testnet, contracts tag v0.1.0 | [CONTRACTS.md](CONTRACTS.md) |
| Roadmap | HackMeridian in progress | [ROADMAP.md](ROADMAP.md) |

<!-- /GENERATED:status -->

Generated together with [QA.md](QA.md), [RELEASES.md](RELEASES.md), [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [ROADMAP.md](ROADMAP.md).

## Try it

1. Install [Freighter](https://www.freighter.app/) and switch it to **Testnet**. Fund the account with [Friendbot](https://friendbot.stellar.org/).
2. Open [the app](https://artifex.0xvera.com), find **Estudio en azul** (offer titled **Try it**), and buy one unit (priced in XLM).
3. Open the transaction on [Stellar Expert](https://stellar.expert/explorer/testnet) and confirm that the units arrived in your account.

Full steps: [TRY-IT.md](TRY-IT.md). Seed catalog: [PIECES.md](PIECES.md).

## Before HackMeridian

Already on Stellar Testnet before Sunday 25 October 2026 09:00 Lisbon:

- Product flows for certification (living / deceased / digitization), public QR verify, whole-work and participation sales, primary and secondary marketplace in XLM and USDC, and multi-wallet organizations.
- Soroban contract registry **v1** and **v2** deployed; public API serving **v2** (contracts tag **v0.1.0**).
- Harbor images for API and web UI, signed keyless with cosign.
- Seed **v6**: 15 fictional works, seven certified under the seed design, ten for sale, recorded on-chain.
- External black-box QA: pass 1 (21 Oct) 9 validated / 11 blockers → pass 2 (22 Oct) 20 / 4 → pass 3 (23 Oct) 22 / 4.

Details: [CONTRACTS.md](CONTRACTS.md), [RELEASES.md](RELEASES.md), [PIECES.md](PIECES.md), [QA.md](QA.md).

## During HackMeridian

From Sunday 25 October 2026 09:00 Lisbon, the Scale track work prioritizes production readiness:

- Whole-work sale on contract registry **v3**
- USDC purchase fix and locked-unit recovery
- Offer / listing indexing and automatic distribution to holders
- Role permissions and verification improvements
- Fourth external QA pass
- Stellar **mainnet** launch

Dated evidence: [HACKMERIDIAN.md](HACKMERIDIAN.md). Roadmap row: [ROADMAP.md](ROADMAP.md).

Application intents that remain on the longer roadmap (not the contracts listed as active today): OpenZeppelin contracts, Trustless Work escrow, and path payments — see phase 3 in [ROADMAP.md](ROADMAP.md).

## Known limitations

- Deployment today is Stellar **Testnet**. Mainnet sections are **PENDING** (`mainnet launch at HackMeridian`) in [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), [PIECES.md](PIECES.md), and [QA.md](QA.md).
- Platform and validator are the same Testnet address today. Splitting them behind multisig is [phase 3](ROADMAP.md). See [WALLETS.md](WALLETS.md).
- Participations are not a legal opinion on title. Counsel review is [phase 3](ROADMAP.md).
- Signing is Freighter. Passkey smart wallet is [phase 1](ROADMAP.md); iOS / Android are [phase 2](ROADMAP.md).
- Fourth external QA pass is in progress. Cases still open are **PENDING** in [QA.md](QA.md).
- Registry **v3** cutover and whole-work sale on v3 are in progress during the event — [HACKMERIDIAN.md](HACKMERIDIAN.md).

## Team

- **Joel** — captain, technical.
- **Luis** — art expert, from a family of gallerists.

## Source access

The implementation is private and stays private:

- `artifex-api`
- `artifex-web-ui`
- `artifex-contracts`
- `artifex-orch`
- `artifex-docs`

All of them are under the GitHub organization [0xVeraHQ](https://github.com/0xVeraHQ). This repository does not contain their source, secrets, or host configuration.

A HackMeridian judge who needs to read the code can request read-only access. Open an issue on this repository titled **Read access for evaluation**, and include the GitHub usernames. Access is for the evaluation. The license is in [LICENSE](LICENSE): all rights reserved.
