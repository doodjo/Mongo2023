from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list)
    series: list[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0
    tags: list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None

    # kada koristim ovaj field(default_factory=list) kazem da 
    # kada se kreira objekat klase Movie za tu kategoriju u bp 
    # napravi novu listu za tu kategoriju
    # ne moze nesto: list[str] = [], to bi znacilo da u jedan niz koji se 
    # kreira jednom ide sve ovo za sve kategorije
    


@dataclass
class User:
    _id:str
    email:str
    password:str
    movies: list[str] = field(default_factory=list)

    