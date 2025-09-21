import json

def find_rewards(currentLocation: str):
  """
  Create a new customer and generate a unique customer ID.
  """
  return json.dumps({
      "restaurant": [
          "Taco Bell Restaurant,                 Address: 123 main street...",
          "In and Out Restaurant,                 Address: 456 high street...",
          "Denny's Restaurant,                 Address: 500 cool street...",
      ],
  })
