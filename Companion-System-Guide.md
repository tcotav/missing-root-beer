# Companion System Implementation
## Owl Following System for RPG Maker

Complete guide for implementing Owl as a following companion character.

## Overview

The companion system creates an NPC (Owl) that follows the player around, provides commentary, and participates in the story without being a traditional party member in combat.

## Implementation Method

### Option 1: Follower Event (Recommended for Beginners)

#### Step 1: Create Owl Follower Event
**Event Name**: Owl_Follower  
**Event Type**: Parallel Process  
**Trigger Condition**: Switch "Owl_Following" is ON  
**Priority**: Below Characters

```
◆Control Variables: [0010:Player_X] = Player's Map X
◆Control Variables: [0011:Player_Y] = Player's Map Y  
◆Control Variables: [0012:Player_Direction] = Player's Direction
◆Control Variables: [0013:Owl_X] = This Event's Map X
◆Control Variables: [0014:Owl_Y] = This Event's Map Y

◆Conditional Branch: Variable [0010:Player_X] != Variable [0013:Owl_X] OR Variable [0011:Player_Y] != Variable [0014:Owl_Y]
  ◆Move Route: This Event
  : Move toward Player
  : Wait: 5 frames
: Branch End

◆Wait: 10 frames
```

#### Step 2: Set Owl Character Graphic
- **Character Image**: Owl sprite sheet
- **Pattern**: 1 (middle frame for idle)
- **Direction**: Fix Direction OFF
- **Walking Animation**: ON
- **Stepping Animation**: ON

#### Step 3: Map Transfer Handling
For each map transfer event, add:

```
◆Transfer Player: [Map ID], (X, Y), Retain
◆Conditional Branch: Switch [0002:Owl_Following] == ON
  ◆Transfer Event: [Owl_Follower Event], [Target Map], (X+1, Y), Retain
: Branch End
```

### Option 2: Party Member System (Advanced)

#### Add Owl to Party (from Story Events)
```
◆Change Actor Images: Owl, owl_sprite.png, owl_face.png
◆Add Actor: Owl
◆Change Formation Access: Disable
```

#### Remove from Combat
```
◆Change Class: Owl, Non_Combatant
◆Change Parameters: Owl, All Stats = 1
```

## Owl Dialogue System

### Context-Sensitive Commentary
Create events that trigger Owl's commentary based on location and situation.

#### Event: Owl Commentary (Parallel Process)
**Trigger Condition**: Switch "Owl_Following" is ON

```
◆Conditional Branch: Player is facing [Specific Object/NPC]
  ◆Conditional Branch: Switch [Owl_Comment_[Object]] == OFF
    ◆Show Text: \C[3]Owl\C[0]
    : [Contextual comment about the object]
    ◆Control Switches: [Owl_Comment_[Object]] = ON
  : Branch End
: Branch End
```

### Location-Based Comments

#### Blue's House
```
◆Show Text: \C[3]Owl\C[0]
: You really should keep your house tidier, Blue.
: A clean space leads to a clear mind.
```

#### Overworld
```
◆Show Text: \C[3]Owl\C[0]
: The neighborhood seems quiet today.
: Too quiet, if you ask me.
```

#### Miskko HQ
```
◆Show Text: \C[3]Owl\C[0]
: This place gives me the creeps.
: Corporate environments always do.
```

## Interactive Owl Features

### Talk to Owl Action
Create an Action Button event that allows the player to talk directly to Owl:

```
◆Show Text: \C[1]Blue Planet Six\C[0]
: Hey Owl, what do you think?
◆Conditional Branch: Variable [0001:Quest_Main_Progress] == 1
  ◆Show Text: \C[3]Owl\C[0]
  : We need to search your house thoroughly
  : before jumping to conclusions.
: Branch End
◆Conditional Branch: Variable [0001:Quest_Main_Progress] == 2  
  ◆Show Text: \C[3]Owl\C[0]
  : Those footprints are definitely suspicious.
  : Let's follow the trail and see where it leads.
: Branch End
◆Conditional Branch: Variable [0001:Quest_Main_Progress] >= 3
  ◆Show Text: \C[3]Owl\C[0]
  : I have a bad feeling about this Miskko place.
  : Stay alert and don't do anything rash.
: Branch End
```

### Relationship System Integration
Track how the player's actions affect their relationship with Owl:

#### Positive Relationship Events
```
◆Conditional Branch: Player chooses calm/logical option
  ◆Control Variables: [0003:Owl_Relationship] += 1
  ◆Show Text: \C[3]Owl\C[0]
  : Good thinking, Blue. I'm proud of you.
: Branch End
```

#### Negative Relationship Events  
```
◆Conditional Branch: Player chooses rash/angry option
  ◆Control Variables: [0003:Owl_Relationship] -= 1
  ◆Show Text: \C[3]Owl\C[0]
  : *sigh* Blue, you need to think before you act.
: Branch End
```

## Owl's Special Abilities

### Hint System
When the player is stuck, Owl can provide hints:

#### Event: Owl Hint (Action Button)
```
◆Conditional Branch: Variable [0004:Clues_Found] == 0
  ◆Show Text: \C[3]Owl\C[0]
  : Have you checked everywhere in your house?
  : Sometimes the most obvious places hold clues.
: Branch End
◆Conditional Branch: Variable [0004:Clues_Found] == 1
  ◆Show Text: \C[3]Owl\C[0]
  : Those footprints... where else might we find them?
  : Think about the path someone would take.
: Branch End
```

### Investigation Skills
Owl can notice things Blue misses:

```
◆Show Text: \C[3]Owl\C[0]
: Wait, Blue. Look more carefully at that.
◆Show Text: \C[3]Owl\C[0]
: My eyes are better than yours - there's
: something you missed.
◆Control Variables: [0004:Clues_Found] += 1
◆Show Text: \C[4]System\C[0]
: Owl discovered an additional clue!
```

## Technical Implementation

### Required Variables
- **[0010] Player_X**: Current player X position
- **[0011] Player_Y**: Current player Y position  
- **[0012] Player_Direction**: Player facing direction
- **[0013] Owl_X**: Current Owl X position
- **[0014] Owl_Y**: Current Owl Y position

### Required Switches
- **[0002] Owl_Following**: Is Owl currently following?
- **[0015] Owl_Can_Comment**: Can Owl make comments? (to prevent spam)
- **[0016-0030] Owl_Comment_[Location]**: Has Owl commented on this location?

### Performance Considerations
- Use **Wait** commands to prevent the follower event from running too frequently
- Limit comment frequency with cooldown switches
- Use conditional branches to minimize unnecessary processing

### Map Transfer Template
For every map transfer event:

```
◆Fadeout Screen
◆Transfer Player: [Target Map], (X, Y), Retain
◆Conditional Branch: Switch [0002:Owl_Following] == ON
  ◆Set Event Location: Owl_Follower, (X-1, Y)
: Branch End
◆Fadein Screen
```

## Troubleshooting

### Common Issues
1. **Owl gets stuck**: Increase wait time in movement route
2. **Owl moves too fast**: Add more wait frames
3. **Owl doesn't transfer between maps**: Check transfer event conditions
4. **Too many comments**: Add cooldown switches

### Testing Checklist
- [ ] Owl follows smoothly on all maps
- [ ] Owl transfers correctly between areas  
- [ ] Comments appear at appropriate times
- [ ] Relationship tracking works properly
- [ ] Hint system provides useful guidance

This companion system adds depth to the gameplay while teaching important RPG Maker concepts like parallel processing, variables, and conditional logic.