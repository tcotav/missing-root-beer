# Story Events Script
## "The Case of the Missing Root Beer"

Complete event scripts for implementing the story in RPG Maker.

## Opening Sequence Events

### Event: Game Introduction (Map 001 - Blue's House)
**Event Type**: Autorun  
**Trigger Condition**: Switch "Game_Started" is OFF  
**Priority**: Normal

```
◆Show Text: \C[1]Blue Planet Six\C[0]
: \I[1]Ahhhhhh! This is terrible!
◆Show Text: \C[1]Blue Planet Six\C[0]
: My precious root beer... it's GONE!
: Someone actually stole my special root beer!
◆Wait: 30 frames
◆Show Text: \C[1]Blue Planet Six\C[0]
: And where is Pudding?
: He was supposed to come over this morning!
◆Control Variables: [0002:Blue_Annoyance_Level] += 30
◆Show Text: \C[1]Blue Planet Six\C[0]
: I'm getting that feeling again...
: Someone is going to PAY for this!
◆Control Switches: [0001:Game_Started] = ON
◆Control Switches: [0006:Root_Beer_Missing] = ON
◆Control Switches: [0007:Pudding_Missing] = ON
◆Control Variables: [0001:Quest_Main_Progress] = 1
```

### Event: Refrigerator Investigation (Action Button)
**Event Type**: Action Button  
**Trigger Condition**: None  

```
◆Conditional Branch: Switch [0005:First_Clue_Found] == OFF
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : This is where I kept my special root beer...
  : It was in a special temperature-controlled compartment!
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : Wait... there are some crumbs here...
  : And these look like... tiny footprints?
  ◆Control Switches: [0005:First_Clue_Found] = ON
  ◆Control Variables: [0004:Clues_Found] += 1
  ◆Control Variables: [0002:Blue_Annoyance_Level] += 10
  ◆Show Text: \C[4]System\C[0]
  : You found your first clue!
  : Press Enter/Space to interact with objects.
  : Try checking other areas of the house!
  ◆Control Switches: [0003:Tutorial_Complete] = ON
: Branch End
◆Conditional Branch: Switch [0005:First_Clue_Found] == ON
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : Those tiny footprints are definitely suspicious...
  : Who could have such small feet?
: Branch End
```

### Event: TV Interaction (Action Button)
**Event Type**: Action Button

```
◆Show Text: \C[6]TV News Reporter\C[0]
: "...and in other news, Miskko Corporation
: announced record profits this quarter..."
◆Show Text: \C[1]Blue Planet Six\C[0]
: Miskko Corp again... 
: They're always in the news for something shady.
◆Conditional Branch: Switch [0005:First_Clue_Found] == ON
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : Wait... didn't I see a Miskko delivery truck
  : in the neighborhood yesterday?
  ◆Control Variables: [0004:Clues_Found] += 1
  ◆Show Text: \C[4]System\C[0]
  : Clue discovered! Miskko connection noted.
: Branch End
```

### Event: Couch Interaction (Action Button)
**Event Type**: Action Button

```
◆Show Text: \C[1]Blue Planet Six\C[0]
: This is where Pudding and I usually watch TV...
: There's some raccoon fur on the cushions.
◆Conditional Branch: Variable [0002:Blue_Annoyance_Level] >= 50
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : I'm getting REALLY annoyed now!
  : Whoever did this better watch out!
: Branch End
◆Control Variables: [0002:Blue_Annoyance_Level] += 5
```

## Owl Introduction Sequence

### Event: Owl Arrival (Map Transfer from House to Overworld)
**Event Type**: Autorun  
**Trigger Condition**: Switch "Tutorial_Complete" is ON AND Switch "Owl_Following" is OFF  

```
◆Show Text: ???
: Blue! BLUE! What's all the commotion?!
◆Move Route: This Event
: Face Down
: Wait: 30 frames
◆Show Picture: 1, Owl_Portrait, Upper Right, (255,255,255,255), Normal, 1
◆Show Text: \C[3]Owl\C[0]
: You're making enough noise to wake
: every neighbor in a three-block radius!
◆Show Text: \C[1]Blue Planet Six\C[0]
: Owl! Thank goodness you're here!
: Someone stole my root beer!
◆Show Text: \C[3]Owl\C[0]
: Your root beer? Are you sure you didn't
: just misplace it somewhere?
◆Show Text: \C[1]Blue Planet Six\C[0]
: NO! It was stolen! And Pudding is missing too!
: I found tiny footprints by the refrigerator!
◆Show Text: \C[3]Owl\C[0]
: *sigh* Alright, alright. I can see you're
: not going to calm down until we investigate.
◆Show Text: \C[3]Owl\C[0]
: But we're doing this MY way - methodically
: and logically. No running around screaming.
◆Add Actor: Owl
◆Control Switches: [0002:Owl_Following] = ON
◆Control Variables: [0003:Owl_Relationship] += 2
◆Erase Picture: 1
◆Show Text: \C[4]System\C[0]
: Owl joined your party!
: Owl will follow you around and provide advice.
◆Control Variables: [0001:Quest_Main_Progress] = 2
```

## Investigation Events

### Event: Neighborhood Exploration Hints
**Event Type**: Action Button (on various overworld objects)

```
# Tree Interaction
◆Show Text: \C[3]Owl\C[0]
: These trees have been here for years.
: Nothing suspicious about them.
◆Show Text: \C[1]Blue Planet Six\C[0]
: Everything looks suspicious to me right now!

# Path/Ground Interaction  
◆Conditional Branch: Variable [0004:Clues_Found] >= 2
  ◆Show Text: \C[3]Owl\C[0]
  : Wait... there are more of those tiny footprints here!
  : They lead toward that big building over there.
  ◆Show Text: \C[1]Blue Planet Six\C[0]
  : That's the Miskko headquarters!
  : I KNEW they were involved somehow!
  ◆Control Variables: [0004:Clues_Found] += 1
  ◆Control Switches: [0004:Miskko_HQ_Unlocked] = ON
: Branch End
```

## Miskko HQ Entry

### Event: Miskko HQ Door (Before Unlocked)
**Event Type**: Action Button  
**Trigger Condition**: Switch "Miskko_HQ_Unlocked" is OFF

```
◆Show Text: \C[1]Blue Planet Six\C[0]
: The door is locked tight.
◆Show Text: \C[7]Door Sign\C[0]
: "Miskko Corporation - Employees Only"
: "Authorized Personnel Required"
◆Show Text: \C[3]Owl\C[0]
: We need more evidence before we can
: justify going in there.
```

### Event: Miskko HQ Door (After Unlocked)  
**Event Type**: Action Button  
**Trigger Condition**: Switch "Miskko_HQ_Unlocked" is ON

```
◆Show Text: \C[1]Blue Planet Six\C[0]
: The footprints definitely lead here!
: Time to get some answers!
◆Show Text: \C[3]Owl\C[0]
: Remember - we're here to investigate,
: not cause trouble.
◆Transfer Player: [0003:Miskko HQ Lobby], (10, 12), Retain
```

## Miskko HQ Reception

### Event: Receptionist Interaction
**Event Type**: Action Button

```
◆Show Text: \C[5]Receptionist\C[0]
: Welcome to Miskko Corporation.
: Do you have an appointment?
◆Show Text: \C[1]Blue Planet Six\C[0]
: Someone from your company stole my root beer!
: And my friend Pudding is missing!
◆Show Text: \C[5]Receptionist\C[0]
: I... what? Sir, that's a very serious
: accusation. Do you have any proof?
◆Conditional Branch: Variable [0004:Clues_Found] >= 3
  ◆Show Text: \C[3]Owl\C[0]
  : We've been following a trail of small footprints
  : that led directly to this building.
  ◆Show Text: \C[5]Receptionist\C[0]
  : Small footprints? Oh no...
  : You don't think it could be...?
  ◆Show Text: \C[5]Receptionist\C[0]
  : I'll call upstairs. Please wait here.
  ◆Control Variables: [0008:Miskko_Access_Level] = 1
  ◆Control Variables: [0001:Quest_Main_Progress] = 3
: Branch End
```

## Quest Progress System

### Event: Annoyance Level Display (Parallel Process)
**Event Type**: Parallel Process  
**Trigger Condition**: Switch "Game_Started" is ON

```
◆Conditional Branch: Variable [0002:Blue_Annoyance_Level] >= 80
  ◆Show Picture: 99, Annoyance_Meter_High, Upper Left
: Branch End
◆Conditional Branch: Variable [0002:Blue_Annoyance_Level] >= 50
  ◆Show Picture: 99, Annoyance_Meter_Medium, Upper Left  
: Branch End
◆Conditional Branch: Variable [0002:Blue_Annoyance_Level] >= 20
  ◆Show Picture: 99, Annoyance_Meter_Low, Upper Left
: Branch End
◆Wait: 60 frames
```

## Event Implementation Notes

### Text Formatting Codes
- `\C[n]` = Change text color (1=Blue, 3=Green, 4=Yellow, 5=Purple, 6=Cyan, 7=Gray)
- `\I[n]` = Display icon n
- `\V[n]` = Display variable n value
- `\N[n]` = Display actor n name

### Variable Management
- Always increment clue counter when discoveries are made
- Update quest progress at major story milestones  
- Track relationship values for dialogue variations
- Use annoyance level to modify Blue's responses

### Switch Logic
- Use switches to prevent event repetition
- Gate content behind story progress switches
- Enable/disable areas based on quest state

This event structure provides a solid foundation for the mystery storyline while teaching key RPG Maker event concepts.