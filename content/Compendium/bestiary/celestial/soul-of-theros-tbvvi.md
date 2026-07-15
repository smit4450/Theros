---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvvi
- monster/cr/27
- monster/size/gargantuan
- monster/type/celestial
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Soul of Theros"
---
# Soul of Theros
*Source: Theros Bestiary, Vol. VI*
![](/Compendium/bestiary/celestial/img/soul-of-theros.webp#center)

```statblock
"name": "Soul of Theros"
"size": "Gargantuan"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "6"
"stats":
  - !!int "22"
  - !!int "22"
  - !!int "22"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "120 ft."
"saves":
  - "strength": !!int "14"
  - "dexterity": !!int "14"
"damage_resistances": "radiant"
"senses": "[truesight](/Compendium/rules/senses.md#Truesight) 120 ft., passive Perception\
  \ 10"
"languages": "Common"
"cr": "27"
"traits":
  - "desc": "As a bonus action on its turn, the avatar chooses any number of creatures\
      \ on Theros. Until the beginning of the avatar's next turn, those creatures\
      \ each get a +2 bonus to Strength and Dexterity checks and damage rolls, gain\
      \ 4 (1d8) temporary Hit Points, and have Advantage on attack rolls. For every\
      \ point of damage dealt by those creatures until the avatar's next turn, it\
      \ regains 1 hit point."
    "name": "Blessing of Theros"
  - "desc": "The avatar can't be surprised."
    "name": "Vigilant"
"actions":
  - "desc": "The avatar makes three melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +14 to hit, reach 5 ft., one creature. Hit: 36 (12d4\
      \ + 6) bludgeoning damage. If the target is a Medium or smaller creature, it\
      \ must succeed on a DC 22 Strength saving throw or be knocked prone."
    "name": "Shield Bash"
  - "desc": "_Melee or Ranged Weapon Attack:_ +14 to hit, reach 50 ft. or range 150/300\
      \ ft., one target. _Hit:_ 48 (12d6 + 6) piercing damage."
    "name": "Spear"
"reactions":
  - "desc": "As the avatar dies, it may take a reaction to use its Blessing of Theros\
      \ trait."
    "name": "Last Hope"
"source":
  - "TBVVI"
```
^statblock