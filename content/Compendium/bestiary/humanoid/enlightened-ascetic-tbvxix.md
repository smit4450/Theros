---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxix
- monster/cr/2
- monster/size/medium
- monster/type/humanoid/leonin
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Enlightened Ascetic"
---
# Enlightened Ascetic
*Source: Theros Bestiary, Vol. XIX*
![](/Compendium/bestiary/humanoid/img/enlightened-ascetic.webp#right)

“I do not reject the gods. I reject their authority, their pettiness, and their arrogance.”

```statblock
"name": "Enlightened Ascetic"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Any alignment"
"ac": !!int "15"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "13"
  - !!int "13"
  - !!int "10"
  - !!int "13"
  - !!int "10"
"speed": "45 ft."
"skillsaves":
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+3"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Common, Leonin"
"cr": "2"
"traits":
  - "desc": "As a bonus action, the sun guide can let out an especially menacing roar.\
      \ Creatures it chooses within 10 feet of itself that can hear it must succeed\
      \ on a DC 12 Wisdom saving throw or become frightened of it until the end of\
      \ its next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "The enlightened ascetic's innate spellcasting ability is Wisdom (spell\
      \ save DC 11, +3 to hit with spell attacks). It can innately cast the following\
      \ spells: At will: Antimagic Field"
    "name": "Innate Spellcasting"
  - "desc": "While the sun guide isn't wearing armor, its armor class includes its\
      \ Wisdom modifier."
    "name": "Unarmored Defense"
"actions":
  - "desc": "_Ranged Spell Attack:_ +3 to hit, range 30 ft., one target. _Hit:_ 3\
      \ (1d4 + 1) radiant damage."
    "name": "Sun Bolt"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 2 (1d4\
      \ + 0) slashing damage."
    "name": "Claws"
"source":
  - "TBVXIX"
```
^statblock