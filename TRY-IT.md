# Try it

A judge can buy one public participation unit on Stellar Testnet and see it arrive. No source code is required.

| Field | Value |
| --- | --- |
| Work | **Estudio en azul** (Elena Varga) |
| Offer title | **Try it** |
| Modality | Participation — future sale |
| Price | **1 XLM** per unit |
| Network | **Stellar Testnet** |
| App | [https://artifex.0xvera.com](https://artifex.0xvera.com) |
| Piece (verify) | [Public verify page](https://artifex.0xvera.com/verify/67b36becdd2b12df0918a9e68cd02b964595b970e0063f53f01066f5fb70fbbe) |

Do not switch Freighter to Public (mainnet). Demo catalog: [PIECES.md](PIECES.md).

## 1. Install Freighter and fund it

1. Install [Freighter](https://www.freighter.app/) in the browser.
2. Create an account, or import one you can spend on Testnet.
3. In Freighter, set the network to **Testnet**.
4. Copy the public key (it starts with `G`).
5. Fund it with [Friendbot](https://friendbot.stellar.org/). Friendbot sends Testnet XLM for fees and for this purchase.

Confirm the account exists on [Stellar Expert Testnet](https://stellar.expert/explorer/testnet) by pasting the public key.

## 2. Open the Try it offer

1. Open [https://artifex.0xvera.com](https://artifex.0xvera.com).
2. Open [Marketplace](https://artifex.0xvera.com/marketplace) (or the catalog) and find **Estudio en azul** / the listing titled **Try it**.
3. Open the piece. Connect Freighter from [Connect](https://artifex.0xvera.com/connect) if the page asks.
4. Confirm the offer, set units to **1**, and press the primary buy action.
5. Freighter shows the payment (1 XLM) and the delivery of units. Approve it.

The page waits until the network confirms the transaction and links to Stellar Expert.

XLM from Friendbot is enough for this path. Other listings use Testnet USDC (Circle issuer `GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5`, faucet [faucet.circle.com](https://faucet.circle.com/)); those need a USDC trustline from the piece page.

## 3. Check that you received it

1. Open the Stellar Expert link from the page, or search the transaction hash on [https://stellar.expert/explorer/testnet](https://stellar.expert/explorer/testnet).
2. In the transaction, confirm:
   - the payment source is your account
   - the asset paid is **XLM**
   - the participation units were delivered to your account
3. On the piece page, available units have decreased by the amount you bought.

A participation is not legal title to the physical work. The terms document on the offer says what the units are.

Project accounts and contract ids: [WALLETS.md](WALLETS.md), [CONTRACTS.md](CONTRACTS.md). QA case for this path: **S-13** in [QA.md](QA.md) (PENDING while the fourth pass runs).
