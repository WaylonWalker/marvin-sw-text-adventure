from typing import List, Tuple
import atexit

from marvin import ai_fn
import pydantic
from pydantic import Field
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from marvin_sw_text_adventure.console import console


@ai_fn
def get_star_wars_character() -> str:
    "return a brand new never before heard of star wars character"


@ai_fn
def create_backstory(name: str) -> str:
    "create a backstory for a character"


class Game(pydantic.BaseModel):
    name: str = Field(..., description="The name of the game")
    id: str = Field(..., description="The id of the game")


class Mission(pydantic.BaseModel):
    name: str = Field(
        ...,
        description="The name of a brand new never before heard of star wars mission",
    )
    place: str = Field(..., description="The place of the mission")
    leader: str = Field(..., description="The name of the leader of the mission")
    year: int = Field(..., description="The year of the mission")
    description: str = Field(
        ...,
        description="The description of the brand new never before heard of star wars mission with important words surrounded by [b][/b]",
    )
    risk: int = Field(
        ..., description="The risk of the mission in health the character will loose"
    )
    reward: int = Field(
        ..., description="The reward of the mission in imperial credits"
    )
    image_prompt: str = Field(
        ..., description="An ai image generator prompt of the mission"
    )

    @property
    def stats(self) -> Table:
        table = Table(title=self.name, show_edge=False, show_header=False)
        # table = Table(show_header=False)
        table.add_row("place", self.place)
        table.add_row("year", str(self.year))
        table.add_row("risk", f"{self.risk} hp")
        table.add_row("reward", f"{self.reward} credits")
        table.add_row("leader", self.leader)

        return table

    @property
    def describe(self) -> str:
        table = Table(show_header=False)
        table.add_row(self.stats, self.description)
        return table


class MissionResult(pydantic.BaseModel):
    success: bool = Field(..., description="The success of the mission")
    imperial_credits_spent: int = Field(
        ..., description="The imperial credits spent on the mission"
    )
    imperial_credits_earned: int = Field(
        ..., description="The imperial credits earned on the mission"
    )
    health_lost: int = Field(..., description="The health lost on the mission")
    health_gained: int = Field(..., description="The health gained on the mission")
    story: str = Field(..., description="The story of the mission")
    image_prompt: str = Field(
        ..., description="An ai image generator prompt of the mission"
    )
    fuel_used: int = Field(..., description="The fuel used on the mission")


class Ship(pydantic.BaseModel):
    name: str = Field(..., description="The name of the ship")
    description: str = Field(..., description="The description of the ship")
    capacity: int = Field(..., description="The capacity of the ship")
    ship_type: str = Field(..., description="The type of the ship")
    year_built: int = Field(..., description="The year built of the ship")
    capacity: int = Field(..., description="The capacity of the ship")
    fuel_type: str = Field(..., description="The fuel type of the ship")
    fuel_level: int = Field(..., description="The fuel level of the ship")
    image_prompt: str = Field(
        ..., description="An ai image generator prompt of the mission"
    )

    @property
    def stats(self) -> Table:
        table = Table(title=self.name, show_edge=False, show_header=False)
        table.add_row("year built", str(self.year_built))
        table.add_row("capacity", str(self.capacity))
        table.add_row("fuel level", str(self.fuel_level))
        return table

    @property
    def describe(self):
        table = Table(show_header=False, show_edge=False)
        table.add_row(self.stats, self.description)
        return table


class StarWarsCharacter(pydantic.BaseModel):
    name: str = Field(
        ...,
        description="The name of a brand new never before heard of star wars character",
    )
    imperial_credits: int = Field(
        ..., description="The imperial credits of the character"
    )
    health: int = Field(..., description="The health of the character")
    home_planet: str = Field(
        ..., description="The name of the planet where the character was born"
    )
    age: int = Field(..., description="The age of the character")
    birth_year_bby: int = Field(..., description="The birth year of the character")
    backstory: str = Field(..., description="The backstory of the character")
    ship: Ship = Field(
        ..., description="The name of the ship where the character operates"
    )
    side: str = Field(..., description="The side of the character")
    city: str = Field(..., description="The name of the city where the character lives")
    friends: List[str] = Field(
        ..., description="The names of the friends of the character"
    )
    team: str = Field(
        ..., description="The name of the team that the character belongs to"
    )
    enemies: List[str] = Field(
        ..., description="The names of the enemies of the character"
    )
    mission: Mission = Field(..., description="The current mission of the character")
    role: str = Field(..., description="The role of the character")
    image_prompt: str = Field(
        ..., description="An ai image generator prompt of the mission"
    )
    previous_missions: List[Tuple[Mission, MissionResult]] = Field(
        [], description="The previous missions of the character"
    )

    @property
    def stats(self) -> Table:
        table = Table(title=self.name, show_edge=False, show_header=False)
        # table = Table(show_header=False)
        table.add_row("health", str(self.health))
        table.add_row("imperial credits", str(self.imperial_credits))
        table.add_row("fuel level", str(self.ship.fuel_level))
        return table

    @property
    def describe(self):
        table = Table(show_header=False, show_edge=False)
        table.add_row(self.stats, self.backstory)
        table.add_row()
        table.add_row(self.ship.stats, self.ship.description)
        table.add_row()
        table.add_row(self.mission.stats, self.mission.description)
        return Panel(
            table,
            title=f"{self.name}'s Mission Card",
            title_align="left",
        )


@ai_fn
def did_complete_mission(character: StarWarsCharacter, action: str) -> MissionResult:
    "check if a character completed the mission or if they failed"


@ai_fn
def get_next_mission(
    character: StarWarsCharacter, action: str, last_mission_success: bool
) -> Mission:
    """given a character, their action and the last mission success, return the next mission"""


@ai_fn
def create_game(character: StarWarsCharacter) -> Game:
    "create a new game"


@ai_fn
def create_character() -> StarWarsCharacter:
    "create a new character"

    console.save_text(f"{game.name}-{character.name}-{game.id}.txt")


def game():
    console.print("generating your character")

    prompt = Prompt()

    character = create_character()
    game = create_game(character)

    def save():
        console.save_text(f"{game.name}-{character.name}-{game.id}.txt")

    atexit.register(save)

    while (
        character.health > 0
        and character.imperial_credits > 0
        and character.ship.fuel_level > 0
    ):
        console.print(character.describe)
        action = prompt.ask("What do you do ❯")
        result = did_complete_mission(character, action)
        character.previous_missions.append((character.mission, result))
        # keep only the last 5 missions
        character.previous_missions = character.previous_missions[-5:]
        character.imperial_credits -= result.imperial_credits_spent
        character.imperial_credits += result.imperial_credits_earned
        character.health -= result.health_lost
        character.health += result.health_gained
        character.ship.fuel_level -= result.fuel_used
        console.print()
        console.print("Your mission has been completed")
        console.print(result.story)
        console.print(f"You earned {result.imperial_credits_earned} imperial credits")
        console.print(f"You spent {result.imperial_credits_spent} imperial credits")
        console.print(f"You gained {result.health_gained} health")
        console.print(f"You lost {result.health_lost} health")
        character.mission = get_next_mission(character, action, result.success)

    if character.health <= 0:
        console.print("You are dead")
    if character.imperial_credits <= 0:
        console.print("You lost all your imperial credits")
    if character.ship.fuel_level <= 0:
        console.print("You lost all your fuel")


if __name__ == "__main__":
    game()
