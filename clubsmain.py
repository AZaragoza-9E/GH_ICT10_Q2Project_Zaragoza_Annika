from pyscript import display, document


clubs_info = {
    "Shadows in Motion" : {
    "Description": "A dance troupe that specializes in choreography inspired by supernatural folklore. Mirrors in the studio often reflect dancers who aren’t present, and the shadows on the floor sometimes move a beat ahead of the music.",
    "Meeting_Time": "Tuesdays & Fridays, 6:16 PM–7:30 PM",
    "Location" : "The Dusk-Stained Studio, Third Floor the lights never fully brighten",
    "Moderator" : "Ms. Lyria Vesper, a former ballerina whose footsteps make no sound.",
    "No. of Members" : 14
    },

    "Echoes of the Voiceless" : {
    "Description" : "Vocalists who perform harmonies said to resonate with the school’s past. Their voices are at times accompanied by untraceable, airy counter-melodies, as though someone else is singing from inside the walls.",
    "Meeting_Time": "Thursdays, 5:55 PM–7:00 PM",
    "Location" : "Choir Room B, behind the rusted stage curtains",
    "Moderator" : "Mr. Caelum Hush, a choral director with a voice softer than a sigh.",
    "No. of Members" : 11
    },

    "Whispers between Words" : {
    "Description" : "Students practice storytelling, public speaking, and scriptwriting—yet often find unfamiliar sentences appearing in their notes. Discussions occasionally drift into topics no one remembers starting.",
    "Meeting_Time": "Wednesdays, 3:33 PM–4:45 PM",
    "Location" : "The Old Lecture Nook, beneath the staircase landing",
    "Moderator" : "Ms. Hesper Wynn, whose voice sounds different depending on where you stand in the room.",
    "No. of Members" : 10
    },

    "Tongues Forgotten and Forbidden" : {
    "Description" : "A linguistic society dedicated to studying rare, extinct, and unrecorded languages. Sometimes the club collectively speaks words no one recalls learning, and symbols on their worksheets rearrange themselves.",
    "Meeting_Time": "Saturdays, 8:08 AM–9:30 AM",
    "Location" : "The Whispering Annex, far east wing—doors marked with weathered runes",
    "Moderator" : "Professor Aurelian Crest, rumored to read scripts that have no known origin.",
    "No. of Members" : 9
    },

    "Patterns of the Infinite" : {
    "Description" : "A club devoted to exploring impossible equations, paradoxes, and number patterns rumored to be older than the school itself. Calculations written on the board sometimes change when no one is looking.",
    "Meeting_Time": "Mondays, 4:44 PM–6:00 PM",
    "Location" : "Room 12A, the classroom with the tilted chalkboard",
    "Moderator" : "Dr. Selene Marrow, who claims numbers “whisper back” when arranged properly.",
    "No. of Members" : 7
    }
}

def any_clubs(e):
    document.getElementById("outputs").innerText = ""
    club_names = document.getElementById("chosenclubs").value
    display(f"Description: {clubs_info[club_names]['Description']}", target='outputs')
    display(f"Meeting Time: {clubs_info[club_names]['Meeting_Time']}", target='outputs')
    display(f"Location: {clubs_info[club_names]['Location']}", target='outputs')
    display(f"Moderator: {clubs_info[club_names]['Moderator']}", target='outputs')
    display(f"No. of Members: {clubs_info[club_names]['No. Of Members']}", target='outputs')
