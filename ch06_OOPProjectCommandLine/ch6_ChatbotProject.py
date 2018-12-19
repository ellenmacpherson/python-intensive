# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:20:06 2018

@author: 612383423
"""
class Friend():
   def __init__(self, name, age, language):
       self.name=name
       self.age = age
       self.language = language

   def languageGreetings(self):
       if self.language == 'french':
           print ('Moi Aussi. Bonjour!')
       elif self.language == 'german':
           print ('Guten Tag!')
       elif self.language == 'english':
           print ('Nice to meet you!')
       else:
           print ('Sorry, i don\'t understand that language.')

   def YearCalculation(self):
        year = str(2018 - self.age)
        print ('So you were born in {}.'.format(year))

class Drawing():

    def portrait():
        print("""
            here's a portrait of you. I hope I got the likeness right!
                  .----''``-.
               -'//   | |  \`-.
              //   __...___    \
             .  /''        `. \\)
             | / .=='  `===  \_ |
             (    <o>  <o>    .)|
              \)     /        J |
               |.   /      . (  |
               (.  (_'.   , )|`/
               |\`-....--'/  '
                \\ |_I_| /  /|
                 \`-===-'  ' |
                  `. --   /  |
                    `.__.'   |
                      |  `   |
        """)
    def dog():
        print("""ok, here's a picture of my dog!
                        ____
       ,-'-,  `---._
_______(0} `, , ` , )
V           ; ` , ` (                            ,'~~~~~~`,
`.____,- '  (,  `  , )                          :`,-'""`. ";
  `-------._);  ,  ` `,                         \;:      )``:
         )  ) ; ` ,,  :                          ``      : ';
        (  (`;:  ; ` ;:\                                 ;;;,
        (:  )``;:;;)`'`'`--.    _____     ____       _,-';;`
        :`  )`;)`)`'   :    "~~~     ~~~~~    ~~~`--',.;;;'
        `--;~~~~~      `  ,  ", "",  "  "   "` ",, \ ;``
          ( ;         ,   `                ;      `; ;
          (; ; ;      `                   ,`       ` :
           (; /            ;   ;          ` ;     ; :
           ;(_; ;  :   ; ; `; ;` ; ; ,,, ";}     `;
           : `; `; `  :  `  `,,;,''''   );;`);     ;
           ;' :;   ; : ``'`'           (;` :( ; ,  ;
           |, `;; ,``                  `)`; `(; `  `;
           ;  ;;  ``:                   `).:` \;,   `.
        ,-'   ;`;;:;`                   ;;'`;;  `)   )
         ~~~,-`;`;,"                    ~~~~~  ,-'   ;
            ""''""                             `"'""
        """)
    def penguin():
        print("""here's a penguin!
      .___.
     /     \
    | O _ O |
    /  \_/  \
  .' /     \ `.
 / _|       |_ \
(_/ |       | \_)
    \       /
   __\_>-<_/__
   ~;/     \;~""")
    def flamingo():
        print("""
              Okay, here goes...
     __
  .^o ~\
Y /'~) }      _____
l/  / /    ,-~     ~~--.,_
   ( (    /  ~-._         ^.
    \ "--'--.    "-._       \
     "-.________     ~--.,__ ^.
               "~r-.,___.-'-. ^.
                YI    \      ~-.\
                ||     \        `\
                ||     //
                ||    //
                ()   //
                ||  //
                || ( c
   ___._ __  ___I|__`--__._ __  _
 "~     ~  "~   ::  ~~"    ~  ~~
                ::
                .:
                 .
"""     )

def statement():
    name = input('what\'s your name: ')
    print('\n')
    print('         \\|||||/        ')
    print('         ( O O )         ')
    print('|--ooO-----(_)----------|')
    print('|                       |')
    print('|     Hello ' + name + '!      ')
    print('|                       |')
    print('|------------------Ooo--|')
    print('         |__||__|        ')
    print('          ||  ||         ')
    print('         ooO  Ooo        ')
    year = int(input('so what year were you born? \n'))
    age=(2018-year)
    print ('hmm, so you are...', age,'years old.' )
    print()
    language = input('I speak English, French, and German. What language do you speak? ')
    #print ('So your name is {}, you\'re {} years old and you speak {}.'.format(name, age, language))
    exampleobject=Friend(name, age, language)
    exampleobject.languageGreetings()
    drawing= input('hey, let me draw you a picture. Would you like me to draw a dog, penguin, or flamingo. Or...I could do a portrait of you. Type the name of the animal or type "portrait" for a portrait!  ')
    if drawing == 'portrait':
        Drawing.portrait()
    elif drawing == 'dog':
        Drawing.dog()
    elif drawing == 'penguin':
        Drawing.penguin()
    elif drawing == 'flamingo':
        Drawing.flamingo()
    else:
        print('sorry, i cannot draw that')

statement()

#statement(o)

#susie=Friend('susie', 40, 'german')
#tom = Friend('tom',30, 'french')
#susie.languageGreetings()
#tom.languageGreetings()
#
#gracy = Friend(name, age, language)
