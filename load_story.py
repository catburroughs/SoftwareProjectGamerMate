import pickle
from hero import *


story = {
    1: {
      'Text': [
            "You wake up alone on a mountaintop under a blanket of stars. ",
            "as you sit up you see two paths by moonlight... ",
            "...one winds down into a city, bright with lights and the other journeys deep into the mountains."
        ],
      'Options': [
          ("You go down into the bustling city", 2, "group", None),
          ("You take the road into the mountains", 2, "indie", None)
        ]
    },
    2: {
        'Text': [
            "Wait a second! You better put some clothes on! ",
            "You have two packs, one containing garments of rich materials, finely worked - clothing fit for royalty and the other pack contains plain, sturdy, servicable garb. "
        ],
        'Options': [
          ("You put on the rich clothing in pack 1. ", 3, "risky", None),
          ("You put on the drab garments in pack 2. ", 3, "safe",None)
        ]
    },
    3: {
        'Text': [
            "After fifteen minutes of walking you come to a man asleep on the path, snoring loudly, an empty bottle by his side and the smell of whisky in the air. ",
            "His money pouch has fallen from his pack - you see the glint of gold - it would be easy to pick it up... "
        ],
        'Options': [
          ("You take the money and keep going. ", 4, "risky","indie"),
          ("You place the money back into the stranger's bag. ", 5, "safe","group")
        ]
    },
    4: {
      'Text': [
            "Suddenly the man appears in front of you on the path, a wicked smile on his face. ",
            "Since you are so adept at pilfering what isn't yours, perhaps you would care to join my group? ",
            "In two days the Marquis will travel past and if you join us in bringing him down, I can promise you fame, fortune, and, above all, DANGER. "
        ],
      'Options': [
          ("You join the band of thieves. ", 6, "risky", "group"),
          ("You pretend to accept but secretly scheme to find a way to turn this to your advantage. ", 6, "indie", None)
          ]
    },
    5: {
      'Text': [
            "Suddenly the man appears in front of you on the path, a kindly smile on his face. ",
            "I have been waiting for you, the legend told of a hero who would be known by their honesty and you are that hero. ",
            "The royal heir has disappeared, the king is dead, and the kingdom is desperate, will you find them and bring them back to rule? "
        ],
      'Options': [
          ("You accept the quest to find the royal heir. ", 7, "group" , "risky"),
          ("You play along but secretly seek to find a way to turn this to your advantage. ", 7, "indie", None)
          ]
    },
    6: {
      'Text': [
            "You set up camp with the thieves and spring a trap for the wealthy Marquis. ",
            "The night before the ambush you sneak to close to the guard patrols outside the city. "
        ],
      'Options': [
          ("You tell the guards about the plan and become rich from the bounty when the thieves are captured. ", 10, "safe", "indie"),
          ("You follow through with the plan, becoming an adept thief and a highly skilled scoundrel. ", 10, "risky", "group")
          ]
    },
    7: {
      'Text': [
            "On reaching the kingdom you are taken aside by the heir's younger sibling, the next in line for the throne. ",
            "They are charming, they are attractive, they are... clearly coming onto you. "
            "They make it clear that if you support their claim and give up the quest, you will be gifted with the freedom of the kindom  "
            " and its ruler."
        ],
      'Options': [
          ("Rebuff their advances and ride out to find the heir", 8, "group","risky"),
          ("Accept with alacrity - fame, power, and fun...you could get used to this", 10, "indie", "safe")
          ]
    },
    8: {
      'Text': [
            "After weeks of searching you track the heir to the castle of a notorious wizard. ",
            "You scale the castle walls and surprise the wizard in their study. "
        ],
      'Options': [
          ("Before the wizard can enchant you, you unsheath your sword and attack", 9, "risky", None),
          ("You challenge the wizard with the accusation of hiding the heir and command them to be freed", 9, "safe", None)
          ]
    },
    9: {
      'Text': [
            "Suddenly the heir rushes into the room, declaring their love for the wizard and their abdication of the throne",
            "The heir pleads with you to let them stay. "
        ],
      'Options': [
          ("This must be an enchantment! You foil the wizard's plans by defeating them and bringing the heir back to a grateful kingdom. ", 10, "group", "safe"),
          ("You believe them, you return empty handed - not knowing if your concession will bring disgrace or worse. ",10, "indie", "risky")
          ]
    },
    10: {
      'Text': [
            "GAME OVER"
        ],
      'Options': []
    }


}

with open('chapter1.ch', 'wb') as chapter:
  pickle.dump(story, chapter)
