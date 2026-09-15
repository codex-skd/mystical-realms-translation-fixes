# CurseForge — Variables del proyecto

## Proyecto

| Variable | Valor |
|----------|-------|
| `curseforge_project_id` | `1679111` |
| `slug` | `mystical-realms-translation-fixes` |
| `mod_id` | `mystical_realms_translation_fixes` |
| `display_name` | `Mystical Realms Translation & Fixes` |
| `summary` | `A server-synced companion resource pack for the Mystical Realms modpack: Spanish (es_es) translations for mods that ship no or partial Spanish locale, plus lightweight fixes for broken model, texture and sound assets in bundled mods — without editing the mods themselves.` |
| Categoría (class Resource Packs) | `Data Packs` (no es un pack de resolución) |

> **Renombrado 2026-09-03**: el proyecto pasó de `Mystical Realms Resource Pack` /
> `mystical-realms-reousrce-pack` a `Mystical Realms Translation & Fixes` /
> `mystical-realms-translation-fixes` por políticas de CurseForge (un "resource pack" en CF implica
> pack de texturas/resolución). El `project_id` no cambia. Remote GitLab nuevo:
> `https://gitlab.com/stalking-dragons/minecraft/mystical-realms-translation-fixes.git`.

## Tokens

El API token de CurseForge es **de cuenta**, el mismo que el resto de proyectos de Stalking Dragons
(ver `enchantventure-pack/docs/curseforge/project_vars.md`). No se versiona aquí.

- Autenticación Upload: cabecera `X-Api-Token`
- Autenticación Core (GET): cabecera `x-api-key`

## Versión actual

| Variable | Valor |
|----------|-------|
| `minecraft_version` | `1.21.1` |
| `pack_format` | `34` |
| `environment` | `Client` (se descarga y aplica en el cliente) |

## Rama

```
minecraft/1.21.1/resourcepack/production
```

## Tag

Formato: `<mc-version>-<version>`
Ejemplo: `1.21.1-0.1.0-beta.1`

## Parámetros del upload

| Campo | Valor | Notas |
|-------|-------|-------|
| `displayName` | `Mystical Realms Translation & Fixes (0.1.0-beta.1)` | `display_name (version)` |
| `changelog` | HTML (no Markdown) | `docs/curseforge/versions/<version>.md` |
| `changelogType` | `html` | Obligatorio |
| `releaseType` | `beta` | Según el tipo de versión |
| `gameVersions` | `[11779]` | `gameVersionId` de Minecraft 1.21.1 (no el pack format) |

> `gameVersions` usa el `gameVersionId` de Minecraft (de `GET /v1/minecraft/version`), **no** el pack
> format 34. `11779` = Minecraft 1.21.1, ya validado en `mystical_realms_data_pack` y demás repos 1.21.1
> de Stalking Dragons.

## Estructura del changelog (HTML)

```html
<h2>v0.1.0-beta.1</h2>

<h3>Added</h3>
<ul>
<li><strong>Spanish (es_es) translations</strong> for 101 mod namespaces (~12.5k keys) that shipped no
Spanish locale or an incomplete one. Merged on top of each mod's own lang files.</li>
</ul>

<hr>

<p><strong>ZIP</strong>: <code>MysticalRealms_TranslationFixes-0.1.0-beta.1.zip</code></p>
```

## Variables parseables (para scripts)

El script `scripts/curseforge-upload.ps1` lee estas líneas (`key = value`). Rellenar tras crear el
proyecto:

```
project_id = 1679111
api_token = ee776b0a-ee95-4850-b554-06be02a8657f
game_versions = 11779
release_type = release
```

## Flujo completo

1. `python build_pack.py`
2. Actualizar `docs/curseforge/versions/<version>.md` con HTML
3. Actualizar `CHANGELOG.md`
4. `git commit -m "chore: bump version to <version>"` + `git push`
5. `git tag -a 1.21.1-<version> -m "v<version>: descripción"` + `git push origin <tag>`
6. Subir ZIP a CurseForge con `scripts/curseforge-upload.ps1`
7. Actualizar la URL + SHA1 del server pack en `server.properties` del servidor
8. Verificar con GET que el changelog se vea bien
