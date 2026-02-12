---
title: Hydra
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvx
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Hydra"]
---
# Hydra
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Hydra](https://img.scryfall.com/cards/art_crop/front/6/5/65368cf0-7d92-4248-b930-633fd023065b.jpg?1578452361#right)  

```statblock
"name": "Hydra (TBVX)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "165"
"hit_dice": "15d12 + 75"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "12"
  - !!int "20"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"senses": "blindsight 0 ft., passive Perception 10"
"languages": ""
"cr": "10"
"traits":
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has three **hydra heads**. Each head is a separate creature. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 10 hit points for each head regrown in this way. The hydra's heads are friendly to one another. Its heads are attached to its body by 10-foot necks. To determine which type of head the hydra grows, roll a d20. 1: The head doesn't regrow this turn. Roll an extra time next turn. 2-13: **hydra head** 14-17: **ravenous brute head** 18: **savage vigor head** 19: **snapping fang head** 20: **shrieking titan head**"
    "name": "Hydra Heads"
"actions":
  - "desc": "Roll a d20. 1-3: **_Disorienting Glower._** On its next turn, as its action, one of the hydra's heads casts a disorienting glower at a non-head creature. That creature must succeed on a DC 10 Wisdom saving throw or become frightened of the hydra and its heads for 1 minute. 4-6: **_Distract the Hydra._** If there is a corpse within 60 feet of the hydra, the hydra moves up to its speed toward the corpse. Each of its heads has a 50% chance of spending its next turn eating that corpse. 7: **_Grown from the Stump._** If the hydra would grow any heads this turn, it grows one additional head. 8: **_Hydra's Impenetrable Hide_** If any of the hydra's heads would be reduced to 0 hit points before the hydra's next turn, it is reduced instead to 1. 9: **_Neck Tangle._** If the hydra has at least five heads, two of them become grappled by one another's necks, escape DC 17 Strength. While tangled, those heads can't move more than 5 feet from one another. 10: **_Noxious Hydra Breath._** The hydra exhales a poison gas, and each head that isn't incapacitated deals 5 necrotic damage to any non-head creature within 5 feet of that head. 11: **_Strike the Weak Spot._** Immediately after the hydra's turn ends, up to one damaged head falls off the hydra and dies. If it was an elite head, the hydra immediately takes an additional turn. 12-14: **_Swallow the Hero Whole._** Until the hydra's next turn, the next successful bite attack a head makes against a Medium or smaller target causes that head to swallow that target. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the hydra, and it takes 10 (3d6) acid damage at the start of each of the hydra's turns. The hydra can have only one target swallowed at a time. If the hydra dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 10 feet of movement, exiting prone. 15-16: **_Torn Between Heads._** Until the hydra's next turn, whenever a head bites a creature, it grapples that creature (escape DC 15). If two or more heads grapple the same creature, that creature takes 1d6 piercing damage per head that is grappling it each time a new head grapples it. The grapple ends at the start of the hydra's next turn. 17-20: **_Unified Lunge._** All the hydra's heads make a bonus bite action simultaneously if possible."
    "name": "Unpredictable"
  - "desc": "Until its next turn, the hydra and its heads have immunity to all damage."
    "name": "Indestructible Skin"
"source":
  - "TBVX"
"image": "Compendium/bestiary/monstrosity/token/hydra-tbvx.webp"
```
^statblock