 from __future__ import annotations

def _get(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def match_offers(offers, requests):
    matches = []

    for offer in offers:
        offer_item_name = _get(offer, "itemName")
        offer_id = _get(offer, "id")
        for request in requests:
            request_item_name = _get(request, "itemName")
            if offer_item_name == request_item_name:
                matches.append({
                    "offer_id": offer_id,
                    "request_id": _get(request, "id"),
                    "itemName": offer_item_name
                })

    return matches
