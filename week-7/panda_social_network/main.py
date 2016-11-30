from panda_social_network import *

network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)

print(network.connection_level(ivo, rado) ) # True