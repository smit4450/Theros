---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxvii
- monster/cr/0
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Sigiled Skink"
---
# Sigiled Skink
*Source: Theros Bestiary, Vol. XVII*
![](/Compendium/bestiary/beast/img/sigiled-skink.webp#right)

The runes seem to come alive as it moves, rippling like slow flames across its scales.

```statblock
"name": "Sigiled Skink"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "3"
"hit_dice": "1d4 + 1"
"modifier": !!int "2"
"stats":
  - !!int "2"
  - !!int "15"
  - !!int "12"
  - !!int "1"
  - !!int "8"
  - !!int "3"
"speed": "20 ft., climb 20 ft."
"skillsaves":
  - "name": "[Acrobatics](/Compendium/rules/skills.md#Acrobatics)"
    "desc": "+4"
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+2"
  - "name": "[Sleight of Hand](/Compendium/rules/skills.md#Sleight%20of%20Hand)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+2"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "0"
"traits":
  - "desc": "If the skink is subjected to an effect that allows it to make a Dexterity\
      \ saving throw to take only half damage, the skink instead takes no damage if\
      \ it succeeds on the saving throw, and only half damage if it fails."
    "name": "Evasion"
  - "desc": "The skink can take the Disengage or Hide action as a bonus action on\
      \ each of its turns."
    "name": "Nimble Escape"
  - "desc": "An oracle of Purphoros has Advantage on interpreting the skink's sigils.\
      \ If the skink dies, the sigils disappear."
    "name": "Sigils"
  - "desc": "The skink has Advantage on ability checks and saving throws made to escape\
      \ a grapple."
    "name": "Slippery"
"actions":
  - "desc": "Melee Weapon Attack: +0 to hit, reach 5 ft., one target smaller than\
      \ its head. Hit: 1 piercing damage."
    "name": "Bite"
"reactions":
  - "desc": "If the skink takes damage greater than 1 that would not kill it, it drops\
      \ its tail and takes only 1 damage instead."
    "name": "Drop Tail"
"source":
  - "TBVXVII"
```
^statblock