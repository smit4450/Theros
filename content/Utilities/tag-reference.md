---
title: Tag Conventions
obsidianUIMode: preview
cssclasses:
  - json5e-note
tags:
  - utility/
  - status/active
aliases:
  - Tag Reference
  - Tag Guide
---

# Tag Conventions

> [!info] Purpose
> This is the **single source of truth** for all tag conventions in this vault. All tags use a **unified hierarchy** — there is no separate `ttrpg-cli/` prefix. Pin this note or link it in your sidebar for easy reference.

## Rules

1. Always use **lowercase**
2. Use **forward slashes** `/` for hierarchy
3. Use **hyphens** `-` for multi-word terms
4. Tags **MUST** be in YAML frontmatter (not inline `#tags` in body text)
5. Every note should have tags appropriate to its content type
6. All tags share one unified namespace — compendium and homebrew content use the same system

---

## Unified Tag Taxonomy

### Source Tags
Identify the publication a note originates from. Applied to compendium content.

| Tag | Source Book |
|-----|------------|
| `src/5e/mot` | Mythic Odysseys of Theros |
| `src/5e/xphb` | Player's Handbook 2024 |
| `src/5e/xdmg` | Dungeon Master's Guide 2024 |
| `src/5e/xmm` | Monster Manual 2024 |
| `src/5e/gmoa` | Gray Merchant of Asphodel |
| `src/5e/frhof` | Forgotten Realms: Heroes of Faerûn |
| `src/5e/fraif` | Forgotten Realms: Adventures in Faerûn |
| `src/5e/tce` | Tasha's Cauldron of Everything |
| `src/5e/ggr` | Guildmaster's Guide to Ravnica |
| `src/5e/gos` | Ghosts of Saltmarsh |
| `src/5e/vgm` | Volo's Guide to Monsters |
| `src/5e/mtf` | Mordenkainen's Tome of Foes |
| `src/5e/xge` | Xanathar's Guide to Everything |
| `src/5e/egw` | Explorer's Guide to Wildemount |
| `src/5e/phb` | Player's Handbook (2014) |
| `src/5e/tftyp` | Tales from the Yawning Portal |
| `src/5e/tbvi` | Theros Bestiary Vol. I |
| `src/5e/tbvii` | Theros Bestiary Vol. II |
| `src/5e/tbviii` | Theros Bestiary Vol. III |
| `src/5e/tbviv` | Theros Bestiary Vol. IV |
| `src/5e/tbvv` | Theros Bestiary Vol. V |
| `src/5e/tbvvi` | Theros Bestiary Vol. VI |
| `src/5e/tbvvii` | Theros Bestiary Vol. VII |
| `src/5e/tbvviii` | Theros Bestiary Vol. VIII |
| `src/5e/tbvix` | Theros Bestiary Vol. IX |
| `src/5e/tbvx` | Theros Bestiary Vol. X |
| `src/5e/tbvxi` | Theros Bestiary Vol. XI |
| `src/5e/tbvxii` | Theros Bestiary Vol. XII |
| `src/5e/tbvxiii` | Theros Bestiary Vol. XIII |
| `src/5e/tbvxiv` | Theros Bestiary Vol. XIV |
| `src/5e/tbvxv` | Theros Bestiary Vol. XV |
| `src/5e/tbvxvi` | Theros Bestiary Vol. XVI |
| `src/5e/tbvxvii` | Theros Bestiary Vol. XVII |
| `src/5e/tbvxviii` | Theros Bestiary Vol. XVIII |
| `src/5e/tbvxix` | Theros Bestiary Vol. XIX |
| `src/5e/tbvxx` | Theros Bestiary Vol. XX |
| `src/5e/tbvxxi` | Theros Bestiary Vol. XXI |
| `src/5e/tbvxxii` | Theros Bestiary Vol. XXII |
| `src/5e/tbvxxiii` | Theros Bestiary Vol. XXIII |
| `src/5e/tbvxxiv` | Theros Bestiary Vol. XXIV |
| `src/5e/tbvxxv` | Theros Bestiary Vol. XXV |
| `src/homebrew` | Original homebrew content |
| `src/adapted` | Adapted from published material |
| `src/theros-block` | From MTG Theros block lore |
| `src/theros-beyond-death` | From MTG Theros: Beyond Death lore |

### Content Type Tags (What is it?)

One tag system for all content — compendium imports and homebrew alike. Use the same prefix regardless of origin.

| Category | Tag Prefix | Sub-tags | Notes |
|----------|-----------|----------|-------|
| Spells | `spell/` | `spell/level/`, `spell/school/`, `spell/class/`, `spell/list/`, `spell/ritual/` | All spells, compendium and homebrew |
| Monsters & Creatures | `monster/` | `monster/cr/`, `monster/size/`, `monster/type/`, `monster/environment/` | All creatures, compendium and homebrew |
| Items | `item/` | `item/rarity/`, `item/weapon/`, `item/armor/`, `item/attunement/`, `item/wondrous/`, `item/potion/`, `item/gear/` | All items |
| Classes | `class/` | `class/[class-name]` | e.g. `class/fighter`, `class/wizard` |
| Subclasses | `subclass/` | `subclass/[class]/[subclass]` | e.g. `subclass/fighter/champion-xphb` |
| Races | `race/` | `race/[race-name]` | e.g. `race/leonin`, `race/satyr` |
| Backgrounds | `background` | — | |
| Deities | `deity/` | `deity/[pantheon]` | e.g. `deity/theros` |
| Feats | `feat` | — | |
| Rewards | `reward/` | `reward/supernatural-gift`, `reward/piety-trait`, `reward/blessing`, `reward/charm` | |
| Optional Features | `optional-feature/` | `optional-feature/ei`, `optional-feature/mm`, `optional-feature/mv-b` | Invocations, Metamagic, etc. |
| Bastions | `bastion` | — | |
| Vehicles | `vehicle/` | `vehicle/type/`, `vehicle/size/`, `vehicle/terrain/` | |
| Objects | `object/` | `object/type/`, `object/size/` | |
| Hazards | `hazard/` | `hazard/trp`, `hazard/env`, `hazard/gen` | Traps, environmental, general |
| Crafting | `crafting/` | `crafting/enchantment`, `crafting/rare-metal` | |
| Locations | `location/` | — | Places in the world |
| NPCs | `npc/` | — | Non-player characters |
| Factions | `faction/` | `faction/[faction-name]` | Organizations and groups |
| Events | `event/` | — | Historical or campaign events |
| Quests | `quest/` | — | Quests and missions |
| Lore | `lore/` | — | World lore, history, mythology |
| Rules | `rule/` | — | Homebrew or house rules |
| Session Notes | `session/` | — | Session recaps and play notes |
| Utility | `utility/` | — | Meta notes, dashboards, tables |

### Place Tags (What kind of place?)
- `place/continent`
- `place/nation`
- `place/region`
- `place/polis` — City-state (Theros-specific)
- `place/city`
- `place/town`
- `place/village`
- `place/district`
- `place/building`
- `place/landmark`
- `place/dungeon`
- `place/wilderness`
- `place/plane`
- `place/ruin`
- `place/divine-realm` — Nyx and divine domains

### Location Hierarchy (Where is it?)
Hierarchical tags for geographic relationships:
```
loc/[world]/[continent]/[region]/[settlement]
```
Examples:
- `loc/theros`
- `loc/theros/meletis`
- `loc/theros/akros`
- `loc/theros/setessa`
- `loc/theros/nyx`
- `loc/theros/meletis/siren-sea`

### Status Tags (Current state)
- `status/active` — Currently in use/relevant
- `status/destroyed` — No longer exists in-world
- `status/abandoned` — Exists but unused
- `status/hidden` — Exists but not commonly known
- `status/planned` — Planned but not yet introduced
- `status/stub` — Note exists but needs significant expansion
- `status/wip` — Work in progress (note is incomplete)
- `status/complete` — Note is finished

### Era/Timeline Tags (When?)
- `era/ancient` — Deep history / primordial age
- `era/age-of-legends` — Mythic era of heroes and gods
- `era/current` — Present day in the campaign
- `era/future` — Planned or prophesied future events

### Campaign Tags (How is it used?)
- `campaign/main` — Main campaign content
- `campaign/side-quest` — Side quest content
- `campaign/backstory` — Background/history content
- `campaign/future-plot` — Planned future plot hooks
- `campaign/homebrew` — Custom homebrew mechanics

### Relevance Tags
- `relevance/critical` — Essential to the campaign
- `relevance/major` — Important but not essential
- `relevance/minor` — Minor detail
- `relevance/flavor` — Atmospheric/flavor only

### Affiliation Tags (Who controls/belongs to?)
- `faction/[faction-name]` — In-world factions (e.g. `faction/iroas-champions`, `faction/mages-circle`, `faction/thieves-guild`)
- `allegiance/lawful`
- `allegiance/neutral`
- `allegiance/chaotic`
- `allegiance/independent`

### Theros-Specific Tags
- `pantheon/theros` — Related to Theros pantheon
- `domain/[domain-name]` — Divine domain (forge, knowledge, light, etc.)

---

## Frontmatter Examples

### Compendium Spell
```yaml
---
title: Fireball
tags:
  - src/5e/xphb
  - spell/class/sorcerer
  - spell/class/wizard
  - spell/level/3rd-level
  - spell/school/evocation
aliases:
  - Fireball
---
```

### Homebrew Spell
```yaml
---
title: Wrath of the Polis
tags:
  - spell/level/4th-level
  - spell/school/evocation
  - spell/class/cleric
  - src/homebrew
aliases:
  - Wrath of the Polis
---
```

### Compendium Monster
```yaml
---
title: Fleecemane Lion
tags:
  - src/5e/mot
  - monster/cr/3
  - monster/size/large
  - monster/type/monstrosity
aliases:
  - Fleecemane Lion
---
```

### Homebrew Creature
```yaml
---
title: Nyxborn Shade
tags:
  - monster/cr/5
  - monster/size/medium
  - monster/type/undead
  - loc/theros/nyx
  - src/homebrew
aliases:
  - Nyxborn Shade
---
```

### Location
```yaml
---
title: The Siren's Rest
tags:
  - location/
  - place/building
  - loc/theros/meletis
  - status/active
  - campaign/main
  - relevance/major
  - src/homebrew
aliases:
  - Siren's Rest
  - The Siren's Rest Tavern
---
```

### NPC
```yaml
---
title: Kynaios the Wanderer
tags:
  - npc/
  - loc/theros/akros
  - faction/iroas-champions
  - allegiance/lawful
  - campaign/main
  - relevance/critical
  - src/homebrew
aliases:
  - Kynaios
---
```

### Lore Note
```yaml
---
title: The Silence of the Gods
tags:
  - lore/
  - pantheon/theros
  - era/current
  - campaign/backstory
  - relevance/major
  - src/theros-beyond-death
  - status/complete
aliases: []
---
```

### Homebrew Class/Subclass
```yaml
---
title: The Warlord Class
tags:
  - class/warlord
  - campaign/homebrew
  - status/wip
  - src/homebrew
aliases:
  - Warlord
---
```

---

## Related
- [[tag-audit|Tag Audit Dashboard]] — Validate tag consistency
- [[spell-table|Spell Table]] — Spell reference
