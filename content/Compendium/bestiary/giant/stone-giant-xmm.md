---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/7
- monster/environment/mountain
- monster/environment/underdark
- monster/size/huge
- monster/type/giant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Stone Giant"
---
# Stone Giant
*Source: Monster Manual (2024) p. 300. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/books/monster-manual-2025/img/stone-giant.webp#right)

## Stone Giant

*Giant of the Earth*

- **Habitat.** Mountain, Underdark  
- **Treasure.** [Armaments](/Compendium/tables/random-magic-items-armaments.md)  

In cavernous depths and amid mountain canyons, stone giants contemplate the strength and persistence of the earth. Stone giants have rugged features and skin with patterns and hues similar to the rock common near their homes. This makes them adept at blending in with their stony surroundings despite their size.

Stone giants rarely interfere in the affairs of other creatures, whether their smaller neighbors or other Giants. Most are slow to act, preferring to weather hardships or wait out perilous times. When roused to action—particularly when sites of ancient wonder or their homes are threatened—stone giants can unleash the might of mountains and crush foes with the force of an avalanche.

Stone giants often ponder the mysteries of natural wonders, such as mountain spires, crystal formations, or mystical petroglyphs. Some know much about the magic and secret messages hidden within the earth. Those who confine themselves to the Underdark often regard the surface world and its inhabitants as dreams imagined into being by slumbering primordials, strange gods, or other entities.

```statblock
"name": "Stone Giant"
"size": "Huge"
"type": "giant"
"alignment": "Neutral"
"ac": !!int "17"
"hp": !!int "126"
"hit_dice": "11d12 + 55"
"modifier": !!int "5"
"stats":
  - !!int "23"
  - !!int "15"
  - !!int "20"
  - !!int "10"
  - !!int "12"
  - !!int "9"
"speed": "40 ft."
"saves":
  - "dexterity": !!int "5"
  - "constitution": !!int "8"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+12"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 14"
"languages": "Giant"
"cr": "7"
"actions":
  - "desc": "The giant makes two attacks, using Stone Club or Boulder in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 15 ft. *Hit:* 22 (3d10 + 6) Bludgeoning\
      \ damage."
    "name": "Stone Club"
  - "desc": "*Ranged Attack Roll:* +9, range 60/240 ft. *Hit:* 15 (2d8 + 6) Bludgeoning\
      \ damage. If the target is a Large or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Boulder"
"reactions":
  - "desc": "Trigger: The giant is hit by a ranged attack roll and takes Bludgeoning,\
      \ Piercing, or Slashing damage from it. _Response:_ The giant reduces the damage\
      \ it takes from the attack by 11 (1d10 + 6), and if that damage is reduced to\
      \ 0, the giant can redirect some of the attack's force. *Dexterity Saving Throw:*\
      \ DC 17, one creature the giant can see within 60 feet. *Failure:* 11 (1d10\
      \ + 6) Force damage."
    "name": "Deflect Missile (Recharge 5-6)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/giant/token/stone-giant-xmm.webp"
```
^statblock

## Environment

mountain, underdark