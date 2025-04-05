
import discord
import json
from discord.ext import commands
import pandas as pd
import random
import cv2
import numpy as np
import aiohttp
import abilities
import re
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="&", intents=intents)

# Disable the default help command
bot.remove_command('help')

ongoing_battles = {}

class Ability:
    def __init__(self, name, description, power):
        self.name = name if name else "Unknown"
        self.description = description if description else "No description available."
        self.power = power if power else 0

class Ball:
    def __init__(self, name, hp, atk, abilities):
        self.name = name if name else "Unknown"
        self.hp = hp
        self.atk = atk
        self.abilities = abilities if abilities else []

    def is_alive(self):
        return self.hp > 0

    def choose_action(self):
        return random.choice(self.abilities + ["attack"])

    def attack(self, target):
        damage = random.randint(1, self.atk)
        target.hp -= damage
        return f"{self.name} attacks and deals {damage} damage!"

    def use_ability(self, ability, target):
        return ability.apply(target)

# Read the Excel file
df = pd.read_excel('Abilities.xlsx')

abilities = []
balls_abilities = {}
valid_balls = set(df['BALL'])

# Process the data and store abilities in a dictionary
for index, row in df.iterrows():
    ability = Ability(row['ABILITY NAME'], row['ABILITY'], row['WORTH'])
    if row['BALL'] not in balls_abilities:
        balls_abilities[row['BALL']] = []
    balls_abilities[row['BALL']].append(ability)

decks = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

REFERENCE_IMAGES = {
    'shiny': "shiny.png",
    'mythic': "mythic.png",
    'boss': "boss.png",
    'summer': "summer.png",
    'clover': "clover.png",
    'ny': "NY.png",
    'lny': "LNY.png",
    'present': "present.png",
    'spooky': "spooky.png",
    'xmas 22': "xmas22.png",
    'easter': "easter.png",
    'cake': "cake.png",
    'ghost': "ghost.png",
    'gobble': "gobble.png",
    'tree': "tree.png",
    'pride': "pride.png",
    'bat': "bat.png",
    'cc': "CC.png",
    'diamond': "diamond.png",
    'emerald': "emerald.png",
    'valentine': "valentine.png",
    'bday 24': "bday 24.png",
    'event be': "event BE.png",
    'event reich': "event Reich.png",
    'event re': "event RE.png",
    'blossom': "spring 25.png",
    'cake bday': "cake birthday.png",
}

def detect_ball_type(user_image_path):
    user_img = cv2.imread(user_image_path)
    if user_img is None:
        return "normal"
    
    for ball_type, ref_path in REFERENCE_IMAGES.items():
        ref_img = cv2.imread(ref_path) if isinstance(ref_path, str) and os.path.isfile(ref_path) else None
        if ref_img is None:
            continue
        
        if np.array_equal(user_img[-1, -1], ref_img[-1, -1]):
            return ball_type
    
    return "normal"

# Define reference images globally so they are accessible everywhere
# Dictionary for alternative names
# Define alternative names mapping
alternative_names = {
    "british empire":"British Empire",
    "be":"British Empire",
    "BE": "British Empire",
    "British empire":"British Empire",
    "british Empire":"British Empire",
    "Be":"British Empire",
    "bE":"British Empire",
    "reichtangle":"Reichtangle",
    "russian empire":"Russian Empire",
    "RE": "Russian Empire",
    "Re":"Russian Empire",
    "re":"Russian Empire",
    "Russian empire":"Russian Empire",
    "russian Empire":"Russian Empire",
    "mongol empire":"Mongol Empire",
    "mongol empire":"Mongol Empire",
    "mongol Empire":"Mongol Empire",
    "mongol":"Mongol Empire",
    "Mongol":"Mongol Empire",
    "kalmar union":"Kalmar Union",
    "Kalmar": "Kalmar Union",
    "Kalmar union":"Kalmar Union",
    "kalmar Union":"Kalmar Union",
    "kalmar":"Kalmar Union",
    "roman empire":"Roman Empire",
    "ROE": "Roman Empire",
    "roe":"Roman Empire",
    "Roman empire":"Roman Empire",
    "roman Empire":"Roman Empire",
    "Roe":"Roman Empire",
    "papal states":"Papal States",
    "Papal":"Papal States",
    "papal":"Papal States",
    "Papals":"Papal States",
    "papals":"Papal States",
    "Papal states":"Papal States",
    "papal States":"Papal States",
    "polish lithuanian commonwealth":"Polish-Lithuanian Commonwealth",
    "PLC": "Polish-Lithuanian Commonwealth",
    "plc":"Polish-Lithuanian Commonwealth",
    "Polish Lithuanian Commonwealth":"Polish-Lithuanian Commonwealth",
    "polish lithuanian Commonwealth":"Polish-Lithuanian Commonwealth",
    "Plc":"Polish-Lithuanian Commonwealth",
    "Polish Lithuanian commonwealth":"Polish-Lithuanian Commonwealth",
    "qin dynasty":"Qin Dynasty",
    "german empire":"German Empire",
    "ge":"German Empire",
    "holy roman empire":"Holy Roman Empire",
    "hre":"Holy Roman Empire",
    "austria hungary":"Austria-Hungary",
    "ah":"Austria-Hungary",
    "a-h":"Austria-Hungary",
    "hunnic empire":"Hunnic Empire",
    "hunnic":"Hunnic Empire",
    "japanese empire":"Japanese Empire",
    "je":"Japanese Empire",
    "republic of china":"Republic of China",
    "ROC": "Republic of China",
    "soviet union":"Soviet Union",
    "USSR": "Soviet Union",
    "tokugawa shogunate":"Tokugawa Shogunate",
    "united states of america":"United States of America",
    "USA": "United States of America",
    "US": "United States of America",
    "United States": "United States of America",
    "vatican":"Vatican",
    "republic of texas":"Republic of Texas",
    "ROT": "Republic of Texas",
    "texas":"Republic of Texas",
    "russia":"Russia",
    "china":"China",    
    "PRC": "China",
    "austrian empire":"Austrian Empire",
    "joseon":"Joseon",
    "india":"India",
    "ancient greece":"Ancient Greece",
    "japan":"Japan",
    "korea":"Korea",
    "napoleonic france":"Napoleonic France",
    "ottoman empire":"Ottoman Empire",
    "brics":"BRICS",
    "Brics":"BRICS",
    "republic of venice":"Republic of Venice",
    "ROV": "Republic of Venice",
    "venice":"Republic of Venice",
    "south korea":"South Korea",
    "ROK": "South Korea",
    "france":"France",
    "spanish empire":"Spanish Empire",
    "united kingdoms of sweden and norway":"United Kingdoms of Sweden and Norway",    
    "UKOSN": "United Kingdoms of Sweden and Norway",
    "ukosn": "United Kingdoms of Sweden and Norway",
    "united kingdoms of sweden and norway": "United Kingdoms of Sweden and Norway",
    "achaemenid empire":"Achaemenid Empire",
    "macedon":"Macedon",
    "united kingdom":"United Kingdom",    
    "UK": "United Kingdom",
    "empire of brazil":"Empire of Brazil",
    "pakistan":"Pakistan",
    "ancient egypt":"Ancient Egypt",
    "brazil":"Brazil",
    "byzantium":"Byzantium",
    "greenland":"Greenland",
    "portuguese empire":"Portuguese Empire",
    "qing":"Qing",
    "british raj":"British Raj",
    "carthage":"Carthage",
    "italy":"Italy",
    "kingdom of italy":"Kingdom of Italy",
    "third french republic":"Third French Republic",
    "French Republic": "Third French Republic",
    "egypt":"Egypt",
    "soviet russia":"Soviet Russia",
    "turkey":"Turkey",
    "French Empire": "French Empire",
    "iran":"Iran",
    "kingdom of greece":"Kingdom of Greece",
    "konbaung empire":"Konbaung Empire",
    "north german confederation":"North German Confederation",    
    "NGC": "North German Confederation",
    "african union":"African Union",
    "arab league":"Arab League",
    "confederate states":"Confederate States",
    "gaul":"Gaul",
    "germania":"Germania",
    "indonesia":"Indonesia",
    "kingdom of hungary":"Kingdom of Hungary",
    "mayan empire":"Mayan Empire",
    "yugoslavia":"Yugoslavia",
    "germany":"Germany",
    "australia":"Australia",
    "hong kong":"Hong Kong",
    "israel":"Israel",
    "xiongnu":"Xiongnu",
    "spain":"Spain",
    "swedish empire":"Swedish Empire",
    "antarctica":"Antarctica",
    "ming dynasty":"Ming Dynasty",
    "saudi arabia":"Saudi Arabia",
    "franks":"Franks",
    "league of nations":"League of Nations",    
    "LON": "League of Nations",
    "monaco":"Monaco",
    "union of south africa":"Union of South Africa",    
    "UOSA": "Union of South Africa",
    "ukraine":"Ukraine",
    "canada":"Canada",
    "kingdom of two sicilies":"Kingdom of the Two Sicilies",    
    "KOTS": "Kingdom of the Two Sicilies",
    "kingdom of brandenburg":"Kingdom of Brandenburg",    
    "KOB": "Kingdom of Brandenburg",
    "poland":"Poland",
    "sweden":"Sweden",
    "macau":"Macau",
    "scotland":"Scotland",
    "south africa":"South Africa",    
    "SA": "South Africa",
    "greece":"Greece",
    "vietnam":"Vietnam",
    "safavid empire":"Safavid Empire",
    "thailand":"Thailand",
    "parthian empire":"Parthian Empire",
    "north korea":"North Korea",    
    "DPRK": "North Korea",
    "england":"England",
    "european union":"European Union",
    "francoist spain":"Francoist Spain",
    "manchukuo":"Manchukuo",
    "nato":"NATO",
    "republican spain":"Republican Spain",
    "united arab republic":"United Arab Republic",    
    "UAR": "United Arab Republic",
    "united nations":"United Nations",
    "warsaw pact":"Warsaw Pact",
    "weimar republic":"Weimar Republic",
    "zhou":"Zhou",
    "asean":"ASEAN",
    "argentine confederation":"Argentine Confederation",
    "kingdom of hawaii":"Kingdom of Hawaii",
    "kingdom of bali":"Kingdom of Bali",
    "kingdom of bora bora":"Kingdom of Bora Bora",
    "yuan dynasty":"Yuan Dynasty",
    "bavaria":"Bavaria",
    "algeria":"Algeria",
    "argentina":"Argentina",
    "bangladesh":"Bangladesh",
    "colombia":"Colombia",
    "czechia":"Czechia",
    "iraq":"Iraq",
    "malaysia":"Malaysia",
    "mexico":"Mexico",
    "myanmar":"Myanmar",
    "netherlands":"Netherlands",
    "nigeria":"Nigeria",
    "norway":"Norway",
    "peru":"Peru",
    "philippines":"Philippines",
    "portugal":"Portugal",
    "prussia":"Prussia",
    "romania":"Romania",
    "singapore":"Singapore",
    "switzerland":"Switzerland",
    "syria":"Syria",
    "tuvalu":"Tuvalu",
    "uae":"UAE",
    "venezuela":"Venezuela",
    "mali empire":"Mali Empire",
    "soviet ukraine":"Soviet Ukraine",
    "federal republic of central america":"Federal Republic of Central America",
    "frca":"Federal Republic of Central America",
    "ancient athens":"Ancient Athens",
    "ancient sparta":"Ancient Sparta",
    "babylon":"Babylon",
    "czechoslovakia":"Czechoslovakia",
    "ethiopian empire":"Ethiopian Empire",
    "french indochina":"French Indochina",
    "nauru":"Nauru",
    "numidia":"Numidia",
    "quebec":"Quebec",
    "siam":"Siam",
    "south vietnam":"South Vietnam",
    "taiwan":"Taiwan",
    "wales":"Wales",
    "west germany":"West Germany",
    "kingdom of egypt":"Kingdom of Egypt",
    "mughal empire":"Mughal Empire",
    "angola":"Angola",
    "austria":"Austria",
    "azerbaijan":"Azerbaijan",
    "bahamas":"Bahamas",
    "belarus":"Belarus",
    "belgium":"Belgium",
    "bolivia":"Bolivia",
    "bulgaria":"Bulgaria",
    "chile":"Chile",
    "croatia":"Croatia",
    "cuba":"Cuba",
    "cyprus":"Cyprus",
    "denmark":"Denmark",
    "dr congo":"DR Congo",
    "ecuador":"Ecuador",
    "ethiopia":"Ethiopia",
    "finland":"Finland",
    "hungary":"Hungary",
    "iberian union":"Iberian Union",
    "jamaica":"Jamaica",
    "jordan":"Jordan",
    "kazakhstan":"Kazakhstan",
    "kenya":"Kenya",
    "kuwait":"Kuwait",
    "libya":"Libya",
    "morocco":"Morocco",
    "north vietnam":"North Vietnam",
    "oman":"Oman",
    "qatar":"Qatar",
    "san marino":"San Marino",
    "serbia":"Serbia",
    "slovakia":"Slovakia",
    "sri lanka":"Sri Lanka",
    "sudan":"Sudan",
    "tunisia":"Tunisia",
    "turkmenistan":"Turkmenistan",
    "uruguay":"Urugay",
    "uzbekistan":"Uzbekistan",
    "yemen":"Yemen",
    "republic of new granada":"Republic of New Granada",
    "faroe islands":"Faroe Islands",
    "trinidad and tobago":"Trinidad and Tobago",
    "orange free state":"Orange Free State",
    "east germany":"East Germany",
    "emirate of nejd":"Emirate of Nejd",
    "free france":"Free France",
    "golden horde":"Golden Horde",
    "maldives":"Maldives",
    "northern ireland":"Northern Ireland",
    "tibet":"Tibet",
    "vichy france":"Vichy France",
    "andorra":"Andorra",
    "brunei":"Brunei",
    "grand duchy of tuscany":"Grand Duchy of Tuscany",
    "khedivate of egypt":"Khedivate of Egypt",
    "micronesia":"Micronesia",
    "byelorussian ssr":"Byelorussian SSR",
    "tonga":"Tonga",
    "khmer empire":"Khmer Empire",
    "barbados":"Barbados",
    "kingdom of saxony":"Kingdom of Saxony",
    "marshall islands":"Marshall Islands",
    "armenia":"Armenia",
    "bahrain":"Bahrain",
    "cambodia":"Cambodia",
    "chad":"Chad",
    "congo free state":"Congo Free State",
    "equatorial guinea":"Equatorial Guinea",
    "fatimid caliphate":"Fatimid Caliphate",
    "georgia":"Georgia",
    "ghana":"Ghana",
    "guatemala":"Guatemala",
    "guyana":"Guyana",
    "ireland":"Ireland",
    "kyrgyzstan":"Kyrgyzstan",
    "latvia":"Latvia",
    "lithuania":"Lithuania",
    "mali":"Mali",
    "malta":"Malta",
    "mongolia":"Mongolia",
    "new zealand":"New Zealand",
    "samoa":"Samoa",
    "slovenia":"Slovenia",
    "togo":"Togo",
    "uganda":"Uganda",
    "zambia":"Zambia",
    "zimbabwe":"Zimbabwe",
    "duchy of limburg":"Duchy of Limburg",
    "malawi":"Malawi",
    "kingdom of sardinia":"Kingdom of Sardinia",
    "rashidi emirate":"Rashidi Emirate",
    "costa rica":"Costa Rica",
    "dominica":"Dominica",
    "guinea bissau":"Guinea-Bissau",
    "sao tome and principe":"Sao Tome and Principe",
    "tannu tuva":"Tannu Tuva",
    "free city of frankfurt":"Free City of Frankfurt",
    "seychelles":"Seychelles",
    "afghanistan":"Afghanistan",
    "albania":"Albania",
    "belize":"Belize",
    "bosnia and herzegovina":"Bosnia and Herzegovina",
    "bosnia":"Bosnia and Herzegovina",
    "botswana":"Botswana",
    "cameroon":"Cameroon",
    "ceylon":"Ceylon",
    "congo":"Congo",
    "dominican republic":"Dominican Republic",
    "eritrea":"Eritrea",
    "estonia":"Estonia",
    "eswatini":"Eswatini",
    "fiji":"Fiji",
    "free city of danzig":"Free City of Danzig",
    "gambia":"Gambia",
    "haiti":"Haiti",
    "honduras":"Honduras",
    "ivory coast":"Ivory Coast",
    "khiva":"Khiva",
    "laos":"Laos",
    "lebanon":"Lebanon",
    "liechtenstein":"Liechtenstein",
    "moldova":"Moldova",
    "mossi kingdoms":"Mossi Kingdoms",
    "mozambique":"Mozambique",
    "nepal":"Nepal",
    "nicaragua":"Nicaragua",
    "niger":"Niger",
    "palestine":"Palestine",
    "paraguay":"Paraguay",
    "saint kitts and nevis":"Saint Kitts and Nevis",
    "saint lucia":"Saint Lucia",
    "somaliland":"Somaliland",
    "south sudan":"South Sudan",
    "south yemen":"South Yemen",
    "tajikistan":"Tajikistan",
    "tanzania":"Tanzania",
    "western sahara":"Western Sahara",
    "peru bolivian confederation":"Peru-Bolivian Confederation",
    "cape verde":"Cape Verde",
    "guinea":"Guinea",
    "grenada":"Grenada",
    "palau":"Palau",
    "solomon islands":"Solomon Islands",
    "saint vincent and the grenadines":"Saint Vincent and the Grenadines",
    "vanuatu":"Vanuatu",
    "principality of moldova":"Principality of Moldova",
    "qajar dynasty":"Qajar Dynasty",
    "antigua and barbuda":"Antigua and Barbuda",
    "benin":"Benin",
    "bhutan":"Bhutan",
    "burkina faso":"Burkina Faso",
    "burundi":"Burundi",
    "central african republic":"Central African Republic",
    "car":"Central African Republic",
    "comoros":"Comoros",
    "el salvador":"El Salvador",
    "gabon":"Gabon",
    "hejaz":"Hejaz",
    "iceland":"Iceland",
    "kiribati":"Kiribati",
    "kosovo":"Kosovo",
    "liberia":"Liberia",
    "lesotho":"Lesotho",
    "luxembourg":"Luxembourg",
    "madagascar":"Madagascar",
    "majapahit":"Majapahit",
    "mauritania":"Mauritania",
    "mauritius":"Mauritius",
    "montenegro":"Montenegro",
    "namibia":"Namibia",
    "nanda empire":"Nanda Empire",
    "north macedonia":"North Macedonia",
    "panama":"Panama",
    "papua new guinea":"Papua New Guinea",
    "paris commune":"Paris Commune",
    "rwanda":"Rwanda",
    "senegal":"Senegal",
    "sierra leone":"Sierra Leone",
    "somalia":"Somalia",
    "suriname":"Suriname",
    "timor leste":"Timor-Leste",
    "dahomey":"Dahomey",
    "djibouti":"Djibouti",
    "djibouti union":"Djibouti Union",
    "birthday":"Birthday",

    # Add more alternative names as needed
}

def get_primary_name(ball_name):
    """ Returns the primary name of the ball if an alternative exists. """
    return alternative_names.get(ball_name, ball_name)

def detect_ball_type(user_image_path):
    """
    Detect if the uploaded card matches one of the special backgrounds.
    Returns the ball type as a string or "normal" if no match.
    """
    user_img = cv2.imread(user_image_path)
    if user_img is None:
        return "normal"
    
    for ball_type, ref_path in REFERENCE_IMAGES.items():
        ref_img = cv2.imread(ref_path)
        if ref_img is None:
            continue
        
        if np.array_equal(user_img[-1, -1], ref_img[-1, -1]):
            return ball_type
    
    return "normal"

@bot.command(name="addball", description="Add a countryball to your deck by detecting its type.")
async def addball(ctx, *, ball_name: str):
    # Normalize input: remove dashes, convert to lowercase, and check alternative names
    ball_name = ball_name.replace("-", " ").lower()
    ball_name = get_primary_name(ball_name)  # Convert to primary name if alternative exists

    if ball_name not in valid_balls:
        await ctx.send(f"{ball_name} is not a valid countryball from the provided list.")
        return
    if ctx.message.reference is None or ctx.message.reference.resolved.author.id != 999736048596816014:
        await ctx.send("You can only add countryballs from the ballsdex card.")
        return
    
    # Get the attached image from the referenced message
    referenced_message = ctx.message.reference.resolved
    if not referenced_message.attachments:
        await ctx.send("No image found in the referenced message.")
        return
    
    image_url = referenced_message.attachments[0].url
    user_image_path = "downloaded_image.png"
    
    # Download the image from Discord
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as resp:
            if resp.status == 200:
                with open(user_image_path, "wb") as f:
                    f.write(await resp.read())
            else:
                await ctx.send("Failed to download the image.")
                return
    
    ball_type = detect_ball_type(user_image_path)
    atk_buffs = {"shiny": 2500, "mythic": random.randint(4200, 6000), "boss": 10000, "normal": 0, "LNY": 750, "present": 250, "NY": 250, "summer": 250, "gobble": 250, "Xmas 22": 750, "pride": 250, "bat": 250, "CC": 0, "diamond": 0, "emerald": 0, "spooky": 750, "clover": 250, "easter": 250, "ghost": 250, "tree": 250, "cake": 250, "event RE": 1000, "event Reich": 1000, "event BE": 1000, "valentine": 250, "spring 25":250}
    hp_buffs = {"shiny": 2500, "mythic": random.randint(6000, 7200), "boss": 10000, "normal": 0, "LNY": 750, "present": 250, "NY": 250, "summer": 250, "gobble": 250, "Xmas 22": 750, "pride": 250, "bat": 250, "CC": 0, "diamond": 0, "emerald": 0, "spooky": 750, "clover": 250, "easter": 250, "ghost": 250, "tree": 250, "cake": 250, "event RE": 1000, "event Reich": 1000, "event BE": 1000, "valentine": 250, "spring 25":250}
    symbols = {"shiny": "✨", "mythic": "🌌", "boss": "⚔️", "normal": "", "summer": ":sunny:", "clover": ":four_leaf_clover:", "NY": ":sparkler:", "LNY": "🧧", "present": ":gift:", "spooky": "🎃", "ghost": ":ghost:", "bat": ":bat:", "Xmas 22": ":snowflake:", "easter": ":egg:", "cake": ":tada:", "gobble": ":turkey:", "tree": "🎄", "pride": ":rainbow_flag:", "CC": ":trophy:", "diamond": ":gem:", "emerald": "❇️", "valentine": ":revolving_hearts:", "B-Day 24": "🎂", "event RE": ":crown:", "event Reich": ":crown:", "event BE": ":crown:" , "blossom": "🌸", "cake BD": "🎂"}
    
    buff_value = atk_buffs.get(ball_type, (int(ball_type) * 1000 if ball_type.isdigit() else 0))
    symbol = symbols.get(ball_type, f"🏆" if ball_type.isdigit() else "")
    
    if ctx.author.id not in decks:
        decks[ctx.author.id] = []

    if len(decks[ctx.author.id]) >= 25:
        await ctx.send("You cannot add more than 25 countryballs to your deck.")
        return

    message_content = referenced_message.content
    id_match = re.search(r"ID:\s*`?#([A-Fa-f0-9]+)`?", message_content)
    atk_match = re.search(r"ATK:\s*([\d]+)", message_content)
    hp_match = re.search(r"HP:\s*([\d]+)", message_content)
    
    if not id_match or not atk_match or not hp_match:
        await ctx.send("Failed to extract HP, ATK, or ID from the card details.")
        return

    ball_id = id_match.group(1)
    atk = int(atk_match.group(1)) + buff_value
    hp = int(hp_match.group(1)) + buff_value

    # Prevent duplicate IDs across all decks using ID matching
    if any(ball_id == re.search(r"ID:\s*`?#([A-Fa-f0-9]+)`?", ball.name).group(1) for user_deck in decks.values() for ball in user_deck if re.search(r"ID:\s*`?#([A-Fa-f0-9]+)`?", ball.name)):
        await ctx.send(f"A countryball with ID #{ball_id} is already in a deck and cannot be added again.")
        return

    ball = Ball(f"[{symbol} **{ball_name}**](https://example.com 'ID: #{ball_id}')", hp, atk, balls_abilities.get(ball_name, []))
    decks[ctx.author.id].append(ball)
    if ball_type.isupper():
        ball_type_display = ball_type.upper()
    else:
        ball_type_display = ball_type.capitalize()
    await ctx.send(f"{symbol} {ball_type_display} {ball_name} added to your deck with {hp} HP and {atk} ATK.".strip())

@bot.tree.command(name="spawnboss", description="Spawn a boss ball with 25000 HP and 7500 ATK (Admin or sky.05 only)")
async def spawnboss(interaction: discord.Interaction, boss_name: str):
    admin_id = 1  # Replace with the actual admin ID
    sky_id = 855321365803171851  # Replace with the actual sky.05 ID

    if interaction.user.id not in [admin_id, sky_id]:
        await interaction.response.send_message("You do not have permission to use this command.")
        return

    boss_ball = Ball(boss_name, 250000, 7500, [])
    if "bosses" not in decks:
        decks["bosses"] = []
    decks["bosses"].append(boss_ball)
    await interaction.response.send_message(f"Boss {boss_name} spawned with 25000 HP and 7500 ATK.")

@bot.tree.command(name="bossattack", description="Attack a boss ball (requires a deck of max 10 balls)")
async def bossattack(interaction: discord.Interaction, boss_name: str):
    if interaction.user.id not in decks or len(decks[interaction.user.id]) > 10:
        await interaction.response.send_message("You need a deck of 10 or fewer balls to attack the boss.")
        return

    boss_ball = next((ball for ball in decks["bosses"] if ball.name == boss_name), None)
    if not boss_ball:
        await interaction.response.send_message(f"No boss named {boss_name} found.")
        return

    battle_log = ""
    player_deck = decks[interaction.user.id]

    while any(ball.is_alive() for ball in player_deck) and boss_ball.is_alive():
        attacker = random.choice([ball for ball in player_deck if ball.is_alive()])
        battle_log += attacker.attack(boss_ball) + "\n"
        if not boss_ball.is_alive():
            battle_log += f"{boss_ball.name} is defeated!\n"
            break

        defender = random.choice([ball for ball in player_deck if ball.is_alive()])
        battle_log += boss_ball.attack(defender) + "\n"
        if not defender.is_alive():
            battle_log += f"{defender.name} is defeated!\n"

    winner = "You" if boss_ball.is_alive() else "Boss"
    battle_log += f"{winner} wins the battle!"

    deck_status = "\n".join([f"{ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for ball in player_deck])
    await interaction.response.send_message(f"```\n{battle_log}\n```\nYour updated deck:\n{deck_status}")

@bot.tree.command(name="removefromdeck", description="Remove a countryball from your deck")
async def removefromdeck(interaction: discord.Interaction, number: int):
    if interaction.user.id in decks:
        if 1 <= number <= len(decks[interaction.user.id]):
            removed_ball = decks[interaction.user.id].pop(number - 1)
            await interaction.response.send_message(f"{removed_ball.name} with {removed_ball.hp} HP and {removed_ball.atk} ATK removed from your deck.")
        else:
            await interaction.response.send_message(f"No countryball found at position {number} in your deck.")
    else:
        await interaction.response.send_message("You don't have a deck yet.")

@bot.tree.command(name="checkdeck", description="View your deck or another player's deck")
async def checkdeck(interaction: discord.Interaction, user: discord.User = None):
    user_id = user.id if user else interaction.user.id
    if user_id in decks:
        deck = decks[user_id]
        deck_list = "\n".join([f"{idx + 1}. {'✨ ' if 'shiny' in ball.name.lower() else '🌌 ' if 'mythic' in ball.name.lower() else '⚔️ ' if 'boss' in ball.name.lower() else ''}{ball.name}: {ball.hp} HP, {ball.atk} ATK" for idx, ball in enumerate(deck)])
        if user:
            await interaction.response.send_message(f"{user.display_name}'s deck:\n{deck_list}")
        else:
            await interaction.response.send_message(f"Your deck:\n{deck_list}")
    else:
        if user:
            await interaction.response.send_message(f"{user.display_name} doesn't have a deck yet.")
        else:
            await interaction.response.send_message("You don't have a deck yet.")

@bot.tree.command(name="checkability", description="View a ball's ability")
async def checkability(interaction: discord.Interaction, ball_name: str):
        # Normalize input: remove dashes, convert to lowercase, and check alternative names
    ball_name = ball_name.replace("-", " ").lower()
    ball_name = get_primary_name(ball_name)  # Convert to primary name if alternative exists

    if ball_name in balls_abilities:
        abilities = balls_abilities[ball_name]
        abilities_list = "\n".join([f"{ability.name}: {ability.description}" for ability in abilities])
        await interaction.response.send_message(f"Abilities of {ball_name}:\n{abilities_list}")
    else:
        await interaction.response.send_message(f"{ball_name} is not a valid countryball from the provided list.")

@bot.tree.command(name="attack", description="Attack an opponent's countryball")
async def attack(interaction: discord.Interaction, target: discord.User, attacker_number: int, target_number: int):
    if interaction.user.id in decks and target.id in decks:
        if 1 <= attacker_number <= len(decks[interaction.user.id]) and 1 <= target_number <= len(decks[target.id]):
            ball1 = decks[interaction.user.id][attacker_number - 1]
            ball2 = decks[target.id][target_number - 1]

            battle_log = ball1.attack(ball2)
            if not ball2.is_alive():
                battle_log += f"\n{ball2.name} is defeated!"

            deck1 = "\n".join([f"{idx + 1}. {ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for idx, ball in enumerate(decks[interaction.user.id])])
            deck2 = "\n".join([f"{idx + 1}. {ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for idx, ball in enumerate(decks[target.id])])
            await interaction.response.send_message(f"```\n{battle_log}\n```\nYour updated deck:\n{deck1}\n\nOpponent's updated deck:\n{deck2}")
        else:
            await interaction.response.send_message("Invalid attacker or target number.")
    else:
        await interaction.response.send_message("Both players need to have a deck to attack.")

@bot.tree.command(name="autobattle", description="Start an automated battle between two players' decks")
async def autobattle(interaction: discord.Interaction, opponent: discord.User):
    if interaction.user.id in decks and opponent.id in decks:
        deck1 = decks[interaction.user.id]
        deck2 = decks[opponent.id]
        battle_log = ""

        while any(ball.is_alive() for ball in deck1) and any(ball.is_alive() for ball in deck2):
            attacker1 = random.choice([ball for ball in deck1 if ball.is_alive()])
            defender2 = random.choice([ball for ball in deck2 if ball.is_alive()])
            battle_log += attacker1.attack(defender2) + "\n"
            if not defender2.is_alive():
                battle_log += f"{defender2.name} is defeated!\n"

            if not any(ball.is_alive() for ball in deck2):
                break

            attacker2 = random.choice([ball for ball in deck2 if ball.is_alive()])
            defender1 = random.choice([ball for ball in deck1 if ball.is_alive()])
            battle_log += attacker2.attack(defender1) + "\n"
            if not defender1.is_alive():
                battle_log += f"{defender1.name} is defeated!\n"
                if not any(ball.is_alive() for ball in deck1):
                    winner = opponent.display_name
                    break

                winner = interaction.user.display_name
                battle_log += f"{winner} wins the battle!"

        deck1_status = "\n".join([f"{ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for ball in deck1])
        deck2_status = "\n".join([f"{ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for ball in deck2])
        await interaction.response.send_message(f"```\n{battle_log}\n```\nYour updated deck:\n{deck1_status}\n\nOpponent's updated deck:\n{deck2_status}")
    else:
        await interaction.response.send_message("Both players need to have a deck to start an automated battle.")

@bot.tree.command(name="resetdeck", description="Reset your deck and start anew")
async def resetdeck(interaction: discord.Interaction):
    if interaction.user.id in decks:
        del decks[interaction.user.id]
        await interaction.response.send_message("Your deck has been reset. You can now start anew.")
    else:
        await interaction.response.send_message("You don't have a deck to reset.")

@bot.tree.command(name="battlestats", description="View your battle statistics")
async def battlestats(interaction: discord.Interaction, user: discord.User = None):
    try:
        # Load the battle stats from the JSON file
        with open("battlestats.json", "r") as file:
            try:
                stats = json.load(file)
            except json.JSONDecodeError:
                stats = {}
    except FileNotFoundError:
        stats = {}

    # Determine the user to check stats for
    user_id = user.id if user else interaction.user.id
    user_stats = stats.get(str(user_id), {"wins": 0})

    await interaction.response.send_message(f"<@{user_id}>, you have won {user_stats['wins']} battles.")

@bot.event
async def on_battle_end(winner_id: int, winner_name: str):
    try:
        # Load the battle stats from the JSON file
        with open("battlestats.json", "r") as file:
            stats = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        stats = {}
        # Update the winner's stats
        if str(winner_id) not in stats:
            stats[str(winner_id)] = {"wins": 0, "name": winner_name}
        stats[str(winner_id)]["wins"] += 1

        # Save the updated stats back to the JSON file
        try:
            with open("battlestats.json", "w") as file:
                json.dump(stats, file, indent=4)
        except IOError as e:
            print(f"Error saving stats: {e}")

    # Save the updated stats back to the JSON file
    try:
        with open("battlestats.json", "w") as file:
            json.dump(stats, file, indent=4)
    except IOError as e:
        print(f"Error saving stats: {e}")

# Ensure this function is called when a battle ends
async def end_battle(winner_id: int, winner_name: str):
    await on_battle_end(winner_id, winner_name)

@bot.tree.command(name="useability", description="Use an ability against an opponent")
async def useability(interaction: discord.Interaction, target: discord.User, attacker_number: int, target_number: int, ability_name: str):
    if interaction.user.id in decks and target.id in decks:
        if 1 <= attacker_number <= len(decks[interaction.user.id]) and 1 <= target_number <= len(decks[target.id]):
            ball1 = decks[interaction.user.id][attacker_number - 1]
            ball2 = decks[target.id][target_number - 1]

            ability = next((a for a in ball1.abilities if a.name == ability_name), None)
            if ability:
                battle_log = ball1.use_ability(ability, ball2)
                if not ball2.is_alive():
                    battle_log += f"\n{ball2.name} is defeated!"

                deck1 = "\n".join([f"{idx + 1}. {ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for idx, ball in enumerate(decks[interaction.user.id])])
                deck2 = "\n".join([f"{idx + 1}. {ball.name} (HP: {ball.hp}, ATK: {ball.atk})" for idx, ball in enumerate(decks[target.id])])
                await interaction.response.send_message(f"```\n{battle_log}\n```\nYour updated deck:\n{deck1}\n\nOpponent's updated deck:\n{deck2}")
            else:
                await interaction.response.send_message(f"{ball1.name} doesn't have the ability {ability_name}.")
        else:
            await interaction.response.send_message("Invalid attacker or target number.")
    else:
        await interaction.response.send_message("Both players need to have a deck to use abilities.")

@bot.command(name="help", description="Show the help message")
async def show_help(ctx):
    help_message = """
    **Bot Commands:**

1. `&addball <ball_name>` - Add a countryball to your deck by responding to the ballsdex card with the right name.
2. `/removefromdeck <number>` - Remove a countryball from your deck by its position number.
3. `/checkdeck [user]` - View your deck or another player's deck.
4. `/checkability <ball_name>` - View a ball's abilities.
5. `/attack <target> <attacker_number> <target_number>` - Attack an opponent's countryball with a specific attacker.
6. `/autobattle <opponent>` - Start an automated battle between you and an opponent.
7. `/resetdeck` - Reset your deck and start anew.
8. `/useability <target> <attacker_number> <target_number> <ability_name>` - Use an ability of your countryball against an opponent's countryball.
9. `&help` - Show this help message.
    """
    await ctx.send(help_message)

bot.run("TOKEN")
