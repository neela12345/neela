class bird:
    def intro(self):
        print('there are different types of birds')
    def flight(self):
        print('most of the birds can fly but some cannot')
class parrot(bird):
    def flight(self):
        print('parrots can fly')
class penguin(bird):
    def flight(self):
        print('penguin cannot fly')
bird=bird()
parr=parrot()
peng=penguin()
bird.intro()
bird.flight()
parr.intro()
parr.flight()
peng.intro()
peng.flight()
