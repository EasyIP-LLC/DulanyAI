###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

file_map = {
    
    "clients.baml": "client<llm> GPT4o_mini {\n  provider openai\n  options {\n    model gpt-4o-mini\n    api_key env.OPEN_AI_KEY\n  }\n}",
    "metrics.baml": "// Data Models\nclass Metrics {\n  sentences string[] @description(\"Every sentence should be a function. Basically a function of what is being patented. There must be 8 sentences.\")\n}\nfunction ExtractPatentMetricsFromQuery(patent_text: string) -> Metrics {\n  // LLM client with params you want (not pictured)\n  client GPT4o_mini\n\n  // BAML prompts use Jinja syntax\n  prompt #\"\n    Parse the following patent and return a structured representation of the data in the schema below.\n\n    Your job is to take a search query and extract 8 functions from it.\n\n    Let me give you an example. Let's say the search query is:\n        \n    A coffee maker that dispenses both milk and coffee. The coffee can be made either from beans or from pods. To prevent spilling, there is a metal or plastic grate at the bottom. There is an electric screen to control it and alert the user once it's done.\n\n        The functions you can extract from this are:\n        Brews hot beverage.\n        Dispenses milk.\n        Can use coffee pods.\n        Can use coffee beans.\n        Has refillable water reservoir.\n        Has grate to prevent spillage.\n        Has electric screen for use.\n        Alerts user when done.\n\n    Search Query Text:\n    ---\n    {{ patent_text }}\n    ---\n\n    {{ ctx.output_format }}\n\n    JSON:\n  \"#\n}\n\ntest TestBacterialPrompt {\n  functions [ExtractPatentMetricsFromQuery]\n  args {\n    patent_text #\"\n        A bacteria that divides rapidly and produces beneficial research chemicals.\n    \"#\n  }\n}\n\n\ntest TestCoffeePrompt {\n  functions [ExtractPatentMetricsFromQuery]\n  args {\n    patent_text #\"\n        A machine that dispenses coffee.\n    \"#\n  }\n}\n\ngenerator bamlMetricClient {\n output_type \"python/pydantic\"\n output_dir \"../\"\n version \"0.52.1\"\n}",
    "word_doc_sum.baml": "// Data Models\nclass Summaries {\n  patent string @description(\"This field should be the patent number.\")\n  title string @description(\"This field should be the title of the patent.\")\n  filing_date string @description(\"This field should be the filing date of the patent.\")\n  summary string @description(\"This field should just be a summary of the patent.\")\n}\nfunction WordDocSummaries(patent_text: string) -> Summaries {\n  // LLM client with params you want (not pictured)\n  client GPT4o_mini\n\n  // BAML prompts use Jinja syntax\n  prompt #\"\n        I am going to give you a list of patents with their respective claims, abstracts, and titles. For each patent, summarize what the patent is about and its key features in 100 words.\n\n        Make sure to include all of the independent claims in the summary. Below are the patents and their respective claims and abstract sections:\n    Search Query Text:\n    ---\n    {{ patent_text }}\n    ---\n\n    {{ ctx.output_format }}\n\n    JSON:\n  \"#\n}\n\ntest TestCoffeBrewingPatent {\n  functions [WordDocSummaries]\n  args {\n    patent_text #\"\n    Abstract\n    The coffee maker for brewing powder coffee contained in a cartridge comprises a brewing chamber adapted to receive the cartridge, at least one punching member for punching the cartridge and a pump for feeding brewing water into the brewing chamber. In order to avoid that the prepared coffee shows froth at its surface, the coffee maker comprises means for restricting the amount of water fed by the pump into the brewing chamber per unit of time. This means ensures that the brewing water flows through the cartridge essentially unpressurized.\n    Claims\n    1. be used for brewing the coffee machine of containing in the coffee powder of material package, it comprises: the beverage making cavity that is suitable for holding described coffee powder material package; At least one is used for dashing wears the device of described coffee powder material package; With heat is brewed water and infeeds pump in the described beverage making cavity; It is characterized in that, also comprise the device that brews the water yield that infeeds in the restricted unit time optionally in the described beverage making cavity, this device make brew water flow through to not supercharging basically the described coffee powder material package that is arranged in described beverage making cavity with produce non-foam coffee, perhaps make brew water under high pressure flow through be arranged in described beverage making cavity described coffee powder material package to produce espresso.\n    2. according to the coffee machine of claim 1, it is characterized in that: be used for limiting the water yield that brews that infeeds described beverage making cavity in the described device restricted unit time that brews the water yield and be no more than per hour 12 liters.\n    3. according to the coffee machine of claim 1, it is characterized in that: be provided with and be used for dashing at least two punching parts wearing material package bottom and material package lid, be used for utilizing described pump to dash by described punching part before being conducted to material package and wear the described bottom of described material package and the device of described lid brewing water thereby be provided with.\n    4. according to the coffee machine of claim 1, it is characterized in that: described beverage making cavity comprises material package supporter and sealing plate, each of described material package supporter and described sealing plate all is provided with the punching part, thereby described coffee machine also comprises the device that makes described material package supporter and described sealing plate move to its closed condition each other from the opening of described beverage making cavity, thereby when sealing during described beverage making cavity, the described material package of utilizing described punching part to make to be contained in the described beverage making cavity at its lid place and the place, bottom dashed and worn.\n    5. according to the coffee machine of claim 4, it is characterized in that: both are provided with the punching part that is positioned at central authorities described sealing plate and described material package supporter.\n    6. according to the coffee machine of claim 4, it is characterized in that: described sealing plate or described material package supporter are provided with the punching part that is positioned at central authorities.\n    7. according to the coffee machine of claim 1, it is characterized in that: the device that brews the water yield that is used for infeeding in the restricted unit time described beverage making cavity comprises the device that is used to limit described pump discharge.\n    8. according to the coffee machine of claim 7, it is characterized in that: described pump is electrically driven (operated) with exchanging, thereby the described device that is used to limit described pump discharge comprises phase control regulator, radio-frequency pulse controller or frequency-variable controller.\n    9. according to the coffee machine of claim 1, it is characterized in that: the device that brews the water yield that is used for infeeding in the restricted unit time described beverage making cavity comprises adjustable choke valve, described choke valve is inserted into from described pump to the pipeline that described beverage making cavity is extended, is used to change the effective cross section circulation area of described pipeline.\n    10. according to the coffee machine of claim 9, it is characterized in that: be provided with the manually operated selector switch that is connected in control module, thereby described control module is operably connected to described pump and/or described choke valve to be conducted to the water yield that brews of described beverage making cavity in the restricted unit time.\n    11. the coffee machine according to claim 4 is characterized in that: when the described beverage making cavity of sealing, described sealing plate is suitable for pushing described material package against the end face of described material package supporter along the annular seating zone.\n    12. coffee machine according to claim 10, also comprise: being used to decode is located at least one sensor of the label or tag on the described material package, comes to be conducted in the restricted unit time water yield that brews of described beverage making cavity according to the information content of described label or tag thereby described sensor is operably connected to described control module.\n    \"#\n  }\n}\n",
}

def get_baml_files():
    return file_map