---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxxi
- monster/cr/23
- monster/size/gargantuan
- monster/type/monstrosity/octopus
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Godhunter Octopus"
---
# Godhunter Octopus
*Source: Theros Bestiary, Vol. XXI*
![](/Compendium/bestiary/monstrosity/img/godhunter-octopus.webp#right)

“I will match Thassa drop for drop and show a god what true power is.”

—Kiora

```statblock
"name": "Godhunter Octopus"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "octopus"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "13"
  - !!int "20"
  - !!int "6"
  - !!int "12"
  - !!int "6"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+8"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+8"
"senses": "arcane smell, [blindsight](/Compendium/rules/senses.md#Blindsight) 0 ft.\
  \ (can't see beyond this radius), passive Perception 10"
"languages": ""
"cr": "23"
"traits":
  - "desc": "The octopus can smell magic and discern precise details about the magic\
      \ it smells. It has Advantage on Wisdom (perception) checks that rely on smelling\
      \ magic."
    "name": "Keen Arcane Smell"
  - "desc": "The octopus deals double damage to creatures that are spells and to creatures\
      \ under spells."
    "name": "Godhunter"
  - "desc": "The octopus has Advantage on Dexterity (Stealth) checks made while underwater."
    "name": "Underwater Camouflage"
  - "desc": "The octopus can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "The monster makes three attacks: one attack with its arms and two with\
      \ its bite."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 40 (10d6\
      \ + 5) bludgeoning damage. If the target is a creature, it is grappled (escape\
      \ DC 16) and brought within 5 ft. of the octopus's mouth. Until this grapple\
      \ ends, the target is restrained, and the octopus can't use its arms on another\
      \ target."
    "name": "Arms"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target grappled by\
      \ the octopus's arms. Hit: 40 (10d6 + 5) piercing damage."
    "name": "Bite"
  - "desc": "A 40-foot-radius cloud of ink extends all around the octopus if it is\
      \ underwater. The area is heavily obscured for 1 minute, although a significant\
      \ current can disperse the ink. After releasing the ink, the octopus can use\
      \ the Dash action as a bonus action."
    "name": "Ink Cloud (Recharges after a Short or Long Rest)"
"source":
  - "TBVXXI"
```
^statblock