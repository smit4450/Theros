---
title: Animal Lord; Sage
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/20
- ttrpg-cli/monster/environment/beastlands
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Animal Lord; Sage"]
---
# Animal Lord; Sage
*Source: Monster Manual (2024) p. 15, FRHoF*  

```statblock
"name": "Animal Lord; Sage (XMM)"
"size": "Medium"
"type": "celestial"
"alignment": "Neutral"
"ac": !!int "19"
"hp": !!int "323"
"hit_dice": "34d8 + 170"
"modifier": !!int "19"
"stats":
  - !!int "24"
  - !!int "25"
  - !!int "20"
  - !!int "19"
  - !!int "23"
  - !!int "22"
"speed": "60 ft., fly 60 ft. (hover), swim 60 ft."
"saves":
  - "constitution": !!int "11"
  - "wisdom": !!int "12"
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+13"
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+13"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+18"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+13"
"damage_resistances": "cold, fire, necrotic, psychic, radiant"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Stunned|stunned]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 28"
"languages": "all"
"cr": "20"
"traits":
  - "desc": "An animal lord represents a Forager, Hunter, or Sage (DM's choice), which\
      \ determines certain traits in this stat block."
    "name": "Animal Lordship"
  - "desc": "If the animal lord fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (4/Day)"
  - "desc": "*Wisdom Saving Throw:* DC 20, any enemy that starts its turn in a 30-foot\
      \ [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the animal lord. *Failure:* The target takes 10 (3d6) Psychic\
      \ damage, and the target is magically bewildered until the end of its next turn.\
      \ While bewildered, the target subtracts 1d4 from its saving throws."
    "name": "Lordly Presence"
  - "desc": "The animal lord has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The animal lord makes two attacks, using Rend or Radiant Ray in any combination,\
      \ and uses Animal Spirit."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +13, reach 5 ft. *Hit:* 14 (2d6 + 7) Slashing\
      \ damage plus 7 (2d6) Force damage."
    "name": "Rend"
  - "desc": "*Ranged Attack Roll:* +12, range 120 ft. *Hit:* 20 (4d6 + 6) Radiant\
      \ damage."
    "name": "Radiant Ray"
  - "desc": "The animal lord conjures an animal spirit that strikes at a creature\
      \ and then disappears. *Dexterity Saving Throw:* DC 20, one creature the animal\
      \ lord can see within 120 feet. *Failure:* 28 (4d10 + 6) Radiant damage. *Success:*\
      \ Half damage. *Failure or Success:* The target has [[disadvantage-xphb|Disadvantage]]\
      \ on attack rolls and ability checks until the end of its next turn."
    "name": "Animal Spirit"
  - "desc": "The animal lord casts one of the following spells, requiring no Material\
      \ components and using Wisdom as the spellcasting ability (spell save DC 20):\n\
      \n**At will:** [[animal-friendship-xphb|Animal Friendship]],\
      \ [[animal-messenger-xphb|Animal Messenger]], [[speak-with-animals-xphb|Speak with\
      \ Animals]]\n\n**2/day each:**\
      \ [[awaken-xphb|Awaken]], [[greater-restoration-xphb|Greater Restoration]]\n\
      \n**1/day each:** [[animal-shapes-xphb|Animal Shapes]],\
      \ [[sunburst-xphb|Sunburst]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The animal lord shape-shifts into a Huge or smaller version of the animal\
      \ it represents or a Medium or Small Humanoid, or it returns to its true form.\
      \ Its game statistics, other than its size, are the same in each form. Any equipment\
      \ it is wearing or carrying isn't transformed."
    "name": "Shape-Shift"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the animal lord; sage can expend a use to take one of the following actions.\
  \ The animal lord; sage regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The animal lord moves up to its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]],\
      \ and it makes one Rend attack."
    "name": "Feral Strike"
  - "desc": "The animal lord makes one Radiant Ray attack."
    "name": "Radiant Strike"
"source":
  - "XMM"
  - "FRHoF"
```
^statblock