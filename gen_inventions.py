import re
import autopep8


# category_name = "groceries"
# tech_dict = [
#     {"tech_name": "Mechanical Dough Preparation", "era": 2, "desc": "Early industrial dough rollers and mechanical mixers", "pm_name": "Roller Mill Integration"},
#     {"tech_name": "Pasteurization Processes", "era": 3, "desc": "Louis Pasteur heat-treatment (1860s) for milk and canned goods.", "pm_name": "Glass-Bottled Dairy"},
#     {"tech_name": "Synthetic Preservatives", "era": 4, "desc": "Sodium benzoate (1900s) for mass-produced non-perishables.", "pm_name": "Chemical Food Stabilization"},
#     {"tech_name": "Conveyor-Belt Packaging", "era": 5, "desc": "Assembly-line packaging (e.g., 1920s cereal production).", "pm_name": "Steel-Frame Automation"},
# ]

# category_name = "logging"
# tech_dict = [
#     {"tech_name": "Hydraulic Logging Systems", "era": 2, "desc": "Early adoption of water-powered systems to transport logs via flumes, reducing reliance on manual labor.", "pm_name": "Hydraulic Flume Transport"},
#     {"tech_name": "Mechanical Band Saw Innovation", "era": 3, "desc": "Introduction of continuous band saws, revolutionizing lumber cutting efficiency.", "pm_name": "Band Saw Mills"},
#     {"tech_name": "Timber Preservation Science", "era": 4, "desc": "Use of creosote and chemicals to treat wood, extending its lifespan for industrial uses.", "pm_name": "Creosote Treatment"},
#     {"tech_name": "Mobile Forestry Machinery", "era": 5, "desc": "Portable diesel-powered sawmills enable logging in remote areas.", "pm_name": "Portable Sawmill Operations"},
# ]

# category_name = "textile"
# tech_dict = [
#     {"tech_name": "Coal-Tar Dye Processing", "era": 2, "desc": "First synthetic dyes from coal byproducts.", "pm_name": "Coal Dye Application"},
#     {"tech_name": "Mechanical Pattern Grading", "era": 3, "desc": "Ebenezer Butterick's paper patterns.", "pm_name": "Paper Templates"},
#     {"tech_name": "Vulcanized Rubber Fasteners", "era": 4, "desc": "Late Victorian elasticized clothing.", "pm_name": "Rubberized Clothing"},
#     {"tech_name": "Electrostatic Lint Control", "era": 5, "desc": "Early industrial air filtration systems.", "pm_name": "Dust Prevention Systems"},
# ]

# category_name = "fishing"
# tech_dict = [
#     {"tech_name": "Pelagic Canning Processes", "era": 3, "desc": " The rise of canned sardines in Europe and salmon in North America.", "pm_name": "Industrial Fish Cannery"},
#     {"tech_name": "Bycatch Utilization", "era": 4, "desc": "Scandinavian practices of using fish waste for fertilizer and animal feed.", "pm_name": "Fishmeal Rendering"},
#     {"tech_name": "Hydroacoustic Navigation", "era": 5, "desc": "Early sonar prototypes used in fishing fleets.", "pm_name": "Echo Sounding Trawlers"},
# ]

# category_name = "furniture"
# tech_dict = [
#     {"tech_name": "Thonet Bentwood Process", "era": 2, "desc": "Revolutionizing furniture crafting through steam-bent wood, this technique allowed mass production of lightweight, elegant chairs like the iconic No. 14 model. By replacing hand-carved joints with standardized components, it democratized stylish furnishings for the burgeoning middle class.", "pm_name": "Steam-Bent Furniture"},
#     {"tech_name": "Veneer Lamination Techniques", "era": 3, "desc": "The adoption of thin, decorative wood veneers glued to cheaper substrates let manufacturers mimic luxury finishes like mahogany or ebony. Paired with synthetic dyes, this innovation fueled the Victorian obsession with ornate, affordable opulence in parlors worldwide.", "pm_name": "Decorative Veneer Furnishings"},
#     {"tech_name": "Synthetic Material Integration", "era": 5, "desc": "Pioneering plastics like Bakelite and laminated composites enabled sleek, modernist designs that embraced the machine age. These durable, moldable materials replaced traditional woodcraft, catering to Art Deco aesthetics and industrial-era practicality.", "pm_name": "Bakelite & Composite Furniture"},
# ]

# category_name = "paper"
# tech_dict = [
#     {"tech_name": "Mechanical Papermaking Automation", "era": 2, "desc": "The Fourdrinier machine, patented in 1801 but widely adopted post-1830, automated continuous paper sheet production.", "pm_name": "Fourdrinier Machine Adoption"},
#     {"tech_name": "Wood Pulp Refinement", "era": 3, "desc": "Mid-19th century use of chlorine for bleaching wood pulp, replacing rags.", "pm_name": "Chlorine Bleaching Process"},
#     {"tech_name": "Industrial Byproduct Utilization", "era": 4, "desc": "1884 kraft process invention, using sulfate pulping for stronger paper.", "pm_name": "Kraft Process Development"},
#     {"tech_name": "Synthetic Additives", "era": 5, "desc": "Early 20th-century experiments with synthetic fibers to strengthen paper.", "pm_name": "Synthetic Fiber Integration"},
# ]

# category_name = "motor"
# tech_dict = [
#     {"tech_name": "High-Pressure Steam Engineering", "era": 2, "desc": "Pioneering valve systems and reinforced boilers allow steam engines to harness unprecedented power, revolutionizing factories and ships—at the cost of voracious steel consumption.", "pm_name": "Corliss Valve System"},
#     {"tech_name": "Continuous Production Flow", "era": 3, "desc": "Electrified conveyor belts synchronize assembly stages, reducing reliance on manual labor while binding manufacturing to the growing power grid.", "pm_name": "Electrified Conveyor Belts"},
#     {"tech_name": "Alloy Metallurgy", "era": 4, "desc": "Lightweight aluminum and nickel alloys enable compact, fuel-efficient engines, though their production demands exotic materials like rubber and precision lubricants.", "pm_name": "Lightweight Steel Alloys"},
#     {"tech_name": "Automated Assembly Systems", "era": 5, "desc": "Programmable robotic arms and hydraulic presses achieve micrometer precision, rendering traditional machinists obsolete in favor of engineers overseeing ‘thinking machines’.", "pm_name": "Robotic Precision Machining"},
# ]

# category_name = "alcohol"
# tech_dict = [
#     {"tech_name": "Microbial Fermentation Control", "era": 3, "desc": "Inspired by Louis Pasteur's 1860s research on yeast, this technology introduces controlled fermentation processes using sulfur-based antiseptics to prevent spoilage and ensure consistent quality.", "pm_name": "Pasteurization Techniques"},
#     {"tech_name": "Temperature-Controlled Aging", "era": 4, "desc": "Adoption of underground concrete aging caves with mechanical ventilation systems enables precise control over maturation conditions.", "pm_name": "Modern Caves d'Élevage"},
#     {"tech_name": "Mechanized Harvesting Systems", "era": 5, "desc": "Early gasoline-powered tractors and mechanical grape crushers revolutionize vineyard operations during the interwar period.", "pm_name": "Industrial Viniculture"},
# ]

# category_name = "meat"
# tech_dict = [
#     {"tech_name": "Selective Livestock Breeding", "era": 2, "desc": "Systematic breeding programs improve livestock yields by focusing on desirable traits like muscle mass and disease resistance.", "pm_name": "Selective Breeding"},
#     {"tech_name": "Industrial Refrigeration Techniques", "era": 3, "desc": "Mechanical refrigeration systems allow for centralized meat processing and reduced spoilage during transport.", "pm_name": "Centralized Abattoirs"},
#     {"tech_name": "Chemical Meat Preservation", "era": 4, "desc": "Advances in food chemistry allow for longer shelf life through curing salts and preservatives.", "pm_name": "Curing Processes"},
#     {"tech_name": "Automated Meatpacking Systems", "era": 5, "desc": "Assembly-line innovations inspired by automotive factories revolutionize meat processing efficiency.", "pm_name": "Conveyor Butchering"},
# ]

# category_name = "mining"
# tech_dict = [
#     {"tech_name": "Cornish Beam Pumping Systems", "era": 2, "desc": "Adaptation of steam-powered pumping technology from Cornish tin mines allows deeper shaft mining operations. While dramatically increasing output, these massive steam engines require significant infrastructure investment.", "pm_name": "Cornish Beam Pumps"},
#     {"tech_name": "Compressed Air Drill Networks", "era": 3, "desc": "Pneumatic rock drills powered by centralized compressor stations revolutionize hard rock mining, particularly in lead and deep iron deposits. Requires precision-machined components.", "pm_name": "Pneumatic  Drills"},
#     {"tech_name": " Differential Flotation Process", "era": 4, "desc": "Advanced chemical separation methods allow efficient extraction of sulfur and lead from complex ores. Requires significant oil byproducts for reagent production.", "pm_name": "Flotation"},
# ]

# category_name = "boats"
# tech_dict = [
#     {"tech_name": "Hull Caulking Techniques", "era": 2, "desc": "Refined methods of sealing wooden hulls with tar and hemp, reducing maintenance costs and increasing ship longevity.", "pm_name": "Tarred Hulls"},
#     {"tech_name": "Composite Hull Construction", "era": 3, "desc": "Combining iron bracing with wooden hulls to create sturdier, faster ships for both military and trade.", "pm_name": "Ironbraced Shipbuilding"},
#     {"tech_name": "Torpedo Boat Development", "era": 3, "desc": "Light, rapid-attack vessels armed with torpedoes, ideal for coastal defense.", "pm_name": "Torpedo Gunboats"},
#     {"tech_name": "Steam Turbine Propulsion", "era": 4, "desc": "High-pressure steam turbines replace older piston engines, allowing larger and faster steamships.", "pm_name": "Turbine Steamers"},
#     {"tech_name": "Welded Hull Prefabrication", "era": 5, "desc": "Assembly-line welding and modular ship sections drastically reduce construction time.", "pm_name": "Welded Prefabs"},
# ]

# category_name = "glass"
# tech_dict = [
#     {"tech_name": "Cylinder Glass Process", "era": 2, "desc": "Developed in the 1840s, this method involves blowing molten glass into a cylinder, splitting it, and flattening it into large panes. Revolutionized window production and reduced reliance on blown glass.", "pm_name": "Cylinder Glass Rolling"},
#     {"tech_name": "Siemens Regenerative Furnace", "era": 3, "desc": "A regenerative heat system for glass furnaces, patented by the Siemens brothers, drastically reduced fuel waste and enabled continuous production.", "pm_name": "Regenerative Glass Furnace"},
#     {"tech_name": "Automated Pressed Glass", "era": 4, "desc": "Mechanized presses standardized glassware production, enabling intricate designs for mass markets like bottles and tableware.", "pm_name": "Glass Pressing Machines"},
#     {"tech_name": "Float Glass Technique", "era": 5, "desc": "A revolutionary method (later perfected by Pilkington in the 1950s) where molten glass floats on tin, creating flawlessly smooth sheets for modern architecture.", "pm_name": "Float Glass Tinning"},
# ]

# category_name = "explosives"
# tech_dict = [
#     {"tech_name": "Smokeless Propellant Synthesis", "era": 3, "desc": "The development of nitrocellulose-based propellants revolutionizes firearms and artillery, replacing black powder with cleaner-burning, more powerful explosives. This innovation reduces visibility on battlefields and increases ballistic efficiency.", "pm_name": "Nitrocellulose Propellant"},
#     {"tech_name": "TNT Industrialization", "era": 4, "desc": "Trinitrotoluene (TNT) becomes the explosive of choice for mining and warfare due to its stability and potency. Its synthesis requires advanced chemical infrastructure and creates lucrative export opportunities.", "pm_name": "TNT Condensation"},
#     {"tech_name": "Ammonium Nitrate Mass Production", "era": 5, "desc": "The Haber process enables large-scale ammonium nitrate synthesis, creating dual-use explosives for agriculture and warfare. Nations with fertilizer industries gain a strategic edge.", "pm_name": "Haber Process Explosives"},
# ]

# category_name = "silk"
# tech_dict = [
#     {"tech_name": "Mulberry Hybridization", "era": 2, "desc": "Selective breeding of mulberry trees to create hardier varieties with larger leaves, improving silkworm feeding efficiency and disease resistance.", "pm_name": "Nutrient-Rich Fertilization"},
#     {"tech_name": "Synthetic Dye Synthesis", "era": 3, "desc": "Development of aniline dyes derived from coal tar, enabling vibrant artificial colors to compete with natural dyes.", "pm_name": "Coal Tar Colorants"},
#     {"tech_name": "Mechanical Reeling Automation", "era": 4, "desc": "Introduction of steam-powered reeling machines to automate silk thread extraction from cocoons.", "pm_name": "Precision Steam Reeling"},
#     {"tech_name": "Rayon Production", "era": 5, "desc": "Development of artificial silk from cellulose, creating competition for natural silk.", "pm_name": "Cellulose Fiber Synthesis"},
# ]

# category_name = "steel"
# tech_dict = [
#     {"tech_name": "Basic Steel Refining", "era": 3, "desc": "A refinement of the Bessemer process using dolomite linings to remove phosphorus from pig iron, enabling the use of lower-grade iron ores. This innovation reduces reliance on high-quality ore imports but increases sulfur dependency.", "pm_name": "Acidic Bessemer Conversion"},
#     {"tech_name": "Alloy Steel Integration", "era": 4, "desc": "Introduces nickel-alloyed steel for armor and machinery, vastly improving durability. This method favors nations with access to nickel.", "pm_name": "Nickel and Steel Armor Plating"},
#     {"tech_name": "Continuous Casting Process", "era": 5, "desc": "Electrified mills automate steel shaping, enabling mass production of standardized beams and sheets. Requires heavy electricity and tooling investments.", "pm_name": "Electrified Rolling Mills"},
# ]

# category_name = "tools"
# tech_dict = [
#     {"tech_name": "Steam-Driven Mechanization", "era": 2, "desc": "The integration of steam engines into tool workshops enables mass production of standardized parts, reducing reliance on skilled artisans and increasing output.", "pm_name": "Steam Drop Hammers"},
#     {"tech_name": "Electroprecision Machining", "era": 4, "desc": "Electric motors power precision lathes and grinders, enabling faster production of complex tools with fewer errors.", "pm_name": "Electric Grinding Wheels"},
#     {"tech_name": "High-Speed Alloy Synthesis", "era": 5, "desc": "Alloying steel with tungsten and chromium creates durable, heat-resistant tools capable of high-speed industrial processes.", "pm_name": "Tungsten Carbide Tools"},
# ]

# category_name = "military"
# tech_dict = [
#     {"tech_name": "Metallic Cartridge Casings", "era": 3, "desc": "The adoption of brass cartridge casings revolutionizes ammunition production, improving reliability and rate of fire for infantry arms.", "pm_name": "Metallic Cartridge Ammunition"},
#     {"tech_name": "Recoil-Operated Mechanisms", "era": 4, "desc": "Harnessing recoil energy for automatic reloading enables the first true machine guns, transforming battlefield tactics.", "pm_name": "Automatic Weapons"},
#     {"tech_name": "Composite Armor Plating", "era": 5, "desc": "Layered steel and hardened alloys allow for lighter yet more resilient armor, enabling faster, deadlier tanks.", "pm_name": "Composite Armor Tanks"},
#     {"tech_name": "Portable Automatic Firearms", "era": 5, "desc": "Lightweight, rapid-fire submachine guns redefine close-quarters combat, ideal for trench warfare and urban engagements.", "pm_name": "Submachine Gun Production"},
# ]

def to_snake_case(text):
    return re.sub(r'[\s\-]+', '_', text.strip()).lower()

def get_tech_schema(tech):
    return f"""{to_snake_case(tech['tech_name'])} = {{
    era = era_{tech['era']}
    texture = "gfx/interface/icons/invention_icons/canneries.dds"
    category = production
    can_research = no

    ai_weight = {{
        value = 1
    }}
}}

"""

def get_journal_schema(tech, previous_tech, category_name):
    return f"""
        else_if = {{
            limit = {{
                AND = {{
                    NOT = {{
                        has_technology_researched = {to_snake_case(tech['tech_name'])}
                    }}
                    has_technology_researched = {to_snake_case(previous_tech['tech_name'])}
                }}
            }}
            add_technology_researched = {to_snake_case(tech['tech_name'])}
            scope:journal_entry = {{
                add_progress = {{
                    name = invention_{category_name}_progress_bar
                    value = -100
                }}
            }}
        }}

"""

def get_pm_schema(tech):
    return f"""pm_{to_snake_case(tech['pm_name'])} = {{
        texture = "gfx/interface/icons/production_method_icons/bakeries.dds" 
        unlocking_technologies = {{ {to_snake_case(tech['tech_name'])} }}

        building_modifiers = {{  
            workforce_scaled = {{  

            }}
            level_scaled = {{  

            }}
        }}
    }}

"""
# category_name = ""
# tech_dict = [
#     {"tech_name": "", "era": 2, "desc": "", "pm_name": ""},
#     {"tech_name": "", "era": 3, "desc": "", "pm_name": ""},
#     {"tech_name": "", "era": 4, "desc": "", "pm_name": ""},
#     {"tech_name": "", "era": 5, "desc": "", "pm_name": ""},
# ]

category_name = "plantations"
tech_dict = [
    {"tech_name": "Selective Cultivation Techniques", "era": 2, "desc": "Development of systematic plant selection and grafting methods to improve yields of cash crops.", "pm_name": "Clonal Propagation"},
    {"tech_name": "Steam-Powered Presses", "era": 2, "desc": "Early steam machinery for processing raw plantation goods", "pm_name": "Mechanical Resin Extraction"},
    {"tech_name": "Tropical Agronomy Studies", "era": 3, "desc": "Scientific soil analysis and crop rotation systems for plantations", "pm_name": "Shade-Grown Polyculture"},
    {"tech_name": "Hydraulic Press Innovations", "era": 3, "desc": "High-pressure processing equipment for compacting goods", "pm_name": "Steam-Cured Leaves"},
    {"tech_name": "Synthetic Alkaloid Extraction", "era": 4, "desc": "Chemical processes to isolate active compounds from plants", "pm_name": "Morphine Refinement"},
    {"tech_name": "Vacuum Sealing", "era": 4, "desc": "Air-tight packaging for long-distance transport", "pm_name": "Nitrogen-Flushed Bags"},
    {"tech_name": "Photoperiod Control", "era": 5, "desc": "Artificial lighting to manipulate plant growth cycles", "pm_name": "Electric Grow Lamps"},
    {"tech_name": "Mycorrhizal Inoculation", "era": 5, "desc": "Soil fungi symbiosis to enhance nutrient uptake", "pm_name": "Bioaugmented Cultivation"},
]

technologies = f"\n\n# {category_name.capitalize()}\n"
journal = f"""\n\non_monthly_pulse = {{
		effect = {{
			if = {{
				limit = {{ 
					scope:journal_entry = {{
						"scripted_bar_progress(invention_{category_name}_progress_bar)" >= 100
					}}
				}}
				if = {{
					limit = {{
						AND = {{
							NOT = {{
								has_technology_researched = {to_snake_case(tech_dict[0]['tech_name'])}
							}}
						}}
					}}
					add_technology_researched = {to_snake_case(tech_dict[0]['tech_name'])}
					scope:journal_entry = {{
						add_progress = {{
							name = invention_{category_name}_progress_bar
							value = -100
						}}
					}}
				}}

"""
pm = "\n\n"
pmg = f"""\n\npmg_invention_building_{category_name}_industry = {{
	texture = "gfx/interface/icons/generic_icons/mixed_icon_base.dds"
	production_methods = {{
		pm_no_invention
"""
locales = "\n\n"

for i, tech in enumerate(tech_dict):
    technologies += get_tech_schema(tech)
    pm += get_pm_schema(tech)
    pmg += f"pm_{to_snake_case(tech['pm_name'])}\n"

    if i > 0:
        journal += get_journal_schema(tech, tech_dict[i-1], category_name)

    if i == len(tech_dict) - 1:
        journal += "}\n}\n}"
        pmg += "}\n}"

    locales += f" {to_snake_case(tech['tech_name'])}:0 \"{tech['tech_name']}\"\n"
    locales += f" {to_snake_case(tech['tech_name'])}_desc:0 \"{tech['desc']}\"\n"
    locales += f" pm_{to_snake_case(tech['pm_name'])}:0 \"{tech['pm_name']}\"\n"

locales += f" pmg_invention_building_{category_name}_industry:0 \"Invention\""

with open("common/technology/technologies/11_production.txt", "a") as tech_file:
    tech_file.write(autopep8.fix_code(technologies))

with open("common/production_method_groups/02_industry.txt", "a") as pmg_file:
    pmg_file.write(autopep8.fix_code(pmg))
    
with open("common/production_methods/02_industry.txt", "a") as pm_file:
    pm_file.write(autopep8.fix_code(pm))

with open("localization/english/specialization_pm_l_english.yml", "a") as loc_file:
    loc_file.write(locales)


with open("common/journal_entries/00_specialization_journal_entries.txt", "r") as journal_file:
    lines = journal_file.readlines()


category_start = f"je_{category_name}_invention_progress = {{"

# Find the category start line
category_line_idx = -1
for i, line in enumerate(lines):
    if line.strip().startswith(category_start.strip()):
        category_line_idx = i
        break
if category_line_idx == -1:
    raise ValueError(f"Category je_{category_name}_invention_progress not found in file")

# Track brace balance to find the end of the category block and locate the weight line
brace_balance = 1  # Already inside the opening brace of the category
weight_line_idx = -1
end_line_idx = -1

for i in range(category_line_idx + 1, len(lines)):
    current_line = lines[i]
    open_braces = current_line.count('{')
    close_braces = current_line.count('}')
    brace_balance += open_braces - close_braces
    
    stripped_line = current_line.lstrip()
    if stripped_line.startswith("weight ="):
        weight_line_idx = i
    
    if brace_balance <= 0:
        end_line_idx = i
        break

if weight_line_idx == -1:
    raise ValueError("Weight line not found within the specified category")

# Split the content into lines and properly indent each line
on_monthly_pulse_lines = []
for line in journal.split('\n'):
    # Add a tab to each line to match the category's indentation level
    indented_line = '\t' + line + '\n'
    on_monthly_pulse_lines.append(indented_line)

# Insert the new lines after the weight line
# To preserve existing structure, insert before the line following weight_line_idx
new_lines = []
new_lines.extend(lines[:weight_line_idx + 1])  # include the weight line
new_lines.extend(on_monthly_pulse_lines)       # add the new content
new_lines.extend(lines[weight_line_idx + 1:])  # add the rest

new_lines = "".join(new_lines)

# Write the modified content back to the file
with open("common/journal_entries/00_specialization_journal_entries.txt", 'w', encoding='utf-8-sig') as journal_file:
    journal_file.writelines(autopep8.fix_code(new_lines).replace("scope: ", "scope:"))