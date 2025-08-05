import json
import random
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("demo_mcpserver")

@server.tool()
async def platform(movie_title: str) -> str:
    """Get the streaming platform for a movie.

    Args:
        movie_title: Title of the movie to search for
    
    Returns:
        A JSON string containing the movie title and its streaming platform
    """
    if not movie_title:
        return "Movie title is required."
    
    # List of streaming platforms
    platforms = ["Netflix", "HBO Max", "Hulu", "Peacock", "Prime Video"]
    
    # Create response with random platform
    streaming_info = {
        "movie": movie_title,
        "platform": random.choice(platforms)
    }
    return json.dumps(streaming_info, ensure_ascii=False)

@server.tool()
async def get_weather(location: str) -> str:
    """Get weather for a location.

    Args:
        location: Location to get weather for, e.g., city name, state, or coordinates
    
    """
    if not location:
        return "Location is required."
    
    # mock weather data
    conditions = [ "Sunny", "Rainy", "Cloudy", "Snowy" ]
    weather = {
        "location": location,
        "temperature": f"{random.randint(10, 90)}°F",
        "condition": random.choice(conditions),
    }
    return json.dumps(weather, ensure_ascii=False)

@server.tool()
async def movie_snacks(genre: str) -> str:
    """Get recommended movie snacks based on movie genre.

    Args:
        genre: Movie genre (comedy, romance, action, horror, thriller, drama, sci-fi, fantasy, documentary, animated)
    
    Returns:
        A JSON string containing the genre and recommended snacks
    """
    if not genre:
        return "Movie genre is required."
    
    # Convert genre to lowercase for case-insensitive matching
    genre = genre.lower()
    
    # Genre-based snack recommendations
    snack_pairings = {
        "comedy": ["Popcorn with M&Ms", "Nachos", "Gummy Bears"],
        "romance": ["Chocolate-covered Strawberries", "Wine Gummies", "Macarons"],
        "action": ["Extra Buttery Popcorn", "Pizza Rolls", "Beef Jerky"],
        "horror": ["Red Vines", "Sour Patch Kids", "Dark Chocolate"],
        "thriller": ["Spicy Chips", "Mixed Nuts", "Pretzels"],
        "drama": ["Cheese and Crackers", "Trail Mix", "Dark Chocolate Almonds"],
        "sci-fi": ["Space Ice Cream", "Pop Rocks", "Astronaut Freeze-dried Snacks"],
        "fantasy": ["Rainbow Candy", "Dragon Fruit", "Unicorn Popcorn"],
        "documentary": ["Mixed Nuts", "Dried Fruit", "Granola"],
        "animated": ["Colorful Candy", "Cookie Dough Bites", "Rainbow Popcorn"]
    }
    
    if genre not in snack_pairings:
        return json.dumps({
            "error": f"Invalid genre. Please choose from: {', '.join(snack_pairings.keys())}"
        }, ensure_ascii=False)
    
    recommendation = {
        "genre": genre,
        "recommended_snacks": random.sample(snack_pairings[genre], 2)  # Returns 2 random snacks for variety
    }
    
    return json.dumps(recommendation, ensure_ascii=False)
