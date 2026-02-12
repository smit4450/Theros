---
title: Snake of the Golden Grove
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/18
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Snake of the Golden Grove"]
---
# Snake of the Golden Grove
*Source: Theros Bestiary TBVIV*  

<blockquote><small>Some fruits are best left ungathered.</small></blockquote><b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more snake cultists might be nearby who will pay tribute.
<li>A friend or foe might be dangerously close to the snake.
<li>A quest goal might involve securing one or more golden apples or a molted skin of the snake.
<li>A quest goal might involve vanquishing the guardian of the grove or protecting the guardian.

![Snake of the Golden Grove](Compendium/bestiary/beast/img/snake-of-the-golden-grove.webp#right)  

```statblock
"name": "Snake of the Golden Grove (TBVIV)"
"size": "Gargantuan"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "16"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "18"
  - !!int "18"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"senses": "blindsight 10 ft., passive Perception 10"
"languages": ""
"cr": "18"
"traits":
  - "desc": "The snake eats four golden apples from the grove and regains 42 (4d20) hit points at the start of its turn. If there are no golden apples available for the snake to eat, this trait doesn't function at the start of the snake's next turn."
    "name": "Regeneration"
  - "desc": "Immediately after initiative rolls in which the snake participates, it expects tribute from a creature within 60 feet that it can see, but does not reveal which one or indicate it expects the tribute. Tribute may be paid by bowing, genuflecting, saluting, or a similar gesture. If by the beginning of the snake's first turn in combat the creature it selected has paid it tribute, the snake sheds its skin, and emerges larger and more powerful. Until the end of combat, the snake gains a +3 bonus to damage rolls and Strength and Dexterity checks, gains 315 (30d20) temporary hit points, and loses its Regeneration trait."
    "name": "Expect Tribute"
"actions":
  - "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 18 (6d4 + 3) piercing damage, and the target must make a DC 16 Constitution saving throw, taking 20 (6d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Bite"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/beast/token/snake-of-the-golden-grove-tbviv.webp"
```
^statblock