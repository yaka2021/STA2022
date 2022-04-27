from scipy import optimize
            
def f(x):
    return x**3 + 3218677114060974854681101264677364361962573*x**2 + 1840445506533666033986484884603728067424458945838727730719646373755070770555336789280*x - 2272154925661249289543362932502122952106062554786355558781247264528866708742672195963818341500

print(optimize.bisect(f, 0, 10000000000))
