---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/24
- monster/environment/forest
- monster/environment/grassland
- monster/size/gargantuan
- monster/type/dragon/metallic
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Ancient Gold Dragon"
---
# Ancient Gold Dragon
*Source: Monster Manual (2024) p. 146. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![The pure of heart have nothing to fear in the presence of an ancient gold dragon](/Compendium/bestiary/dragon/img/ancient-gold-dragon.webp#right)

Ancient gold dragons are wise and mysterious. Many aid virtuous groups, guiding them in secret or patronizing them from afar. Only when stakes are at their highest do ancient gold dragons reveal themselves in all their majesty.

## Gold Dragons

*Dragons of Hope and Majesty*

- **Habitat.** Forest, Grassland  
- **Treasure.** [Arcana](/Compendium/tables/random-magic-items-arcana.md)  

Gold dragons work to make the world a better place. The most powerful of the metallic dragons, these awe-inspiring dragons strive to protect that which is good and bend fate toward a brighter future. Their kind dispositions don't prevent gold dragons from engaging in combat when necessary, though, and they exhale brilliant flames and weakening magic to rout their foes.

Gold dragons favor grasslands and pristine forests, frequently dwelling near awe-inspiring natural wonders or guarding monuments from ancient civilizations. In their lairs, gold dragons hoard coins and gems, but they frequently put their treasure to use in pursuit of greater goals. They often use their riches to buy rare lore books, pay informants, or patronize idealistic adventurers.

### Gold Dragon Lairs

Gold dragons make their homes in places of natural and magical wonder.

## Statblock

```statblock
"name": "Ancient Gold Dragon"
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
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+10"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+17"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+16"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+9"
"damage_immunities": "fire"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 60 ft., [Darkvision](/Compendium/rules/senses.md#Darkvision)\
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
      \ use of (A) Spellcasting to cast [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md)\
      \ (level 4 version) or (B) Weakening Breath."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +17 to hit, reach 15 ft. *Hit:* 19 (2d8 + 10) Slashing\
      \ damage plus 9 (2d8) Fire damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 24, each creature in a 90-foot [Cone](/Compendium/rules/variant-rules/cone-area-of-effect-xphb.md).\
      \ *Failure:* 71 (13d10) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Strength Saving Throw:* DC 24, each creature that isn't currently affected\
      \ by this breath in a 90-foot [Cone](/Compendium/rules/variant-rules/cone-area-of-effect-xphb.md).\
      \ *Failure:* The target has [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on Strength-based [D20 Tests](/Compendium/rules/variant-rules/d20-test-xphb.md)\
      \ and subtracts 5 (1d10) from its damage rolls. It repeats the save at the end\
      \ of each of its turns, ending the effect on itself on a success. After 1 minute,\
      \ it succeeds automatically."
    "name": "Weakening Breath"
  - "desc": "The dragon casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 24, +16 to hit\
      \ with spell attacks):\n\n**At will:** [Detect Magic](/Compendium/spells/detect-magic-xphb.md),\
      \ [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md) (level 4 version),\
      \ [Shapechange](/Compendium/spells/shapechange-xphb.md) (Beast or Humanoid form\
      \ only, no [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
      \ gained from the spell, and no Concentration or [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
      \ required to maintain the spell)\n\n**1/day each:** [Flame Strike](/Compendium/spells/flame-strike-xphb.md)\
      \ (level 6 version), [Word of Recall](/Compendium/spells/word-of-recall-xphb.md),\
      \ [Zone of Truth](/Compendium/spells/zone-of-truth-xphb.md)"
    "name": "Spellcasting"
"regional_effects":
  - "desc": "The region containing an adult or ancient gold dragon's lair is altered\
      \ by its presence, creating the following effects:\n\n- **Dream Messenger.**\
      \ While in its lair, the dragon can cast [Dream](/Compendium/spells/dream-xphb.md),\
      \ requiring no Material components and using Charisma as the spellcasting ability.\
      \ When casting the spell this way, the dragon can target any creature within\
      \ 6 miles.  \n- **Foretelling Fog.** The area within 1 mile of the lair is [Lightly\
      \ Obscured](/Compendium/rules/variant-rules/lightly-obscured-xphb.md) by opalescent\
      \ fog. While in that area, creatures can't be [surprised](/Compendium/rules/conditions.md#Surprised),\
      \ as the fog swirls into shapes that warn of danger.  \n\nIf the dragon dies\
      \ or moves its lair elsewhere, these effects end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3 (4 in Lair). Immediately after\
  \ another creature's turn, the dragon can expend a use to take one of the following\
  \ actions. The dragon regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "*Charisma Saving Throw:* DC 24, one creature the dragon can see within\
      \ 120 feet. *Failure:* 24 (7d6) Force damage, and the target has the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition and is transported to a harmless demiplane until the start of the\
      \ dragon's next turn, at which point it reappears in an unoccupied space of\
      \ the dragon's choice within 120 feet of the dragon. *Failure or Success:* The\
      \ dragon can't take this action again until the start of its next turn."
    "name": "Banish"
  - "desc": "The dragon uses Spellcasting to cast [Guiding Bolt](/Compendium/spells/guiding-bolt-xphb.md)\
      \ (level 4 version)."
    "name": "Guiding Light"
  - "desc": "The dragon moves up to half its [Speed](/Compendium/rules/variant-rules/speed-xphb.md),\
      \ and it makes one Rend attack."
    "name": "Pounce"
"source":
  - "XMM"
"image": "/Compendium/bestiary/dragon/token/ancient-gold-dragon-xmm.webp"
```
^statblock

## Environment

forest, grassland