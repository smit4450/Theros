---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/1-2
- monster/size/tiny
- monster/type/construct
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Anvilwrought Raptor"
---
# Anvilwrought Raptor
*Source: Mythic Odysseys of Theros p. 209*
![](/Compendium/bestiary/construct/img/anvilwrought-raptor.webp#right)

Prized among Meletis's thaumaturges, anvilwrought raptors are often crafted in the form of a hawk or an owl. Most serve as messengers and spies, flying over the busy streets or high over the land while carrying or seeking vital information for their masters.

The first anvilwroughts were created by the god of the forge, Purphoros. He gave the secret of breathing life into these metal creatures to his most devoted followers so they could mimic his works and invent new forms at their own forges.

Some anvilwroughts are vigilant guardians at holy shrines, others serve as familiars and messengers, and a few were created to emulate beauty found among the animals of the mortal world. Each exhibits abilities suited to its role, with some behaving like companionable creatures or stoic guardians.

A few extremely rare and valuable anvilwroughts were crafted by the hand of Purphoros himself. A number of these magnificent creations are now heirlooms of monarchs; others are lost to the sands of time or are guarded by ancient monsters.

```statblock
"name": "Anvilwrought Raptor"
"size": "Tiny"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "18"
"hit_dice": "4d4 + 8"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "16"
  - !!int "14"
  - !!int "3"
  - !!int "14"
  - !!int "1"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [petrified](/Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 14"
"languages": "understands one language of its creator but can't speak"
"cr": "1/2"
"traits":
  - "desc": "The raptor has advantage on Wisdom ([Perception](/Compendium/rules/skills.md#Perception))\
      \ checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "The raptor can mimic any sound, including voices, it has heard in the\
      \ last 24 hours. A creature that hears the sounds can tell they are imitations\
      \ with a successful DC 12 Wisdom ([Insight](/Compendium/rules/skills.md#Insight))\
      \ check."
    "name": "Recorded Mimicry"
"actions":
  - "desc": "The raptor makes two attacks with its beak."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 5 (1d4\
      \ + 3) piercing damage."
    "name": "Beak"
"source":
  - "MOT"
"image": "/Compendium/bestiary/construct/token/anvilwrought-raptor-mot.webp"
```
^statblock