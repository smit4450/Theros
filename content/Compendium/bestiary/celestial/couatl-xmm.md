---
title: Couatl
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/4
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/urban
- monster/size/medium
- monster/type/celestial
statblock: inline
aliases: ["Couatl"]
---
# Couatl
*Source: Monster Manual (2024) p. 82, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/couatl.webp#right)  
## Couatl

*Guardian Manifestation of the Divine*

- **Habitat.** Desert, Forest, Grassland, Urban  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Embodiments of prophecy and protectors of divine secrets, couatls ensure fate unfolds as it should. They resemble serpents with rainbow wings, and each is a manifestation of a divine edict, a truth or fate that a righteous god decrees must hold true for all time. Most couatls appear in places of ancient power, where they guard hidden magic or ensure foretold acts do or don't come to pass. Rarely, couatls watch over communities or travel lands in disguise, interpreting omens or manipulating factors to set fate on its proper course.

Motivated by eternal mandates, couatls sometimes behave in inscrutable or antagonistic ways. They are inflexible and uncompromising, as their existences are fundamentally tied to their divine directives, but they harm other creatures only when absolutely necessary to achieve divine goals.

Each couatl goes through a period of renewal at the end of an age. In a couatl's lifecycle, an age might correspond to a celestial calendar or some divine chronology. Near the age's end, the couatl lays a wondrous, rainbow-hued egg. When the age ends, the couatl dies. For a period—perhaps a single day, perhaps until an annual solar event—the couatl's work is unattended. Once this time passes, the same couatl that laid the egg hatches from it, fully grown and renewed to serve for another age.
```statblock
"name": "Couatl (XMM)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "19"
"hp": !!int "60"
"hit_dice": "8d8 + 24"
"modifier": !!int "5"
"stats":
  - !!int "16"
  - !!int "20"
  - !!int "17"
  - !!int "18"
  - !!int "20"
  - !!int "18"
"speed": "30 ft., fly 90 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "psychic, radiant"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 15"
"languages": "all; telepathy 120 ft."
"cr": "4"
"traits":
  - "desc": "The couatl's thoughts can't be read by any means, and other creatures\
      \ can communicate with it telepathically only if it allows them."
    "name": "Shielded Mind"
"actions":
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 11 (1d12 + 5) Piercing\
      \ damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the end of the couatl's next turn."
    "name": "Bite"
  - "desc": "*Strength Saving Throw:* DC 15, one Medium or smaller creature the couatl\
      \ can see within 5 feet. *Failure:* 8 (1d6 + 5) Bludgeoning damage. The target\
      \ has the [[conditions#Grappled|Grappled]] condition (escape\
      \ DC 13), and it has the [[conditions#Restrained|Restrained]]\
      \ condition until the grapple ends."
    "name": "Constrict"
  - "desc": "The couatl casts one of the following spells, requiring no spell components\
      \ and using Wisdom as the spellcasting ability (spell save DC 15):\n\n**At will:**\
      \ [[detect-evil-and-good-xphb|Detect Evil and Good]], [[detect-magic-xphb|Detect\
      \ Magic]], [[detect-thoughts-xphb|Detect Thoughts]],\
      \ [[shapechange-xphb|Shapechange]] (Beast or Humanoid form\
      \ only, no [[temporary-hit-points-xphb|Temporary Hit Points]]\
      \ gained from the spell, and no Concentration or [[temporary-hit-points-xphb|Temporary Hit Points]]\
      \ required to maintain the spell)\n\n**1/day each:** [[create-food-and-water-xphb|Create Food and Water]],\
      \ [[dream-xphb|Dream]], [[greater-restoration-xphb|Greater Restoration]],\
      \ [[scrying-xphb|Scrying]], [[sleep-xphb|Sleep]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The couatl casts [[bless-xphb|Bless]], [[lesser-restoration-xphb|Lesser Restoration]],\
      \ or [[sanctuary-xphb|Sanctuary]], requiring no spell components\
      \ and using the same spellcasting ability as Spellcasting.\n"
    "name": "Divine Aid (2/Day)"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/celestial/token/couatl-xmm.webp"
```
^statblock