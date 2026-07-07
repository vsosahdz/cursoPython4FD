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

## Cómo liberarlas (instructor), después de la sesión de retos

Elige **una** de estas dos opciones:

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
