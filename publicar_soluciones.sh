#!/usr/bin/env bash
#
# publicar_soluciones.sh
# -----------------------------------------------------------------------------
# Publica las soluciones del taller (modulo-*/soluciones.ipynb) DESPUÉS de la
# sesión de retos. Las soluciones están excluidas del material inicial por
# .gitignore (ver SOLUCIONES.md); este script las libera de forma controlada.
#
# Lo puede correr el instructor o cualquier persona con acceso al repo.
#
# USO:
#   ./publicar_soluciones.sh [metodo] [opciones]
#
#   metodo:
#     rama      (por defecto) publica las soluciones en la rama 'soluciones'
#     release   crea un GitHub Release con un ZIP de soluciones (requiere gh)
#     ambos     hace las dos cosas
#
#   opciones:
#     -y, --si   no pedir confirmación (para ejecución automática)
#     -h, --help mostrar esta ayuda
#
# EJEMPLOS:
#   ./publicar_soluciones.sh                 # publica en la rama 'soluciones' (pregunta)
#   ./publicar_soluciones.sh rama -y         # rama, sin preguntar
#   ./publicar_soluciones.sh release         # crea un Release con ZIP
#   ./publicar_soluciones.sh ambos -y        # rama + release, sin preguntar
# -----------------------------------------------------------------------------

set -euo pipefail

# ---- Colores ----------------------------------------------------------------
VERDE=$'\033[92m'; ROJO=$'\033[91m'; AMARILLO=$'\033[93m'; AZUL=$'\033[96m'; RESET=$'\033[0m'
ok()    { echo "${VERDE}✅ $*${RESET}"; }
err()   { echo "${ROJO}✗ $*${RESET}" >&2; }
aviso() { echo "${AMARILLO}⚠️  $*${RESET}"; }
info()  { echo "${AZUL}➜ $*${RESET}"; }

# ---- Argumentos -------------------------------------------------------------
METODO="rama"
CONFIRMAR="si"
RAMA_SOLUCIONES="soluciones"

for arg in "$@"; do
  case "$arg" in
    rama|release|ambos) METODO="$arg" ;;
    -y|--si)            CONFIRMAR="no" ;;
    -h|--help)
      sed -n '2,40p' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) err "Opción no reconocida: $arg (usa -h para ayuda)"; exit 1 ;;
  esac
done

# ---- Ubicarse en la raíz del repo ------------------------------------------
cd "$(dirname "$0")"
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  err "Esto no es un repositorio git. Ejecuta el script dentro del repo del taller."
  exit 1
fi
RAIZ="$(git rev-parse --show-toplevel)"
cd "$RAIZ"

# ---- 1) Verificar que existen las soluciones -------------------------------
info "Buscando archivos de soluciones..."
SOLUCIONES=( modulo-*/soluciones.ipynb )
if [ ! -e "${SOLUCIONES[0]}" ]; then
  err "No encontré ningún modulo-*/soluciones.ipynb."
  aviso "Genera las soluciones antes de publicar (deberían estar en cada carpeta de módulo)."
  exit 1
fi
ok "Encontradas ${#SOLUCIONES[@]} solución(es):"
for f in "${SOLUCIONES[@]}"; do echo "     - $f"; done

# ---- 2) (Opcional) Verificar que las soluciones corren ----------------------
# Si hay un Python con las librerías, ejecutamos las soluciones para confirmar
# que pasan antes de publicarlas. Si no se puede, se avisa y se continúa.
verificar_soluciones() {
  local PY=""
  if [ -x ".venv/bin/python" ]; then PY=".venv/bin/python"
  elif command -v python3 >/dev/null 2>&1; then PY="python3"
  else return 2; fi
  if ! "$PY" -c "import nbclient, nbformat, pandas, duckdb, matplotlib" >/dev/null 2>&1; then
    return 2  # faltan librerías -> no podemos verificar
  fi
  info "Verificando que las soluciones corren sin errores..."
  "$PY" - "$@" <<'PY'
import sys, os
import nbformat
from nbclient import NotebookClient
import matplotlib; matplotlib.use("Agg")
fallos = 0
for ruta in sys.argv[1:]:
    nb = nbformat.read(ruta, as_version=4)
    carpeta = os.path.dirname(os.path.abspath(ruta))
    try:
        NotebookClient(nb, timeout=120, kernel_name="python3",
                       resources={"metadata": {"path": carpeta}}).execute()
        print(f"   OK  {ruta}")
    except Exception as e:
        fallos += 1
        print(f"   FALLA {ruta}: {type(e).__name__}")
sys.exit(1 if fallos else 0)
PY
}

if verificar_soluciones "${SOLUCIONES[@]}"; then
  ok "Todas las soluciones corren correctamente."
else
  rc=$?
  if [ "$rc" = "2" ]; then
    aviso "No pude verificar (falta Python o librerías). Continúo sin verificar."
  else
    err "Alguna solución falló al ejecutarse. Revisa antes de publicar."
    exit 1
  fi
fi

# ---- 3) Confirmación --------------------------------------------------------
echo
info "Método de publicación: ${METODO}"
if [ "$CONFIRMAR" = "si" ]; then
  read -r -p "¿Publicar las soluciones ahora? [s/N] " resp
  case "$resp" in
    s|S|si|SI|Si) ;;
    *) aviso "Cancelado. No se publicó nada."; exit 0 ;;
  esac
fi

# ---- 4a) Publicar en la rama 'soluciones' -----------------------------------
publicar_rama() {
  info "Publicando en la rama '${RAMA_SOLUCIONES}'..."

  # Requiere árbol de trabajo limpio (archivos rastreados) para no mezclar cambios
  if ! git diff --quiet || ! git diff --cached --quiet; then
    err "Tienes cambios sin confirmar. Haz commit o stash antes de continuar."
    exit 1
  fi

  local RAMA_ACTUAL; RAMA_ACTUAL="$(git rev-parse --abbrev-ref HEAD)"

  # Recrear la rama desde la actual (idempotente)
  git branch -D "$RAMA_SOLUCIONES" 2>/dev/null || true
  git checkout -q -b "$RAMA_SOLUCIONES"

  # Forzar el alta de las soluciones (están en .gitignore)
  git add -f modulo-*/soluciones.ipynb
  git commit -q -m "Publicar soluciones del taller Python for Ford 2026"

  info "Subiendo la rama al remoto..."
  git push -f -u origin "$RAMA_SOLUCIONES"

  git checkout -q "$RAMA_ACTUAL"
  ok "Soluciones publicadas en la rama '${RAMA_SOLUCIONES}'."
  local URL; URL="$(git remote get-url origin 2>/dev/null | sed 's/\.git$//' | sed 's#git@github.com:#https://github.com/#')"
  [ -n "$URL" ] && echo "     Míralas en: ${URL}/tree/${RAMA_SOLUCIONES}"
}

# ---- 4b) Publicar como GitHub Release (ZIP) ---------------------------------
publicar_release() {
  info "Publicando como GitHub Release (ZIP)..."
  if ! command -v gh >/dev/null 2>&1; then
    err "No está instalado 'gh' (GitHub CLI). Instálalo o usa el método 'rama'."
    aviso "Instalar en Mac:  brew install gh   |  luego:  gh auth login"
    exit 1
  fi

  local FECHA; FECHA="$(date +%Y%m%d)"
  local TAG="soluciones-${FECHA}"
  local ZIP="soluciones_taller_${FECHA}.zip"

  info "Empaquetando soluciones + datos en ${ZIP}..."
  rm -f "$ZIP"
  # ZIP autocontenido: soluciones + datos + requirements para que sea ejecutable
  zip -q -r "$ZIP" modulo-*/soluciones.ipynb datos requirements.txt

  info "Creando el Release '${TAG}'..."
  gh release create "$TAG" "$ZIP" \
    --title "Soluciones del taller (${FECHA})" \
    --notes "Soluciones de los retos del taller Python for Ford 2026. Descarga el ZIP, descomprímelo y ábrelo en VS Code." \
    2>&1 | tail -3

  rm -f "$ZIP"
  ok "Release '${TAG}' publicado con el ZIP de soluciones."
}

case "$METODO" in
  rama)    publicar_rama ;;
  release) publicar_release ;;
  ambos)   publicar_rama; publicar_release ;;
esac

echo
ok "Listo. 🎉  Comparte el enlace de las soluciones con los participantes para la próxima sesión."
