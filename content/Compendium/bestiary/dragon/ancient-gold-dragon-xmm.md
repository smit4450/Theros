---
title: Ancient Gold Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/24
- monster/environment/forest
- monster/environment/grassland
- monster/size/gargantuan
- monster/type/dragon/metallic
statblock: inline
aliases: ["Ancient Gold Dragon"]
---
# Ancient Gold Dragon
*Source: Monster Manual (2024) p. 146. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![The pure of heart have not...](Compendium/bestiary/dragon/img/ancient-gold-dragon.webp#right|850)  
Ancient gold dragons are wise and mysterious. Many aid virtuous groups, guiding them in secret or patronizing them from afar. Only when stakes are at their highest do ancient gold dragons reveal themselves in all their majesty.

## Gold Dragons

*Dragons of Hope and Majesty*

- **Habitat.** Forest, Grassland  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Gold dragons work to make the world a better place. The most powerful of the metallic dragons, these awe-inspiring dragons strive to protect that which is good and bend fate toward a brighter future. Their kind dispositions don't prevent gold dragons from engaging in combat when necessary, though, and they exhale brilliant flames and weakening magic to rout their foes.

Gold dragons favor grasslands and pristine forests, frequently dwelling near awe-inspiring natural wonders or guarding monuments from ancient civilizations. In their lairs, gold dragons hoard coins and gems, but they frequently put their treasure to use in pursuit of greater goals. They often use their riches to buy rare lore books, pay informants, or patronize idealistic adventurers.

### Gold Dragon Lairs

Gold dragons make their homes in places of natural and magical wonder.
## Statblock

```statblock
"name": "Ancient Gold Dragon (XMM)"
"size": "Gargantuan"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "22"
"hp": !!int "546"
"hit_dice": "28d20 + 252"
"modifier": !!int "16"
"stats":
  - !!int "30"
  - !!int "14"
  - !!int "29"
  - !!int "18"
  - !!int "17"
  - !!int "28"
"speed": "40 ft., fly 80 ft., swim 40 ft."
"saves":
  - "dexterity": !!int "9"
  - "wisdom": !!int "10"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+10"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+17"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+16"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+9"
"damage_immunities": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 27"
"languages": "Common, Draconic"
"cr": "24"
"traits":
  - "desc": "The dragon can breathe air and water."
    "name": "Amphibious"
  - "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (4/Day, or 5/Day in Lair)"
"actions":
  - "desc": "The dragon makes three Rend attacks. It can replace one attack with a\
      \ use of (A) Spellcasting to cast [[guiding-bolt-xphb|Guiding Bolt]]\
      \ (level 4 version) or (B) Weakening Breath."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +17 to hit, reach 15 ft. *Hit:* 19 (2d8 + 10)\
      \ Slashing damage plus 9 (2d8) Fire damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 24, each creature in a 90-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 71 (13d10) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Strength Saving Throw:* DC 24, each creature that isn't currently affected\
      \ by this breath in a 90-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has [[disadvantage-xphb|Disadvantage]]\
      \ on Strength-based [[d20-test-xphb|D20 Tests]]\
      \ and subtracts 5 (1d10) from its damage rolls. It repeats the save at the\
      \ end of each of its turns, ending the effect on itself on a success. After\
      \ 1 minute, it succeeds automatically."
    "name": "Weakening Breath"
  - "desc": "The dragon casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 24, +16 to\
      \ hit with spell attacks):\n\n**At will:** [[detect-magic-xphb|Detect Magic]],\
      \ [[guiding-bolt-xphb|Guiding Bolt]] (level 4 version),\
      \ [[shapechange-xphb|Shapechange]] (Beast or Humanoid form\
      \ only, no [[temporary-hit-points-xphb|Temporary Hit Points]]\
      \ gained from the spell, and no Concentration or [[temporary-hit-points-xphb|Temporary Hit Points]]\
      \ required to maintain the spell)\n\n**1/day each:** [[flame-strike-xphb|Flame Strike]]\
      \ (level 6 version), [[word-of-recall-xphb|Word of Recall]],\
      \ [[zone-of-truth-xphb|Zone of Truth]]"
    "name": "Spellcasting"
"regional_effects":
  - "desc": "The region containing an adult or ancient gold dragon's lair is altered\
      \ by its presence, creating the following effects:\n\n- **Dream Messenger.**\
      \ While in its lair, the dragon can cast [[dream-xphb|Dream]],\
      \ requiring no Material components and using Charisma as the spellcasting ability.\
      \ When casting the spell this way, the dragon can target any creature within\
      \ 6 miles.  \n- **Foretelling Fog.** The area within 1 mile of the lair is [[lightly-obscured-xphb|Lightly\
      \ Obscured]] by opalescent\
      \ fog. While in that area, creatures can't be [[conditions#Surprised|surprised]],\
      \ as the fog swirls into shapes that warn of danger.  \n\nIf the dragon dies\
      \ or moves its lair elsewhere, these effects end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3 (4 in Lair). Immediately after\
  \ another creature's turn, the dragon can expend a use to take one of the following\
  \ actions. The dragon regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "*Charisma Saving Throw:* DC 24, one creature the dragon can see within\
      \ 120 feet. *Failure:* 24 (7d6) Force damage, and the target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition and is transported to a harmless demiplane until the start of the\
      \ dragon's next turn, at which point it reappears in an unoccupied space of\
      \ the dragon's choice within 120 feet of the dragon. *Failure or Success:* The\
      \ dragon can't take this action again until the start of its next turn."
    "name": "Banish"
  - "desc": "The dragon uses Spellcasting to cast [[guiding-bolt-xphb|Guiding Bolt]]\
      \ (level 4 version)."
    "name": "Guiding Light"
  - "desc": "The dragon moves up to half its [[speed-xphb|Speed]],\
      \ and it makes one Rend attack."
    "name": "Pounce"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/ancient-gold-dragon-xmm.webp"
```
^statblock