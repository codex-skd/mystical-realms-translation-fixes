# Mystical Realms Translation & Fixes

Companion resource pack for the **Mystical Realms** modpack (Minecraft **1.21.1**, NeoForge 21.1.249).

It ships two things for bundled mods **without touching the mods themselves**:

1. **Spanish (`es_es`) translations** for mods that ship no Spanish locale, or an incomplete one — so
   item / block / entity names, tooltips and GUI text show up in Spanish instead of English or raw
   translation keys. Minecraft merges these `lang` files on top of whatever each mod already provides.
2. **Small asset fixes** for broken model / texture / sound files that make Minecraft log errors.

It is meant to be:

- distributed inside the CurseForge modpack (loads client-side), **and**
- served from the game server via `resource-pack` + `resource-pack-sha1` in `server.properties`
  (auto-downloaded by every client on join).

## Contents

### Spanish translations (`assets/<mod>/lang/es_es.json`)

89 mod namespaces, ~15.3k keys. For mods that already ship a partial `es_es`, only the missing keys
are added (Minecraft merges lang files across packs). Source text is each mod's own `en_us.json`.
See `CHANGELOG.md` for the full mod list.

### Asset fixes

| Fix | Path | Why |
|-----|------|-----|
| Butchery — `ravager_carcass` model | `assets/butchery/models/custom/ravager_carcass.json` | Butchery 5.2 ships an orphan model file with an illegal element rotation (`angle: -90`, only ±45/±22.5/0 are valid). Nothing references it, but MC 1.21 bulk-loads every `models/**/*.json` at startup and logs a parse error for it. This replaces it with the mod's own already-fixed sibling model (`custom/ravager_carcas.json`), so the load succeeds and the log stays clean. No in-game visual change. |

## Requirements

- Minecraft **1.21.1** (resource pack format **34**)
- The Mystical Realms modpack (or any subset of the mods it patches / translates)

## Build

Pack content lives under `resourcepack/`. The build script validates every JSON file and zips the
folder with `pack.mcmeta` at the root (loads directly):

```bash
python build_pack.py
# → build/MysticalRealms_TranslationFixes-<version>.zip
# also prints the SHA1 for server.properties (resource-pack-sha1=...)
```

Version is read from `version.txt`.

## Serving from the game server

1. `python build_pack.py`
2. Upload `build/MysticalRealms_TranslationFixes-<version>.zip` somewhere with a stable direct URL
   (GitLab Releases / Pages, or any static host).
3. In `server.properties`:
   ```
   resource-pack=<direct URL to the zip>
   resource-pack-sha1=<sha1 printed by build_pack.py>
   require-resource-pack=true
   ```
4. Restart the server. Bump `version.txt` and the URL each release so clients re-download.

## CurseForge

`scripts/curseforge-upload.ps1` uploads the built ZIP. Fill `docs/curseforge/project_vars.md` first.

Project slug: `mystical-realms-translation-fixes`.

## Branch layout

```
minecraft/1.21.1/resourcepack/production   # working branch (this one)
minecraft/1.21.1/resourcepack/main         # public mirror, synced by CI
```

## License

All Rights Reserved.
