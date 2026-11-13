# open.siflo.app

The second domain of Siflo's app links on iPhone (issue paulasquin/siflo#404, AP1). The "Open in Siflo" button of
siflo.app's link pages points to `https://open.siflo.app<path>#<fragment>`: navigating to another domain lets iOS hand
the link to the app signed by team `285X8VFA49` (associated domain `applinks:open.siflo.app`), instead of the
`siflo://` scheme that any app can claim.

- `.well-known/apple-app-site-association`: the same paths as siflo.app's (keep both in step).
- `index.html` / `404.html`: shown when the link was not handed over. On an iPhone: install or update Siflo, or back
  to the siflo.app page; elsewhere: straight back to the same path on siflo.app. The fragment never leaves the phone.
- DNS: `bws-env run ovh -- uv run -q --with ovh python -I tools/ovh_dns.py` (CNAME `open` → `paulasquin.github.io.`),
  then GitHub Pages with custom domain `open.siflo.app` and HTTPS enforced.
