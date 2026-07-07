# 🔓 Estrategia de liberación de soluciones

Las soluciones de los retos (`modulo-*/soluciones.ipynb`) se **liberan después**
de que los participantes intenten los retos por su cuenta, para que el reto
conserve su valor de aprendizaje.

## Cómo está implementado

En la **publicación inicial** del repositorio, los archivos `soluciones.ipynb`
están **excluidos** vía [`.gitignore`](.gitignore):

```
modulo-*/soluciones.ipynb
```

Esto significa que, al crear el repo público y subir el material, **las
soluciones NO se publican** — aunque existan en la copia local del instructor.

## ✅ Forma recomendada: el script automatizado

Usa **[`publicar_soluciones.sh`](publicar_soluciones.sh)**, que hace todo por ti
(verifica que las soluciones corren y las publica). Lo puede correr el instructor
o cualquier persona con acceso al repo, **después** de la sesión de retos:

```bash
# Publicar en la rama 'soluciones' (por defecto):
./publicar_soluciones.sh

# Sin pedir confirmación (ejecución automática):
./publicar_soluciones.sh rama -y

# Como GitHub Release con un ZIP (requiere gh CLI):
./publicar_soluciones.sh release

# Ver la ayuda:
./publicar_soluciones.sh --help
```

El script: (1) comprueba que existan las soluciones, (2) intenta ejecutarlas para
confirmar que pasan, (3) pide confirmación y (4) las publica por el método elegido.

---

## Cómo liberarlas manualmente (alternativa)

Si prefieres hacerlo a mano, elige **una** de estas dos opciones:

### Opción A — Rama `soluciones` (recomendada para quien usa git)
```bash
git checkout -b soluciones
git add -f modulo-*/soluciones.ipynb   # -f para forzar, ya que están en .gitignore
git commit -m "Publicar soluciones del taller"
git push origin soluciones
```
Los participantes verán las soluciones cambiando de rama a `soluciones` en GitHub.

### Opción B — GitHub Release (recomendada para participantes no técnicos)
1. Comprime la carpeta con las soluciones en un `.zip`.
2. En GitHub: **Releases → Draft a new release**.
3. Adjunta el `.zip` como *asset* y publica.
4. Comparte el enlace del release. Los participantes descargan el ZIP con un clic.

> 💡 La **Opción B** es más amigable para contadores/financieros, porque replica
> el mismo flujo de "Download ZIP" que ya conocen del material principal.

## Nota

El script `datos/generar_datos.py` es reproducible (semilla fija), así que
cualquiera puede regenerar el dataset idéntico. Las soluciones dependen de ese
mismo dataset.
