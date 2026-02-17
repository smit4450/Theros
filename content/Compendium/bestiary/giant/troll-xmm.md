---
title: Troll
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/5
- monster/environment/arctic
- monster/environment/forest
- monster/environment/hill
- monster/environment/mountain
- monster/environment/swamp
- monster/environment/underdark
- monster/size/large
- monster/type/giant
statblock: inline
aliases: ["Troll"]
---
# Troll
*Source: Monster Manual (2024) p. 310. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/giant/img/troll.webp#right|850)  
## Troll

*Loathsome, Regenerating Lurker*

- **Habitat.** Arctic, Forest, Hill, Mountain, Swamp, Underdark  
- **Treasure.** None  

Trolls creep forth to prey on smaller creatures and drag captives back to festering lairs. These misshapen brutes can regenerate from wounds and regrow severed body parts—including their heads. A troll's severed limbs continue to move and attack. Unless they're burned by flames or acid, trolls can recover from egregious wounds and seek revenge on those who felled them.

Trolls typically hunt alone, but small groups occasionally cooperate to ambush prey or raid villages. Creatures such as hags and hill giants might convince trolls to work for them in exchange for disgusting meals.
```statblock
"name": "Troll (XMM)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "94"
"hit_dice": "9d10 + 45"
"modifier": !!int "1"
"stats":
  - !!int "18"
  - !!int "13"
  - !!int "20"
  - !!int "7"
  - !!int "9"
  - !!int "7"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 15"
"languages": "Giant"
"cr": "5"
"traits":
  - "desc": "If the troll ends any turn [[conditions#Bloodied|Bloodied]]\
      \ and took 15+ Slashing damage during that turn, one of the troll's limbs is\
      \ severed, falls into the troll's space, and becomes a [[troll-limb-xmm|Troll Limb]].\
      \ The limb acts immediately after the troll's turn. The troll has 1 [[conditions#Exhaustion|Exhaustion]]\
      \ level for each missing limb, and it grows replacement limbs the next time\
      \ it regains [[hit-points-xphb|Hit Points]]."
    "name": "Loathsome Limbs (4/Day)"
  - "desc": "The troll regains 15 [[hit-points-xphb|Hit Points]]\
      \ at the start of each of its turns. If the troll takes Acid or Fire damage,\
      \ this trait doesn't function on the troll's next turn. The troll dies only\
      \ if it starts its turn with 0 [[hit-points-xphb|Hit Points]]\
      \ and doesn't regenerate."
    "name": "Regeneration"
"actions":
  - "desc": "The troll makes three Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 11 (2d6 + 4) Slashing\
      \ damage."
    "name": "Rend"
"bonus_actions":
  - "desc": "The troll moves up to half its [[speed-xphb|Speed]]\
      \ straight toward an enemy it can see."
    "name": "Charge"
"source":
  - "XMM"
"image": "Compendium/bestiary/giant/token/troll-xmm.webp"
```
^statblock