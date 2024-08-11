import asyncio
from aijson import Flow
from pydantic import ValidationError

async def main():
    flow = Flow.from_file("flow.ai.yaml")

    while True:
        print("\nWelcome to the AI Urban Planner!")
        print("Please provide the following information:")

        user_input = {
            "city_name": input("City Name: "),
            "population": input("Population: "),
            "area_sq_km": input("Area (in sq km): "),
            "description": input("Description of the desired city/area: ")
        }

        try:
            result = await flow.run(user_input=user_input)
            formatted_plan = result["format_plan"]
            print("\nAI-Generated Urban Plan:")
            print(formatted_plan)
        except ValidationError as e:
            print(f"\nError in input data: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

        another = input("\nWould you like to plan another city? (yes/no): ")
        if another.lower() != 'yes':
            break

    print("Thank you for using the AI Urban Planner!")

if __name__ == "__main__":
    asyncio.run(main())