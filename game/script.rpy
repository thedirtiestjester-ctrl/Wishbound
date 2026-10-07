# Wishbound: Her Morning v0.2
# All characters in this prototype are adults (25+).

define n = Character(None)
define wish = Character("???", color="#f1a0ff")
define pc = Character("You", color="#ef9bea")
define other = Character("???", color="#b8d8ff")

image bg title = "images/bg_title.png"
image bg void = "images/bg_void.png"
image bg bedroom = "images/bg_bedroom.png"
image bg bathroom = "images/bg_bathroom.png"
image bg closet = "images/bg_closet.png"
image bg phone = "images/bg_phone.png"
image bg kitchen = "images/bg_kitchen.png"
image bg city = "images/bg_city.png"
image fx wish = "images/fx_wish.png"
image avery = "images/sprite_avery_lane.png"
image mia = "images/sprite_mia_hart.png"
image chloe = "images/sprite_chloe_vale.png"
image naomi = "images/sprite_naomi_cross.png"
image lila = "images/sprite_lila_morgan.png"
image rhea = "images/sprite_rhea_park.png"
image bg event_venue = "images/bg_event_venue.png"
image bg office_lobby = "images/bg_office_lobby.png"
image bg photo_studio = "images/bg_photo_studio.png"
image bg tattoo_studio = "images/bg_tattoo_studio.png"
image bg cafe = "images/bg_cafe.png"
image bg rooftop_club = "images/bg_rooftop_club.png"

transform sprite_enter:
    xalign .72 yalign 1.0
    alpha 0.0 xoffset 80
    ease .45 alpha 1.0 xoffset 0

transform sprite_breathe:
    xalign .72 yalign 1.0
    yoffset 0
    ease 2.1 yoffset 4
    ease 2.1 yoffset 0
    repeat

transform nervous_shake:
    xalign .72 yalign 1.0
    linear .06 xoffset -5
    linear .06 xoffset 5
    linear .06 xoffset -3
    linear .06 xoffset 3
    linear .06 xoffset 0

transform wish_burst:
    alpha 0.0 zoom .5 rotate -10
    parallel:
        ease .45 alpha 1.0
        ease .35 alpha 0.35
        ease .35 alpha 0.0
    parallel:
        ease .8 zoom 1.35 rotate 18

transform blink_in:
    alpha 0
    ease 1.2 alpha 1

init python:
    PROTAGONISTS = {
        "evan": {"name":"Evan Cole", "age":28, "job":"IT support technician", "wish":"I wish I could wake up as someone people actually notice."},
        "marcus": {"name":"Marcus Reed", "age":31, "job":"sales representative", "wish":"I wish I could wake up in a life where being wanted came easily."},
        "theo": {"name":"Theo Park", "age":25, "job":"small-time streamer", "wish":"Fine. I wish I could prove I'd make a hotter woman than anyone expects."},
    }
    REALITIES = {
        "avery": {
            "name":"Avery Lane", "age":26, "job":"event planner", "sprite":"avery",
            "home":"a stylish apartment downtown", "relationship":"complicated",
            "contact":"Noah", "contact_role":"a man saved with a heart beside his name",
            "message":"Morning, trouble. Black dress tonight? I still haven't recovered from the last time you wore it.",
            "closet":"tailored dresses, soft sweaters, heels, gym clothes, and one drawer that is aggressively more lace than you are emotionally prepared for",
            "id_note":"Her driver's license photo looks annoyingly good. The signature underneath is yours—apparently.",
            "history":"Avery has lived in the city for six years, works events, knows half the downtown bars, and has a reputation for being fearless on a dance floor.",
            "visitor":"Jules", "visitor_role":"roommate and best friend",
            "visitor_line":"If you're wearing that sleep shirt to breakfast again, I am legally allowed to judge you.",
            "ending_flirt":"You send Noah a single black-heart emoji. Three dots appear almost immediately. Your stomach flips before you can decide whether that reaction belongs to you or Avery.",
            "first_stop":"event venue", "hook":"A demanding client expects Avery to take command of a ballroom setup while Noah is scheduled to arrive with the lighting crew."
        },
        "mia": {
            "name":"Mia Hart", "age":29, "job":"management consultant", "sprite":"mia",
            "home":"a spotless condo that looks shared", "relationship":"married",
            "contact":"Daniel", "contact_role":"your husband, according to literally everything",
            "message":"Coffee is ready. Also: you stole the blankets again. I expect reparations in the form of that smile I like.",
            "closet":"expensive workwear, soft weekend clothes, dresses arranged by color, and a suspiciously confident collection of matching lingerie you refuse to inspect for more than two seconds",
            "id_note":"Mia Hart. Twenty-nine. Same address as the man whose toothbrush is beside yours.",
            "history":"Mia has been married for two years, travels for consulting work, and apparently has a habit of winning arguments with one raised eyebrow.",
            "visitor":"Daniel", "visitor_role":"husband",
            "visitor_line":"Morning, beautiful. You okay? You're looking at me like I changed overnight.",
            "ending_flirt":"You force yourself to hold Daniel's gaze and say, 'Maybe I did.' The grin he gives you is warm enough to be dangerous. Your new face answers with a blush before your old instincts can file an objection.",
            "first_stop":"office lobby", "hook":"Mia has a client presentation in less than an hour, and the executive team expects her to lead it without notes."
        },
        "chloe": {
            "name":"Chloe Vale", "age":25, "job":"fitness and lifestyle creator", "sprite":"chloe",
            "home":"a bright loft full of camera gear", "relationship":"newly engaged",
            "contact":"Sam", "contact_role":"your fiancé, backed up by dozens of photographs",
            "message":"Good morning, gorgeous. Please tell me you remember we promised the internet a 'lazy morning' post before brunch. And no, wearing my hoodie does not count as styling.",
            "closet":"athleisure in every possible shade, tiny stage outfits from sponsored shoots, oversized hoodies, and enough carefully coordinated underwear to make you close the drawer on reflex",
            "id_note":"Chloe Vale. Twenty-five. The emergency contact is Sam. The tiny engagement photo tucked behind the card is much harder to explain away.",
            "history":"Chloe built a public following around confidence, fitness, and relentless flirting with the camera. Thousands of strangers believe they know exactly how she moves and talks.",
            "visitor":"Sam", "visitor_role":"fiancé",
            "visitor_line":"There she is. I was about to come make sure my favorite menace hadn't fallen back asleep.",
            "ending_flirt":"You tilt the phone toward the mirror, copy the smile from Chloe's feed, and take one cautious selfie. It is unfair how natural it looks. Sam reacts with three heart-eyes before you even lower the phone.",
            "first_stop":"photo studio", "hook":"A sponsored couples shoot is already on the schedule, and the photographer expects Chloe's practiced confidence."
        },
        "naomi": {
            "name":"Naomi Cross", "age":33, "job":"tattoo artist and studio owner", "sprite":"naomi",
            "home":"a dark, art-filled apartment above her studio", "relationship":"single, with an ex who still texts too comfortably",
            "contact":"Vera", "contact_role":"your ex-girlfriend and fellow artist",
            "message":"You left your leather jacket at my place again. If this is your strategy for getting invited back, it is annoyingly effective.",
            "closet":"black denim, fitted tanks, boots, soft sleepwear, work aprons, and a drawer of daring night-out pieces that make you wonder how often Naomi enjoyed being stared at",
            "id_note":"Naomi Cross. Thirty-three. Owner of Crossline Studio. The license photo has the same cool stare currently failing to appear on your face.",
            "history":"Naomi owns a respected tattoo studio, knows nearly everyone in the local art scene, and has a reputation for being fearless, blunt, and impossible to embarrass.",
            "visitor":"Tess", "visitor_role":"studio manager and oldest friend",
            "visitor_line":"Boss, if you're awake, your ten o'clock moved early. Also Vera is downstairs pretending she isn't here to see you.",
            "ending_flirt":"You type, 'Maybe I just like knowing you keep my things.' Vera replies with a single: 'Dangerous answer.' Your pulse approves before your common sense does.",
            "first_stop":"tattoo studio", "hook":"Your first client trusts Naomi completely, and Vera is waiting by the front desk with history written all over her expression."
        },
        "lila": {
            "name":"Lila Morgan", "age":28, "job":"pastry chef and café co-owner", "sprite":"lila",
            "home":"a cozy apartment that smells faintly of vanilla and coffee", "relationship":"quietly dating",
            "contact":"June", "contact_role":"your girlfriend, currently trying to keep the relationship private from coworkers",
            "message":"Morning, pretty girl. I saved you the corner table. Try not to smile at me like that in front of the staff or they're finally going to figure us out.",
            "closet":"soft cardigans, chef whites, practical jeans, date-night dresses, and a few surprisingly bold pieces hidden behind an apron collection",
            "id_note":"Lila Morgan. Twenty-eight. Co-owner of Juniper Café. A folded photo booth strip shows you kissing June with zero ambiguity.",
            "history":"Lila is known for being gentle, observant, and devastatingly good at remembering everyone's favorite dessert. The café staff treats her like the emotional center of the place.",
            "visitor":"Mara", "visitor_role":"younger business partner, age 27",
            "visitor_line":"Lila? Please tell me you're up. The croissant delivery is wrong and June is doing that calm thing she does when she's absolutely not calm.",
            "ending_flirt":"You send June: 'Maybe they should figure it out.' The typing indicator appears, vanishes, then returns. You have apparently found a button Lila rarely pressed.",
            "first_stop":"café", "hook":"The morning rush expects Lila's practiced warmth while June tries very hard not to look like your girlfriend."
        },
        "rhea": {
            "name":"Rhea Park", "age":30, "job":"DJ and rooftop club manager", "sprite":"rhea",
            "home":"a minimalist high-rise apartment full of vinyl and stage clothes", "relationship":"casually dating",
            "contact":"Dani", "contact_role":"a bartender you've apparently been seeing for three months",
            "message":"Soundcheck at four. Drinks after? And yes, I'm still thinking about the red top. You knew exactly what you were doing.",
            "closet":"streetwear, fitted stage looks, platform boots, oversized jackets, glittering accessories, and several outfits clearly engineered to win arguments with gravity",
            "id_note":"Rhea Park. Thirty. Venue manager and resident DJ at Halo Roof. Your access badge opens every staff door in the building.",
            "history":"Rhea built her reputation on controlled chaos: packed dance floors, cool confidence, and an uncanny ability to make a room follow her mood.",
            "visitor":"Alex", "visitor_role":"club co-manager and longtime friend",
            "visitor_line":"Rhea, tell me you did not forget the promoter meeting. Also Dani asked if you're 'still pretending last night didn't happen,' which feels above my pay grade.",
            "ending_flirt":"You answer Dani: 'Depends which part you mean.' The response is only a smirking emoji and a time. Apparently Rhea's confidence came with consequences.",
            "first_stop":"rooftop club", "hook":"A promoter meeting, a soundcheck, and Dani's knowing smile are waiting at the venue before you've learned how Rhea even walks in those boots."
        }
    }

    def apply_rewrite(pid, rid):
        global original, reality, player_name, player_age, evidence_count
        global reality_name, reality_age, reality_contact, reality_contact_role, reality_message
        global reality_relationship, reality_closet, reality_id_note, reality_history
        global reality_visitor, reality_visitor_role, reality_visitor_line, reality_ending_flirt
        global reality_first_stop, reality_hook
        original = PROTAGONISTS[pid].copy()
        reality = REALITIES[rid].copy()
        player_name = reality["name"]
        player_age = reality["age"]
        reality_name = reality["name"]
        reality_age = reality["age"]
        reality_contact = reality["contact"]
        reality_contact_role = reality["contact_role"]
        reality_message = reality["message"]
        reality_relationship = reality["relationship"]
        reality_closet = reality["closet"]
        reality_id_note = reality["id_note"]
        reality_history = reality["history"]
        reality_visitor = reality["visitor"]
        reality_visitor_role = reality["visitor_role"]
        reality_visitor_line = reality["visitor_line"]
        reality_ending_flirt = reality["ending_flirt"]
        reality_first_stop = reality.get("first_stop", "city")
        reality_hook = reality.get("hook", "The rewritten life is already demanding your attention.")
        evidence_count = 0

    def discover(label):
        global evidence_count, seen_mirror, seen_phone, seen_closet, seen_wallet
        if label == 'mirror' and not seen_mirror:
            seen_mirror = True; evidence_count += 1
        elif label == 'phone' and not seen_phone:
            seen_phone = True; evidence_count += 1
        elif label == 'closet' and not seen_closet:
            seen_closet = True; evidence_count += 1
        elif label == 'wallet' and not seen_wallet:
            seen_wallet = True; evidence_count += 1

    def current_sprite():
        return reality.get('sprite', 'avery')

    if persistent.spice_mode is None:
        persistent.spice_mode = True

default original = {}
default reality = {}
default original_name = "Evan Cole"
default original_age = 28
default original_job = "IT support technician"
default reality_name = "Avery Lane"
default reality_age = 26
default reality_contact = "Noah"
default reality_contact_role = "a contact"
default reality_message = "Morning."
default reality_relationship = "complicated"
default reality_closet = "a complete wardrobe"
default reality_id_note = "The ID is valid."
default reality_history = "The history is internally consistent."
default reality_visitor = "Jules"
default reality_visitor_role = "friend"
default reality_visitor_line = "Morning."
default reality_ending_flirt = "You send a reply."
default reality_first_stop = "city"
default reality_hook = "The rewritten life is already demanding your attention."
default protagonist_id = "evan"
default reality_id = "avery"
default player_name = "Avery Lane"
default player_age = 26
default evidence_count = 0
default seen_mirror = False
default seen_phone = False
default seen_closet = False
default seen_wallet = False
default curiosity = 0
default boldness = 0
default acceptance = 0
default suspicion = 0
default first_choice = ""
default ending = ""

label start:
    $ quick_menu = False
    scene bg title
    with fade
    centered "{size=46}{b}CONTENT NOTE{/b}{/size}\n\nAll characters in this prototype are adults aged 25+.\nLewd Reactions mode contains suggestive humor, body/clothing awareness, flirtatious messages, and romantic awkwardness—no explicit sex scenes."
    menu:
        "Lewd Reactions: ON (default)":
            $ persistent.spice_mode = True
        "Use milder reaction lines":
            $ persistent.spice_mode = False
    window hide
    $ protagonist_id = renpy.call_screen("protagonist_select")
    $ original = PROTAGONISTS[protagonist_id].copy()
    $ original_name = original["name"]
    $ original_age = original["age"]
    $ original_job = original["job"]
    $ quick_menu = True

    scene bg void
    with dissolve
    n "[original_name], age [original_age], had spent the last few years becoming extremely good at being overlooked."
    n "The job—[original_job]—was stable. The apartment was tolerable. The dating apps were mostly an archaeological record of conversations that died after 'hey.'"

    if protagonist_id == "evan":
        pc "I don't need to be famous. I just want to know what it feels like when people actually look at me and mean it."
    elif protagonist_id == "marcus":
        pc "Everybody keeps saying confidence makes life easier. Great. I wish I could wake up as somebody who already has it."
    else:
        pc "People online keep saying I couldn't handle being a woman for a day. Please. I'd probably be devastating."

    show fx wish at wish_burst
    wish "A wish should be specific."
    pc "...Who said that?"
    wish "Too late."
    n "Something bright folds through the room without casting a shadow. Your stomach drops as though the floor forgot where it belonged."
    wish "Let's find out what kind of woman reality thinks you asked to become."

    $ quick_menu = False
    window hide
    $ reality_id = renpy.call_screen("reality_select")
    $ apply_rewrite(protagonist_id, reality_id)
    $ seen_mirror = False
    $ seen_phone = False
    $ seen_closet = False
    $ seen_wallet = False
    $ curiosity = 0
    $ boldness = 0
    $ acceptance = 0
    $ suspicion = 0
    $ quick_menu = True

    show fx wish at wish_burst
    with hpunch
    n "Your name, your address, your past, and every memory anyone else has of you are rewritten in the space between one heartbeat and the next."
    scene black
    with Fade(.5,.5,1.2)

    jump awakening

label awakening:
    scene bg bedroom
    with blink_in
    n "Morning arrives in pieces. Soft sheets. A ceiling you don't recognize. Hair tickling your cheek."
    pc "Nnngh..."
    n "The sound stops you cold."
    pc "That was not my voice."
    if persistent.spice_mode:
        n "You sit up too quickly. The unfamiliar weight against your chest moves a fraction later than the rest of you, and you immediately yank the blanket higher as if modesty can somehow reverse physics."
    else:
        n "You sit up too quickly. Your proportions, balance, hair, and voice are all unmistakably wrong."
    n "Your hands are smaller. Your nails are neat. Your legs under the blanket are smooth and very definitely not the legs you went to sleep with."
    pc "No. No, no, no."
    n "A phone on the nightstand lights up. The lock screen is a photograph of a woman you have never met."
    n "Then you realize you're seeing the same face reflected faintly in the black glass."
    pc "...Oh, you've got to be kidding me."
    n "Somewhere beyond the bedroom door, a life is already in progress."
    n "You need evidence before you open that door."
    jump exploration

label exploration:
    scene bg bedroom
    $ choice = renpy.call_screen("bedroom_hub")
    if choice == "mirror":
        call inspect_mirror
    elif choice == "phone":
        call inspect_phone
    elif choice == "closet":
        call inspect_closet
    elif choice == "wallet":
        call inspect_wallet
    elif choice == "continue":
        jump morning_reveal
    jump exploration

label inspect_mirror:
    $ discover('mirror')
    scene bg bathroom
    with dissolve
    if reality_id == "avery":
        show avery at sprite_enter
    elif reality_id == "mia":
        show mia at sprite_enter
    elif reality_id == "chloe":
        show chloe at sprite_enter
    elif reality_id == "naomi":
        show naomi at sprite_enter
    elif reality_id == "lila":
        show lila at sprite_enter
    else:
        show rhea at sprite_enter
    n "The woman in the mirror is [reality_name], age [reality_age]. At least, that is what the universe has decided."
    n "She copies every tiny movement you make. The expression of escalating disbelief is entirely yours."
    pc "Okay. That's... me. Apparently."
    menu:
        "Immediately cover up and focus on the face.":
            $ suspicion += 1
            pc "Eyes up. Face. Hair. Important details. Everything below the neck can file an appointment."
            n "It is a sensible plan, ruined slightly by the mirror showing you blushing at your own reflection."
        "Take an embarrassingly thorough look.":
            $ curiosity += 2
            $ boldness += 1
            if persistent.spice_mode:
                n "You tell yourself this is an inventory. Purely scientific. That excuse lasts approximately three seconds."
                n "The sleep shirt hangs differently on a body with curves. When you turn sideways, your gaze gets caught on the silhouette, and you make the fatal mistake of testing what happens when you straighten your posture."
                pc "...Wow."
                n "The woman in the mirror looks far too pleased with that reaction. Unfortunately, she is you."
                pc "This does not count as staring if I'm technically the person being stared at."
            else:
                n "You study height, posture, face, hands, hair, and proportions until the reflection stops feeling like a photograph and starts feeling alarmingly responsive."
        "Test the new voice and mannerisms.":
            $ curiosity += 1
            $ acceptance += 1
            pc "Hello. I'm [reality_name]."
            n "The first attempt is stiff. The second accidentally lands on a warmer cadence that feels practiced."
            if persistent.spice_mode:
                pc "...And apparently I can make my own name sound flirty. That's going to be a problem."
            else:
                pc "That sounded way too natural."
    $ renpy.call_screen("evidence_card", "MIRROR EVIDENCE", "Body: [reality_name], age [reality_age]. Your original memories remain intact, but the new body already has tiny habits your muscles seem to remember.")
    return

label inspect_phone:
    $ discover('phone')
    scene bg phone
    with dissolve
    n "Face recognition unlocks immediately. Of course it does."
    n "The home screen is an ambush: work apps, photos, social media, contacts, calendar reminders, and years of messages."
    pc "This isn't a fake profile. It's a whole life."
    n "A message from [reality_contact] sits at the top. [reality_contact_role]."
    other "[reality_message]"
    menu:
        "Do not touch anything. This is evidence.":
            $ suspicion += 1
            pc "Nope. Not replying until I know whether I'm walking into a date, a marriage, or a hostage negotiation conducted through emojis."
        "Scroll the photos for clues.":
            $ curiosity += 2
            n "There are vacations you never took, birthdays you never celebrated, candid pictures where your new face is laughing with total ease."
            if persistent.spice_mode:
                n "There are also enough glamorous selfies to establish that [reality_name] knew exactly which angles made strangers lose their train of thought. You resent how effective they are."
            else:
                n "There are enough carefully composed selfies to establish that [reality_name] is very comfortable in front of a camera."
        "Flirt back experimentally.":
            $ boldness += 2
            $ acceptance += 1
            if persistent.spice_mode:
                pc "Purely as a diagnostic test."
                n "You type: 'Maybe. Depends how convincingly you ask.'"
                n "The reply arrives so fast you nearly drop the phone."
                other "Oh, we're starting early today? I like this version of you."
                pc "I have made a tactical error."
            else:
                n "You send a cautious heart emoji and immediately regret the confidence implied by it."
    $ renpy.call_screen("evidence_card", "PHONE EVIDENCE", "Relationship status: [reality_relationship]. Key contact: [reality_contact]. The phone contains years of internally consistent history and recognizes you as its owner.")
    return

label inspect_closet:
    $ discover('closet')
    scene bg closet
    with dissolve
    n "The closet answers one question immediately: [reality_name] did not dress like you."
    n "You find [reality_closet]."
    menu:
        "Choose the safest, loosest outfit available.":
            $ suspicion += 1
            n "You assemble something conservative enough to function as emotional armor."
            pc "Great. Clothes. Normal clothes. I can work with clothes."
        "Try the outfit that looks most like 'her.'":
            $ acceptance += 2
            $ curiosity += 1
            if persistent.spice_mode:
                n "The outfit fits with insulting precision. You tug at the hem, adjust the neckline twice, then catch the mirror proving that the problem is not the clothing. The problem is that you look good in it."
                pc "I hate how much this works."
                n "A traitorous little thrill answers before your dignity can."
            else:
                n "The outfit fits perfectly and changes your posture almost immediately. You look less like someone borrowing a body and more like the person the room expects."
        "Open the drawer you already know is a bad idea.":
            $ curiosity += 2
            if persistent.spice_mode:
                n "You stare into a drawer of coordinated lace and immediately close it."
                pc "Information acquired. Too much information acquired."
                n "After a three-second pause, you open it again just long enough to confirm that yes, apparently [reality_name] had opinions about color coordination."
                pc "This is research. Stop judging me."
            else:
                n "You discover a drawer of personal clothing, decide boundaries are healthy, and close it again."
    $ renpy.call_screen("evidence_card", "CLOSET EVIDENCE", "The wardrobe is consistent with [reality_name]'s job and public persona. Nothing looks newly planted; wear patterns, receipts, and laundry make the history feel lived-in.")
    return

label inspect_wallet:
    $ discover('wallet')
    scene bg bedroom
    with dissolve
    n "The wallet is worse because official documents don't have a sense of humor."
    n "[reality_id_note]"
    n "Cards, receipts, membership IDs, insurance information. Every system agrees that [reality_name] exists."
    pc "What happened to [original_name]?"
    n "Searching your old name on the phone gives you nothing useful. No social profile. No contact card. No old apartment lease."
    pc "Reality didn't move me. It edited me out."
    $ suspicion += 2
    $ renpy.call_screen("evidence_card", "IDENTITY EVIDENCE", "Legal identity: [reality_name], [reality_age]. Original identity: absent from local records. Reality appears retroactively rewritten rather than merely disguised.")
    return

label morning_reveal:
    scene bg bedroom
    with dissolve
    n "You know enough to be frightened properly now."
    n "[reality_history]"
    n "Then someone knocks."
    other "[reality_visitor_line]"
    pc "..."
    n "[reality_visitor]—your [reality_visitor_role]—is on the other side of the door."
    menu:
        "Open the door and imitate the version of you they expect.":
            $ acceptance += 2
            $ boldness += 1
            $ first_choice = "perform"
            pc "Coming!"
            n "Your new voice answers before your nerves finish voting."
        "Ask for a minute and panic quietly.":
            $ suspicion += 1
            $ first_choice = "stall"
            pc "One minute!"
            n "The answer comes in a tone that suggests this is completely normal behavior for [reality_name]. Somehow that is more unsettling."
        "Open the door and tell a careful half-truth.":
            $ curiosity += 1
            $ first_choice = "honest"
            pc "I'm having a really strange morning."
            other "That sounds ominous. Coffee first?"

    scene bg kitchen
    with dissolve
    if reality_id == "avery":
        show avery at sprite_breathe
    elif reality_id == "mia":
        show mia at sprite_breathe
    elif reality_id == "chloe":
        show chloe at sprite_breathe
    elif reality_id == "naomi":
        show naomi at sprite_breathe
    elif reality_id == "lila":
        show lila at sprite_breathe
    else:
        show rhea at sprite_breathe

    n "Breakfast becomes an interrogation where only one person knows an interrogation is happening."
    n "You learn little things by pretending to remember them: how you take your coffee, where you left your keys, which cupboard has the mugs."
    if persistent.spice_mode:
        n "More dangerous are the tiny familiar gestures from [reality_visitor]—a teasing look, an easy compliment, the kind of closeness your new body reacts to a fraction before your old brain understands why."
    else:
        n "More dangerous are the tiny familiar gestures from [reality_visitor], because your new body's instinctive responses occasionally arrive before conscious recognition."

    if reality_id == "mia":
        other "You really are acting weird. Come here."
        n "Daniel leans in and kisses your forehead, casual and affectionate."
        if persistent.spice_mode:
            n "Your entire brain stalls over the fact that the gesture feels familiar to a body you've inhabited for less than an hour."
            pc "...System error."
        else:
            pc "I—sorry. Just tired."
    elif reality_id == "avery":
        other "Also Noah texted me because apparently you're ignoring him. Whatever game you're playing, he's extremely invested."
        pc "That's... useful information."
    elif reality_id == "chloe":
        other "Sam says brunch is at eleven and asked whether you're still doing the couple-photo thing."
        if persistent.spice_mode:
            pc "The what thing?"
            other "The cute one where you pretend you don't know the camera loves you."
            pc "Right. That thing I definitely remember doing."
        else:
            pc "Right. The photo."
    elif reality_id == "naomi":
        other "And Vera is downstairs wearing the expression that means the two of you have unresolved business."
        if persistent.spice_mode:
            pc "How unresolved?"
            other "Based on the jacket situation? Extremely."
    elif reality_id == "lila":
        other "June saved your corner table again. You two are the least convincing secret couple I've ever seen."
        pc "We're a— right. Of course we are."
    else:
        other "Dani wants to know whether you're still pretending last night was 'just drinks.' I declined to become involved."
        if persistent.spice_mode:
            pc "That sentence raised more questions than it answered."
        else:
            pc "I'll... handle it."

    n "By the time you escape with your phone and keys, one fact is unavoidable: nobody is pretending."
    n "To everyone else, you have always been [reality_name]."
    jump outside_choice

label outside_choice:
    scene bg city
    with dissolve
    n "Outside, the city is offensively normal."
    pc "So what now?"
    menu:
        "Play along for one day—and see how far this new life goes.":
            $ ending = "play"
            $ acceptance += 3
            jump ending_play
        "Investigate the wish and find a way to reverse it.":
            $ ending = "investigate"
            $ suspicion += 3
            jump ending_investigate
        "Lean into the most dangerous part of the new identity.":
            $ ending = "flirt"
            $ boldness += 3
            jump ending_flirt

label ending_play:
    n "One day. You can survive one day as [reality_name]."
    n "You straighten your shoulders and head toward [reality_first_stop], because this new life has no intention of waiting for you to catch up."
    n "[reality_hook]"

    if reality_id == "avery":
        scene bg event_venue
        with dissolve
        n "The ballroom staff greets you by name. A clipboard is placed in your hand before you can admit you don't know what half the notes mean."
        other "Avery! Lighting wants your approval. Noah's crew is five minutes out."
        if persistent.spice_mode:
            n "Apparently 'being noticed' includes having three people watch you walk across the room like you own it. Avery's heels know what they're doing even if you don't."
    elif reality_id == "mia":
        scene bg office_lobby
        with dissolve
        n "The security gate accepts your badge. Two coworkers immediately fall into step beside you and start asking for decisions."
        other "Mia, the client moved the presentation up. You're still leading, right?"
        pc "Naturally."
        n "Your mouth says it with a confidence your stomach absolutely does not share."
    elif reality_id == "chloe":
        scene bg photo_studio
        with dissolve
        n "Studio lights click on around you. Sam is already there, holding coffee and looking at you with the comfortable affection of someone who has done this a hundred times."
        if persistent.spice_mode:
            other "There she is. Give me that dangerous little camera smile and we'll be done before brunch."
            n "The terrifying part is that your face seems to know exactly which smile he means."
        else:
            other "Ready for the morning shoot?"
    elif reality_id == "naomi":
        scene bg tattoo_studio
        with dissolve
        show naomi at sprite_breathe
        n "Crossline Studio smells like disinfectant, ink, and expensive coffee. Your first client trusts your hands more than you do."
        other "There you are." 
        n "Vera's voice comes from behind the counter. She looks at your borrowed jacket, then at you, and raises one eyebrow."
        if persistent.spice_mode:
            other "Keeping it this time, or do you need another excuse to come over?"
            pc "I... haven't decided."
    elif reality_id == "lila":
        scene bg cafe
        with dissolve
        show lila at sprite_breathe
        n "The café is already busy. Three regulars wave. Someone calls out your name from the pastry case."
        other "Morning." 
        n "June passes you a cup without asking what you drink. Her fingers brush yours, and your new body reacts with a warmth that feels embarrassingly practiced."
        if persistent.spice_mode:
            pc "So much for keeping this subtle."
    else:
        scene bg rooftop_club
        with dissolve
        show rhea at sprite_breathe
        n "Halo Roof is empty except for staff, but the sound system makes the glass railings hum. Everyone expects you to be in charge."
        other "Rhea." 
        n "Dani leans against the bar with a smile that says she remembers something you don't."
        if persistent.spice_mode:
            other "Red top tonight? Or was last night enough trouble for one week?"
            pc "I am beginning to understand why this life came with a warning label."

    if persistent.spice_mode:
        n "A passing reflective surface catches your new silhouette. This time you only stare for half a second before giving yourself a crooked smile. Progress, apparently."
    centered "{size=46}{b}ROUTE OPEN — BORROWED CONFIDENCE{/b}{/size}\n\n[reality_name] • [reality_first_stop]\nAcceptance [acceptance] • Curiosity [curiosity] • Boldness [boldness]\n\nThe full route continues from this location with relationship pressure, memory bleed, wardrobe choices, and reality-specific consequences."
    jump prototype_end

label ending_investigate:
    n "You search the phrase you remember hearing before reality folded: 'A wish should be specific.'"
    n "For a moment, the search results glitch. One impossible line appears and vanishes."
    wish "Better question: what would make you want to stay?"
    pc "There you are."
    centered "{size=46}{b}ENDING 2 — TERMS AND CONDITIONS{/b}{/size}\n\nSuspicion [suspicion] • Evidence [evidence_count]/4\n\nThe next chapter would turn the rewritten life into a mystery: discovering the wish rules, testing what reality can and cannot rewrite, and learning why the wish-granter expects resistance."
    jump prototype_end

label ending_flirt:
    n "You look at [reality_contact]'s message one more time."
    n "[reality_ending_flirt]"
    if persistent.spice_mode:
        n "For the first time since waking up, the heat in your face isn't entirely panic. That realization may be more frightening than the magic."
    centered "{size=46}{b}ENDING 3 — TOO CONVINCING{/b}{/size}\n\nBoldness [boldness] • Acceptance [acceptance]\n\nThe next chapter would explore the awkward, lewd-comedic side of inheriting a romantic reputation and a body that already has social habits your mind doesn't remember learning."
    jump prototype_end

label prototype_end:
    scene bg title
    with fade
    centered "{size=52}{b}WISHBOUND v0.2 COMPLETE{/b}{/size}\n\nThis vertical slice establishes the reality engine, six identities, six route hooks, discovery loop, relationship shock, and mature reaction tone.\n\nFuture build targets: layered sprites, dedicated phone UI, animated memory bleed, multiple wish types, relationship meters, outfit system, full Chapter 1."
    menu:
        "Replay prototype":
            jump start
        "Return to main menu":
            return
