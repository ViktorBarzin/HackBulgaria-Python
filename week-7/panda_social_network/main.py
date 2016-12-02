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

# print(network.friends_of(tony)[0].name())

print(network.how_many_gender_in_network(1, rado, "female")) # True