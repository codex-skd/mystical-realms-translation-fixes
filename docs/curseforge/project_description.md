<h1 align="center">&#127760; Mystical Realms Translation &amp; Fixes</h1>

<p align="center"><strong>Companion resource pack for the Mystical Realms modpack &mdash; Spanish (es_ES) translations and small asset fixes for the bundled mods. Drop-in install, nothing patched in the mods themselves.</strong></p>

<br>

---

<br>

<h2>&#10024; Overview</h2>

<p><strong>Mystical Realms Translation &amp; Fixes</strong> is the companion resource pack for the
<strong>Mystical Realms</strong> modpack (Minecraft 1.21.1, NeoForge). It bundles
<strong>Spanish (<code>es_ES</code>) translations</strong> and a few <strong>asset fixes</strong> for
the included mods <strong>without editing the mods themselves</strong>, so everything survives mod
updates and can be served straight from the game server.</p>

<br>

<h2>&#128483;&#65039; Spanish translations</h2>

<p>Adds <code>es_ES</code> language files for <strong>85 mod namespaces</strong> (~12,700 keys) that
either shipped no Spanish locale at all or an incomplete one. Item, block and entity names, tooltips
and GUI text that used to show up in English (or as raw <code>translation.keys</code>) now appear in
Spanish.</p>

<p>Minecraft merges language files across resource packs, so for mods that already had a partial
Spanish translation this pack only fills in the missing keys &mdash; it never overwrites work the mod
authors or their translators already did. Source text is each mod's own <code>en_us.json</code>, and
the machine-translated first pass is being reviewed mod by mod against a fixed Spanish glossary.</p>

<p>Covered mods include Every Compat, Supplementaries, Ars Nouveau, Butchery, Reliquary,
Iron's Spells 'n Spellbooks, BetterEnd, Quark, Create, Farmer's Delight, JEI, Waystones,
Xaero's Minimap / World Map, Macaw's Roofs, Biomes O' Plenty, Deeper and Darker,
L_Ender's Cataclysm, Sophisticated Backpacks, Tom's Simple Storage, Corail Tombstone and dozens more
&mdash; see the changelog for the full per-batch list.</p>

<br>

<h2>&#127919; Asset fixes</h2>

<h3>&#129447; Butchery</h3>
<p>Replaces an orphan <code>ravager_carcass</code> model file that has an illegal element rotation,
which otherwise makes Minecraft's model loader print an <code>ERROR</code> on every startup. Purely a
log-noise fix; no visual change in-game.</p>

<br>

<h2>&#128229; Installation</h2>

<ol>
<li>Bundled with the Mystical Realms modpack &mdash; already installed if you run the pack.</li>
<li>Also served by the official server via <code>server.properties</code>
  (<code>resource-pack</code> + <code>resource-pack-sha1</code>), so it downloads automatically when
  you join.</li>
<li>Standalone: drop <code>MysticalRealms_TranslationFixes-&lt;version&gt;.zip</code> into
  <code>resourcepacks/</code> and enable it in <strong>Options &rarr; Resource Packs</strong>.</li>
<li>Set your game language to <strong>Espa&ntilde;ol (Espa&ntilde;a)</strong> to see the
  translations.</li>
</ol>

<br>

<h2>&#128203; Requirements</h2>

<table>
<tr><td><strong>Minecraft</strong></td><td>1.21.1</td></tr>
<tr><td><strong>Pack format</strong></td><td>34</td></tr>
<tr><td><strong>Loader</strong></td><td>NeoForge 21.1+</td></tr>
<tr><td><strong>Environment</strong></td><td>Client (server-distributable)</td></tr>
</table>

<br>

---

<br>

<h2>&#128591; Credits</h2>

<p>Maintained by <strong>Stalking Dragons</strong>. Translations are derived from each mod's own
English locale. The <em>ravager carcass</em> geometry is the mod author's own corrected model,
redistributed here under the fix.</p>

<br>
<br>

<p align="center">
  <a href="https://codex.skdragons.com/" target="_blank">
    <img src="https://node-files.skdragons.com/uploads/MINECRAFT/Codex/logo_codex_stalking_dragons.png" alt="Codex Stalking Dragons" width="200">
  </a>
  <br>
  <a href="https://codex.skdragons.com/">https://codex.skdragons.com/</a>
  <br>
  <em>Codex Stalking Dragons &mdash; Minecraft Modding</em>
</p>
