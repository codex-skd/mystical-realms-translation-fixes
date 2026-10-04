# Flujo de trabajo — Mystical Realms Translation & Fixes (Resource Pack)

> **Versión del workflow**: 1.21.0 (codex-docs)
> Este archivo pertenece al proyecto **Mystical Realms Translation & Fixes**. Cambios aquí solo afectan a este proyecto.
> **Trabaja directamente con este archivo**: es el workflow operativo del resource pack, autocontenido. No leas `codex-docs/WORKFLOW_AGENT.md` ni `WORKFLOW_GENERIC.md` de forma rutinaria.
> On-demand (solo si la tarea lo necesita): `codex-docs/reference/CURSEFORGE.md` (formato HTML al publicar), `codex-docs/reference/GRAPHIFY.md` (backend LLM de Graphify), `codex-docs/reference/REPO_SETUP.md` (setup único de repo), `codex-docs/reference/WIKI.md` (wiki pública del mod — solo si hay que crearla o cambiarla).

## Específico del resource pack

| Dato | Valor |
|---|---|
| Display name (Title Case) | `Mystical Realms Translation & Fixes` |
| Versión de Minecraft | `1.21.1` (NeoForge 21.1.249) |
| Pack format | `34` (`resourcepack/pack.mcmeta`) |
| Rama de trabajo | `minecraft/1.21.1/resourcepack/production` |
| Repositorio | https://gitlab.com/stalking-dragons/minecraft/mystical-realms-translation-fixes.git |
| CurseForge project id | `1679111` |
| Glosario de traducción | `docs/GLOSARIO_ES.md` (ratificado — usarlo siempre) |

## Qué es este proyecto

Resource pack de la modpack Mystical Realms, cargado en cliente (dentro de la modpack) y servido desde el servidor (`resource-pack` + `resource-pack-sha1` en `server.properties`). Contiene:

- **Traducciones `es_es`** de los mods que no traen español o lo traen incompleto (`assets/<mod>/lang/es_es.json`, libros Patchouli, tabla de diálogos de Better Villager Animations). Para mods con `es_es` parcial solo se añaden las claves que faltan.
- **Fixes de assets** de otros mods (modelos/recetas de guía rotos), cada uno inventariado en `NOTICE.md`.

No modifica ningún JAR. Detalle de contenidos en `README.md`.

## Diferencias con un mod NeoForge

| Aspecto | Mod | Resource pack |
|---|---|---|
| Build | `./gradlew.bat clean build` → JAR | `python build_pack.py` → ZIP (valida todos los JSON e imprime el SHA1) |
| Artefacto | `build/libs/<mod_id>-...-<version>.jar` | `build/MysticalRealms_TranslationFixes-<version>.zip` |
| Versión | `mod_version` en `gradle.properties` | `version.txt` (única fuente de verdad) |
| Upload CurseForge | `codex-docs/scripts/curseforge-upload.ps1` | `scripts/curseforge-upload.ps1` propio (lee `version.txt`) |
| docs/curseforge | project_description / project_vars / versions | **idéntica** |

## Estructura del proyecto

`resourcepack/` (contenido real, versionado) · `build_pack.py` · `version.txt` · `scripts/curseforge-upload.ps1` · `NOTICE`/`NOTICE.md` + `LICENSE` · `docs/` (este workflow, `GLOSARIO_ES.md`, snapshots de la modpack, `curseforge/`) · `CHANGELOG.md` · `README.md` · `build/`, `temp/`, `_i18n_work/` (no versionados).

## Versionado

- Beta `0.0.0-beta.X` · Release `X.Y.Z` (SemVer)
- Versión en `version.txt`. ZIP: `MysticalRealms_TranslationFixes-<version>.zip`

## Commits (Conventional Commits)

`<tipo>[<ámbito>]: <descripción>` · tipos `feat fix refactor docs chore style perf test` · el mensaje incluye la versión (`v<version>`).

## Sin tags

**No se crean tags git** (ni en GitLab ni en ningún remoto): apuntan a commits de `production` y el mirror los publicaría con el contenido privado. El commit exacto de cada ZIP es su `chore: bump version to <version>`.

## Flujo por tarea

**0. Alcance** — una sola versión (1.21.1). Si se plantea soporte multi-versión, preguntar con la herramienta `question`: **"Todas"** o una versión. No asumir.

**1. Desarrollo**

```bash
git checkout minecraft/1.21.1/resourcepack/production
python build_pack.py
git add -A
git commit -m "feat(i18n): <descripción>

v<version>"
git push
```

Traducciones: partir siempre del `en_us.json` del propio mod (instancia de la modpack), respetar `docs/GLOSARIO_ES.md` y revisar que no queden claves en inglés ni placeholders rotos (`%s`, `§`). Los lotes grandes se trocean por namespace; el trabajo intermedio va en `_i18n_work/` (no versionado).

**2. CurseForge / servidor** — solo si el usuario confirma:
- Bump `version.txt` → `python build_pack.py` (anotar el SHA1 si se sirve desde el servidor)
- Release notes `docs/curseforge/versions/<version>.md` (HTML) + actualizar `CHANGELOG.md`
- Commit `chore: bump version to <version>` → push (sin tag)
- Subir ZIP: `powershell -File scripts/curseforge-upload.ps1` (desde este repo; si el classifier lo bloquea, replicar con `curl -F` a `/upload-file`)
- Formato HTML de descripciones/changelog: `codex-docs/reference/CURSEFORGE.md`

**3. Release estable** — bump `X.Y.Z` + commit (sin tag).

**4. Graphify** — tras cada push a remoto. Versión 0.9.12: **`build` no existe**, usar `extract` (1ª vez) o `update . --force` (tras cambios):

```bash
GRAPHIFY="C:\Users\llagu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\graphify.exe"
"$GRAPHIFY" extract .              # 1ª vez (si graphify-out/ NO existe)
"$GRAPHIFY" update . --force       # tras cambios
git add graphify-out/ && git commit -m "chore: update knowledge graph" && git push
```

Leer siempre `GRAPH_REPORT.md`, nunca `graph.json`/`graph.html` (pesan >1MB). Sin copias fechadas de `graphify-out/`.

## Buenas prácticas

- Un commit por cambio lógico · commit+push tras cada cambio funcional y de docs
- Todo fix sobre un fichero de otro mod se inventaría en `NOTICE.md`
- `python build_pack.py` antes de subir (valida los JSON) · versionar antes de CurseForge · CHANGELOG al día
- El ZIP resultante debe tener `pack.mcmeta` en la raíz
- Sin basura en repo (`nul`, `*.zip` sueltos en raíz) · `.gitignore` excluye `build/`, `temp/`, `lib_ext/`, `_i18n_work/`, `wiki/`
- **Nunca** subir versiones de dependencias ni borrar ficheros sin que se pida
- README en inglés siempre actualizado

## Idioma

| Ámbito | Idioma |
|---|---|
| código, logs, commits | en-US |
| README.md | en-US |
| Wiki pública (repos de wiki GitHub + GitLab, ver `codex-docs/reference/WIKI.md`) | **Inglés** (en-US) |
| docs internas (docs/, CHANGELOG, este archivo) | es-ES |
| CurseForge | en-US |
| Contenido traducido (`lang/es_es.json`, libros) | es-ES (glosario `docs/GLOSARIO_ES.md`) |
