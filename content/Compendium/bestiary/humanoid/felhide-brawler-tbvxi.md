---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxi
- monster/cr/1-2
- monster/size/medium
- monster/type/humanoid/minotaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Felhide Brawler"
---
# Felhide Brawler
*Source: Theros Bestiary, Vol. XI*
![](/Compendium/bestiary/humanoid/img/felhide-brawler.webp#center)

```statblock
"name": "Felhide Brawler"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "0"
"stats":
  - !!int "14"
  - !!int "10"
  - !!int "14"
  - !!int "10"
  - !!int "10"
  - !!int "12"
"speed": "30 ft."
"skillsaves":
  - "name": "[Intimidation](/Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common, Minotaur"
"cr": "1/2"
"traits":
  - "desc": "When another Felhide minotaur falls in combat, if the brawler is the\
      \ only Felhide in a 120-foot radius, the brawler spends its turns running from\
      \ combat. After one hour, it returns to its fallen comrades and eats them."
    "name": "Felhide Burial Rites"
"actions":
  - "desc": "The minotaur makes two halberd attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 10 ft., one target. _Hit:_ 7\
      \ (1d10 + 2) slashing damage."
    "name": "Halberd"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
      \ + 2) piercing damage, and it can use a bonus action to attempt to shove that\
      \ target with its horns. The target must be within 5 feet of the minotaur and\
      \ no more than one size larger than it. Unless the target succeeds on a DC 12\
      \ Strength saving throw, the minotaur pushes it up to 10 feet away from the\
      \ minotaur."
    "name": "Horns"
"reactions":
  - "desc": "Immediately after the minotaur uses the Dash action on its turn and moves\
      \ at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
"source":
  - "TBVXI"
```
^statblock