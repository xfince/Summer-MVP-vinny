from aijson import register_action
from pydantic import BaseModel, Field, PositiveInt, constr

class UrbanPlanningInput(BaseModel):
    city_name: constr(min_length=1, max_length=100) = Field(..., description="Name of the city or area")
    population: PositiveInt = Field(..., description="Current population of the city or area")
    area_sq_km: PositiveInt = Field(..., description="Total area of the city in square kilometers")
    description: constr(min_length=10, max_length=1000) = Field(..., description="Description of the desired city/area")

@register_action
def validate_input(input_data: dict) -> UrbanPlanningInput:
    """
    Validate and process the input data for urban planning.
    """
    try:
        return UrbanPlanningInput(**input_data)
    except ValueError as e:
        raise ValueError(f"Invalid input data: {str(e)}")

@register_action
def format_urban_plan(plan: str) -> str:
    """
    Format the urban plan for better readability.
    """
    sections = plan.split("\n\n")
    formatted_plan = ""
    for section in sections:
        if ":" in section:
            title, content = section.split(":", 1)
            formatted_plan += f"## {title.strip().upper()}\n{content.strip()}\n\n"
        else:
            formatted_plan += f"{section.strip()}\n\n"
    return formatted_plan.strip()