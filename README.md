# Artifex

Provenance and funding for art, on Stellar Testnet.

Live app: [https://artifex.0xvera.com](https://artifex.0xvera.com)

Artifex is built for HackMeridian 2026, track Scale. This repository is the presentation. It has no source code. It has the product, the public Testnet identifiers, and the status of QA, releases, contracts, and the roadmap. The tables are generated from the real sources. Do not edit them by hand.

## What Artifex is

Galleries, museums, and foundations need a record that travels with the work: who made it, who certified it, and, when they choose, a way to fund it without pretending that a token is the legal title.

Two problems sit on top of each other. A certificate that lives only in a folder cannot be checked by the next buyer. A sale that is only a private invoice cannot show, in public, that the payment and the delivery happened together. Artifex puts both on Stellar Testnet, where anyone can open the transaction.

A participation is a contractual position in a work (a future sale, a guaranteed repurchase, financing with a return, or exploitation rights). It is not a claim that the holder owns the physical object. That distinction stays visible in the product, and the legal review of participations is [phase 3 of the roadmap](ROADMAP.md).

## How it works

**Certification.** A living author certifies a work with one signature and a fee (5 XLM or 1 USDC). A deceased author needs two signatures: a connoisseur, and a second signature from the heir, a museum, or a foundation. The museum or foundation authorizes the connoisseur first. An existing paper certificate can be digitized, with the document hash stored on the fiche.

**Verification.** Anyone can open a QR code or a link and read the certificate, including who signed it. No wallet is required. A work that is not certified can still be listed, and the page marks it as not certified.

**Whole work.** The owner sells the entire work. The sale is digital, or it includes a physical-delivery clause. The delivery form is off-chain. The payment and the change of ownership are on-chain.

**Participations.** Museums and foundations offer units in a work. There are four types: future sale, guaranteed repurchase, financing with a return, and exploitation rights. Each offer carries a terms document. A buyer can take the whole offer or part of it. The payment and the delivery of units happen in the same contract call.

**Marketplace.** Primary sales and secondary listings are public. A secondary listing can be filled in part, and the seller can cancel what remains. Prices are in XLM or in Testnet USDC.

## Architecture

The web app talks to an API. The API keeps the catalog, the fiches, and the documents, and it prepares the transactions. The buyer or the signer approves them in Freighter. Soroban contracts on Stellar Testnet hold roles, certificates, the whole-work NFT, participation offers, the secondary marketplace, distribution, and the certification fee. Stellar Expert is the public receipt.

The component diagram and the certification and sale flows are in [docs/architecture.md](docs/architecture.md).

## Status

<!-- GENERATED:status -->
| Area | State | Document |
| --- | --- | --- |
| QA | PENDING — third QA pass in progress | [QA.md](QA.md) |
| Latest release | api 0.16.6, web 0.4.7, cosign verified | [RELEASES.md](RELEASES.md) |
| Active contracts | Registry v2 on Testnet, contracts tag v0.1.0 | [CONTRACTS.md](CONTRACTS.md) |
| Roadmap | HackMeridian in progress | [ROADMAP.md](ROADMAP.md) |

<!-- /GENERATED:status -->

The four rows above are generated together with [QA.md](QA.md), [RELEASES.md](RELEASES.md), [CONTRACTS.md](CONTRACTS.md), [WALLETS.md](WALLETS.md), and [ROADMAP.md](ROADMAP.md).

## Try it

1. Install [Freighter](https://www.freighter.app/) and switch it to **Testnet**. Fund the account with [Friendbot](https://friendbot.stellar.org/).
2. Get Testnet USDC, open [the app](https://artifex.0xvera.com), and buy the offer titled **Try it**.
3. Open the transaction on [Stellar Expert](https://stellar.expert/explorer/testnet) and confirm that the units arrived in your account.

The clicks, the USDC issuer, and the trustline are in [TRY-IT.md](TRY-IT.md).

## Before / During HackMeridian

This section is a marker. Fill it in on Sunday 25 October 2026.

### Before the event

<!-- SUNDAY-25: before -->

> **Sunday 25.** Replace this block with what already existed before HackMeridian 2026.

<!-- /SUNDAY-25: before -->

### During the event

<!-- SUNDAY-25: during -->

> **Sunday 25.** Replace this block with what is built during the event.

<!-- /SUNDAY-25: during -->

## Known limitations

- The deployment is Stellar Testnet. Mainnet is [phase 3](ROADMAP.md).
- The platform account and the validator account are the same address today. Splitting them, and putting each behind a multisig, is [phase 3](ROADMAP.md). See [WALLETS.md](WALLETS.md).
- Participations are not a legal opinion on title. Counsel reviews them in [phase 3](ROADMAP.md).
- Signing is Freighter on Testnet. A passkey smart wallet is [phase 1](ROADMAP.md). iOS and Android are [phase 2](ROADMAP.md).
- OpenZeppelin contracts, Trustless Work escrow, and payment in any asset through path payments are the HackMeridian scope in [the roadmap](ROADMAP.md). They are not the contracts listed in [CONTRACTS.md](CONTRACTS.md).
- The third external QA pass is still running. Every case in [QA.md](QA.md) is PENDING until that pass reports.
- The judge path buys an offer titled **Try it**. That title was not in the public catalog on 22 October 2026. The steps are in [TRY-IT.md](TRY-IT.md).

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
