---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbviv
- monster/cr/15
- monster/size/gargantuan
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Graverobber Spider"
---
# Graverobber Spider
*Source: Theros Bestiary, Vol. IV*
![](/Compendium/bestiary/beast/img/graverobber-spider.webp#right)

Cloaks woven from its webs are durable and waterproof but said to bring on nightmares.

```statblock
"name": "Graverobber Spider"
"size": "Gargantuan"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "12"
  - !!int "18"
  - !!int "2"
  - !!int "11"
  - !!int "4"
"speed": "120 ft., climb 60 ft."
"skillsaves":
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+3"
"senses": "[blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., [darkvision](/Compendium/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 10"
"languages": ""
"cr": "15"
"traits":
  - "desc": "The spider can climb difficult surfaces, including upside down on ceilings,\
      \ without needing to make an ability check."
    "name": "Spider Climb"
  - "desc": "While in contact with a web, the spider knows the exact location of any\
      \ other creature in contact with the same web."
    "name": "Web Sense"
  - "desc": "The spider ignores movement restrictions caused by webbing."
    "name": "Web Walker"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit: 20 (4d8\
      \ + 2) piercing damage, and the target must make a DC 14 Constitution saving\
      \ throw, taking 18 (4d8) poison damage on a failed save, or half as much damage\
      \ on a successful one. If the poison damage reduces the target to 0 Hit Points,\
      \ the target is stable but poisoned for 1 hour, even after regaining Hit Points,\
      \ and is paralyzed while poisoned in this way."
    "name": "Bite"
  - "desc": "The spider vomits digestive juices on a target that has a speed of 5\
      \ feet or less or is incapacitated. At the beginning of that target's turn,\
      \ as long as less than three rounds of combat have passed and the juice has\
      \ not been rinsed off, the target takes 9 (2d8) acid damage."
    "name": "Digest"
  - "desc": "The spider makes a bite attack on a target that it has vomited digestive\
      \ juices on. For every point of damage dealt, the spider gains that many temporary\
      \ Hit Points."
    "name": "Consume"
  - "desc": "Ranged Weapon Attack: +3 to hit, range 30/60 ft., one creature. Hit:\
      \ The target is restrained by webbing. As an action, the restrained target can\
      \ make a DC 12 Strength check, bursting the webbing on a success. The webbing\
      \ can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage;\
      \ immunity to bludgeoning, poison, and psychic damage)."
    "name": "Web (Recharge 5-6)"
"source":
  - "TBVIV"
```
^statblock