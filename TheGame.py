import time
import os
def clear():
    command = 'cls'
    os.system(command)

clear()
print(' ___________________________________________________________________')
print('| Welcome to the game:                                              |')
print('| This game is about you who awakes with no memorie of the past     |')
print('| You will encounter choices you have to make                       |')
print('| Choose wisely because your life might depend on those choices     |')
print('| Good luck...                                                      |')
print('|___________________________________________________________________|')
print('|                                                                   |')
print('| You awake in total darkness, you light a candle to see that you   |')
print('| are inside an arena.                                              |')
print('| Suddenly a huge door opens and a dragon comes out.                |')
print('| You see three things laying on the ground:                        |')
print('| Option 1- A comically large spoon                                 |')
print('| Option 2- A backpack filled with paper airplanes strapped with    |')
print('| bombs                                                             |')
print(' ___________________________________________________________________')
print('')
input('Press enter to continue')
clear()
keuze1 = input('You can only take one item, which one do you take? spoon/backpack: ')
if keuze1 == 'spoon':
    clear()    
    keuze2 = input('You grab the comically large spoon. You try to kill the dragon but soon notice that it\'s a tough dragon. \nYou see a wound on his wing and think that it is his weakspot, you also see a hole in the ground with a ladder going down. What do you do? weakspot/ladder: ')
    if keuze2 == 'weakspot':
        clear()
        keuze3 = input('You go for the wing and slice it off in one go, the dragon bleeds to death and 2 doors open; one red and one blue. Which door do you choose? red/blue: ')
        if keuze3 == 'red':
            clear()
            keuze4 = input('You choose the red door. You see a large window on the left where the blue door would have been and see yourself dying. You sigh with relief. You walk out and see a helicopter and an 8x8 offroad truck, which one do you choose? heli/8x8: ')
            if keuze4 == 'heli':
                clear()
                print('You choose the helicopter. You try to start it but it doesn\'t work, you try again and the helicopter explodes while you are sitting inside, you instantly turn into ashes... RIP ')                                   
            elif keuze4 == '8x8':
                clear()
                keuze5 = input('You choose the 8x8 Offroad truck. You drive into a cave filled with sleeping dogs, you are afraid to wake them up but see a key and a lock pick set laying on the ground, you can only take 1 with you, which one do you choose? key/lockpick: ')
                if keuze5 == 'key':
                    clear()
                    print('You choose the key. You drive out of the cave again and come across a large door with a security guard. He asks: "Do you have the key for the door?". You answer yes and take the key out of your pocket, the door opens. You see a huge paradise and live happily ever after...WIN ')
                elif keuze5 == 'lockpick':
                    clear()
                    print('You choose the lock pick set. You drive out of the cave again and come across a large door with a security guard. He asks: "Do you have the key for the door?". You answer no but show your lock pick set. The security guard thinks you were trying to break in and cuts your legs off and you bleed to death...RIP ')
        elif keuze3 == 'blue':
            clear()
            keuze6 = input('You choose the blue door. The door closes behind you and you feel you are trapped by 2 nailbeds, then you are roasted alive and eaten by some dogs...RIP ')        
    elif keuze2 == 'ladder': 
        clear()
        print('You take the ladder. It gets darker as you go down, suddenly the ladder stops and you fall down. ')
        print('You take out your candle and see that you have entered a cave filled with sleeping dogs. You remember the saying \'don\'t wake sleeping dogs\'.')
        print('You see a corridor with a faint light at the end but also think: maybe one of these dogs can help me.')
        print('You wake up a sleeping dog. He seems like a wise old friendly dog and asks if he knows what to do. The dog says: "Woof woef wöof woof wof wuf".')
        print('You have no idea what he is saying but suddenly you see a smooth purple object in your hand, you recognize it as a dog language-translator and find out that he is saying:')
        print('"You\'re not supposed to be here, follow me." You follow him until you come to an exit, you thank the dog and continue on your own. You walk out and see a helicopter on fire ')
        keuze7 = input('Do you walk towards the flaming helicopter or do you walk past it? heli/walk past: ')
        if keuze7 == 'heli':
            subkeuze1 = input('You see a beaker laying on the ground, do you take it? yes/no: ')
            if subkeuze1 == 'yes':
                clear()
                print('As you walk closer and closer, the helicopter explodes. A pile of ashes lands before your feet, you remember the beaker that you picked up.')
                print('You throw it on the pile of ash and a person that looks just like you appears')
                print('Inception...RIP')
            elif subkeuze1 == 'no':
                clear()
                print('As you walk closer and closer, the helicopter explodes. A pile of ashes lands before your feet, you think of how tragic the death must have been.')
                keuze11 = input('Do you commit suicide or do you lay in the grass? suicide/grass: ')
                if keuze11 == 'suicide':
                    clear()
                    print('You die but end up in heaven...WIN')
                elif keuze11 == 'grass':
                    clear()
                    print('You go lay down in the grass')
                    print('A couple of hours pass but then suddenly the ground collapses and you get stuck and eaten by worms...RIP')
        elif keuze7 == 'walk past':
            print('You walk past and the helicopter explodes, a piece of debris impales your left lung and you suffocate...RIP')
elif keuze1 == 'backpack':
    clear()
    print('You take the backpack. You grab a plane, throw it at the dragon, the dragon and the plane have a huge dogfight. ')
    print('The plane comes right behind the dragon and explodes ....... Suddenly the dragon comes flying out of the fire and you are friends. You can sit on its back and fly away.')
    print('You land in Zimbabwe. There is water shortage there and you find out that the dragon can spew water instead of fire. You help a few villages and are faced with a choice: ')
    keuze8 = input('Do I go back home by plane or do I keep helping people with the dragon? home/help: ')
    if keuze8 == 'home':
        clear()
        print('You choose to go home with the airport.')
        print('You never even arrive at the airport because in the taxi to the airport you were robbed, cut into pieces and your organs sold on the black market...RIP ')
    elif keuze8 == 'help':
        clear()
        print('You choose to help solve the water shortage, you start with a few small villages but quickly move on to help large cities.')
        keuze9 = input('The head of state Emmerson Mnangagwa asks you if you want to become emperor of zimbabwe, do you accept his offer? yes/no: ')
        if keuze9 == 'no':
            clear()
            print('You decline his offer. On the way to Lesotho the dragon loses its other wing, you plummit towards earth from 12 kilometers high...RIP ')
        elif keuze9 == 'yes':
            clear()
            print('You accept his offer and are now Emperor of Zimbabwe.')
            print('17 years later you are still Emperor of Zimbabwe with the Dragon as an accomplice, you have 12 Nobel Prizes and the average income per household in Zimbabwe is now the highest in the world.')
            print('You are happy with what you have achieved but want more, the plan: conquer the world.')
            keuze10 = input('You think the dragon won\'t like the idea, so you\'re in a dilemma: do I continue on my own or with my dragon? with/without: ')
            if keuze10 == 'without':
                clear()
                print('You go on on your own. You almost conquered the whole world when. You are sitting in a mansion somewhere off the coast of Mexico when suddenly the Dragon comes back and fills you house with water. You drown...RIP')
            elif keuze10 == 'with':
                clear()
                print('You ask the dragon to help, the dragon says yes and you call in the entire Zimbabwean army. First you take over all of Africa, then Europe, Russia and Asia.')
                print('When you come to the USA you have a bit of trouble but eventually conquer it. ')
                print('You now own the whole world...WIN')                

input('')
clear()
