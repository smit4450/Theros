---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/5
- monster/size/large
- monster/type/construct
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Gold-Forged Sentinel"
---
# Gold-Forged Sentinel
*Source: Mythic Odysseys of Theros p. 211*
![](/Compendium/bestiary/construct/img/gold-forged-sentinel.webp#right)

The original purpose of gold-forged sentinels is a mystery, and of all Purphoros's original anvilwroughts, this construct is the most difficult to control. A sentinel often operates without a master, stalking the high places of the mortal world or waiting, still as a statue, for what could be decades before reanimating to carry out their mysterious purpose.

The first anvilwroughts were created by the god of the forge, Purphoros. He gave the secret of breathing life into these metal creatures to his most devoted followers so they could mimic his works and invent new forms at their own forges.

Some anvilwroughts are vigilant guardians at holy shrines, others serve as familiars and messengers, and a few were created to emulate beauty found among the animals of the mortal world. Each exhibits abilities suited to its role, with some behaving like companionable creatures or stoic guardians.

A few extremely rare and valuable anvilwroughts were crafted by the hand of Purphoros himself. A number of these magnificent creations are now heirlooms of monarchs; others are lost to the sands of time or are guarded by ancient monsters.

```statblock
"name": "Gold-Forged Sentinel"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "76"
"hit_dice": "8d10 + 32"
"modifier": !!int "1"
"stats":
  - !!int "18"
  - !!int "13"
  - !!int "19"
  - !!int "3"
  - !!int "16"
  - !!int "10"
"speed": "40 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [petrified](/Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 16"
"languages": "understands one language of its creator but can't speak"
"cr": "5"
"traits":
  - "desc": "If the sentinel moves at least 20 feet straight toward a target and then\
      \ hits it with a ram attack on the same turn, the target takes an extra 10 (3d6)\
      \ bludgeoning damage. If the target is a creature, it must succeed on a DC 15\
      \ Strength saving throw or be knocked [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Charge"
  - "desc": "The sentinel has advantage on saving throws against any spell that targets\
      \ only the sentinel (not an area). If the sentinel's saving throw succeeds and\
      \ the spell is of 4th level or lower, the spell has no effect on the sentinel\
      \ and instead targets the caster."
    "name": "Spell Turning"
"actions":
  - "desc": "The sentinel makes two ram attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 13\
      \ (2d8 + 4) bludgeoning damage."
    "name": "Ram"
  - "desc": "The sentinel exhales fire in a 15-foot cone. Each creature in that area\
      \ must make a DC 15 Dexterity saving throw, taking 27 (6d8) fire damage on a\
      \ failed save, or half as much damage on a successful one."
    "name": "Fire Breath (Recharge 5-6)"
"source":
  - "MOT"
"image": "/Compendium/bestiary/construct/token/gold-forged-sentinel-mot.webp"
```
^statblock