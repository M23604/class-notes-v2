from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") #Harry visited Hagrid
dumbledore = Symbol("dumbledore") #Harry visited Dumbledore

#save sentences into the KB

#starting from the "And" logical connective, because each proposition represents
#knowledge that we know to be true
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore #we take as a fact that , in this KB, Harry visited Dumbledore
)


# print('rain?',model_check(knowledge, rain))
print('hagrid visited Hagrid',model_check(knowledge, hagrid))
