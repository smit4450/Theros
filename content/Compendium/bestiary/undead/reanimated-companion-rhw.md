---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/rhw
- monster/cr/
- monster/size/medium
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Reanimated Companion"
---
# Reanimated Companion
*Source: RHW*

```statblock
"name": "Reanimated Companion"
"size": "Medium"
"type": "undead"
"alignment": "Neutral"
"ac_class": "10 plus your Intelligence modifier"
"modifier": !!int "0"
"stats":
  - !!int "11"
  - !!int "10"
  - !!int "16"
  - !!int "4"
  - !!int "10"
  - !!int "6"
"speed": "30 ft."
"damage_resistances": "necrotic, poison"
"damage_immunities": "lightning"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[blindsight](/Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 10"
"languages": "understands the languages you know"
"traits":
  - "desc": "The companion explodes when it dies. *Dexterity Saving Throw:* DC equals\
      \ your spell save DC, each creature in a 10-foot Emanation originating from\
      \ the companion. *Failure:* 2d4 Necrotic damage. *Success:* Half damage."
    "name": "Death Burst"
  - "desc": "Whenever the companion is subjected to Lightning damage, it regains a\
      \ number of Hit Points equal to the Lightning damage dealt."
    "name": "Lightning Absorption"
"actions":
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d4 plus your Intelligence modifier Necrotic damage, and the target\
      \ can't take Opportunity Attacks until the start of its next turn."
    "name": "Dreadful Swipe"
"source":
  - "RHW"
```
^statblock