# Task can be found here: https://github.com/HackBulgaria/Programming101-Python-2016/tree/master/week07/PandaSocialNetwork

from panda_social_network import *

network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")
tony2 = Panda("Tony2", "tony23@pandamail.com", "female")

for panda in [ivo, rado, tony, tony2]:
    network.add_panda(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)
network.make_friends(tony, tony2)

print(network.save('s-network.json'))
