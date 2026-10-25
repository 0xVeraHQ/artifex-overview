#!/usr/bin/env python3
"""Build pieces.yaml from the public Testnet API + indexed on-chain txs."""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://artifex.0xvera.com/api"
MAPS = ROOT / "sources" / "_tx_maps.json"

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
    maps = {"fee": {}, "offers": {}, "listings": {}, "distrib": {}}
    if MAPS.exists():
        maps.update(json.loads(MAPS.read_text(encoding="utf-8")))
    fee = maps.get("fee") or {}
    offers = maps.get("offers") or {}
    listings = maps.get("listings") or {}
    distrib = maps.get("distrib") or {}

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
            modality = (
                "Whole work (physical delivery)"
                if detail.get("physicalDeliveryFlag")
                else "Whole work (digital)"
            )
        elif product == "participation":
            part = sm.get("participationType")
            modality = "Participation — " + PART_LABELS.get(part, part or "unspecified")
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
        oid_s = str(oid) if oid is not None else None
        lid_s = str(lid) if lid is not None else None
        pieces.append(
            {
                "n": n,
                "title": title,
                "artist": detail.get("artistName"),
                "pieceId": pid,
                "certification": CERT_LABELS.get(
                    detail.get("certType"), detail.get("certType")
                ),
                "status": status,
                "modality": modality,
                "forSale": for_sale,
                "price": price_disp if for_sale else "—",
                "tryIt": bool(sm.get("tryIt")),
                "offerId": oid_s if oid_s and for_sale else None,
                "listingId": lid_s if lid_s and for_sale else None,
                "certTx": fee.get(pid),
                "offerTx": offers.get(oid_s) if oid_s and for_sale else None,
                "listingTx": listings.get(lid_s) if lid_s and for_sale else None,
                "distribTx": distrib.get(oid_s) if oid_s else None,
            }
        )
    doc = {
        "network": "testnet",
        "seed": "15-demo-artworks",
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
