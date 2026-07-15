---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/2
- monster/size/medium
- monster/type/fey
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Satyr Thornbearer"
---
# Satyr Thornbearer
*Source: Mythic Odysseys of Theros p. 243*
![](/Compendium/bestiary/fey/img/satyr-thornbearer.webp#right)

Not all satyrs live lives of pure whimsy. When forced to defend their friends and homes, satyr thornbearers are quick to take up their bows and strike against danger. Particularly amid the dense trees of the Skola Vale, these satyr skirmishers cooperate in loose teams, using guerrilla tactics to harass foes then melt back into the forest. The blessings of Nylea aid the satyrs in protecting their home, and a single arrow from a thornbearer's bow might rain down like a volley from a whole army.

While most satyrs are known for their high spirits, love of revels, and gregarious personalities, these outgoing people are neither naive nor defenseless. Some satyrs delightedly torment stuffy individuals or pull pranks on the unwary, pastimes that can predictably lead to scuffles. If a satyr can't talk their way out of a conflict—or diffuse it with a good-natured distraction—they readily defend themselves, their friends, and their homes in the Skola Vale. With diversions aside, satyrs bend their cleverness toward tactics and methods of ending conflicts as swiftly as possible. This often means turning the same skills that make them famed celebrants toward battle, be it captivating performances or the aim developed through endless games of skill. Once a threat is overcome, though, satyrs are quick to engage in their favorite part of battle: the victory celebration.

```statblock
"name": "Satyr Thornbearer"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"ac_class": "leather armor"
"hp": !!int "38"
"hit_dice": "7d8 + 7"
"modifier": !!int "4"
"stats":
  - !!int "12"
  - !!int "18"
  - !!int "12"
  - !!int "11"
  - !!int "13"
  - !!int "14"
"speed": "40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
  - "name": "[Performance](/Compendium/rules/skills.md#Performance)"
    "desc": "+6"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
"gear":
  - "shortbow"
"senses": "passive Perception 15"
"languages": "Common, Sylvan"
"cr": "2"
"traits":
  - "desc": "The satyr has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "Magic can't put the satyr to sleep."
    "name": "Sleepless Reveler"
"actions":
  - "desc": "The satyr makes three ram attacks or three shortbow attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 6 (2d4\
      \ + 1) bludgeoning damage."
    "name": "Ram"
  - "desc": "*Ranged Weapon Attack:* +6 to hit, range 80/320 ft., one target. *Hit:*\
      \ 7 (1d6 + 4) piercing damage."
    "name": "Shortbow"
  - "desc": "The satyr fires an arrow that magically transforms into a flurry of missiles\
      \ in a 30-foot cone. Each creature in that area must make a DC 14 Dexterity\
      \ saving throw, taking 17 (5d6) piercing damage on a failed save, or half as\
      \ much damage on a successful one."
    "name": "Hail of Arrows (Recharges after a Short or Long Rest)"
"source":
  - "MOT"
"image": "/Compendium/bestiary/fey/token/satyr-thornbearer-mot.webp"
```
^statblock