
with urllib.request.urlopen("http://api.eia.gov/bulk/manifest.txt") as url:
    manifest = json.loads(url.read().decode())