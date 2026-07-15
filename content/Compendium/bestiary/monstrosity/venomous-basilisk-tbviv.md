---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbviv
- monster/cr/3
- monster/size/medium
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Venomous Basilisk"
---
# Venomous Basilisk
*Source: Theros Bestiary, Vol. IV*
![](/Compendium/bestiary/monstrosity/img/venomous-basilisk.webp#center)

```statblock
"name": "Venomous Basilisk"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "-1"
"stats":
  - !!int "16"
  - !!int "8"
  - !!int "15"
  - !!int "2"
  - !!int "8"
  - !!int "7"
"speed": "20 ft."
"damage_immunities": "poison, acid"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "If a non-basilisk creature starts its turn within 30 ft. of the basilisk\
      \ and the two of them can see each other, the basilisk can force the creature\
      \ to make a DC 12 Constitution saving throw if the basilisk isn't incapacitated.\
      \ On a failed save, the creature becomes infected with the basilisk's venom.\
      \ Until cured, the venom deals 36 (8d8) poison damage to the creature at the\
      \ end of its turn. A creature that isn't surprised can avert its eyes to avoid\
      \ the saving throw at the start of its turn. If it does so, it can't see the\
      \ basilisk until the start of its next turn, when it can avert its eyes again.\
      \ If it looks at the basilisk in the meantime, it must immediately make the\
      \ save."
    "name": "Venomous Gaze"
  - "desc": "Any creature that starts its turn within 10 feet of the basilisk must\
      \ succeed on a DC 14 Constitution saving throw or be poisoned until the start\
      \ of its next turn."
    "name": "Stench"
  - "desc": "The odor of a living or dead weasel is toxic to the basilisk, although\
      \ the weasel has no immunity to the basilisk's venom, so both die."
    "name": "Weakness to Weasels"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6\
      \ + 3) piercing damage plus 7 (2d6) poison damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6\
      \ + 3) poison damage plus 7 (2d6) acid damage."
    "name": "Acidic Touch"
"source":
  - "TBVIV"
```
^statblock