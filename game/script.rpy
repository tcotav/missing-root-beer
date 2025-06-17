# The Case of the Missing Root Beer
# A silly mystery game created with Renpy

################################
# Init block and screen definitions
################################

init python:
    # Add any custom Python functions here
    def increase_annoyance(amount):
        global annoyance_level
        annoyance_level += amount
        if annoyance_level > 10:
            renpy.show("blue angry")
        elif annoyance_level > 5:
            renpy.show("blue annoyed")

# Define transitions
define fade = Fade(0.5, 0.0, 0.5)
define dissolve = Dissolve(0.5)
define wipeleft = CropMove(0.5, "wipeleft")

# Define audio files (to be added later)
# define audio.main_theme = "audio/main_theme.ogg"
# define audio.mystery_sound = "audio/mystery_sound.ogg"
# define audio.annoyed_sound = "audio/annoyed_sound.ogg"

################################
# Define characters
################################

define blue = Character("Blue Planet Six", color="#3498db", image="blue")
define pudding = Character("Pudding", color="#8B4513", image="pudding")
define owl = Character("Owl", color="#663300", image="owl")
define miskers = Character("Miskers", color="#4A235A", image="miskers")
define scrappy = Character("Scrappy Blue", color="#1ABC9C", image="scrappy")
define narrator = Character(None, what_italic=True)
define raccoon_worker = Character("Raccoon Worker", color="#8B4513")
define receptionist = Character("Receptionist", color="#8B4513")
define security = Character("Security Raccoon", color="#8B4513")
define janitor = Character("Janitor Raccoon", color="#8B4513")

# Define variables to track game state
default clues_found = 0
default annoyance_level = 0
default knows_about_pudding = False
default suspects_scrappy = False
default has_keycard = False
default has_disguise = False
default miskers_encountered = False
default root_beer_samples = 0

################################
# Define images (placeholders for now)
################################

# Characters
image blue normal = "images/blue_normal.png"
image blue annoyed = "images/blue_annoyed.png"
image blue angry = "images/blue_angry.png"
image blue happy = "images/blue_happy.png"

image pudding normal = "images/pudding_normal.png"
image pudding sad = "images/pudding_sad.png"
image pudding happy = "images/pudding_happy.png"

image owl normal = "images/owl_normal.png"
image owl annoyed = "images/owl_annoyed.png"
image owl thinking = "images/owl_thinking.png"

image miskers normal = "images/miskers_normal.png"
image miskers scheming = "images/miskers_scheming.png"

image scrappy normal = "images/scrappy_normal.png"
image scrappy mischievous = "images/scrappy_mischievous.png"

# Locations
image bg home = "images/bg_blue_home.png"
image bg miskko_entrance = "images/bg_miskko_entrance.png"
image bg miskko_hallway = "images/bg_miskko_hallway.png"
image bg miskko_lobby = "images/bg_miskko_lobby.png"
image bg miskko_office = "images/bg_miskko_office.png"
image bg miskko_secret = "images/bg_miskko_secret.png"

# Items
image root_beer = "images/root_beer.png"
image clue_footprints = "images/clue_footprints.png"
image clue_note = "images/clue_note.png"

################################
# The game starts here
################################

label start:
    
    # Setup - Establishing the normal world
    scene bg home
    show blue normal at left
    
    "The one-foot-tall blue humanoid, known as Blue Planet Six, shuffles around his small but cozy home, looking increasingly frustrated."
    
    blue "My root beer! Where is my special root beer?! And... wait, where's Pudding?"
    
    show owl normal at right
    
    owl "Did you misplace your root beer again? And Pudding? How do you lose a raccoon?"
    
    blue "I didn't lose anything! They were both here yesterday. My prized root beer was in the cooling unit, and Pudding was sleeping on the couch."
    
    owl "Maybe Pudding took your root beer and went for a walk?"
    
    blue "Pudding would never! We were planning to enjoy that root beer together during our weekly movie night."
    
    # Inciting Incident - Finding the first clues
    blue "Wait... what's this?"
    
    "Blue notices small raccoon footprints on the floor, accompanied by drops of what appears to be root beer."
    
    show blue annoyed
    
    blue "And why do I suddenly feel so annoyed? There's this weird feeling... like something obnoxious was here."
    
    show owl thinking
    
    owl "The footprints and drops lead outside... toward..."
    
    blue "The Miskko headquarters! That bizarre place run by that criminal raccoon Miskers!"
    
    owl "You're not seriously considering going there, are you? That place is like a labyrinth designed by someone who read Alice in Wonderland while having a fever dream."
    
    blue "I have to find Pudding and my root beer! Will you help me, Owl?"
    
    owl "..."
    
    owl "Fine. But if we end up trapped in some ridiculous raccoon prison, I'm blaming you."
    
    # Investigation Begins - Heading to Miskko HQ
    scene bg miskko_entrance
    show blue normal at left
    show owl annoyed at right
    
    "The towering Miskko headquarters looms above them, a bizarre architectural nightmare of twisting corridors, upside-down staircases, and doors that lead to nowhere."
    
    blue "According to these footprints, they went inside."
    
    menu:
        "Which entrance should we take?"
        
        "The front door":
            jump front_entrance
            
        "The suspicious side vent":
            jump side_entrance
            
        "Try to find another way":
            jump alternative_entrance

# Different entrance choices
label front_entrance:
    "Blue boldly marches toward the front entrance."
    
    scene bg miskko_lobby
    show blue normal at left
    show owl normal at right
    
    "The lobby is unexpectedly ordinary, with a reception desk and several uncomfortable-looking chairs."
    
    "A well-dressed raccoon receptionist eyes them suspiciously."
    
    "Receptionist" "Do you have an appointment with Mr. Miskers?"
    
    blue "No, but—"
    
    "Receptionist" "No appointment, no entry. Company policy."
    
    menu:
        "How should Blue respond?"
        
        "Try to sneak past when the receptionist isn't looking":
            $ annoyance_level += 1
            "Blue feels a sudden spike in annoyance as he approaches a nearby door."
            blue "Ughhh, why do I feel so irritated all of a sudden?"
            "The feeling is strange but somehow familiar..."
            jump main_hallway
            
        "Make up a story about having a delivery":
            "Blue claims to have an important delivery for someone in the building."
            "The receptionist remains skeptical but eventually lets them pass."
            jump main_hallway
            
        "Look for another way in":
            jump side_entrance

label side_entrance:
    "Blue and Owl find a suspicious-looking side vent."
    
    blue "This looks just big enough for us to squeeze through."
    
    owl "This is undignified..."
    
    scene bg miskko_hallway
    show blue normal at left
    show owl annoyed at right
    
    "They emerge in a strange hallway with doors of various sizes lining the walls."
    
    $ annoyance_level += 2
    show blue annoyed
    
    blue "Ugh, there's that annoying feeling again! It's even stronger here."
    
    jump main_hallway

label alternative_entrance:
    "Blue and Owl circle the building and find an employee entrance."
    
    "They wait until a group of raccoon workers approaches and blend in with them."
    
    scene bg miskko_hallway
    show blue normal at left
    show owl normal at right
    
    "They successfully infiltrate the building and find themselves in a hallway."
    
    jump main_hallway

# Main investigation sequence
label main_hallway:
    "The hallway stretches in both directions, with strange doors of all shapes and sizes."
    
    blue "Now where do we go? Pudding could be anywhere in this crazy place."
    
    owl "Let's look for clues. Any more root beer drips? Or that weird annoyed feeling you keep getting?"
    
    menu:
        "Which way should they go?"
        
        "Follow the subtle root beer smell coming from the left":
            $ clues_found += 1
            "Blue sniffs the air and detects a faint root beer aroma."
            jump office_area
            
        "Head right, where Blue feels more annoyed":
            $ annoyance_level += 2
            $ clues_found += 1
            show blue annoyed
            blue "I feel increasingly irritated this way... ugh, it must be important."
            owl "Your 'annoyance sense' is tingling again?"
            jump secret_room
            
        "Check a random door":
            "Blue opens a random door, revealing..."
            "A room full of raccoons having a business meeting. They all stare at the intruders."
            "One raccoon" "Are you the new interns?"
            "Blue and Owl back away slowly and close the door."
            jump main_hallway

# This is just the initial structure - the game would continue with more locations,
# clues, and eventually lead to the confrontation with Scrappy Blue

# Additional locations to be developed:
label office_area:
    scene bg miskko_office
    show blue normal at left
    show owl normal at right
    
    "Blue and Owl enter what appears to be an office area, with raccoons busily working at tiny desks."
    
    "Blue spots a familiar raccoon tail disappearing around a corner."
    
    blue "Wait! Was that Pudding?"
    
    "They hurry after the raccoon, but when they turn the corner, they find themselves in yet another bizarre corridor."
    
    # Continue investigation...
    # Add more choices and paths
    
    jump mystery_continues

label secret_room:
    scene bg miskko_secret
    show blue annoyed at left
    show owl thinking at right
    
    "Following Blue's 'annoyance sense,' they discover a hidden room."
    
    "The room is filled with empty root beer bottles and raccoon-sized furniture."
    
    blue "Someone's been having a root beer party here!"
    
    $ annoyance_level += 3
    
    "Blue's annoyance reaches new heights as he examines a small blue cushion on the floor."
    
    blue "This... this is MY cushion from home! And it feels like... like..."
    
    owl "Like what?"
    
    blue "Like when my nephew visits! That little pest Scrappy Blue!"
    
    $ suspects_scrappy = True
    
    "A new theory begins to form in Blue's mind..."
    
    # Continue investigation...
    # Add more choices and paths
    
    jump mystery_continues

# Mid-game investigation continues here
label mystery_continues:
    "The investigation continues as Blue and Owl delve deeper into the mystery..."
    
    # Midpoint twist - discovering Pudding's true role
    if suspects_scrappy and clues_found >= 3:
        jump midpoint_twist
    else:
        menu:
            "Where should we look next?"
            
            "The executive floor":
                jump executive_floor
                
            "The cafeteria":
                jump cafeteria
                
            "The maintenance tunnels":
                jump maintenance_tunnels

# Executive floor sequence
label executive_floor:
    scene bg miskko_office
    show blue normal at left
    show owl normal at right
    
    "Blue and Owl manage to find an elevator that takes them to the executive floor."
    
    "The hallways here are lined with expensive-looking decorations, all raccoon-themed."
    
    blue "Miskers must be around here somewhere. Maybe he knows where Pudding is."
    
    "As they turn a corner, they come face to face with none other than Miskers himself."
    
    show miskers normal at center
    
    miskers "Well, well, well. What do we have here? A little blue intruder and his feathered friend."
    
    $ miskers_encountered = True
    
    blue "Miskers! Where's Pudding? And my root beer?"
    
    miskers "Root beer? The beverage you're always going on about? Why would I care about your silly drink?"
    
    blue "Because Pudding disappeared with it, and all clues lead here!"
    
    miskers "Ah, the kind raccoon. Yes, I did see him earlier today. He seemed quite distressed about something."
    
    owl "What was he distressed about?"
    
    miskers "He mentioned something about protecting a special beverage from a 'smaller blue menace.' Does that mean anything to you?"
    
    $ clues_found += 2
    $ knows_about_pudding = True
    
    blue "A smaller blue menace? That sounds like..."
    
    $ annoyance_level += 3
    show blue annoyed
    
    blue "Ugh! That annoying feeling is back!"
    
    miskers "I'm afraid I can't help you further. I have an empire to run. But you're welcome to keep looking around. Just don't break anything expensive."
    
    hide miskers
    
    owl "A smaller blue menace... and that annoying feeling you keep getting... are you thinking what I'm thinking?"
    
    blue "Scrappy Blue! That miniature nuisance must be behind this!"
    
    $ suspects_scrappy = True
    
    jump mystery_continues

# Cafeteria sequence
label cafeteria:
    scene bg miskko_lobby
    show blue normal at left
    show owl normal at right
    
    "Blue and Owl find their way to the company cafeteria, which is bustling with raccoon employees on their lunch break."
    
    blue "Look at all these raccoons. Pudding could be anywhere."
    
    "As they scan the room, Blue notices something interesting on one of the tables."
    
    blue "Is that... root beer?"
    
    "They approach the table to find several bottles of root beer, but not Blue's special brand."
    
    raccoon_worker "Oh, are you here for the root beer taste test too?"
    
    blue "Taste test?"
    
    raccoon_worker "Yeah, some small blue guy has been going around collecting samples of different root beers. Said he was looking for the 'perfect formula' or something."
    
    $ clues_found += 1
    $ annoyance_level += 2
    show blue annoyed
    
    blue "A small blue guy? Did he happen to be incredibly annoying?"
    
    raccoon_worker "The most annoying! Kept saying how he was going to upstage his uncle with the ultimate root beer collection."
    
    $ suspects_scrappy = True
    
    owl "I think we just got a major clue."
    
    menu:
        "What should we do with the root beer samples?"
        
        "Take one as evidence":
            $ root_beer_samples += 1
            "Blue pockets one of the root beer samples."
            blue "This might come in handy."
            
        "Ask where the small blue guy went":
            raccoon_worker "Last I saw, he was heading to the maintenance tunnels with a raccoon helping him carry a bunch of root beer bottles."
            $ clues_found += 1
            
        "Look for more clues in the cafeteria":
            "Blue searches around and finds a discarded note."
            "The note reads: 'Meet me in storage room B with the special root beer. -S.B.'"
            $ clues_found += 2
    
    jump mystery_continues

# Maintenance tunnel sequence
label maintenance_tunnels:
    scene bg miskko_hallway
    show blue normal at left
    show owl annoyed at right
    
    "Blue and Owl find a door marked 'Maintenance - Authorized Personnel Only.'"
    
    owl "Are you sure about this? These tunnels could go on for miles."
    
    blue "If Scrappy is collecting root beers, he'd need somewhere private to store them."
    
    if has_keycard:
        "Blue uses the keycard to unlock the door."
    else:
        "Blue tries the door and surprisingly finds it unlocked."
    
    "They enter the dim maintenance tunnels, a maze of pipes and narrow corridors."
    
    "As they walk, Blue notices fresh footprints on the dusty floor - some raccoon-sized and some tiny blue footprints."
    
    $ clues_found += 1
    
    blue "Look! Pudding and someone else came through here recently."
    
    $ annoyance_level += 3
    show blue annoyed
    
    blue "And that annoying feeling is stronger than ever!"
    
    "They follow the footprints until they reach a fork in the tunnel."
    
    menu:
        "Which way should they go?"
        
        "Follow the pipe marked 'Storage B'":
            "Blue remembers the note mentioning 'Storage room B'."
            blue "This must be it!"
            $ clues_found += 1
            jump storage_room_b
            
        "Take the tunnel with more footprints":
            "They follow the tunnel with the most visible footprints."
            "The tunnel eventually leads to a small door."
            $ clues_found += 1
            jump hidden_hideout
            
        "Follow the sound of clinking bottles":
            "Blue hears a faint sound of glass bottles clinking together."
            "They follow the sound through the twisting tunnels."
            $ clues_found += 1
            jump scrappy_lab

# Midpoint twist - discovering Pudding's true role
label midpoint_twist:
    scene bg miskko_hallway
    show blue normal at left
    show owl thinking at right
    
    "As Blue and Owl continue their investigation, they turn a corner and almost bump into a familiar figure."
    
    show pudding sad at center
    
    blue "Pudding! There you are!"
    
    pudding "Blue! Oh no, you shouldn't be here! It's not safe!"
    
    blue "What do you mean? What's going on? And where's my root beer?"
    
    pudding "I didn't steal your root beer, Blue! I was trying to protect it!"
    
    blue "Protect it? From what?"
    
    pudding "From your nephew! Scrappy Blue snuck into your house and was going to take your special root beer to complete his collection."
    
    pudding "I caught him in the act, so I grabbed the root beer first and ran. He's been chasing me through Miskko headquarters ever since!"
    
    $ knows_about_pudding = True
    
    owl "So Pudding is innocent! He was trying to help you all along."
    
    blue "But why didn't you just bring the root beer back to me?"
    
    pudding "I tried! But Scrappy is surprisingly fast for his size. He's been recruiting raccoons to help trap me. I've been hiding and moving the root beer to keep it safe."
    
    "Suddenly, they hear a high-pitched voice from around the corner."
    
    scrappy "Oh Puuuuudding! Where are you hiding? You can't keep Uncle Blue's root beer forever!"
    
    pudding "He's coming! Quick, I've hidden your root beer in the old storage room. Here's the key!"
    
    "Pudding hands Blue a keycard."
    
    $ has_keycard = True
    
    pudding "I'll lead him away while you get your root beer. Meet me at the exit when you have it!"
    
    hide pudding
    
    "Pudding scurries off in the opposite direction from the voice."
    
    blue "We have to find that storage room and get my root beer!"
    
    owl "And maybe teach your nephew a lesson while we're at it."
    
    # Raising the stakes
    jump find_storage_room

# New locations for the second half of the game
label find_storage_room:
    "With Pudding's keycard and directions, Blue and Owl set off to find the storage room where the root beer is hidden."
    
    menu:
        "How should we proceed?"
        
        "Head directly to the storage area":
            jump storage_room_b
            
        "Try to find Scrappy first":
            blue "Let's confront that little pest directly!"
            jump scrappy_hunt
            
        "Look for a map of the building":
            "Blue and Owl search for a directory or map of the Miskko headquarters."
            "They find one on the wall, showing the quickest route to the storage areas."
            $ clues_found += 1
            jump storage_room_b

# Storage Room B - where the root beer is hidden
label storage_room_b:
    scene bg miskko_secret
    show blue normal at left
    show owl normal at right
    
    "They arrive at Storage Room B and use Pudding's keycard to unlock the door."
    
    "The room is filled with various supplies and equipment, but in the center sits Blue's special root beer, safely stashed inside a small refrigerator."
    
    blue "My root beer! At last!"
    
    "Just as Blue reaches for the bottle, they hear that familiar, irritating voice."
    
    show scrappy normal at center
    
    scrappy "Well, well, well! If it isn't my favorite uncle!"
    
    $ annoyance_level += 5
    show blue angry
    
    blue "Scrappy! I should have known it was you all along!"
    
    scrappy "All I wanted was to borrow your famous root beer for my collection! Is that so wrong?"
    
    blue "Yes! It's my special root beer! And you made poor Pudding run all over this crazy building!"
    
    scrappy "Details, details. Now hand it over! I've collected 99 different root beers from across the galaxy, and yours will complete my collection!"
    
    # Final confrontation
    menu:
        "How should Blue handle this situation?"
        
        "Refuse to give up the root beer":
            blue "Never! This root beer is MINE!"
            jump final_chase
            
        "Suggest a compromise":
            blue "How about I give you a SMALL sample, and you leave me and Pudding alone?"
            scrappy "Hmm... how small are we talking?"
            
            if root_beer_samples >= 1:
                blue "Here, take this other root beer sample I found instead."
                "Blue offers Scrappy the sample collected earlier."
                scrappy "This isn't the same... but it is rare... Fine, deal!"
                jump good_ending
            else:
                scrappy "Nice try, but I need the real deal! Raccoon minions, attack!"
                jump final_chase
            
        "Set a trap":
            "Blue discretely places the root beer on a shelf and steps away."
            blue "Fine, take it. It's right there."
            "As Scrappy rushes for the root beer, Blue pulls a hidden lever, dropping a net from the ceiling."
            "Scrappy is caught in the net, struggling and shouting."
            blue "Got you, you little pest!"
            jump best_ending

# Hidden hideout - Scrappy's root beer collection
label hidden_hideout:
    scene bg miskko_secret
    show blue normal at left
    show owl normal at right
    
    "They enter a small room that appears to have been converted into some kind of shrine to root beer."
    
    "Shelves line the walls, filled with 99 different bottles of root beer from across the galaxy."
    
    blue "What is this place?"
    
    owl "It looks like someone's been collecting root beer... a lot of root beer."
    
    "Blue notices a small blue cushion and a tiny desk in the corner."
    
    $ annoyance_level += 4
    show blue annoyed
    
    blue "This is definitely Scrappy's hideout. I'd recognize his annoying taste anywhere."
    
    "On the desk is a list titled 'Root Beers of the Galaxy: My Collection' with 99 entries checked off and one final entry circled: 'Uncle Blue's Special Recipe - THE CROWN JEWEL.'"
    
    $ clues_found += 2
    $ suspects_scrappy = True
    
    blue "So that's it! Scrappy wants my root beer to complete his collection!"
    
    owl "But where's Pudding in all this?"
    
    "As if on cue, they hear a commotion from the next room."
    
    pudding "Let me go! Blue will find me, and you'll be in big trouble!"
    
    scrappy "Quiet, raccoon! Once I add Uncle Blue's root beer to my collection, I'll be the most renowned root beer connoisseur in the galaxy!"
    
    blue "He's got Pudding! We need to save him and my root beer!"
    
    jump scrappy_confrontation

# Scrappy's makeshift lab
label scrappy_lab:
    scene bg miskko_office
    show blue normal at left
    show owl normal at right
    
    "They follow the sound of clinking bottles to what appears to be a makeshift laboratory."
    
    "Inside, various root beers are being analyzed, measured, and cataloged."
    
    blue "What is all this?"
    
    "They hide behind some equipment as they hear someone entering."
    
    show scrappy normal at center
    
    scrappy "Just one more root beer to analyze, and my collection will be complete! Uncle Blue will be so jealous when I become the galaxy's premier root beer expert!"
    
    "Scrappy is carrying Blue's special root beer, about to pour it into a testing apparatus."
    
    $ annoyance_level += 5
    show blue angry
    
    blue "STOP RIGHT THERE!"
    
    blue "Put down MY root beer, you miniature menace!"
    
    scrappy "Uncle Blue! How did you find me?"
    
    blue "I followed my annoyance sense. You leave a trail of irritation wherever you go!"
    
    # Final confrontation
    jump scrappy_confrontation

# Scrappy hunt - searching for Scrappy directly
label scrappy_hunt:
    scene bg miskko_hallway
    show blue annoyed at left
    show owl normal at right
    
    "Blue decides to hunt down Scrappy directly, following his 'annoyance sense.'"
    
    blue "The more annoyed I feel, the closer we must be to Scrappy."
    
    "They wander through the bizarre corridors of Miskko headquarters, with Blue's annoyance growing stronger in certain directions."
    
    "Eventually, they reach a door marked 'Authorized Personnel Only.'"
    
    $ annoyance_level += 4
    
    blue "He's in there. I can feel the annoyance radiating through the door!"
    
    "They burst through the door to find Scrappy in the middle of cataloging his root beer collection."
    
    show scrappy normal at center
    
    scrappy "Uncle Blue! How did you find my secret lab?"
    
    blue "It wasn't hard. I just followed the trail of extreme irritation you always leave behind!"
    
    scrappy "Well, you're too late! I already have your precious root beer!"
    
    "Scrappy holds up Blue's special root beer triumphantly."
    
    blue "Give it back, you miniature menace!"
    
    # Final confrontation
    jump scrappy_confrontation

# Scrappy confrontation - the final showdown
label scrappy_confrontation:
    show blue angry at left
    show owl annoyed at right
    show scrappy mischievous at center
    
    scrappy "Why should I? This root beer is the final piece of my collection! Do you know how long I've been working on this?"
    
    blue "I don't care! It's MY root beer, and you made Pudding run all over this crazy building!"
    
    if knows_about_pudding:
        blue "Pudding was trying to protect my root beer from you!"
        scrappy "That meddling raccoon! He ruined my perfect plan!"
    else:
        blue "Where is Pudding anyway?"
        scrappy "That furry friend of yours? He's locked in a closet somewhere. He tried to stop me, can you believe it?"
        $ knows_about_pudding = True
    
    scrappy "But now I have the root beer, and soon I'll be famous!"
    
    menu:
        "How should Blue handle the situation?"
        
        "Try to grab the root beer":
            "Blue lunges for the root beer, but Scrappy is surprisingly quick."
            jump final_chase
            
        "Reason with Scrappy":
            blue "Look, Scrappy, I know we don't always get along, but this isn't the way to get my attention."
            scrappy "...What do you mean?"
            blue "Is this whole root beer collection thing just to impress me?"
            
            "Scrappy looks momentarily vulnerable before putting his guard back up."
            
            scrappy "NO! I'm doing this for me! To be famous!"
            "But his voice wavers slightly."
            
            blue "What if we worked on a new root beer recipe together? Something even better than my special recipe?"
            
            "Scrappy hesitates, clearly tempted by the offer."
            
            scrappy "You'd... do that? With me?"
            
            jump compromise_ending
            
        "Set a trap":
            "Blue notices a precariously balanced shelf above Scrappy."
            blue "You know what? Fine. Keep the root beer. I'll just make more."
            "Blue secretly presses a button, causing the shelf to tilt and dump a pile of empty bottles onto Scrappy."
            "In the confusion, Blue grabs the root beer."
            jump final_chase

# Final chase sequence
label final_chase:
    scene bg miskko_hallway
    show blue angry at left
    show owl annoyed at right
    
    "Scrappy makes a run for it, clutching Blue's special root beer!"
    
    blue "After him! Don't let him escape with my root beer!"
    
    "Blue and Owl chase Scrappy through the twisting corridors of Miskko headquarters."
    
    "They run past confused raccoon workers, through bizarre rooms with upside-down furniture, and down spiraling staircases."
    
    scrappy "You'll never catch me, Uncle Blue! I'm small and quick!"
    
    blue "But I know your weakness, Scrappy!"
    
    # The chase continues through different areas
    scene bg miskko_lobby
    
    "The chase leads them back to the main lobby."
    
    "Scrappy dodges between the legs of surprised raccoon employees."
    
    blue "Excuse us! Small annoying blue menace coming through!"
    
    # The dark night of the soul
    scene bg miskko_entrance
    
    "The chase leads outside, where Scrappy heads toward a waiting spaceship."
    
    scrappy "So long, Uncle Blue! I'll send you a postcard when I'm famous!"
    
    "Scrappy is just steps away from his escape ship when..."
    
    show pudding normal at right
    
    "Pudding appears, blocking Scrappy's path!"
    
    pudding "Not so fast, tiny troublemaker!"
    
    "In his surprise, Scrappy trips and the root beer bottle flies from his hands."
    
    "Blue dives dramatically, sliding across the ground to catch the bottle just before it smashes on the pavement."
    
    blue "Gotcha!"
    
    show blue happy at left
    
    # Resolution
    "Scrappy sits on the ground, defeated."
    
    show scrappy normal at center
    
    scrappy "Fine! Keep your stupid root beer! I was so close to having the perfect collection..."
    
    # Decision time for the ending
    menu:
        "What should Blue do with Scrappy?"
        
        "Send him home with a stern warning":
            jump normal_ending
            
        "Offer to share the root beer as a peace offering":
            jump compromise_ending
            
        "Make him work for Pudding as punishment":
            jump comeuppance_ending

# Various endings

# Normal ending - Scrappy is sent home
label normal_ending:
    blue "Scrappy, I'm sending you back home. No more sneaking into my house, no more stealing my things, and no more chasing my friends around bizarre corporate headquarters!"
    
    scrappy "But Uncle Blue..."
    
    blue "No buts! Now go home and think about what you've done."
    
    "Scrappy sulks away, boarding his tiny spacecraft."
    
    scrappy "This isn't over, Uncle Blue! I'll be back with an even better plan next time!"
    
    "The ship takes off, leaving Blue, Owl, and Pudding behind."
    
    blue "Well, that was an adventure I wasn't expecting today."
    
    owl "At least you got your root beer back."
    
    pudding "And I'm free from being chased by that little blue menace!"
    
    blue "Let's go home and enjoy this root beer together. I think we've all earned it."
    
    scene bg home
    show blue happy at left
    show owl normal at right
    show pudding happy at center
    
    "Back at Blue's home, the three friends relax and share the special root beer."
    
    blue "Thanks for protecting my root beer, Pudding. You're a true friend."
    
    pudding "Anytime, Blue! Though maybe next time, let's just keep it in a locked refrigerator."
    
    owl "I have a feeling this won't be the last we see of Scrappy Blue..."
    
    blue "Probably not. But at least we know I can track him with my annoyance sense!"
    
    "THE END"
    
    return

# Compromise ending - Blue and Scrappy work together
label compromise_ending:
    blue "Look, Scrappy, if you're so interested in root beer, why don't we work together? We could create a new recipe that's even better."
    
    scrappy "You'd... really do that with me? Even after I stole your root beer and caused all this trouble?"
    
    blue "You're still my nephew, as annoying as you are. And clearly you have a passion for root beer that matches mine."
    
    pudding "Plus, it might keep him out of trouble for a while!"
    
    scrappy "I... I'd like that, Uncle Blue."
    
    "Scrappy hands back the special root beer."
    
    scrappy "But I still get to keep my collection, right?"
    
    blue "As long as you don't steal any more from me or anyone else."
    
    # Epilogue
    scene bg home
    show blue happy at left
    show scrappy normal at center
    show pudding happy at right
    
    "Over the next few weeks, Blue and Scrappy worked together in Blue's kitchen, experimenting with different root beer recipes."
    
    "To everyone's surprise, they actually got along quite well when focused on their shared passion."
    
    blue "I think we've done it! The perfect root beer!"
    
    scrappy "It's even better than your original recipe, Uncle Blue!"
    
    "They clink their glasses together in a toast."
    
    pudding "Who would have thought that a stolen root beer would lead to this?"
    
    show owl normal at left
    hide blue
    show blue happy at right
    hide pudding
    
    owl "Just wait until he steals something else next month..."
    
    blue "Let's enjoy the peace while it lasts!"
    
    "THE END"
    
    return

# Comeuppance ending - Scrappy works for Pudding
label comeuppance_ending:
    blue "Scrappy, as punishment for all the trouble you've caused, you're going to work for Pudding for a month!"
    
    scrappy "What?! No way!"
    
    pudding "I could use help organizing my recycling collection..."
    
    blue "It's either that, or I tell Grandma Blue what you've been up to."
    
    "Scrappy's eyes widen in horror."
    
    scrappy "Not Grandma Blue! She'll make me clean her entire spaceship with a toothbrush again!"
    
    scrappy "Fine! I'll work for the raccoon!"
    
    # Epilogue
    scene bg home
    show blue happy at left
    show owl normal at right
    
    "A week later, Blue and Owl visit Pudding's recycling center."
    
    show pudding happy at center
    
    pudding "Blue! Owl! Come to check on your nephew?"
    
    blue "How's he doing?"
    
    pudding "Surprisingly well! He's very organized. Come see."
    
    "They walk over to find Scrappy sorting tiny pieces of recycling with remarkable efficiency."
    
    show scrappy normal at center
    hide pudding
    
    scrappy "Uncle Blue! You won't believe it - Pudding has items from all over the galaxy in his recycling collection! I've started cataloging them all!"
    
    blue "You're... enjoying this?"
    
    scrappy "It's like my root beer collection, but with junk! And Pudding says I can keep some of the rare pieces!"
    
    "Blue looks at Pudding with surprise."
    
    show pudding happy at right
    
    pudding "What can I say? The kid's growing on me. He's still annoying, but in a helpful way now."
    
    blue "Well, I'm glad something good came out of this whole root beer fiasco."
    
    "Blue raises his bottle of special root beer."
    
    blue "Here's to finding new friends in unexpected places!"
    
    "THE END"
    
    return

# Best ending - Blue outsmarts Scrappy completely
label best_ending:
    "With Scrappy trapped in the net, Blue retrieves his special root beer and frees Pudding."
    
    show pudding happy at right
    
    pudding "Blue! You saved me and your root beer!"
    
    blue "And caught this little troublemaker in the process."
    
    "Scrappy struggles in the net, looking both annoyed and impressed."
    
    scrappy "How did you know there was a trap there? I checked this room thoroughly!"
    
    blue "I didn't. I just got lucky. But let's pretend I planned it all along."
    
    owl "What should we do with him now?"
    
    "Blue thinks for a moment, then smiles."
    
    blue "I have the perfect solution."
    
    # Epilogue
    scene bg home
    show blue happy at left
    show owl normal at center
    show pudding happy at right
    
    "Back at Blue's home, the three friends relax and enjoy the special root beer."
    
    blue "I still can't believe Miskers agreed to let Scrappy work as an intern in his 'legitimate businesses' division."
    
    owl "It's the perfect punishment. All that corporate structure will drive him crazy."
    
    pudding "And Miskers said something about putting him in charge of the company's recycling program?"
    
    blue "Yep! Scrappy's obsessive collecting might finally be put to good use."
    
    "Blue's communication device beeps with a message."
    
    blue "It's from Scrappy! He says... he's actually enjoying the work and has already organized the entire department alphabetically, by color, AND by planet of origin."
    
    owl "Some punishment that turned out to be."
    
    blue "As long as he stays out of my house and away from my root beer, I'm happy."
    
    pudding "To solving the case of the missing root beer!"
    
    "They all clink their glasses together in celebration."
    
    "THE END"
    
    return

# Good ending - Blue gets his root beer and makes peace
label good_ending:
    "Scrappy accepts the alternative root beer sample, examining it carefully."
    
    scrappy "This is... wait, this is Zorblatt's Ultra Fizz Root Beer? This is incredibly rare!"
    
    blue "I found it during our search. Consider it a peace offering."
    
    scrappy "But I was so mean to you and Pudding..."
    
    blue "Yes, you were. But maybe next time you can just ask if you want something instead of stealing it?"
    
    "Scrappy looks down, embarrassed."
    
    scrappy "I guess I could try that..."
    
    # Epilogue
    scene bg home
    show blue happy at left
    show owl normal at right
    show pudding happy at center
    
    "Back at Blue's home, Blue, Owl, and Pudding relax after their adventure."
    
    blue "Well, that was quite a day."
    
    owl "At least we recovered your root beer and found Pudding."
    
    pudding "And maybe Scrappy learned a lesson about asking before taking?"
    
    blue "I wouldn't count on it, but at least he seemed genuinely happy with that rare root beer sample."
    
    "Blue's communication device beeps with a message."
    
    blue "It's from Scrappy. He's... inviting us to see his complete root beer collection next week. Says he'll have proper refreshments for everyone."
    
    owl "Are you going to go?"
    
    blue "You know what? I think I will. Maybe there's hope for that little pest after all."
    
    pudding "Just make sure to count your root beer bottles before and after the visit!"
    
    "They all laugh and continue enjoying their well-deserved relaxation time."
    
    "THE END"
    
    return
