#!/usr/bin/env python3
"""Forward buffered events to the analytics ingest API."""
import requests

import settings


def flush(events):
    r = requests.post(f'{settings.API_BASE}/events',
                      json={'events': events},
                      headers={'Authorization': f'Bearer {settings.API_TOKEN}'}, timeout=30)
    r.raise_for_status()
    return r.json()


if __name__ == '__main__':
    print('forwarder ready; batch size', settings.BATCH_SIZE)
