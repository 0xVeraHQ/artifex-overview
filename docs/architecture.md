# Architecture

Artifex on Stellar Testnet. The diagrams match the running Scale deployment: a web app, an API, and Soroban contracts. Host layout, ports, and operational paths are not part of this document.

Identifiers for the contracts and the project accounts are generated in [CONTRACTS.md](../CONTRACTS.md) and [WALLETS.md](../WALLETS.md).

## Components

```mermaid
flowchart LR
  visitor[Visitor]
  freighter[Freighter]
  web[Web app]
  api[API]
  catalog[(Catalog, fiches, documents)]
  rpc[Stellar Testnet RPC]
  contracts[Soroban contracts]
  expert[Stellar Expert]

  visitor --> web
  freighter --> web
  web --> api
  api --> catalog
  api --> rpc
  rpc --> contracts
  visitor --> expert
  web --> expert
```

The visitor can browse and verify with no wallet. Freighter is required to sign a certification, a purchase, a listing, or a trustline. The API prepares the transaction. The signer approves it. The contracts record the result. Stellar Expert is the public receipt.

The contracts are: roles, connoisseur authorization, certificate registry, fee collector, whole-work NFT, participation, marketplace, and distribution. Payments use the Stellar asset contracts for XLM and for Testnet USDC.

## Certification

A living author signs once. A deceased author needs two signatures: the connoisseur, and one of the heir, a museum, or a foundation. The museum or foundation authorizes the connoisseur before that connoisseur can sign. The fee is 5 XLM or 1 USDC, collected before the certificate is finalized.

```mermaid
flowchart TD
  fiche[Piece fiche, with photographs and document hashes]
  kind{Author}
  living[Living author signs once]
  auth[Museum or foundation authorizes the connoisseur]
  first[Connoisseur signs]
  second[Heir, museum, or foundation signs]
  fee[Fee: 5 XLM or 1 USDC]
  done[Certificate finalized on the registry]
  qr[Public QR or link, no wallet]
  pending[Stays pending until the second signature]

  fiche --> kind
  kind -->|Living| living
  kind -->|Deceased| auth
  living --> fee
  auth --> first
  first --> pending
  pending --> second
  second --> fee
  fee --> done
  done --> qr
```

Digitizing an existing certificate is the same registry, with the prior document hash on the fiche.

Verification reads the registry. It shows the signers. A fiche that was never finalized is shown as not certified, including when it is offered for sale.

## Sale

Two sale shapes share the marketplace. A whole work transfers the NFT. A participation transfers units of one of the four types. Both settle in XLM or Testnet USDC. Primary participation sales deliver the units in the same contract call as the payment. Secondary listings can be filled in part.

```mermaid
flowchart TD
  piece[Piece, certified or marked uncertified]
  whole[Whole work]
  part[Participation offer from a museum or foundation]
  digital[Digital transfer of the NFT]
  physical[Physical-delivery clause, form off-chain]
  types[Future sale, guaranteed repurchase, financing with return, or exploitation rights]
  primary[Primary buy: payment and units together]
  secondary[Secondary listing]
  partial[Partial fill, or cancel the remainder]
  pay[Buyer pays XLM or Testnet USDC]
  receipt[Transaction on Stellar Expert]
  dist[Distribution under the terms]

  piece --> whole
  piece --> part
  whole --> digital
  whole --> physical
  digital --> pay
  physical --> pay
  part --> types
  types --> primary
  primary --> secondary
  primary --> dist
  secondary --> partial
  partial --> pay
  pay --> receipt
```

Distribution follows the terms hash stored for that offer. Burning or retiring units is part of that policy, and it does not revoke the certificate.
