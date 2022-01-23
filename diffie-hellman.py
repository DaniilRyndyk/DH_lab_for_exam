p, q = [int(x) for x in input("Prime1: ").split()]


# Private Keys for Alice and Bob
alice_Key, bob_Key = [int(x) for x in input("Alice and Bob Private Key: ").split()]


# Compute public values
alice, bob = (p**alice_Key % q), (p**bob_Key % q)


# Alice and Bob, compute same keys
alice, bob = (bob**alice_Key % q), (alice**bob_Key % q)


print(alice)
print(bob)