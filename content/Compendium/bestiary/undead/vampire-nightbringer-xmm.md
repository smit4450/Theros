---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/8
- monster/environment/underdark
- monster/environment/urban
- monster/size/small-or-medium
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Vampire Nightbringer"
---
# Vampire Nightbringer
*Source: Monster Manual (2024) p. 316*
![A vampire familiar provides a meal for a vampire spawn](/Compendium/bestiary/undead/img/vampires.webp#right)

Born of necromantic rituals and planes of existence suffused with negative energy, vampire nightbringers manipulate shadows and feed on the raw life force of living creatures.

## Vampires

*Blood-Sucking Lords of the Night*

- **Habitat.** Underdark, Urban  
- **Treasure.** Any  

Vampires disguise their accursed, immortal natures, passing as mortals to feed on the blood of the living. While the youngest vampires might be little more than bloodthirsty servants of their creators, the eldest possess incredible cunning and control over supernatural forces of the night.

Undead vampires lie dormant during the day, retreating to resting places hidden from foes and the sun's searing rays. Roll on or choose a result from the Vampire Resting Places table to inspire a vampire's grim sanctuary.

**Vampire Resting Places**

| dice: 1d6 | The Vampire's Resting Place Is... |
|-----------|-----------------------------------|
| 1 | Among the roots of a dead tree. |
| 2 | At the bottom of a stagnant pool. |
| 3 | A coffin filled with grave dirt. |
| 4 | A large pot full of blood or vinegar. |
| 5 | A space accessible only by shape-shifting. |
| 6 | Within a statue or suit of armor. |
^vampire-resting-places

### Vampire Lairs

Vampires and vampire umbral lords create sanctuaries apart from the living, whether hidden in cosmopolitan cities or sequestered in ruins where they dwelled in life.

> [!quote] A quote from Astarion, Vampire Spawn  
> 
> Darling, you are simply delicious...


## Statblock

```statblock
"name": "Vampire Nightbringer"
"size": "Small or Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "16"
"hp": !!int "142"
"hit_dice": "19d8 + 57"
"modifier": !!int "4"
"stats":
  - !!int "16"
  - !!int "18"
  - !!int "16"
  - !!int "13"
  - !!int "14"
  - !!int "15"
"speed": "30 ft., fly 30 ft. (hover)"
"saves":
  - "dexterity": !!int "7"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"damage_immunities": "cold, necrotic"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 15"
"languages": "Common plus one other language"
"cr": "8"
"traits":
  - "desc": "The vampire takes 10 Radiant damage if it starts its turn in sunlight.\
      \ While in sunlight, it has [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on attack rolls and ability checks."
    "name": "Sunlight Hypersensitivity"
"actions":
  - "desc": "The vampire makes one Bite attack and one Shadow Strike attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 7 (1d6 + 4) Piercing damage\
      \ plus 10 (3d6) Necrotic damage. The target's [Hit Point](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ maximum decreases by an amount equal to the Necrotic damage taken, and the\
      \ vampire regains [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ equal to that amount."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 7 (1d6 + 4) Slashing damage\
      \ plus 14 (4d6) Cold damage."
    "name": "Shadow Strike"
"bonus_actions":
  - "desc": "While in [Dim Light](/Compendium/rules/variant-rules/dim-light-xphb.md)\
      \ or [Darkness](/Compendium/rules/variant-rules/darkness-xphb.md), the vampire\
      \ takes the [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Shadow Stealth"
"source":
  - "XMM"
"image": "/Compendium/bestiary/undead/token/vampire-nightbringer-xmm.webp"
```
^statblock

## Environment

underdark, urban