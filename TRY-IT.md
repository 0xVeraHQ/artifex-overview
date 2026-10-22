# Try it

A judge can buy one public offer on Stellar Testnet and see the units arrive. No source code is required.

The offer to buy is the marketplace listing titled **Try it**. On 22 October 2026 that title was not in the public catalog at [artifex.0xvera.com](https://artifex.0xvera.com). Use the steps below once the listing is up. Until then this path is part of the pending QA in [QA.md](QA.md) (case S-13).

Network: **Stellar Testnet**. Do not switch Freighter to Public.

## 1. Install Freighter and fund it

1. Install [Freighter](https://www.freighter.app/) in the browser.
2. Create an account, or import one you can spend on Testnet.
3. In Freighter, set the network to **Testnet**.
4. Copy the public key (it starts with `G`).
5. Fund it with [Friendbot](https://friendbot.stellar.org/). Friendbot sends Testnet XLM, which pays the fees. Friendbot does not send USDC.

Confirm the account exists on [Stellar Expert Testnet](https://stellar.expert/explorer/testnet) by pasting the public key.

## 2. Get Testnet USDC

The certification fee and some listings are priced in USDC. The asset is Circle's Testnet USDC:

| Field | Value |
| --- | --- |
| Code | `USDC` |
| Issuer | `GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5` |
| Faucet | [faucet.circle.com](https://faucet.circle.com/) (choose Stellar) |
| Explorer | [USDC on Testnet](https://stellar.expert/explorer/testnet/asset/USDC-GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5) |

1. Request Testnet USDC from the Circle faucet to your Freighter public key.
2. The account also needs a trustline for that issuer. On the piece page, use **Abrir trustline USDC** (open USDC trustline) and approve it in Freighter. The page then shows the USDC balance.

XLM from Friendbot is enough when the offer is priced in XLM. The Try it offer is the USDC path, so do both.

## 3. Buy the Try it offer

1. Open [https://artifex.0xvera.com](https://artifex.0xvera.com).
2. Open [Marketplace](https://artifex.0xvera.com/marketplace) and find the listing titled **Try it**.
3. Open the piece. Connect Freighter from [Connect](https://artifex.0xvera.com/connect) if the page asks.
4. Confirm the offer id, set the units (1 is enough), and press **Primary buy**.
5. Freighter shows the payment and the delivery of units. Approve it.

The page waits until the network confirms the transaction and links to Stellar Expert.

## 4. Check that you received it

1. Open the Stellar Expert link from the page, or search the transaction hash on [https://stellar.expert/explorer/testnet](https://stellar.expert/explorer/testnet).
2. In the transaction, confirm:
   - the source of the payment is your account
   - the asset paid is Testnet USDC (or XLM, if the listing is priced in XLM)
   - the participation units were delivered to your account
3. On the piece page, the units you bought are no longer available, or the remaining amount has decreased.

A participation is not legal title to the physical work. The terms document on the offer says what the units are.

Project accounts and contract ids, if you want to match them in the transaction, are in [WALLETS.md](WALLETS.md) and [CONTRACTS.md](CONTRACTS.md).
