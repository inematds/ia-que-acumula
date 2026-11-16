#!/usr/bin/env bash
set -euo pipefail
BASE=$(cd "$(dirname "$0")/.." && pwd)
TRADUTOR=${INEMA_TRADUZ_BIN:-inema-traduz}
command -v "$TRADUTOR" >/dev/null || { echo 'Instale/configure o tradutor central inema-traduz pela assinatura antes de traduzir.' >&2; exit 2; }
cd "$BASE"
for idioma in en es; do
 test -s "i18n/pedido-$idioma.txt" || { echo "Prepare i18n/pedido-$idioma.txt com o JSON PT e a instrução de preservação." >&2; exit 2; }
 timeout 900 "$TRADUTOR" -o "i18n/$idioma.json" < "i18n/pedido-$idioma.txt"
done
