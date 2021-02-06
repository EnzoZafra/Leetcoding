# Question:
# You are on a flight and wanna watch two movies during this flight.
# You are given List<Integer> movieDurations which includes all the movie durations.
# You are also given the duration of the flight which is d in minutes.
# Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

# Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.



def getMovies(movie_durations, flight_duration):
    originalIndicies = {}
    
    for i, num in enumerate(movie_durations):
        originalIndicies[num] = i
    
    movie_durations.sort()
    
    start = 0
    end = len(movie_durations) - 1
    maxDuration = 0
    maxIndices = [-1, -1]
    
    while start < end:
        movieStart = movie_durations[start]
        movieEnd = movie_durations[end]
        totalDuration = movieStart + movieEnd
        
        if totalDuration <= flight_duration - 30:
            if totalDuration > maxDuration:
                maxDuration = totalDuration
                maxIndices = [movieStart, movieEnd]
                
            start += 1
        
        else:
            end -= 1
    
    return [originalIndicies[maxIndices[0]], originalIndicies[maxIndices[1]]]
            
    
    
movieDurations = [90, 85, 75, 60, 120, 150, 125] 
d = 250
# expectedAns = [0, 6]
# Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)

movies = getMovies(movieDurations, d)
print(movies)
