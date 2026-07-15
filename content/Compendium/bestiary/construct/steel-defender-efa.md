---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/efa
- monster/cr/
- monster/size/medium
- monster/type/construct
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Steel Defender"
---
# Steel Defender
*Source: Eberron: Forge of the Artificer p. 19*

```statblock
"name": "Steel Defender"
"size": "Medium"
"type": "construct"
"alignment": "Neutral"
"ac_class": "12 + your Intelligence modifier"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "12"
  - !!int "14"
  - !!int "4"
  - !!int "10"
  - !!int "6"
"speed": "40 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "understands the languages you know"
"traits":
  - "desc": "Add your [Proficiency Bonus](/Compendium/rules/variant-rules/proficiency-xphb.md)\
      \ to any ability check or saving throw the defender makes."
    "name": "Steel Bond"
"actions":
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d8 + 2 plus your Intelligence modifier Force damage."
    "name": "Force-Empowered Rend"
  - "desc": "The defender, or one Construct or object it can see within 5 feet of\
      \ itself, regains a number of [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ equal to 2d8 plus your Intelligence modifier."
    "name": "Repair (3/Day)"
"reactions":
  - "desc": "Trigger: A creature the defender can see within 5 feet of itself makes\
      \ an attack roll against a creature other than the defender. _Response:_ The\
      \ triggering creature makes the attack roll with [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)."
    "name": "Deflect Attack"
"source":
  - "EFA"
"image": "/Compendium/bestiary/construct/token/steel-defender-efa.webp"
```
^statblock