# RPG Maker Project Setup Guide
## "The Case of the Missing Root Beer"

This guide provides step-by-step instructions for setting up the RPG Maker project structure.

## Initial Project Setup

### 1. Create New Project
1. Open RPG Maker MZ (or MV)
2. Select "Create New Project"
3. Project Name: "The Case of the Missing Root Beer"
4. Choose a project folder location
5. Select default resources (we'll customize later)

### 2. Project Settings
**Game Title**: The Case of the Missing Root Beer  
**Initial Party**: Blue Planet Six (Actor 001)  
**Initial Position**: Map001 (Blue's House), X: 5, Y: 7  
**Currency Unit**: "Annoyance Points" (for the mood system)  

### 3. Required Variables Setup
Create these variables in the Database > System > Variables:

| ID | Name | Purpose |
|----|------|---------|
| 001 | Quest_Main_Progress | Tracks main story progression (0-10) |
| 002 | Blue_Annoyance_Level | Blue's annoyance meter (0-100) |
| 003 | Owl_Relationship | Relationship with Owl companion (-10 to +10) |
| 004 | Clues_Found | Number of clues discovered (0-15) |
| 005 | Root_Beer_Location | Tracks root beer search progress |
| 006 | Pudding_Rescued | Has Pudding been found? (0=No, 1=Yes) |
| 007 | Scrappy_Encountered | Has player met Scrappy? (0=No, 1=Yes) |
| 008 | Miskko_Access_Level | Which floors of Miskko HQ are accessible |

### 4. Required Switches Setup
Create these switches in Database > System > Switches:

| ID | Name | Purpose |
|----|------|---------|
| 001 | Game_Started | Has the game intro played? |
| 002 | Owl_Following | Is Owl currently following? |
| 003 | Tutorial_Complete | Has tutorial been completed? |
| 004 | Miskko_HQ_Unlocked | Can player enter Miskko HQ? |
| 005 | First_Clue_Found | Has first clue been discovered? |
| 006 | Root_Beer_Missing | Is the root beer confirmed missing? |
| 007 | Pudding_Missing | Is Pudding confirmed missing? |
| 008 | Scrappy_Revealed | Has Scrappy been revealed as culprit? |

## Character Setup

### Main Character: Blue Planet Six
**Database > Actors > Actor 001**
- Name: Blue Planet Six
- Nickname: Blue  
- Class: Explorer (create custom class)
- Character Image: [Create 4-direction sprite - small blue humanoid]
- Face Image: [Create face portrait - blue alien with large eyes]
- Initial Level: 1
- EXP: 0 (no combat system needed)

**Parameters** (set all to 1, no combat):
- ATK, DEF, MAT, MDF, AGI, LUK = 1

### Companion Character: Owl
**Database > Actors > Actor 002**  
- Name: Owl
- Nickname: Owl
- Class: Companion
- Character Image: [Create owl sprite with flying/perching animations]
- Face Image: [Create owl face portrait]
- Note: Will be added/removed from party via events

## Map Structure Plan

### Map 001: Blue's House Interior
**Size**: 17x13 tiles  
**Tileset**: Interior A  
**BGM**: "Theme1" (peaceful home music)

**Key Areas**:
- Entrance (bottom center)
- Living area with TV and couch
- Kitchen area (where root beer was stored)
- Blue's bedroom
- Interaction points for tutorial

### Map 002: Neighborhood Overworld  
**Size**: 30x20 tiles  
**Tileset**: Exterior A  
**BGM**: "Field1" (outdoor exploration music)

**Key Locations**:
- Blue's House (center-left)
- Miskko HQ (top-right, large building)
- Small park area (center)
- Paths connecting all areas
- Hidden areas for secrets

### Map 003: Miskko HQ Lobby
**Size**: 20x15 tiles  
**Tileset**: Interior B (modern/office style)  
**BGM**: "Dungeon1" (mysterious corporate music)

**Key Features**:
- Reception desk with NPC
- Elevators (locked initially)
- Corporate art and decorations
- Security checkpoint

## Initial Events Setup

### Event: Game Start (Autorun on Map 001)
**Trigger**: Autorun  
**Priority**: Normal  
**Condition**: Switch "Game_Started" is OFF

```
◆Show Text: Blue Planet Six
: I can't believe it...
: My precious root beer is GONE!
: And where's Pudding? He was supposed to help me today!
◆Wait: 60 frames
◆Show Text: Blue Planet Six  
: This is the WORST day ever!
: Wait... I'm getting that annoying feeling again...
: Someone's going to pay for this!
◆Control Switches: Game_Started = ON
◆Control Variables: Blue_Annoyance_Level = 25
◆Control Switches: Root_Beer_Missing = ON
◆Control Switches: Pudding_Missing = ON
```

### Event: Tutorial Trigger (Action Button on refrigerator)
**Trigger**: Action Button  
**Priority**: Normal

```
◆Show Text: Blue Planet Six
: This is where I kept my special root beer...
: It was RIGHT HERE this morning!
◆Show Text: System
: Press the arrow keys to move around.
: Press Enter/Space to interact with objects.
: Check everything in the house for clues!
◆Control Switches: Tutorial_Complete = ON
◆Control Variables: Quest_Main_Progress = 1
```

### Event: Owl Introduction (Map transfer from house)
**Trigger**: Autorun  
**Priority**: Normal  
**Condition**: Switch "Tutorial_Complete" is ON AND Switch "Owl_Following" is OFF

```
◆Show Text: ???
: Blue! BLUE! What's all this noise about?
◆Show Picture: 1, Owl_Portrait, Upper Right
◆Show Text: Owl
: You're making enough racket to wake the dead!
: What's got you so worked up?
◆Show Text: Blue Planet Six
: Owl! Someone stole my root beer!
: And Pudding is missing too!
◆Show Text: Owl
: *sigh* Alright, alright. I'll help you look.
: But we're doing this MY way - methodically.
◆Add Actor: Owl
◆Control Switches: Owl_Following = ON
◆Show Text: System
: Owl joined your party!
: Owl will follow you and provide helpful advice.
```

## Asset Requirements

### Character Sprites Needed
- **Blue Planet Six**: 32x32 pixel sprite, 4-direction movement, 3 frames per direction
  - Colors: Bright blue body, large eyes, simple design
  - Emotions: Normal, annoyed, angry expressions
- **Owl**: 32x32 pixel sprite, flying/walking animations
  - Colors: Brown and white, wise appearance
  - Should look like a helpful companion

### Map Assets
- Modern house interior tileset
- Suburban neighborhood exterior
- Corporate office building interior
- Interactive object sprites (refrigerator, TV, etc.)

### UI Elements
- Custom menu theme (blue/space theme)
- Annoyance meter graphic
- Quest log interface
- Relationship indicators

## Next Steps

1. **Create the basic project** using the settings above
2. **Design and import character sprites** for Blue and Owl
3. **Build the three starter maps** with proper connections
4. **Set up the initial events** for story introduction
5. **Test the basic gameplay loop** (movement, interaction, dialogue)
6. **Add companion following system** for Owl
7. **Implement quest tracking** using variables

This foundation provides a playable start to the mystery RPG with room for expansion following the learning plan structure.