"""Point open.siflo.app at GitHub Pages in the OVH zone (CNAME to paulasquin.github.io.). Idempotent.

    bws-env run ovh -- uv run -q --with ovh python -I tools/ovh_dns.py
"""
import os

import ovh

c = ovh.Client(endpoint=os.environ["OVH_ENDPOINT"], application_key=os.environ["OVH_APPLICATION_KEY"],
               application_secret=os.environ["OVH_APPLICATION_SECRET"], consumer_key=os.environ["OVH_CONSUMER_KEY"])
z = "siflo.app"
recs = [c.get(f"/domain/zone/{z}/record/{rid}") for rid in c.get(f"/domain/zone/{z}/record", subDomain="open")]
if any(r["fieldType"] == "CNAME" and r["target"] == "paulasquin.github.io." for r in recs):
    print("open CNAME already there")
else:
    c.post(f"/domain/zone/{z}/record", fieldType="CNAME", subDomain="open", target="paulasquin.github.io.", ttl=3600)
    c.post(f"/domain/zone/{z}/refresh")
    print("open CNAME -> paulasquin.github.io., zone refreshed")
