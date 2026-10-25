#!/usr/bin/env python3
"""One-shot helper: build pieces.yaml from the public Testnet API + known txs."""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://artifex.0xvera.com/api"

SEED = [
    "Mar de invierno",
    "Figura en reposo",
    "Puerto al alba",
    "Serie Kyoto nº 3",
    "Cuenco ceniza",
    "Estudio en azul",
    "Retrato de Clara",
    "Torso II",
    "Ventana norte",
    "Paisaje de sal",
    "Nocturno en rojo",
    "Silencio blanco",
    "Autorretrato con sombrero",
    "Cerámica nº 7",
    "Mercado de flores",
]

FEE = {
    "87458dade39f63f1806bd6e64ccc0c56fdf370d31edba7d2a6c645fcfbdafcc4": "485621f69bb3d2d77ad63925840b92727d20a8d0f3297dcd45e0c290f52e4849",
    "f3c7e94f3c327d158c6b533f723e13da05827355403ab055b6efe2512df48a41": "a50c7e8d12bc81457559435947a5f301df61e6dee9610a691a0e26c90c793f54",
    "67b36becdd2b12df0918a9e68cd02b964595b970e0063f53f01066f5fb70fbbe": "e2231eb4e9bad4c5f2c49ffb179eb17d503750ea64c008f9da0d104837a4e3d3",
    "bdaf39d626a0832062f9973afcc1ef72a0f88e479c3faec3e8fec04f336f7a9a": "9fd3d311c0c5e1b5eba60908f466c072fd6bc8726e69415386a5491e9ac42dab",
    "a36a38e6b9f448fc1d1276df22a94618dc498cce36f83bbca3980b5c0ee7ab07": "1bfba4f506f0667dba2569ac3b74e52a0abff76bc62af7e8908f074c57bda0c9",
    "da4ff18543b9f027a34d70ef7b570f77a8ea7244b7cc13ccf6e0fdc2e531ed54": "85e23ecde722d37452b44e45838c536809d9780c81165ea96cae030a0fb260ec",
    "b7a5f13b81b1fe9d8dde798e4594028f0d63494adaa4e24cd0af9a41d7ba6789": "70a30834e0ccf177639ff60b857097e67c4bb547b053a95aee340b5a73d1015c",
}

OFFERS = {
    "152": "8a95b58d6670a52b203faa60f11fc0965c091cb19a696a11da0dd8ead5dcd7ee",
    "153": "b5bc47646bdb2d720fc899d26a79c2c6345685fe9a7c84e25918b28875285fbf",
    "154": "72feeb63cb1eb30d68657700bddf3ae9ef2299aa6468981d011b5f9c39aa5654",
    "155": "09b0101c66ca8cedf668bd80fca13633e9d01975ded9b9a18d7bd39180994c8a",
    "156": "aeda0a2465cd4fcb6356f31e7e9d50260804a485c1161e78ec2b38c335afad9a",
    "157": "51f347fd05a84fa0bec0a2ec95c6231477f5c65808c725770b69765753b593ca",
}

LISTINGS = {
    "18": "f6cc4e52102d9cad119a5107a2ded823cd8f91b83f184cd21e8b0651d188b30e",
}

CERT_LABELS = {
    "living_author": "Living author (1 signature)",
    "deceased_connoisseur": "Deceased author (connoisseur + institution)",
    "deceased_heir": "Deceased author (connoisseur + heir)",
    "deceased_institution": "Deceased author (institution + connoisseur)",
    "prior_digitization": "Prior certificate digitization",
}

PART_LABELS = {
    "future_sale": "Future sale",
    "guaranteed_buyback": "Guaranteed buyback",
    "return_financing": "Return financing",
    "exploitation_rights": "Exploitation rights",
}


def get(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def main() -> None:
    items = get(f"{BASE}/pieces")["items"]
    by_title = {p["title"]: p for p in items}
    pieces = []
    for n, title in enumerate(SEED, 1):
        summary = by_title[title]
        detail = get(f"{BASE}/pieces/{summary['pieceId']}")
        sm = (detail.get("contractsSnapshot") or {}).get("saleMeta") or {}
        price = sm.get("unitPrice")
        cur = (sm.get("currencies") or [None])[0]
        price_disp = "—"
        if price and cur:
            price_disp = f"{int(price) / 10_000_000:g} {cur}"
        product = sm.get("product")
        for_sale = bool(sm.get("forSale"))
        if not for_sale or product in (None, "null"):
            modality = "Not for sale"
        elif product == "whole":
            modality = "Whole work (physical delivery)" if detail.get(
                "physicalDeliveryFlag"
            ) else "Whole work (digital)"
        elif product == "participation":
            part = sm.get("participationType")
            modality = (
                "Participation — "
                + PART_LABELS.get(part, part or "unspecified")
            )
        else:
            modality = "Not for sale"
        oid = sm.get("primaryOfferId")
        lid = sm.get("secondaryListingId")
        pid = detail["pieceId"]
        certified = bool(detail.get("certified"))
        chain_cert = sm.get("chainCert")
        status = "Certified" if certified else "Not certified"
        if chain_cert == "pending_second":
            status = "Pending second signature"
        pieces.append(
            {
                "n": n,
                "title": title,
                "artist": detail.get("artistName"),
                "pieceId": pid,
                "certification": CERT_LABELS.get(detail.get("certType"), detail.get("certType")),
                "status": status,
                "modality": modality,
                "forSale": for_sale,
                "price": price_disp if for_sale else "—",
                "tryIt": bool(sm.get("tryIt")),
                "offerId": str(oid) if oid and for_sale else None,
                "listingId": str(lid) if lid and for_sale else None,
                "certTx": FEE.get(pid),
                "offerTx": OFFERS.get(str(oid)) if oid and for_sale else None,
                "listingTx": LISTINGS.get(str(lid)) if lid and for_sale else None,
                "distribTx": None,
            }
        )
    doc = {
        "network": "testnet",
        "seed": "hackathon-scale-15-v6",
        "pieces": pieces,
        "mainnet": {
            "status": "PENDING",
            "reason": "mainnet launch at HackMeridian",
            "pieces": [],
        },
    }
    out = ROOT / "pieces.yaml"
    out.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
        newline="\n",
    )
    print(f"wrote {out} ({len(pieces)} pieces)")


if __name__ == "__main__":
    main()
