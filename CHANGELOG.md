# Changelog

Todos los cambios notables de Mystical Realms Translation & Fixes se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-09-21

### Añadido

- **Cierre de huecos de traducción tras actualización del modpack**: una auditoría completa
  (comparando el `en_us.json` de cada jar de mod instalado contra el `es_es` propio del mod +
  el de este resourcepack) detectó 155 claves nuevas sin traducir en 13 namespaces, aparecidas
  porque varios mods subieron de versión desde el release 1.0.0 (`bountiful`, `moonlight`,
  `fragmentum`, `sophisticatedcore`, `patchouli`, `xaeroworldmap`, `everycomp`, `yungsapi`,
  `apotheosis`, `aquamirae`, `kaelos_gems`, `supplementaries`, `just_in_nether`). Se añaden 5
  namespaces nuevos al pack (`bountiful`, `fragmentum`, `patchouli`, `yungsapi`, `apotheosis` no
  tenían `es_es.json` propio en este resourcepack todavía) y se completan los 8 restantes.
  Auditoría re-verificada tras el fix: **131/131 namespaces del modpack sin ninguna clave
  pendiente**.

## [1.0.0] - 2026-09-15

### Primera versión estable

Tras 48 betas (2026-09-02 → 2026-09-15) validadas en la instancia de traducción y funcionando
correctamente en el pack, esta versión gradúa el proyecto a **release** estable. Sin cambios de
contenido respecto a beta.48 — mismo `es_es` y mismos fixes de assets, solo cambia el número de
versión y el `releaseType` en CurseForge (`beta` → `release`).

**Alcance actual**: **89 namespaces de mods** con traducción `es_es` (~15.300 claves), más el diálogo
embebido de Better Villager Animations (708 frases) y el fix de modelo de Butchery
(`ravager_carcass`). Historial completo de cada lote en las entradas `0.1.0-beta.*` de más abajo.

## [0.1.0-beta.48] - 2026-09-15

### Añadido

- **3 namespaces nuevos (mods añadidos al modpack desde la 5.134.4)**: el modpack subió de versión
  (5.134.4 → 5.144.21, 164 jars frente a los 158 auditados hasta beta.47) y trajo mods sin traducción
  al español. Se añade `es_es` completo para:
  - **`hexerei`** (mod Hexerei, brujería/folclore: calderos, escobas, familiares, hexes) — 1070 claves.
  - **`apothic_ascension`** (addon de progresión/ascensión para Apotheosis) — 627 claves, terminología
    alineada con `apotheosis`/`apothic_attributes`/`apothic_enchanting` ya traducidos en el pack.
  - **`kaelos_gems`** (gemas nuevas para el sistema de gemas de Apotheosis) — 241 claves.
  - Los otros 4 namespaces nuevos del barrido (`better_connections`, `integrated_cataclysm`,
    `waystone_towers`, `wover-preset`) no aportan texto (`en_us.json` vacío), no necesitan traducción.

## [0.1.0-beta.47] - 2026-09-14

### Añadido

- **Diálogo de aldeanos de Better Villager Animations (708 frases)**: ese mod muestra texto de
  bocadillo sobre los aldeanos (saludos, comentarios ambientales, banter de comercio) que estaba
  completamente en inglés — no son claves de traducción de Minecraft, sino texto embebido en el
  bytecode Java del mod, así que ningún `lang/es_es.json` podía traducirlas. Se añade
  `assets/bettervillageranimations/dialogue/es_es.json`, una tabla de correspondencia inglés→español
  (no un `lang.json` estándar) que consume en tiempo de ejecución un mixin nuevo del mod
  `utility_nexus_fixes` (v1.1.0). Los marcadores de posición del propio mod (`{player}`,
  `{speaker_goods}`, `{speaker_station}`, `{speaker_task}`, `{listener_goods}`,
  `{listener_station}`, `{listener_task}`, `{time}`, `{weather}`) se conservan literalmente en la
  traducción para que el mod los sustituya con normalidad. Solo tiene efecto si
  `utility_nexus_fixes` 1.1.0+ y `Better Villager Animations` están ambos instalados y el idioma del
  cliente es `es_es`; en cualquier otro caso el texto original en inglés se muestra sin cambios.

## [0.1.0-beta.46] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 39: namespaces pequeños en un solo lote**
  (12 namespaces con cambios de un total de 34 revisados).
  - **Balm** (`balm`, 26 claves): Title Case inglés eliminado de las etiquetas `c:*` («Tintes
    Negros» → «Tintes negros», «Lingotes de Hierro» → «Lingotes de hierro»…), *purple* alineado con
    vanilla («Tintes Púrpura» → «Tintes morados») y acentos restaurados en los mensajes de
    desconexión («instalalo» → «instálalo», «version» → «versión», «tu tienes» → «tú tienes»).
  - **Not Enough Crashes** (`notenoughcrashes`, 7 claves): Title Case en las etiquetas de config
    («Capturar Cierres de Inicialización» → «Capturar cierres de inicialización», «Límite de
    Cierres» → «Límite de cierres», «Volver al Menú Principal» → «Volver al menú principal»…).
  - **wover-generator** (`wover-generator`, 10 claves): «del Fin» → «del End», «del Inframundo» →
    «del Nether», «Mundo Superior» → «mundo superior» y los títulos `title.wover.the_end/the_nether`
    a «End»/«Nether».
  - **YUNG's Better End Island** (`betterendisland`, 7 claves): «en el Fin»/«del Fin» → «del End»,
    «Ender Dragón» → «Enderdragón».
  - **Zeta** (`zeta`, 4): Title Case en los botones de config («Guardar Cambios» → «Guardar
    cambios»…, «Sub Categorías» → «Subcategorías»).
  - **Iris/NeOculus** (`iris`, 2): «Espacio de Color» → «Espacio de color», «Distancia de
    Renderizado» → minúsculas a mitad de frase.
  - **lionfishapi** (2), **justenoughbreeding** (2, «Duplicación de Allays» → «…allays»),
    **irons_patreon_lib** (1, «Mesa de Transmogrificación» → «…transmogrificación»),
    **mysticalautomation** (1, «Polvo de Hueso» → «Polvo de hueso» vanilla).

### Notas

- Revisados y ya limpios (sin cambios): `craftingtweaks`, `moogs_structures`, `cucumber`, `fusion`,
  `terrablender`, `mes`, `mns`, `ars_elemental`, `idas`, `integrated_stronghold`, `just_in_nether`,
  `better_party_x_xaeros_world_map`, `farmer_delight_pizza_lovers`, `wishfulrecipes` y 8 namespaces
  de una sola clave (`dangerous`, `jeresources`, `justenoughprofessions`, `mysticalagriculture`,
  `naturescompass`, `supermartijn642corelib`, `villagertradingplus`, `visualworkbench`).
- En `idas`/`integrated_stronghold` «Cama - …» NO es un error: el `en_us` del propio mod escribe
  «Cama» (nombre del artista). Claves y `\n` sin tocar.
- Quedan pendientes de repaso namespaces medianos/grandes que necesitan pasada propia: `butchery`
  (880), `sodium-extra` (342), `modernfix` (155), `spell_power` (147), `bclib` (128),
  `farmers_sandwiches` (96), `aces_spell_utils` (91), `morevillagers` (78), `embeddium` (71),
  `irons_lib` (70) y los `apothic_*` de la snapshot inicial.

## [0.1.0-beta.45] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 38: Macaw's Bridges** (`mcwbridges`, 6 claves,
  todas reescritas).
  - Title Case inglés eliminado de los 6 nombres de bloque de puente de roble pálido («Puente de
    Roble Pálido» → «Puente de roble pálido», etc.).

## [0.1.0-beta.44] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 37: Better Villager Animations**
  (`bettervillageranimations`, 15 claves). Ya estaba limpio; 1 arreglo.
  - *Farmer* «Granjero» → «Agricultor» para concordar con el nombre de profesión de aldeano del
    `es_es` vanilla.

### Notas

- Los otros 12 nombres de profesión ya coincidían exactamente con vanilla (Cartógrafo, Clérigo,
  Albañil, Peletero, Flechero…). Nombre del mod conservado.

## [0.1.0-beta.43] - 2026-09-08

### Eliminado

- **Overlays es_es de 8 mods de Stalking Dragons** cuya traducción ahora vive en el propio mod:
  `vellumli`, `teleport_animation`, `skd_menu`, `data_miner`, `info_tab`, `carry_mechanics`,
  `regalia_slots_api`, `workhand_tools`.
- Este resource pack es para mods de terceros sin es_es o con es_es parcial. Estos 8 son mods
  nuestros — su locale español (con las correcciones del QA aplicadas) se ha commiteado al repo de
  cada mod, así que viaja con el mod y ya no necesita overlay aquí.

### Notas

- Quedan 84 namespaces de terceros. El QA de traducción (betas 6-42) sigue sobre esos.
- Hasta que cada mod afectado publique su próxima build, las claves movidas solo están en el código
  fuente del mod; los locales que ya vienen en el jar no cambian.

## [0.1.0-beta.42] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 36: Sophisticated Core** (`sophisticatedcore`,
  15 claves, 9 reescritas).
  - **Title Case inglés eliminado** de las etiquetas de config y los detalles de botón («Posición
    de Botones de Ordenación» → «Posición de botones de ordenación», «Reproducir Sonido de Botón» →
    «Reproducir sonido de botón», «Debajo de las Pestañas de Mejoras» → «Debajo de las pestañas de
    mejoras», «Fuera = Clic Izquierdo» → «Fuera = clic izquierdo»). *Mouse Tweaks* (nombre de mod)
    conservado.

### Notas

- Claves y todos los `\n` intactos. La descripción de config `enabledItems` se dejó intacta.

## [0.1.0-beta.41] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 35: Relics** (`relics`, 15 claves). Ya estaba
  limpio; 1 arreglo.
  - *Unholiness* «Maldad» → «Impiedad» en la habilidad Fe del Relicario Sagrado, para concordar con
    el `es_es` propio de Relics (que empareja «Santidad / Impiedad»).

### Notas

- Las otras 14 cadenas (descripciones de habilidad, fuentes de nivel, atajos) ya estaban en español
  de España natural con todos los placeholders `%1$s%%` / `%2$s` / `%3$s` correctos.

## [0.1.0-beta.40] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 34: Better Combat** (`bettercombat`, 20 cadenas
  de config). Ya estaba limpio; 1 arreglo.
  - «Formatear Rango de Interacción de Entidad a Rango de Ataque» → «Formatear rango de interacción
    de entidad a rango de ataque» (Title Case).

### Notas

- Las otras 19 etiquetas y tooltips de config ya estaban en español de España natural.

## [0.1.0-beta.39] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 33: Aquaculture** (`aquaculture`, 30 claves, 24
  reescritas).
  - **Title Case inglés eliminado** de los subtítulos de sonido y los tags de objeto, siguiendo el
    estilo vanilla de subtítulos («El Pez nada» → «El pez nada», «La Caja de Pesca se abre» → «La
    caja de pesca se abre», «Soporte de Peces roto» → «Soporte de peces roto», «Lingotes de
    Neptunio» → «Lingotes de neptunio»).
  - «Caja de Pesca Tinte Verde» reescrito a «Tinte verde para caja de pesca».

### Notas

- Claves y placeholders intactos.

## [0.1.0-beta.38] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 32: Aquaculture Delight** (`aquaculturedelight`,
  34 claves, 11 reescritas).
  - **«surullito» → «rollito»** — el MT usó un regionalismo caribeño para *roll*. *Crispy Roll
    Medley* → «Surtido de rollitos crujientes», *Fried Perch Roll* → «Rollito de perca frita», etc.
  - **«Sargo» → «Abadejo»** para *Pollock* (el sargo es otro pez).

### Notas

- Los otros 23 nombres de plato ya estaban en español de España excelente («Perca frita crujiente»,
  «Fletán con salsa tártara», «Chorba de pescado»…). Nombres propios de preparación de pescado
  (Buckling, Rollmops, Halászlé) conservados.
- Claves y todos los códigos `§` intactos.

## [0.1.0-beta.37] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 31: Aquamirae** (`aquamirae`, 31 claves, 18
  reescritas).
  - **«biosomas» → «biomas»** — el MT se inventó una no-palabra para *biomes* en las opciones de la
    estructura Laberinto de Hielo.
  - **Title Case inglés eliminado** de las etiquetas de config, el título de logro y el nombre de
    objeto («Más Allá del Abismo» → «Más allá del abismo», «Probabilidad de Crítico» → «Probabilidad
    de crítico», «Barco Pirata (Estructura)» → «Barco pirata (estructura)», «Espaciado de
    Colocación» → «Espaciado de colocación»).

### Notas

- Los tooltips de lore y las descripciones largas de estructuras ya estaban en español de España
  excelente. Nombres inventados (Shipbreaker → «Rompebarcos», Capitán Cornelia) conservados.
- Claves y todos los `%s` / código `§` intactos.

## [0.1.0-beta.36] - 2026-09-08

### Eliminado

- **Carpetas de locale es_es de 12 mods que ya no están en el modpack Mystical Realms**:
  `arssophisticatedcompat`, `ascendant_spawners`, `caravans`, `common_toolkit`, `configured`,
  `guardvillagers`, `horde_hoard`, `inventoryessentials`, `mowzies_cataclysm`, `mowziesmobs`,
  `obscure_tooltips`, `player_activity_view`.
- Venían arrastradas de la auditoría de beta.1. Minecraft ignora los `lang` de namespaces sin mod,
  así que en el juego no cambia nada — solo quita ~350 claves sin uso y mantiene el repo honesto.

### Notas

- Los 93 namespaces restantes se verificaron contra los jars del modpack actual. El QA de
  traducción por tandas (betas 6-35) sigue sobre los namespaces vivos.

## [0.1.0-beta.35] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 30: Guard Villagers** (`guardvillagers`, 59
  cadenas de config, 32 reescritas).
  - **Tildes restauradas en todo el archivo** — la config entera las había perdido: «clerigos» →
    «clérigos», «heroe» → «héroe», «reputacion» → «reputación», «funcion» → «función»,
    «conversion / reparacion / curacion», «minima», «dia», «Angulo», «bebes», «estan», «hara»,
    «Que tan» → «Qué tan».
  - **Signos de apertura `¿` añadidos** a las preguntas sí/no de config que solo tenían el `?` de
    cierre.
  - **Illagers:** «Illagers» en minúscula a media frase.

### Notas

- Claves y todos los `%s` intactos.
- Arreglado por script; verificado con script (0 palabras comunes sin tilde restantes).

## [0.1.0-beta.34] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 29: Bookshelf** (`bookshelf`, 208 claves, 125
  reescritas).
  - **Restos en inglés traducidos:** las entradas de comentario de sección («Names of the months» →
    «Nombres de los meses», «The names of different moon phases…» → «Los nombres de las distintas
    fases lunares…», «Command Text» → «Texto de comandos», etc.).
  - **Illagers (glosario):** «Alfabeto de los Pillagers» → «Alfabeto illager»; «por los pillagers» →
    «por los illagers»; «Avanposto de Pillagers» → «Puesto de avanzada saqueador» (además «Avanposto»
    no era ni español).
  - **Title Case inglés eliminado** de los nombres de tabla de botín, fases lunares, nombres de día
    / mes y etiquetas de pestaña de creativo («Luna Llena» → «Luna llena», «Ruina Oceánica - Fría» →
    «Ruina oceánica - fría», «Pestaña de Bloques de Color» → «Pestaña de bloques de color»). *Templo
    de la Selva* → *Templo de la jungla* (vanilla).

### Notas

- Claves y todos los `%s` intactos. La pasada de sentence-case protegió la letra tras `¿`/`¡`.

## [0.1.0-beta.33] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 28: Tom's Simple Storage** (`toms_storage`, 217
  claves, 119 reescritas).
  - **Title Case inglés eliminado** de los nombres de bloque / objeto y sus tooltips — eran 96 de
    las cadenas («Conector de Inventario» → «Conector de inventario», «Terminal de Almacenamiento» →
    «Terminal de almacenamiento», «Tolva Básica de Inventario» → «Tolva básica de inventario»,
    «Configurando Bloque: %s» → «Configurando bloque: %s»).

### Notas

- Claves y todos los `%s` intactos. El nombre del mod *Tom's Simple Storage* conservado.
- Normalizado por script; integridad de claves, placeholders y Title Case residual verificados con
  script.

## [0.1.0-beta.32] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 27: Moonlight Lib** (`moonlight`, 239 claves, 100
  reescritas).
  - **Title Case inglés eliminado** de las etiquetas de la pantalla de config y las opciones de
    depuración «test» («Mods Configurables» → «Mods configurables», «Selector de Color» → «Selector
    de color», «Control Deslizante Doble de Prueba» → «Control deslizante doble de prueba», «Discord
    del Mod» → «Discord del mod»).
  - **«Youtube» → «YouTube».** Nombres de marca (Twitter, Discord, Patreon, CurseForge, Modrinth)
    conservados.

### Notas

- La pasada de sentence-case también protegió la letra tras `¿`/`¡` y el emoticono `:D`.
- Claves y todos los `%s` / `%1$s` intactos.

## [0.1.0-beta.31] - 2026-09-08

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 26: Dawn of Time** (`dawnoftimebuilder`, 275
  claves). Ya estaba limpio; 3 arreglos.
  - El nombre del mod *Dawn of Time* estaba traducido como «Amanecer del Tiempo» en el objeto
    insignia, el título del logro raíz y su descripción → revertido a «Dawn of Time» para concordar
    con el `es_es` propio del mod (que lo deja sin traducir).

### Notas

- Los 200 nombres de bloque ya estaban en español de España natural («Escaleras de tapial y
  enlucido blanco», «Columna de piedra revocada amarilla»…). Nombres propios (Puuc, la Gran
  Muralla, General Kenoblocki, Marte, Roma, Quetzalcóatl) conservados.
- Claves y placeholders intactos.

## [0.1.0-beta.30] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 25: Enchantment Descriptions** (`enchdesc`, 151
  claves). Ya estaba limpio; 3 arreglos.
  - «Selector de Bloques» → «Selector de bloques» y «Gancho de Agarre» → «Gancho de agarre» dentro
    de descripciones de encantamiento.
  - «JEI Compat» → «Compatibilidad con JEI».

### Notas

- Las 148 frases de descripción de encantamiento ya estaban en español de España natural. Líneas de
  crédito de mods con URL conservadas literalmente.
- Claves y placeholders intactos.

## [0.1.0-beta.29] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 24: Armor of the Ages** (`armoroftheages`, 161
  claves, 101 reescritas).
  - **Title Case inglés eliminado** de las 134 etiquetas de opción de config («Durabilidad del
    Sombrero de Bambú» → «Durabilidad del sombrero de bambú», «Defensa de Casco de Placa de Hierro»
    → «Defensa de casco de placa de hierro», «Tipo de Cuerpo» → «Tipo de cuerpo») y los 27 nombres
    de bonus de conjunto («Mariposa Nocturna» → «Mariposa nocturna», «Hombre de Acero» → «Hombre de
    acero»).
  - Nombres de armadura japonesa *O-Yoroi* y *Do-Maru* conservados intactos (la pasada de
    sentence-case había bajado la «Do»).

### Notas

- Claves y todos los `%s` / código `§` intactos. Nombres propios de conjunto (O-Yoroi, Do-Maru,
  Aurum Exaltado, Faraón, Centurión) y la leyenda de colores de nivel de material en la cabecera de
  la config conservados.
- Normalizado por script; verificado con script.

## [0.1.0-beta.28] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 23: L_Ender's Cataclysm** (`cataclysm`, 61
  claves, 16 reescritas). Casi todo son subtítulos, que ya estaban bien.
  - **Nombres de jefe / mob alineados con el `es_es` propio de Cataclysm:** *Ancient / Modern
    Remnant* estaba como «Resto Antiguo / Moderno» → «Remanente Antiguo / moderno»; el subtítulo de
    *Coral Golem* «El Gólem de Coral» → «El gólem de coral» (concuerda con el nombre de la entidad).
  - **Resto en inglés:** «Aparecen Halberds Fantasma» → «Aparecen alabardas fantasma».
  - **Title Case:** «Cerca de Obsidiana» → «Cerca de obsidiana», «Monstruosidad de Netherita
    Antigua» → «Monstruosidad de netherita antigua», «Cúmulo de Amatista» → «Cúmulo de amatista»,
    «Comprobar Enlace» → «Comprobar enlace», y las cadenas del aviso de MakeShip.

### Notas

- Claves y todos los `%s` intactos. Nombres de criatura nórdicos (Draugr, Aptrgangr) y de jefe
  (Maledictus, Ignis, Ceraunus) conservados.
- Arreglado por script; verificado con script.

## [0.1.0-beta.27] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 22: Corail Tombstone** (`tombstone`, 72 claves,
  19 reescritas).
  - **Tildes restauradas:** «Lampara» → «Lámpara», «melodia» → «melodía», «ningun» → «ningún»,
    «Vinculo» → «Vínculo».
  - **Title Case inglés eliminado** de nombres de objeto / perk / efecto / logro / config («Cetro
    de Hueso» → «Cetro de hueso», «Rito de Remanencia» → «Rito de remanencia», «Escalar Pantallas
    de Interfaz» → «Escalar pantallas de interfaz»). Nombres propios (Sarheed, Erdos, Nour)
    conservados.
  - Dos mensajes de «necesitas encontrar todas las partes de…» tenían el título de pergamino en
    minúscula → restaurados a «Noches de Nour» / «Fragmentos de Erdos».

### Notas

- Claves y todos los `%s` intactos.
- Arreglado por script + a mano; verificado con script.

## [0.1.0-beta.26] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 21: Sophisticated Backpacks**
  (`sophisticatedbackpacks`, 149 claves, 129 reescritas).
  - **Title Case inglés eliminado** — eran 124 de las 149 cadenas, casi todo el archivo: nombres de
    mejora, etiquetas de GUI, etiquetas de config y los objetos de conversión de mejora de pila
    («Conversión de Mejora de Pila: Nivel Inicial a Nivel 1» → «Conversión de mejora de pila: nivel
    inicial a nivel 1», «Ranuras por Fila» → «Ranuras por fila», «Objetos No Permitidos» → «Objetos
    no permitidos»).
  - «Mobs» en minúscula a media frase («captura de mobs»); «de la Netherita» → «de netherita».

### Notas

- Claves y todos los `%s` intactos. Las frases de estado / tooltip ya estaban bien.
- Normalizado por script; integridad de claves, placeholders y Title Case residual verificados con
  script.

## [0.1.0-beta.25] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 20: Deeper Darker** (`deeperdarker`, 136 claves).
  Ya estaba limpio; un único arreglo.
  - «Transmisor de sculk púrpura» → «Transmisor de sculk morado» (nombre de color vanilla).

### Notas

- Comprobado contra el `es_es` propio de Deeper Darker: *Resonarium* → «resonario», *sculk* en
  minúscula, *warden* conservado — todo ya consistente. *Block of Lite* es un nombre de broma
  intencional y se mantiene.
- Claves y placeholders intactos.

## [0.1.0-beta.24] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 19: Jade** (`jade`, 105 claves). Ya estaba
  limpio; un único arreglo.
  - «Forma: Punto» → «Forma: punto» (Title Case).

### Notas

- Las 60 cadenas de accesibilidad / lector de pantalla («Cerrado %s», «Encendido %s»…) se revisaron
  y se dejaron con el estado primero, que coincide con el inglés y evita problemas de concordancia
  de género con el nombre de bloque sustituido.
- Claves y placeholders intactos.

## [0.1.0-beta.23] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 18: Biomes O' Plenty** (`biomesoplenty`, 119
  claves). El MT estaba bien en su mayoría; 20 cadenas tocadas.
  - **Término vanilla:** *End* estaba como «Fin» en los nombres de bioma y bloques temáticos del
    End — «Corrupción del Fin» → «Corrupción del End», «Arrecife del Fin» → «Arrecife del End»,
    «Floración del Fin» → «Floración del End», «Piedra del Fin algal» → «Piedra del End algal».
    *End Wilds* → «Tierras salvajes del End».
  - **Término vanilla:** *Sign* estaba como «Señal» en los bloques de cartel empíreo / de arce / de
    pino → «Cartel» (es_es vanilla), con el género del adjetivo y *Wall Sign* → «Cartel de pared»
    corregidos para concordar.

### Notas

- Claves y todos los códigos `§` intactos. El resto de nombres de bloque del set de madera ya
  estaban bien (la concordancia «empíreo/empírea» era correcta). Nombre de disco de música
  conservado.
- Verificado con script: integridad de claves, placeholders, Title Case residual.

## [0.1.0-beta.22] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 17: Just Enough Items** (`jei`, 188 claves, 89
  reescritas).
  - **Title Case inglés eliminado** de las etiquetas de config y nombres de atajo que son casi todo
    el archivo («Siguiente Receta» → «Siguiente receta», «Mostrar Marcadores de JEI» → «Mostrar
    marcadores de JEI», «Cerrar GUI de Recetas» → «Cerrar GUI de recetas», «Alineación Vertical» →
    «Alineación vertical»). *JEI* y *GUI* en mayúscula.
  - **«Trampear»:** los atajos de modo trampa «Trampear 1 Objeto / Pila» → «Hacer trampa con 1
    objeto / pila».

### Notas

- Claves y todos los `%s` intactos. Las descripciones de opciones de config ya estaban bien.
  Atajos en mayúsculas (RIGHT-CLICK → CLIC DERECHO) conservados.
- Normalizado por script; integridad de claves, placeholders y Title Case residual verificados con
  script.

## [0.1.0-beta.21] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 16: BetterEnd** (`betterend`, 367 claves, 131
  reescritas).
  - **Nombres de materiales inventados alineados con el `es_es` propio de BetterEnd** para que
    bloques y objetos concuerden entre menús: *Aeternium* → «Aeternio», *Terminite* → «Terminita»,
    *Thallasium* → «Talismanio», *Violecite* → «Violecita», *Flavolite* → «Flavolita»,
    *Pythadendron* → «Fitadendrón», *Hydralux* → «Hidrálux».
  - **Término vanilla:** *End Stone* estaba como «piedra del Fin» → «piedra del End»; «Herrero del
    Fin» → «Herrero del End»; «un mejor Fin» → «un mejor End».
  - **Title Case inglés eliminado** de nombres de bloque / objeto / logro, manteniendo en mayúscula
    el nombre del mod *BetterEnd* y los nombres de material inventados.

### Notas

- Claves y todos los `%s` / `\n` intactos. Nombres de discos de música (noqwww — …) conservados.
  El locale propio de BetterEnd es también una traducción automática tosca; solo se alinearon los
  términos de material recurrentes, el resto se dejó en español de España con minúscula de frase.
- Verificado con script: integridad de claves, placeholders, Title Case residual, consistencia de
  términos.

## [0.1.0-beta.20] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 15: Xaero's Better PvP** (`xaerobetterpvp`, 17
  claves). Solo 3 cadenas necesitaban retoque.
  - «Mejor Sprint» → «Mejor sprint» (Title Case).
  - «Objeto mano principal» / «Objeto mano secundaria» → «Objeto de mano principal» / «Objeto de
    mano secundaria» (preposición que faltaba).

### Notas

- Las otras 14 etiquetas de GUI ya estaban correctas. Con esto se cierra la familia Xaero (Minimap,
  World Map, Better PvP).

## [0.1.0-beta.19] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 14: Xaero's World Map** (`xaeroworldmap`, 317
  claves). Como el minimapa, ya estaba bien; solo 20 cadenas tocadas.
  - **Término de waypoint unificado:** el MT mezclaba «punto de referencia» (28×) con la abreviatura
    «PxR» (16×). Todas las «PxR» expandidas, con el plural corregido donde hacía falta («fondos de
    puntos de referencia», «puntos de referencia locales»).
  - **Title Case:** «Abrir Mapa del Mundo» → «Abrir mapa del mundo»; «Ajustes del Mapa del Mundo de
    Xaero» → «Ajustes del mapa del mundo de Xaero»; «(Teletransporte) Deshabilitado» →
    «(Teletransporte) deshabilitado».

### Notas

- Claves y todos los `%s` / `%1$d` / código `§` / `\n` intactos. El resto de la UI ya estaba en
  español de España natural.
- Verificado con script: integridad de claves, placeholders, consistencia de términos, Title Case
  residual.

## [0.1.0-beta.18] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 13: Xaero's Minimap** (`xaerominimap`, 522
  claves). Ya estaba bien; solo 35 cadenas tocadas.
  - **Término de waypoint unificado:** el MT mezclaba «punto de referencia» (60×) con la
    abreviatura «PxR» (27×). Todas las «PxR» expandidas a «punto(s) de referencia», con el plural
    corregido donde la abreviatura era plural.
  - **Término de Waystones (glosario):** «piedra(s) de camino» → «Waystone(s)» en las opciones de
    auto-mostrado de la compat con Waystones y en el nombre por defecto de waypoint.
  - **Title Case:** «Eliminar Mundo/Servidor» → «Eliminar mundo/servidor»; «Rastreado (ej.
    Grupo/Aliados)» → «Rastreado (ej. grupo/aliados)».

### Notas

- Claves y todos los `%1$s` / código `§` / `\n` intactos. El resto de la UI de ajustes ya estaba
  en español de España natural y se dejó sin tocar.
- Verificado con script: integridad de claves, placeholders, consistencia de términos, Title Case
  residual.

## [0.1.0-beta.17] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 12: Farmer's Delight** (`farmersdelight`, 193
  claves, 139 reescritas).
  - **Title Case inglés eliminado** de nombres de bloque, tags de objeto, etiquetas de config y
    subtítulos («Cosechas de Cebolla» → «Cosechas de cebolla», «Salmón Crudo» → «Salmón crudo»,
    «Probabilidad de Impulso de Tierra Fértil» → «Probabilidad de impulso de tierra fértil»).
    Términos de mecánicas del mod en minúscula en la prosa de config («la Olla de Cocina», «la
    Parra de Tomate», «el Mercader Errante»).
  - **Término vanilla:** *Sign* estaba como «Señal» en todos los bloques de cartel de lienzo →
    corregido a «Cartel» (es_es vanilla) para los ~40 carteles de pared / colgantes.
  - **MT literal:** «pozos de botín» (loot pools) → «grupos de botín».

### Notas

- Claves y todos los `%s` / `\n` / código `§l` intactos. Las descripciones de config ya estaban
  bien y se dejaron salvo el casing de términos.
- Normalizado por script (casing + terminología); integridad de claves, placeholders y Title Case
  residual verificados con script.

## [0.1.0-beta.16] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 11: Create** (`create`, 178 claves, 141
  reescritas).
  - **Title Case inglés eliminado** de las etiquetas de tag de objeto comunes que son casi todo el
    archivo («Lingotes de Aluminio» → «Lingotes de aluminio», «Bloques de Almacenamiento de Azogue»
    → «Bloques de almacenamiento de azogue», «No Erguidos en Cintas» → «No erguidos en cintas»).
  - **«Raw ... ores»:** «Minerales de Uranio Brutos» → «Minerales de uranio en bruto».
  - **Terminología alineada con el `es_es` propio de Create:** *Stock Keeper* (que el MT dejó en
    inglés) → «Encargado del almacén»; *Recipe Viewer* → «visor de recetas» en las descripciones de
    sincronización con JEI.
  - El nombre del mod *Create* se mantiene en mayúscula («Lingotes de Create»).

### Notas

- Claves y todos los `%1$s` / `\n` intactos; las cadenas vacías de las herramientas de esquema se
  dejan vacías. Nombres de teclas modificadoras (Alt, Ctrl, Shift) conservados.
- Nombres normalizados por script (casing + terminología); las pocas descripciones de GUI
  comprobadas contra el inglés y el locale español propio de Create. Integridad de claves,
  placeholders y Title Case residual verificados con script.

## [0.1.0-beta.15] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 10: Quark** (`quark`, 324 claves, 214 reescritas).
  - **Title Case inglés eliminado** en todos los nombres de bloque, objeto, etiquetas de pestaña y
    colores de runa (~114 de las 324 cadenas): «Cofre de Botín de Roble Oscuro» → «Cofre de botín
    de roble oscuro», «Lámpara de Corindón Negro» → «Lámpara de corindón negro», «Grabado Rúnico
    Azul Claro» → «Grabado rúnico azul claro».
  - **Terminología vanilla:** «del Inframundo» → «del Nether» / «ladrillos del Nether»; «Purpura» →
    «purpur»; «Selva» → «jungla»; «fruta chorus» → «fruta de coro»; «púrpura» → «morado»;
    «Plantilla de Herrero» → «Plantilla de herrería»; «Enderdragón».
  - **Texto de pistas de JEI** pulido a español de España fluido (comas/puntos y coma en listas,
    MT forzado reescrito).

### Notas

- Claves y todos los `%s` / `\n` intactos. Nombres de autor (AmyMialee, DJBaphomet, Shiba) y la
  criatura *Oretoise* se mantienen; `itemGroup` sigue «Quark».
- Pasada en dos trozos con OpenCode (MiMo-V2.5 para el texto de pistas) más normalización de
  casing/terminología por script para los nombres de bloque y objeto; integridad de claves,
  placeholders y Title Case residual verificados con script tras el merge.

## [0.1.0-beta.14] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 9: Iron's Spells 'n Spellbooks**
  (`irons_spellbooks`, 475 claves, 275 reescritas).
  - **Title Case inglés eliminado** en todos los nombres de objeto, conjuntos de armadura,
    etiquetas de hechizo/UI y logros («Botas de Batallamago de Netherita» → «Botas de batallamago
    de netherita», «Mejora Menor de Ranura de Hechizo» → «Mejora menor de ranura de hechizo»).
  - **Terminología (glosario §2.3):** unificado *Spellbook* → «Libro de hechizos», *Scroll* →
    «Pergamino», *Rune* / *Runestone* → «Runa» / «Piedra rúnica», *Upgrade Orb* → «Orbe de
    mejora». Varas según regla V1 (*Cane* → «bastón»: «Bastón del artificiero»).
  - **Términos vanilla:** deepslate / blackstone → «pizarra profunda» / «piedra negra»;
    *ender magic* → «magia del End».
  - **Mensajes de muerte y texto de libros:** ya estaban bien en su mayoría; solo retoques de
    gramática («Primero Portador» → «Primer Portador»; títulos de capítulo a minúscula). El orden
    víctima/asesino de `%1$s` / `%2$s` se conserva.

### Notas

- Claves y todos los `%s` / `%1$s` / `\n` intactos. `itemGroup` se mantiene «Iron's Spellbooks»
  (marca).
- Pasada en dos trozos con OpenCode (MiMo-V2.5) más un pequeño repaso manual de los mensajes de
  muerte y el texto de diarios; integridad de claves y placeholders verificados con script tras
  el merge.

## [0.1.0-beta.13] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 8: Reliquary** (`reliquary`, 551 claves, 350
  reescritas).
  - **Title Case inglés eliminado** en todos los nombres de objeto/bloque, etiquetas de config y
    entradas de JEI («Radio de Explosión» → «Radio de explosión», «Disparo de Exorcismo» → «Disparo
    de exorcismo»). Nombres propios de mob en mayúscula (Blaze, Ender, Creeper, Ghast, Slime).
  - **Varas mágicas (regla V1):** el MT usaba «bastón» para todo. Ahora *Staff* → «báculo»
    (piromante / Ender / glacial / serpiente / viajero), *Rod* → «vara» (Ice Magus Rod, vara de
    cosecha, vara de Lyssa).
  - **Terminología (glosario §2.4):** «Piedra de Tocar de Midas» → «Piedra de toque de Midas»;
    «Viento Desgarrador» → «Vendaval desgarrador»; «Granada Santa» → «Granada de mano sagrada».
    *Alkahestry* / *Alkahest* se mantienen sin traducir.
  - **Términos vanilla:** «Inframundo» → «Nether»; «nether wart» (en inglés) → «fruto del Nether»;
    «Nether Stars» → «Estrellas del Nether»; *redstone* / *glowstone* en minúscula en prosa.
  - MT literal: serpent staff «renderizado» → «aturdido»; sojourner staff «almacén» → «soporte».

### Notas

- Claves y todos los `%s` / `\n` intactos. `itemGroup.reliquary` se mantiene «Reliquary» (marca).
- Pasada en tres trozos con OpenCode (MiMo-V2.5) más normalización de casing/terminología por
  script; integridad de claves, placeholders y restos de inglés/Title Case verificados con script
  tras el merge.

## [0.1.0-beta.12] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 7: últimos add-ons de Ars Nouveau**
  (`ars_creo`, `ars_elemental`).
  - **Ars Creo** (8 de 18 cadenas): tildes restauradas en las páginas de guía («visualizacion» →
    «visualización», «aumentara» → «aumentará», «tuberias» → «tuberías», «Basica» → «básica»);
    Title Case inglés eliminado («Torreta de Hechizos» → «Torreta de hechizos», «Cantidad de
    Fuente» → «Cantidad de fuente», «Tanque de Fluidos» → «Tanque de fluidos»); el párrafo
    `page.behaviors` reescrito en español fluido.
  - **Ars Elemental**: revisado — su única cadena (descripción del encantamiento *soulbound*) ya
    era correcta; sin cambios.

### Notas

- Claves y placeholders `%s` intactos. `itemGroup.ars_creo.general` se mantiene «Ars Creo» (marca).
- Lote lo bastante pequeño para arreglarlo y verificarlo a mano contra el `en_us` y
  `docs/GLOSARIO_ES.md`.

## [0.1.0-beta.11] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 6: Ars Nouveau — Additions** (`ars_additions`,
  235 claves, 139 reescritas).
  - **Title Case inglés eliminado** de todos los nombres de bloque, objeto y tooltip («Piedra de
    Fuente Pulida Agrietada» → «Piedra de fuente pulida agrietada»; «Muro de Piedra de Fuente» →
    «Muro de piedra de fuente»), con el orden de adjetivo español restaurado («Grandes Ladrillos»
    → «ladrillos grandes»).
  - **«Warp» unificado a «traslado»** (glosario): el MT mezclaba «teletransporte» — ahora *Warp
    Portal* → «portal de traslado», *Warp Scroll* → «pergamino de traslado», etc.
  - **Terminología (glosario §2.2):** *Sourcestone* → «piedra de fuente» (minúscula, consistente);
    *Archwood* nunca «arcano»; el glifo *Recall* → «Retorno». *Scribes Table* se mantiene «Mesa de
    Escriba» (acorde al locale del propio Ars Nouveau).
  - **MT literal arreglado:** «maná worth» → «100 maná»; «pool» → «reserva»; «carga chunks
    forzadamente» → «fuerza la carga de los chunks cercanos»; «Antiguo Mago» → «mago antiguo».
    Registro a español de España («coste», no «costo»).

### Notas

- Claves y todos los `%s` / `%d` intactos. Nombres propios en mayúscula (Nexus, End, Archwood,
  Magebloom, Wilden, Starbuncle, Nether).
- Pasada con OpenCode (LongCat-2.0, en sustitución de MiMo-V2.5) contra `docs/GLOSARIO_ES.md` y el
  `es_es` vanilla 1.21.1; integridad de claves, placeholders y Title Case residual verificados con
  script.

## [0.1.0-beta.10] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 5: Ars Nouveau** (`ars_nouveau`, 921 claves).
  255 cadenas arregladas; el grueso es el selector de sonidos/partículas.
  - **Etiquetas de sonido y partícula (219 cadenas) reescritas.** El MT había producido ensalada
    literal para la config de sonidos/partículas de Ars Nouveau («Bloque de Amatista Romper»,
    «Harified de Hueso Usar», «Popped de Carga Sculk»). Ahora son frases naturales con el orden de
    palabras correcto («Romper bloque de amatista», «Usar harina de huesos», «Estallido de carga de
    sculk»), nombres de mob vanilla y minúscula de frase.
  - **Terminología (glosario §2.2):** *Archwood* estaba como «Madera Arcana» / «Bosque Arcano» en
    bloques, objetos y el libro guía → se mantiene *Archwood* / «bosque de Archwood».
  - **Términos vanilla:** *Brewing Stand* sin traducir en dos alias → «Soporte para pociones»;
    «Toque de Seda» → «Toque de seda» en ~22 descripciones de aumento.
  - Menores: «Conversión Alakarkinos» → «Conversión de Alakarkinos»; «Hacia la LUNA» → «Hacia la
    luna»; algún arreglo de mayúscula a media frase.

### Notas

- Claves y todos los `%s` intactos; las descripciones de aumento y casi todo el texto de tomos y
  páginas ya estaban bien. La capitalización de los *nombres* de bloque/objeto se deja acorde al
  estilo del propio `es_es` de Ars Nouveau (que los pone en Title Case).
- Pasada en tres trozos (sonido/partícula, descripciones de aumento, tomos y varios) con OpenCode
  (MiMo-V2.5) contra `docs/GLOSARIO_ES.md` y el `es_es` vanilla 1.21.1; integridad de claves y
  placeholders verificados con script tras el merge.

## [0.1.0-beta.9] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 4: Supplementaries** (`supplementaries`, 1055
  claves). El MT estaba bien en general; 64 cadenas arregladas.
  - **Illagers:** «pillager / pillagers» sin traducir → «saqueador / saqueadores» (opciones de IA
    y sus descripciones).
  - **Términos vanilla:** *blackstone* / *deepslate* → «piedra negra» / «pizarra profunda»;
    *The End* «el Fin» → «el End»; colores a vanilla («púrpura» → «morado», «verde lima» → «lima»),
    incluidas las 16 banderas Carga de dragón («Dragón negro» → «Carga de dragón negro», acorde con
    el nombre vanilla de las banderas).
  - **Capitalización:** minúscula/mayúscula de frase restaurada donde la descripción empieza tras
    salto de línea o `¿`. Etiqueta de pestaña unificada a «Pestaña de creativo».
  - **MT erróneo o forzado:** «Palo de palo» → «Mástil»; «Lluvia lava ceniza» → «La lluvia lava la
    ceniza»; «caer en libre» → «caída libre»; «Sopla burbujas» → «Soplador de burbujas»;
    preposiciones que faltaban en los nombres de barco/balsa con cañón; algún arreglo de subjuntivo
    y concordancia; la clave de configuración de broma traducida.

### Notas

- Claves y todos los `%s` / `%d` / `\n` intactos; 991 cadenas ya estaban bien.
- Pasada en tres trozos (config x2, resto) con OpenCode (MiMo-V2.5) contra `docs/GLOSARIO_ES.md` y
  el `es_es` vanilla 1.21.1; integridad de claves, placeholders y restos en inglés verificados con
  script tras el merge.

## [0.1.0-beta.8] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 3: Every Compat** (`everycomp`, 1179 claves).
  El `es_es` de este namespace estaba bien en general; solo 29 cadenas necesitaban arreglo.
  - **Palabras inventadas:** «rejerada / rejerado» (no existe, de *barred*) → «enrejada / enrejado»
    en todas las puertas, trampillas y cristales con barrotes de Chipped y Macaw's; «waffle» →
    «gofre»; «Tronso» (errata) → «Tronco».
  - **Restos en inglés traducidos:** los nombres de madera/hojas del árbol *blossom* de Quark
    (*Trumpet*, *Frosty / Serene / Warm / Sweet / Sunny / Fiery Trumpet*) → «Trompeta», «Trompeta
    gélida / serena / cálida / dulce / soleada / ardiente»; *Trellis* → «Celosía».
  - **Términos vanilla:** *blackstone* / *deepslate* sin traducir en dos encimeras → «piedra negra»
    / «pizarra profunda».
  - Correcciones menores de gramática en tres descripciones de configuración y en la pantalla de
    error de carga; concordancia («Tablones trenzado» → «trenzados»).

### Notas

- Claves y todos los `%s` intactos; 1150 cadenas ya estaban bien. `itemGroup.everycomp` se mantiene
  «Every Compat» (marca).
- Pasada en tres trozos con OpenCode (MiMo-V2.5) contra `docs/GLOSARIO_ES.md` y el `es_es` vanilla
  1.21.1; integridad de claves, placeholders, Title Case residual y restos en inglés verificados
  con script tras el merge.

## [0.1.0-beta.7] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 2: Macaw's Roofs** (`mcwroofs`, 606 de 610
  cadenas reescritas).
  - **Eliminado el *Title Case* inglés** de todos los nombres de bloque y objeto («Techo de Ático
    de Roble» → «Techo de ático de roble»). Era el defecto dominante de este namespace: casi todo
    el archivo.
  - **Nombres de madera y material alineados con el `es_es` vanilla**: *spruce* «picea» → «abeto»;
    *warped* «retorcido» → «distorsionado»; *Blackstone* «Negroita» → «piedra negra»; *cobblestone*
    «adoquín» → «roca»; además *cherry*, *bamboo*, *crimson*, *dark oak*, *deepslate*.
  - **Vocabulario de tejado consistente** en todo el archivo: *attic* → «de ático», *top* →
    «superior», *lower* → «inferior», *steep* → «empinado», *Roofing Hammer* → «Martillo de tejador».
  - Correcciones menores de concordancia de género en las losas de techo de color.

### Notas

- Claves y placeholders intactos; solo valores. 4 cadenas ya estaban bien. `itemGroup.mcwroofs`
  se mantiene «Macaw's Roofs» (marca).
- Pasada con OpenCode (MiMo-V2.5) contra `docs/GLOSARIO_ES.md` y el `es_es` vanilla 1.21.1;
  integridad de claves, placeholders y Title Case residual verificados con script.

## [0.1.0-beta.6] - 2026-09-07

### Corregido

- **Repaso de calidad del `es_es` de beta.1 — lote 1: Waystones** (190 de 263 cadenas reescritas).
  La traducción automática original tenía errores de criterio; este es el primer lote de una pasada
  por tandas contra un glosario ratificado (`docs/GLOSARIO_ES.md`).
  - **«Mojón» eliminado.** La MT traducía *Waystone* como «mojón» (vulgar en España). Por decisión
    del proyecto, *Waystone* se mantiene sin traducir, igual que la familia `-stone` (*Portstone*,
    *Sharestone*, *Warpstone*). Lo descriptivo sí se traduce: *Warp Plate* → «Placa de traslado»,
    *Warp Portal* → «Portal de traslado», *Bound / Return Scroll* → «Pergamino vinculado / de regreso».
  - **Terminología vanilla.** *Blackstone* «Negrita» → «piedra negra»; *Nether* «Inframundo» →
    «Nether»; *Ender* «del Fin» → «del End»; nombres de color alineados con el `es_es` vanilla
    (light blue → «azul claro», etc.).
  - **Capitalización española.** Eliminado el *Title Case* inglés de todos los nombres de bloque,
    objeto y GUI («Piedra de Puerto Azul Claro» → «Portstone azul claro»).
  - **Concordancia de género.** Toda la familia `-stone` concuerda ahora en femenino («la Waystone»,
    «las Waystones activadas», «Portstone amarilla»).

### Notas

- Claves, placeholders (`%s`, `%d`, `%1$s`) y códigos de formato intactos; solo se tocaron valores.
  73 cadenas ya estaban correctas y se dejaron igual.
- Pasada con OpenCode (MiMo-V2.5) contra el glosario, con el `es_es` vanilla 1.21.1 como referencia;
  integridad de claves, placeholders y concordancia verificados con script.

## [0.1.0-beta.5] - 2026-09-07

### Añadido

- **Locale español (`es_es`) para Apothic Attributes** — 161 claves, tomando como origen el
  `en_us.json` del mod (Apothic Attributes 2.10.1). El mod trae un `es_es.json`, pero está
  **obsoleto**: se escribió para una versión anterior y sus claves ya no coinciden con las que
  busca la versión actual. Las 161 claves vivas caían a inglés en la partida: nombres de atributos
  en el equipo, sus tooltips con Shift, los efectos de estado propios con sus pociones, y los
  mensajes de muerte de combate. El pack aporta ahora esas 161 claves, fusionadas sobre el archivo
  (desactualizado) del propio mod.
  - **Atributos** — nombre + descripción de Perforación/Trituración de armadura y de protección,
    Probabilidad/Daño de crítico, Daño de frío/fuego/HP actual/flecha/proyectil, Robo de vida,
    Sobrecuración, Salud fantasma, Velocidad de tensado/minado, Velocidad de flecha, Probabilidad
    de esquiva, Experiencia/Curación recibida, Reducción de enfriamiento, Vuelo con élitros/creativo.
  - **Descripciones de atributos vanilla y de NeoForge** — las líneas `.desc` de Armadura, Daño/
    Velocidad/Empuje de ataque, Suerte, Salud máxima, Velocidad de movimiento, Alcance de bloques/
    entidades, Altura de escalón, Velocidad de nado, Gravedad, y los efectos de poción vanilla.
  - **Efectos de estado propios** — Sangrado, Vitalidad desbordante, Conocimiento antiguo, Heridas
    graves, Resquebrajadura, Detonación, Vuelo: nombre, tooltip y descripción del efecto, más los
    nombres de poción / poción arrojadiza / poción persistente / flecha con punta de cada uno.
  - **Mensajes de muerte** — fuentes de daño por Sangrado, Detonación, HP actual, Fuego y Frío
    (variantes con objeto y con jugador).
  - **Pantalla de atributos** — cadenas de la GUI (Mantén Shift, base, mín, máx, modificadores,
    fórmula).

### Notas

- La terminología se alineó, donde el archivo obsoleto del mod aún tenía español utilizable, con
  sus decisiones previas (*Sundering* → «Resquebrajadura», *Knowledge* → «Sabiduría», *Bleeding*
  → «Sangrado»).
- Se conservan literalmente el glifo de enfriamiento `⌛`, todos los especificadores de formato
  `%s` / `%1$s` y los nombres propios del estilo *Eterna / Quanta / Arcana*.
- Traducción hecha con OpenCode (MiMo-V2.5); integridad de claves, placeholders y validez JSON
  verificados con script.

## [0.1.0-beta.4] - 2026-09-04

### Añadido

- **Traducción al español (`es_es`) de las guías Patchouli con texto incrustado** — 188 ficheros
  JSON, ~779 cadenas. Estos libros no usan claves de idioma (`i18n`), así que la capa `lang` del
  pack no los cubría y salían en inglés en la partida aunque el mod trajera `es_es`. Se inyectan
  como carpeta `es_es/` paralela a la `en_us/` del mod (Patchouli la prioriza; *fallback* a inglés
  fichero a fichero). Todos los códigos de formato de Patchouli (`$(br)`, `$(l:...)`, colores
  `$(#...)`, `$(playername)`…) se conservan literalmente; no se tocan `type`/`icon`/`recipe` ni
  las *resource locations*.
  - `butchery` · `butchers_guide` — 52 ficheros (47 entradas + 5 categorías). Terminología alineada
    con `assets/butchery/lang/es_es.json` (p. ej. *cleaver* → «Cuchillo de forjar», *skinning knife*
    → «Cuchillo de despiece», *blood grate* → «Rejilla de sangre»).
  - `apotheosis` · `apoth_chronicle` — 126 ficheros (107 entradas + 19 categorías).
  - `irons_spellbooks` · `iss_guide_book` — 10 ficheros (9 entradas + 1 categoría).

### Notas

- **No traducible desde un resource pack**: el título del libro y el `landing_text` (página de
  bienvenida) de `butchery` e `irons_spellbooks` viven en `book.json` (zona de *data pack*) y no
  usan `i18n`; quedan en inglés. El de `apotheosis` sí sale en español (usa clave de idioma, ya
  traducida en el `es_es` oficial del mod).
- `BetterEnd` (`guidebook`), `ars_nouveau`/`ars_elemental` (`worn_notebook`) y
  `mysticalagriculture` (`guide`) **no** se incluyen: el primero trae carpeta `es_es/` propia en
  el jar; los otros dos usan claves `i18n` ya traducidas en sus locales oficiales.
- Traducción hecha con OpenCode (MiMo-V2.5); revisión de estructura, tokens y cadenas restantes
  con script propio.

## [0.1.0-beta.3] - 2026-09-03

### Añadido

- **Traducciones al español (`es_es`) para 3 namespaces más** (~520 claves), tomando como origen el
  `en_us.json` de cada mod. Cierra los huecos de traducción reales detectados en el snapshot del
  modpack v5.134.4 (`docs/SNAPSHOT_MODPACK_5.134.4.md`):
  - `apothic_enchanting` (Apothic Enchanting 1.6.2) — 425 claves. Nombres de bloques (estanterías
    Hellshelf/Seashelf/Deepshelf/Endshelf…), GUI de la mesa de encantamientos, tooltips y descripciones.
    Los nombres propios del sistema de Apotheosis (`Eterna`, `Quanta`, `Arcana`) y los numerales
    romanos de nivel se mantienen sin traducir.
  - `apothic_spawners` (Apothic Spawners 1.4.0) — 89 claves. Estadísticas de generador, tooltips y el
    encantamiento *Capturing*.
  - `placebo` (Placebo 9.9.2) — 6 claves (comandos y toggles cosméticos de mecenas).
- Total del pack: **104 namespaces**, ~13k claves.

### Notas

- El snapshot `docs/SNAPSHOT_MODPACK_5.134.4.md` marcaba como huecos otros mods que tras verificación
  jar a jar **no lo son**: `embeddium_extra` empaqueta su texto bajo el namespace `sodium-extra` (ya
  traducido); `integrated_cataclysm`, `integrated_villages` y `waystone_towers` traen `en_us.json`
  vacío o ningún `lang/`; `attributefix` y `utility_nexus_fixes` no tienen archivos de idioma. Sin
  cadenas que traducir en ninguno.

## [0.1.0-beta.2] - 2026-09-03

### Añadido

- **Fixes de guías Patchouli** — sobrescribe 3 entradas de libro de mods incluidos que
  referencian recetas inexistentes (spam `Recipe X not found` en el log del cliente, la
  página del libro salía sin la receta):
  - `butchery` · `butchers_guide/blocks/butchers_table` — `butchery:crimnsonbutcherstablerecipe`
    → `butchery:crimsonbutcherstablerecipe` (errata en el propio libro); `jungle:acaciabutcherstablerecipe`
    → `butchery:junglebutcherstablerecipe` (namespace y nombre erróneos).
  - `butchery` · `butchers_guide/resources/dragon_scale` — la página era `patchouli:smithing`
    pero `dragonscaleingotrecipe` / `dragonscaleblockrecipe` son `minecraft:crafting_shaped`;
    cambiada a `patchouli:crafting`.
  - `irons_spellbooks` · `iss_guide_book/progression/late_game` — `irons_spellbooks:cryomancer_helmet`
    / `pyromancer_helmet` → `..._helmet_crafting` (los ids reales llevan sufijo `_crafting`).
- `apotheosis` · `apoth_chronicle` referencia `minecraft:bookshelf` (receta vanilla válida y
  crafteable in-game): **no se toca**, es ruido de orden de carga de Patchouli, no un fallo del libro.

## [0.1.0-beta.1] - 2026-09-03

### Cambiado

- **Proyecto renombrado** de *Mystical Realms Resource Pack* a **Mystical Realms Translation & Fixes**
  (slug `mystical-realms-translation-fixes`) por políticas de CurseForge. El `project_id` de CurseForge
  no cambia. Remote GitLab nuevo:
  `https://gitlab.com/stalking-dragons/minecraft/mystical-realms-translation-fixes.git`.
- Nombre del ZIP: `MysticalRealms_ResourcePack-*.zip` → `MysticalRealms_TranslationFixes-*.zip`.
- `pack.mcmeta`, `README.md` y la descripción de CurseForge actualizados para reflejar el nuevo alcance
  (traducciones + fixes).

### Añadido

- **Traducciones al español (`es_es`)** para **101 namespaces de mods** (~12.515 claves), tomando como
  origen el `en_us.json` de cada mod. Minecraft fusiona estos ficheros `lang` sobre lo que cada mod ya
  trae, así que en los mods con `es_es` parcial solo se añaden las claves que faltaban.
  - **59 mods sin ninguna traducción española previa**: everycomp, butchery, mcwroofs, reliquary,
    sodium-extra (rubidium-extra), xaeroworldmap, ars_additions, toms_storage, bookshelf, modernfix,
    spell_power, bclib, caravans, farmers_sandwiches, aces_spell_utils, morevillagers, irons_lib,
    inventoryessentials, mysticalautomation, notenoughcrashes, craftingtweaks, arssophisticatedcompat,
    balm, aquaculturedelight, player_activity_view, wishfulrecipes, carry_mechanics, teleport_animation,
    worldweaver (wover / wover-generator / wover-ui), horde_hoard, justenoughbreeding, info_tab,
    better_party_x_xaeros_world_map, farmer_delight_pizza_lovers, ars_creo, cucumber, just_in_nether,
    better-villager-animations, moogs_structures, betterendisland, zeta, idas, integrated_stronghold,
    skd_menu, fusion, mes, mns, data_miner, mowzies_cataclysm, lionfishapi, common_toolkit,
    irons_patreon_lib, terrablender, dangerous, justenoughprofessions, supermartijn642corelib,
    visualworkbench.
  - **42 mods con `es_es` incompleto, completados** (nº de claves añadidas): supplementaries (+1055),
    ars_nouveau (+921), xaerominimap (+522), irons_spellbooks (+475), betterend (+367), quark (+324),
    dawnoftimebuilder (+275), waystones (+263), moonlight (+239), farmersdelight (+193), jei (+188),
    create (+178), armoroftheages (+161), enchdesc (+151), sophisticatedbackpacks (+149),
    deeperdarker (+136), biomesoplenty (+119), jade (+105), tombstone (+72), embeddium (+71),
    L_Ender's Cataclysm + integrated_cataclysm (+61), guardvillagers (+59), obscure_tooltips (+41),
    mowziesmobs (+36), aquamirae (+31), aquaculture (+30), bettercombat (+20), xaerobetterpvp (+17),
    relics (+15), sophisticatedcore (+15), vellumli (+13), regalia_slots_api (+12), iris (neoculus) (+11),
    configured (+10), mcwbridges (+6), workhand_tools (+3), ascendant_spawners (+2), ars_elemental (+1),
    jeresources (+1), mysticalagriculture (+1), naturescompass (+1), villagertradingplus (+1).

## [0.0.0-beta.1] - 2026-09-02

### Añadido

- Primera versión versionada del resource pack para el modpack **Mystical Realms** (MC 1.21.1).
- Icono del pack (`resourcepack/pack.png`, 256x256).
- **Fix Butchery `ravager_carcass`**: `assets/butchery/models/custom/ravager_carcass.json`.
  Butchery 5.2 incluye un archivo de modelo huérfano (`custom/ravager_carcass.json`, doble `s`) con una
  rotación de elemento ilegal (`angle: -90`; solo se admiten ±45/±22.5/0). No lo referencia nada, pero
  MC 1.21 carga en bloque todos los `models/**/*.json` al arrancar y registra un `ERROR` de parseo por él.
  Se sustituye por el modelo hermano ya corregido del propio mod (`custom/ravager_carcas.json`, una `s`),
  de modo que la carga tiene éxito y el log queda limpio. Sin cambios visuales in-game
  (la carcasa en el mundo usa un modelo Java por código; el ítem usa `custom/ravager_carcas`).
