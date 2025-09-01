
# "Phase 1: Implemented vector similarity engine (dot, cosine, euclidean, manhattan, normalize)"

def dot(v1,v2):
    l = 0 
    for i in range(len(v1)):
        l = l + (v1[i]*v2[i])
    return l
def magnitude(v1):
    l = 0 
    for i in range(len(v1)):
        l = l + (v1[i]**2)
    return l**0.5
def cosine_similarity(v1,v2):
    return dot(v1,v2)/(magnitude(v1) * magnitude(v2))

def euclidean(v1,v2):
    l=0
    for i in range(len(v1)):
        l = l + ((v1[i]-v2[i])**2)
    return l**0.5
def manhattan(v1,v2):
    l = 0 
    for i in range(len(v1)):
        l = l + abs(v1[i]-v2[i])
    return l
def normalize(v1):
    v2 = []
    for i in range(len(v1)):
        k = v1[i]/magnitude(v1)
        v2.append(k)
    return v2
v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Dot product:", dot(v1, v2))
print("Magnitude v1:", magnitude(v1))
print("Magnitude v2:", magnitude(v2))
print("Cosine similarity:", cosine_similarity(v1, v2))
print("Euclidean distance:", euclidean(v1, v2))
print("Manhattan distance:", manhattan(v1, v2))
print("Normalized v1:", normalize(v1))
print("Normalized v2:", normalize(v2))
