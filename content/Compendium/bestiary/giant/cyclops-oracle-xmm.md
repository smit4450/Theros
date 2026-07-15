---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/10
- monster/environment/coastal
- monster/environment/desert
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/environment/underdark
- monster/size/huge
- monster/type/giant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Cyclops Oracle"
---
# Cyclops Oracle
*Source: Monster Manual (2024) p. 88*
![](/Compendium/bestiary/giant/img/cyclopes.webp#right)

Cyclops oracles gaze through history to learn hidden truths. Many share these secrets with those who aid them in correcting the mistakes of the past.

## Cyclopes

*Monocular Servants of Destiny*

- **Habitat.** Coastal, Desert, Grassland, Hill, Mountain, Underdark  
- **Treasure.** [Armaments](/Compendium/tables/random-magic-items-armaments.md)  

Cyclopes are gigantic, one-eyed descendants of the gods. Using their mystical vision, cyclopes can witness how future events are likely to occur.

## Statblock

```statblock
"name": "Cyclops Oracle"
"size": "Huge"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"hp": !!int "207"
"hit_dice": "18d12 + 90"
"modifier": !!int "8"
"stats":
  - !!int "22"
  - !!int "11"
  - !!int "20"
  - !!int "16"
  - !!int "18"
  - !!int "10"
"speed": "40 ft."
"saves":
  - "constitution": !!int "9"
  - "wisdom": !!int "8"
"skillsaves":
  - "name": "[History](/Compendium/rules/skills.md#History)"
    "desc": "+11"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+12"
"senses": "[Truesight](/Compendium/rules/senses.md#Truesight) 30 ft., passive Perception\
  \ 22"
"languages": "Giant"
"cr": "10"
"actions":
  - "desc": "The cyclops makes three attacks, using Radiant Strike or Flash of Light\
      \ in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 10 ft. *Hit:* 22 (3d10 + 6) Radiant damage."
    "name": "Radiant Strike"
  - "desc": "*Ranged Attack Roll:* +10, range 120 ft. *Hit:* 17 (2d10 + 6) Radiant\
      \ damage, and the target has [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on attack rolls until the end of the cyclops's next turn."
    "name": "Flash of Light"
  - "desc": "The cyclops casts one of the following spells, requiring no Material\
      \ components and using Wisdom as the spellcasting ability (spell save DC 16):\n\
      \n**2/day each:** [Arcane Eye](/Compendium/spells/arcane-eye-xphb.md), [Detect\
      \ Magic](/Compendium/spells/detect-magic-xphb.md), [Locate Object](/Compendium/spells/locate-object-xphb.md)\n\
      \n**1/day:** [Legend Lore](/Compendium/spells/legend-lore-xphb.md)"
    "name": "Spellcasting"
"reactions":
  - "desc": "Trigger: The cyclops or an ally it can see makes a [D20 Test](/Compendium/rules/variant-rules/d20-test-xphb.md).\
      \ _Response:_ The cyclops rolls 1d20 and chooses whether to use that roll in\
      \ place of the d20 rolled for the [D20 Test](/Compendium/rules/variant-rules/d20-test-xphb.md)."
    "name": "Portent (Recharge 4-6)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/giant/token/cyclops-oracle-xmm.webp"
```
^statblock

## Environment

coastal, desert, grassland, hill, mountain, underdark