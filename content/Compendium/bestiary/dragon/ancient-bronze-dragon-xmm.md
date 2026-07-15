---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/22
- monster/environment/coastal
- monster/size/gargantuan
- monster/type/dragon/metallic
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Ancient Bronze Dragon"
---
# Ancient Bronze Dragon
*Source: Monster Manual (2024) p. 60. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![An ancient bronze dragon uses its repulsion breath to protect a community from rampaging Water elementals](/Compendium/bestiary/dragon/img/ancient-bronze-dragon.webp#right)

Ancient bronze dragons develop dramatic patinas on their glimmering scales. These dragons strive to protect whole regions, continents, or planets from threats. They seek solutions to planes-spanning calamities or multiversal perils and oppose the evil of mighty chromatic dragons.

## Bronze Dragons

*Dragons of Potential and Preservation*

- **Habitat.** Coastal  
- **Treasure.** [Implements](/Compendium/tables/random-magic-items-implements.md)  

Where bronze dragons dwell, wonders flourish. Imaginative yet mindful, these metallic dragons work toward greatness and help others achieve all they can. They strive to preserve innovations, from the works of past civilizations to new discoveries, and they share such works widely. When dealing with shorter-lived beings, bronze dragons prefer to win them over through conversation and cultivation, but they don't shy from battle when villains keep others from achieving their potential.

Bronze dragons enjoy the power and endless possibilities of the sea, and they often make their lairs in places of natural beauty or communities they wish to preserve. Within their dwellings, bronze dragons hoard things they believe will be useful one day. They salvage treasure lost to the sea, reclaiming wealth or sunken ships.

### Bronze Dragon Lairs

Bronze dragons usually make their homes near or under the sea.

## Statblock

```statblock
"name": "Ancient Bronze Dragon"
"size": "Gargantuan"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "22"
"hp": !!int "444"
"hit_dice": "24d20 + 192"
"modifier": !!int "14"
"stats":
  - !!int "29"
  - !!int "10"
  - !!int "27"
  - !!int "18"
  - !!int "17"
  - !!int "25"
"speed": "40 ft., fly 80 ft., swim 40 ft."
"saves":
  - "dexterity": !!int "7"
  - "wisdom": !!int "10"
"skillsaves":
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+10"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+17"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"damage_immunities": "lightning"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 60 ft., [Darkvision](/Compendium/rules/senses.md#Darkvision)\
  \ 120 ft., passive Perception 27"
"languages": "Common, Draconic"
"cr": "22"
"traits":
  - "desc": "The dragon can breathe air and water."
    "name": "Amphibious"
  - "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (4/Day, or 5/Day in Lair)"
"actions":
  - "desc": "The dragon makes three Rend attacks. It can replace one attack with a\
      \ use of (A) Repulsion Breath or (B) Spellcasting to cast [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md)\
      \ (level 2 version)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +16, reach 15 ft. *Hit:* 18 (2d8 + 9) Slashing damage\
      \ plus 9 (2d8) Lightning damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 23, each creature in a 120-foot-long, 10-foot-wide\
      \ [Line](/Compendium/rules/variant-rules/line-area-of-effect-xphb.md). *Failure:*\
      \ 82 (15d10) Lightning damage. *Success:* Half damage."
    "name": "Lightning Breath (Recharge 5-6)"
  - "desc": "*Strength Saving Throw:* DC 23, each creature in a 30-foot [Cone](/Compendium/rules/variant-rules/cone-area-of-effect-xphb.md).\
      \ *Failure:* The target is pushed up to 60 feet straight away from the dragon\
      \ and has the [Prone](/Compendium/rules/conditions.md#Prone) condition."
    "name": "Repulsion Breath"
  - "desc": "The dragon casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 22, +14 to hit\
      \ with spell attacks):\n\n**At will:** [Detect Magic](/Compendium/spells/detect-magic-xphb.md),\
      \ [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md) (level 2 version),\
      \ [Shapechange](/Compendium/spells/shapechange-xphb.md) (Beast or Humanoid form\
      \ only, no [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
      \ gained from the spell, and no Concentration or [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
      \ required to maintain the spell), [Speak with Animals](/Compendium/spells/speak-with-animals-xphb.md),\
      \ [Thaumaturgy](/Compendium/spells/thaumaturgy-xphb.md)\n\n**1/day each:** [Detect\
      \ Thoughts](/Compendium/spells/detect-thoughts-xphb.md), [Control Water](/Compendium/spells/control-water-xphb.md),\
      \ [Scrying](/Compendium/spells/scrying-xphb.md), [Water Breathing](/Compendium/spells/water-breathing-xphb.md)"
    "name": "Spellcasting"
"regional_effects":
  - "desc": "The region containing an adult or ancient bronze dragon's lair is changed\
      \ by its presence, creating the following effects:\n\n- **Buoying Currents.**\
      \ Creatures within 1 mile of the lair that lack a [Swim Speed](/Compendium/rules/variant-rules/swim-speed-xphb.md)\
      \ ignore the extra cost of movement while swimming.  \n- **Sun and Storms.**\
      \ While in its lair, the dragon can cast [Control Weather](/Compendium/spells/control-weather-xphb.md),\
      \ requiring no Material components and using the same spellcasting ability as\
      \ its Spellcasting action. When casting the spell this way, the dragon can control\
      \ the weather within 1 mile of its lair, regardless if the dragon is inside\
      \ or outside.  \n\nIf the dragon dies or moves its lair elsewhere, these effects\
      \ end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3 (4 in Lair). Immediately after\
  \ another creature's turn, the dragon can expend a use to take one of the following\
  \ actions. The dragon regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The dragon uses Spellcasting to cast [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md)\
      \ (level 2 version)."
    "name": "Guiding Light"
  - "desc": "The dragon moves up to half its [Speed](/Compendium/rules/variant-rules/speed-xphb.md),\
      \ and it makes one Rend attack."
    "name": "Pounce"
  - "desc": "*Constitution Saving Throw:* DC 22, each creature in a 20-foot-radius\
      \ [Sphere](/Compendium/rules/variant-rules/sphere-area-of-effect-xphb.md) centered\
      \ on a point the dragon can see within 120 feet. *Failure:* 13 (3d8) Thunder\
      \ damage, and the target has the [Deafened](/Compendium/rules/conditions.md#Deafened)\
      \ condition until the end of its next turn."
    "name": "Thunderclap"
"source":
  - "XMM"
"image": "/Compendium/bestiary/dragon/token/ancient-bronze-dragon-xmm.webp"
```
^statblock

## Environment

coastal