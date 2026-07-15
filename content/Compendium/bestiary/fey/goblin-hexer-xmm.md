---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/3
- monster/environment/acheron
- monster/environment/feywild
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/planar
- monster/environment/underdark
- monster/size/small
- monster/type/fey/goblinoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Goblin Hexer"
---
# Goblin Hexer
*Source: Monster Manual (2024) p. 143*
![A goblin boss, a goblin hexer, and a goblin Warrior prepare to strike against a bitter foe](/Compendium/bestiary/fey/img/goblins.webp#right)

Goblin hexers use flashy and disruptive magic. Many goblin hexers are theatrical, dressing and behaving in exaggerated mimicry of archmages.

## Goblins

*Wild Tricksters and Troublemakers*

- **Habitat.** Forest, Grassland, Hill, Planar (Acheron), Planar (Feywild), Underdark  
- **Treasure.** [Implements](/Compendium/tables/random-magic-items-implements.md), Individual  

Goblins are Feywild embodiments of recklessness and ruin. They delight in wreckage—the louder, the more energetic, and the more convoluted, the better. Goblin raids are often as much opportunities to enjoy setting fires and tormenting livestock as they are parts of more disruptive plots.

Goblins obey those who accomplish the wildest plans. Such leaders might be goblin raid masterminds, bombastic magic-users, or those capable of making the loudest noises. Hobgoblins and forceful humanoids might also command ornery groups of goblins, directing their destructiveness toward banditry, sabotage, or war.

The deity Maglubiyet claims to be the god of goblins, hobgoblins, and bugbears, and on the Infinite Battlefield of Acheron, the deity commands innumerable goblinoid legions. In ages long past, Maglubiyet witnessed the destructive propensity of goblinoids and relocated a population of them from the Feywild to his realm on the Outer Planes. Since then, hordes of these more martial-minded goblins have flourished, with some finding their ways to Material Plane worlds. These vicious invaders seek to sow ruin in preparation for their god's conquest.

> [!quote] A quote from Approximate translation from Goblin to Common: "Hey, rube!"  
> 
> Bree-yark!


## Statblock

```statblock
"name": "Goblin Hexer"
"size": "Small"
"type": "fey"
"subtype": "goblinoid"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "45"
"hit_dice": "10d6 + 10"
"modifier": !!int "3"
"stats":
  - !!int "8"
  - !!int "16"
  - !!int "12"
  - !!int "16"
  - !!int "10"
  - !!int "10"
"speed": "30 ft."
"skillsaves":
  - "name": "[Sleight of Hand](/Compendium/rules/skills.md#Sleight%20of%20Hand)"
    "desc": "+5"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Common, Goblin"
"cr": "3"
"actions":
  - "desc": "The goblin makes two Hex Stick attacks. It can replace one attack with\
      \ a use of Spellcasting."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +5, reach 5 ft. or range 60 ft. *Hit:*\
      \ 12 (2d8 + 3) Psychic damage."
    "name": "Hex Stick"
  - "desc": "The goblin casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (spell save DC 13):\n\n**At will:** [Minor Illusion](/Compendium/spells/minor-illusion-xphb.md)\n\
      \n**1/day each:** [Blindness/Deafness](/Compendium/spells/blindness-deafness-xphb.md),\
      \ [Faerie Fire](/Compendium/spells/faerie-fire-xphb.md), [Grease](/Compendium/spells/grease-xphb.md)"
    "name": "Spellcasting"
"reactions":
  - "desc": "Trigger: A creature the goblin can see hits it with an attack roll. _Response—\
      _*Wisdom Saving Throw:* DC 13, the triggering creature. *Failure:* The attack\
      \ misses instead."
    "name": "Jinx"
"source":
  - "XMM"
"image": "/Compendium/bestiary/fey/token/goblin-hexer-xmm.webp"
```
^statblock

## Environment

forest, grassland, hill, planar, acheron, planar, feywild, underdark