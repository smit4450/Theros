---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/2
- monster/size/medium
- monster/type/construct
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Burnished Hart"
---
# Burnished Hart
*Source: Mythic Odysseys of Theros p. 211*


Among the first anvilwroughts to be forged by Purphoros, elegant burnished harts wander the mortal realm in search of new sights to bring back to the god of the forge. On every trip from Mount Velus, where Purphoros has his forge, they seek out the far reaches of the world so they can witness beauty in all its forms, then later reunite with their creator, their minds filled with tales of how life's splendor continues to develop.

The first anvilwroughts were created by the god of the forge, Purphoros. He gave the secret of breathing life into these metal creatures to his most devoted followers so they could mimic his works and invent new forms at their own forges.

Some anvilwroughts are vigilant guardians at holy shrines, others serve as familiars and messengers, and a few were created to emulate beauty found among the animals of the mortal world. Each exhibits abilities suited to its role, with some behaving like companionable creatures or stoic guardians.

A few extremely rare and valuable anvilwroughts were crafted by the hand of Purphoros himself. A number of these magnificent creations are now heirlooms of monarchs; others are lost to the sands of time or are guarded by ancient monsters.

```statblock
"name": "Burnished Hart"
"size": "Medium"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "6d8 + 18"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "14"
  - !!int "16"
  - !!int "3"
  - !!int "15"
  - !!int "1"
"speed": "50 ft."
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [petrified](/Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 12"
"languages": "understands one language of its creator but can't speak"
"cr": "2"
"traits":
  - "desc": "If the hart moves at least 20 feet straight toward a target and then\
      \ hits it with an antlers attack on the same turn, the target takes an extra\
      \ 7 (2d6) fire damage. If the target is a creature, it must succeed on a DC\
      \ 13 Strength saving throw or be knocked [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Charge"
  - "desc": "A creature that touches the hart or hits it with a melee attack while\
      \ within 5 feet of it takes 5 (1d10) fire damage."
    "name": "Heated Body"
  - "desc": "The hart has advantage on Strength and Dexterity saving throws made against\
      \ effects that would knock it [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Sure-Footed"
"actions":
  - "desc": "The hart makes two attacks: one with its antlers and one with its hooves."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8\
      \ + 3) piercing damage."
    "name": "Antlers"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 5 (1d4\
      \ + 3) bludgeoning damage plus 2 (1d4) fire damage."
    "name": "Hooves"
"source":
  - "MOT"
"image": "/Compendium/bestiary/construct/token/burnished-hart-mot.webp"
```
^statblock