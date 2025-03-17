from nodes import NODE_CLASS_MAPPINGS
import random

# Hair colors
hair_colours = [
    # Natural
    "black", "brunette/brown", "dark brown", "medium brown", "light brown",
    "blonde", "platinum blonde", "ash blonde", "honey blonde", "strawberry blonde",
    "red", "auburn", "copper red", "cherry red", "gray/silver", "white",
    # Fashion
    "pastel pink", "lavender", "baby blue", "electric blue", "neon green",
    "hot pink", "ombre", "balayage", "highlights/lowlights", "rose gold",
    "bronde", "mermaid", "rainbow",
    # Fantasy
    "icy blonde", "smoky gray", "mocha brown", "caramel highlights", "opal",
    "galaxy", "tiger eye",
    # Techniques
    "root shadow", "color melt", "dip-dye", "foilayage", "money piece",
]

# Hair styles
hair_styles = [
    # Classic
    "bob", "pixie cut", "shag", "mullet", "bowl cut", "buzz cut",
    # Braided
    "french braid", "dutch braid", "fishtail braid", "boxer braids", "cornrows",
    "micro braids", "fulani braids", "goddess braids", "waterfall braid",
    # Updos
    "bun", "top knot", "chignon", "messy bun", "ballerina bun", "french twist",
    "victory roll",
    # Ponytails
    "high ponytail", "low ponytail", "bubble ponytail", "side ponytail",
    "half-up ponytail",
    # Layers
    "layered cut", "feathered", "beach waves", "sleek straight", "curly", "afro",
    "textured crop",
    # Bangs
    "blunt bangs", "side-swept bangs", "curtain bangs", "wispy bangs",
    "baby bangs",
    # Others
    "wolf cut", "undercut", "fade", "mohawk", "space buns", "half-up half-down",
    "pineapple updo",
]

# Hair adjectives
hair_adjectives = [
    "long", "messy", "wet", "glossy", "sleek", "voluminous", "tousled", "shiny",
    "flowing", "textured",
]

# Helper functions for random selection
def random_hair_colour():
    return random.choice(hair_colours)

def random_hair_style():
    return random.choice(hair_styles)

def random_hair_adjective():
    return random.choice(hair_adjectives)

def random_age():
    return random.randint(25, 34)

# Function to generate prompts dynamically
def generate_prompts(room, profiles):
    prompts = {}
    if not profiles:  # Handle empty profiles case (e.g., "none" category)
        prompts[1] = "No prompt selected"
    else:
        for index, profile in enumerate(profiles, start=1):
            prompt = (
                f"hyperrealistic 8K, {profile['age']}-year-old woman, "
                f"{profile['hair_adjective']} {profile['hairstyle']} "
                f"{profile['haircolour']} hair, stunningly beautiful, "
                f"{profile['attire']}, dynamic pose, {room}, high resolution, "
                f"best quality, real human aesthetic, high detail, realistic textures, uncensored, nsfw"
            )
            prompts[index] = prompt
    return prompts

# Define the structure of NSFW presets
NSFW_PRESETS_STRUCTURE = {
    "none": {"label": "Tidak Ada", "profiles": []},
"cum on face": {
        "label": "Cum on Face",
        "profiles": [
            {"attire": "nude with glossy cum on face from one man, seductive gaze"},
            {"attire": "nude with cum trails on face and body from one man, drooling"},
            {"attire": "nude with cum trails on face and body from one man, drooling"},
            {"attire": "nude with cum on face and wet skin from one man, intense expression"},
            {"attire": "nude with cum on face and direct eye contact from one man"},
            {"attire": "nude with cum on face and flushed cheeks from one man"},
            {"attire": "nude with cum on face and parted lips from one man"},
            {"attire": "nude with cum on face and sweat on skin from one man"},
            {"attire": "nude with cum on face and dim lighting from one man"},
            {"attire": "nude with cum on face and high detail from one man"}
        ]
    },
    "cumshot on tongue": {
        "label": "Cumshot on Tongue",
        "profiles": [
            {"attire": "nude with thick cum on tongue from one man, tongue out"},
            {"attire": "nude with cum on tongue and wet lips from one man, seductive gaze"},
            {"attire": "nude with cum on tongue and face from one man, drooling"},
            {"attire": "nude with cum on tongue and intense expression from one man"},
            {"attire": "nude with cum on tongue and glistening skin from one man"},
            {"attire": "nude with cum on tongue and high-angle shot from one man"},
            {"attire": "nude with cum on tongue and parted lips from one man"},
            {"attire": "nude with cum on tongue and flushed cheeks from one man"},
            {"attire": "nude with cum on tongue and sweat on skin from one man"},
            {"attire": "nude with cum on tongue and dim lighting from one man"}
        ]
    },
    "dildo": {
        "label": "Dildo",
        "profiles": [
            {"attire": "nude using dildo vaginally, legs spread"},
            {"attire": "nude with dildo vaginally, kneeling with intense expression"},
            {"attire": "nude using dildo vaginally, lying down with flushed cheeks"},
            {"attire": "nude with dildo vaginally, dynamic pose with sweat on skin"},
            {"attire": "nude using dildo vaginally, sitting with parted lips"},
            {"attire": "nude with dildo vaginally, legs apart on silk sheets"},
            {"attire": "nude using dildo vaginally, moaning expression"},
            {"attire": "nude with dildo vaginally, seductive gaze"},
            {"attire": "nude using dildo vaginally, high detail"},
            {"attire": "nude with dildo vaginally, dim lighting"}
        ]
    },
    "from behind": {
        "label": "From Behind",
        "profiles": [
            {"attire": "nude, lying on stomach, ass and pussy visible from behind"},
            {"attire": "nude, all fours, spreading ass, pussy juice visible"},
            {"attire": "nude, kneeling, ass up, pussy glistening from behind"},
            {"attire": "nude, standing, ass exposed, pussy visible with sweat on skin"},
            {"attire": "nude, bending over, ass and pussy in focus"},
            {"attire": "nude, on knees, spreading ass, pussy in high detail"},
            {"attire": "nude, lying down, ass raised, pussy visible with dim lighting"},
            {"attire": "nude, crouching, ass exposed, pussy visible with flushed skin"},
            {"attire": "nude, leaning forward, ass and pussy in view, realistic textures"},
            {"attire": "nude, on all fours, pussy juice dripping from behind"}
        ]
    },
    "kneeling blowjob": {
        "label": "Kneeling Blowjob",
        "profiles": [
            {"attire": "nude, kneeling, performing deepthroat blowjob on one man"},
            {"attire": "nude, kneeling, blowjob with saliva dripping on one man"},
            {"attire": "nude, kneeling, blowjob with cum on face from one man"},
            {"attire": "nude, kneeling, intense blowjob on one man, seductive gaze"},
            {"attire": "nude, kneeling, blowjob with drool from one man, flushed cheeks"},
            {"attire": "nude, kneeling, blowjob with hand on head from one man"},
            {"attire": "nude, kneeling, blowjob with cum dripping from one man"},
            {"attire": "nude, kneeling, blowjob with sweat on skin from one man"},
            {"attire": "nude, kneeling, blowjob with dim lighting from one man"},
            {"attire": "nude, kneeling, blowjob with high detail from one man"}
        ]
    },
    "kneeling tongue out": {
        "label": "Kneeling Tongue Out",
        "profiles": [
            {"attire": "wearing decent dress, kneeling with tongue out, seductive gaze, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and wet lips, intense expression, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and glistening skin, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and playful pose, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and dynamic angle, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and steamy background, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and parted lips, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and flushed cheeks, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and sweat on skin, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"},
            {"attire": "wearing decent dress, kneeling with tongue out and high detail, (1girl:1.6), (solo:1.6), (alone:1.6), (pov), eyes closed, anticipation, (looking up), (close top view), (facing straight up into the camera), cinematic, photorealistic"}
        ]
    },
    "penetration": {
        "label": "Penetration",
        "profiles": [
            {"attire": "nude, missionary position with vaginal penetration by one man, moaning expression"},
            {"attire": "nude, cowgirl position with vaginal penetration by one man, sweat on skin"},
            {"attire": "nude, doggy-style with vaginal penetration by one man, intense expression"},
            {"attire": "nude, reverse cowgirl with vaginal penetration by one man, dynamic angle"},
            {"attire": "nude, standing sex with vaginal penetration by one man, flushed cheeks"},
            {"attire": "nude, squatting cowgirl with vaginal penetration by one man, realistic textures"},
            {"attire": "nude, lying on side with vaginal penetration by one man, dim lighting"},
            {"attire": "nude, kneeling with vaginal penetration by one man, seductive gaze"},
            {"attire": "nude, sitting with vaginal penetration by one man, parted lips"},
            {"attire": "nude, against wall with vaginal penetration by one man, high detail"}
        ]
    },
    "pov blowjob": {
        "label": "POV Blowjob",
        "profiles": [
            {"attire": "nude, POV blowjob on one man, deepthroat with saliva dripping"},
            {"attire": "nude, POV blowjob with cum on face from one man, intense gaze"},
            {"attire": "nude, POV blowjob with wet lips from one man, drooling"},
            {"attire": "nude, POV blowjob with cum on tongue from one man, parted lips"},
            {"attire": "nude, POV blowjob with hand on head from one man, flushed cheeks"},
            {"attire": "nude, POV blowjob with high-angle shot from one man, realistic textures"},
            {"attire": "nude, POV blowjob with sweat on skin from one man"},
            {"attire": "nude, POV blowjob with dim lighting from one man"},
            {"attire": "nude, POV blowjob with seductive gaze from one man"},
            {"attire": "nude, POV blowjob with high detail from one man"}
        ]
    },
    "spreading legs": {
        "label": "Spreading Legs",
        "profiles": [
            {"attire": "nude, lying on back with legs spread, pussy glistening"},
            {"attire": "nude, sitting with legs spread, pussy visible with sweat on skin"},
            {"attire": "nude, standing with legs spread, pussy visible with seductive pose"},
            {"attire": "nude, kneeling with legs spread, pussy in focus"},
            {"attire": "nude, lying with legs spread and masturbating, intense expression"},
            {"attire": "nude, sitting with legs spread and wet pussy, flushed cheeks"},
            {"attire": "nude, lying with legs spread and cum dripping, dim lighting"},
            {"attire": "nude, kneeling with legs spread and realistic textures"},
            {"attire": "nude, sitting with legs spread and steamy background"},
            {"attire": "nude, standing with legs spread and high detail"}
        ]
    },
    "shower tease": {
        "label": "Shower Tease",
        "profiles": [
            {"attire": "nude, standing in steamy shower with water droplets, seductive pose"},
            {"attire": "nude, sitting in shower with legs apart, water streaming"},
            {"attire": "nude, leaning against shower wall with wet skin, parted lips"},
            {"attire": "nude, standing in shower with soap suds, glistening body"},
            {"attire": "nude, sitting in shower with steamy air, intense expression"},
            {"attire": "nude, standing in shower with seductive gaze, misty background"},
            {"attire": "nude, leaning forward in shower with water dripping, flushed cheeks"},
            {"attire": "nude, sitting in shower with warm water, realistic textures"},
            {"attire": "nude, standing in shower with misty air, high detail"},
            {"attire": "nude, leaning in shower with glistening skin, dim lighting"}
        ]
    },
    "missionary passion": {
        "label": "Missionary Passion",
        "profiles": [
            {"attire": "nude, missionary with vaginal penetration by one man, moaning expression"},
            {"attire": "nude, missionary with legs spread by one man, sweat on skin"},
            {"attire": "nude, missionary with intense expression by one man, flushed cheeks"},
            {"attire": "nude, missionary with dynamic angle by one man, realistic textures"},
            {"attire": "nude, missionary with wet skin by one man, dim lighting"},
            {"attire": "nude, missionary with legs apart on silk sheets by one man"},
            {"attire": "nude, missionary with sensual pose by one man, parted lips"},
            {"attire": "nude, missionary with realistic textures by one man"},
            {"attire": "nude, missionary with high detail by one man"},
            {"attire": "nude, missionary with steamy atmosphere by one man"}
        ]
    },
    "topless beach": {
        "label": "Topless Beach",
        "profiles": [
            {"attire": "topless with wet hair and sunglasses, ocean waves in background"},
            {"attire": "topless with sandy skin and subtle smile, bright sunlight"},
            {"attire": "topless with glistening skin and ocean spray, tan lines visible"},
            {"attire": "topless with sandy beach and natural pose, soft breeze"},
            {"attire": "topless with waves crashing and warm glow, realistic textures"},
            {"attire": "topless with sunny day and detailed pores, ocean horizon"},
            {"attire": "topless with wet skin and high detail, gentle waves"},
            {"attire": "topless with sandy toes and bright sunlight, natural pose"},
            {"attire": "topless with ocean spray and soft glow, realistic textures"},
            {"attire": "topless with dusk skyline and warm tones, high detail"}
        ]
    },
    "kitchen seduction": {
        "label": "Kitchen Seduction",
        "profiles": [
            {"attire": "nude with apron, pussy visible, leaning against counter"},
            {"attire": "nude with apron lifted, pussy glistening, seductive pose"},
            {"attire": "nude with apron, legs apart, pussy visible with warm lighting"},
            {"attire": "nude with apron, leaning over, pussy visible with sweat on skin"},
            {"attire": "nude with apron, sitting, pussy in focus, flushed cheeks"},
            {"attire": "nude with apron, standing, pussy visible with realistic textures"},
            {"attire": "nude with apron, legs spread, pussy visible with dim lighting"},
            {"attire": "nude with apron, leaning against counter, pussy visible with high detail"},
            {"attire": "nude with apron, seductive pose, pussy visible with warm tones"},
            {"attire": "nude with apron, wet skin, pussy visible with realistic lighting"}
        ]
    },
    "reverse cowgirl": {
        "label": "Reverse Cowgirl",
        "profiles": [
            {"attire": "nude, reverse cowgirl with vaginal penetration by one man, dynamic angle"},
            {"attire": "nude, reverse cowgirl with wet skin by one man, intense expression"},
            {"attire": "nude, reverse cowgirl with sweating by one man, flushed cheeks"},
            {"attire": "nude, reverse cowgirl with legs spread by one man, realistic textures"},
            {"attire": "nude, reverse cowgirl with seductive pose by one man, dim lighting"},
            {"attire": "nude, reverse cowgirl with realistic textures by one man, parted lips"},
            {"attire": "nude, reverse cowgirl with high detail by one man, steamy atmosphere"},
            {"attire": "nude, reverse cowgirl with moaning expression by one man"},
            {"attire": "nude, reverse cowgirl with sweat on skin by one man"},
            {"attire": "nude, reverse cowgirl with dynamic pose by one man"}
        ]
    },
    "bathtub solo": {
        "label": "Bathtub Solo",
        "profiles": [
            {"attire": "nude, sitting in bathtub with legs spread, fingering pussy, steamy air"},
            {"attire": "nude, lying in bathtub with legs apart, masturbating, candlelight"},
            {"attire": "nude, sitting in bubbly bathtub, fingering pussy, glistening skin"},
            {"attire": "nude, leaning back in bathtub with legs spread, intense expression"},
            {"attire": "nude, sitting in bathtub with wet skin, masturbating, flushed cheeks"},
            {"attire": "nude, lying in bathtub with steamy air, fingering pussy, realistic textures"},
            {"attire": "nude, sitting in bathtub with warm water, masturbating, dim lighting"},
            {"attire": "nude, leaning back in bathtub with bubbly water, fingering pussy, high detail"},
            {"attire": "nude, sitting in bathtub with reflective water, masturbating"},
            {"attire": "nude, lying in bathtub with warm glow, fingering pussy"}
        ]
    },
    "standing quickie": {
        "label": "Standing Quickie",
        "profiles": [
            {"attire": "nude, standing against wall with vaginal penetration by one man, urgent expression"},
            {"attire": "nude, standing with skirt lifted, vaginal sex by one man, sweat on skin"},
            {"attire": "nude, standing with panties aside, vaginal penetration by one man, flushed cheeks"},
            {"attire": "nude, standing in hallway with vaginal sex by one man, dim lighting"},
            {"attire": "nude, standing with dress lifted, vaginal sex by one man, realistic textures"},
            {"attire": "nude, standing with wet skin, vaginal penetration by one man, intense expression"},
            {"attire": "nude, standing with dynamic pose, vaginal sex by one man, parted lips"},
            {"attire": "nude, standing with skirt pulled up, vaginal sex by one man, high detail"},
            {"attire": "nude, standing with steamy atmosphere, vaginal penetration by one man"},
            {"attire": "nude, standing with warm lighting, vaginal sex by one man"}
        ]
    },
    "mirror selfie": {
        "label": "Mirror Selfie",
        "profiles": [
            {"attire": "nude, taking mirror selfie with legs apart, pussy visible, steamy background"},
            {"attire": "nude, mirror selfie with phone in hand, pussy glistening, wet tiles"},
            {"attire": "nude, mirror selfie with seductive pose, pussy visible, misty mirror"},
            {"attire": "nude, mirror selfie with wet skin, pussy visible, flushed cheeks"},
            {"attire": "nude, mirror selfie with legs spread, pussy in focus, realistic textures"},
            {"attire": "nude, mirror selfie with casual vibe, pussy visible, dim lighting"},
            {"attire": "nude, mirror selfie with dynamic angle, pussy visible, high detail"},
            {"attire": "nude, mirror selfie with warm lighting, pussy visible, seductive pose"},
            {"attire": "nude, mirror selfie with misty background, pussy visible, glistening skin"},
            {"attire": "nude, mirror selfie with realistic lighting, pussy visible, intense expression"}
        ]
    },
    "car backseat": {
        "label": "Car Backseat",
        "profiles": [
            {"attire": "nude, sitting with vaginal creampie from one man, cum dripping, foggy windows, soft glow"},
            {"attire": "nude, lying with vaginal sex by one man, foggy windows, dim interior"},
            {"attire": "nude, sitting with vaginal creampie, cum dripping, night lights, flushed cheeks"},
            {"attire": "nude, lying with vaginal penetration by one man, foggy windows, realistic textures"},
            {"attire": "nude, sitting with vaginal sex, foggy windows, soft glow, intense expression"},
            {"attire": "nude, lying with vaginal creampie from one man, cum dripping, night setting"},
            {"attire": "nude, sitting with vaginal penetration, foggy windows, high detail"},
            {"attire": "nude, lying with vaginal sex, foggy windows, warm tones, sweat on skin"},
            {"attire": "nude, sitting with vaginal creampie, cum dripping, dim light, parted lips"},
            {"attire": "nude, lying with vaginal penetration, foggy windows, realistic textures, steamy atmosphere"}
        ]
    },
    "balcony tease": {
        "label": "Balcony Tease",
        "profiles": [
            {"attire": "nude, standing with legs apart, pussy visible, city skyline"},
            {"attire": "nude, leaning on railing with pussy glistening, dusk lighting"},
            {"attire": "nude, sitting with legs spread, pussy visible, night lights"},
            {"attire": "nude, standing with gentle breeze, pussy visible, warm glow"},
            {"attire": "nude, leaning forward with pussy visible, city lights in background"},
            {"attire": "nude, standing with seductive pose, pussy visible, high detail"},
            {"attire": "nude, sitting with dusk skyline, pussy glistening, realistic textures"},
            {"attire": "nude, leaning on balcony with pussy visible, warm tones"},
            {"attire": "nude, standing with night lights, pussy visible, flushed cheeks"},
            {"attire": "nude, sitting with city skyline, pussy visible, dim lighting"}
        ]
    }
}

# Create a mapping of category keys to labels
CATEGORY_LABELS = {
    key: value["label"] for key, value in NSFW_PRESETS_STRUCTURE.items()
}

# Custom Node Class
class NSFWPromptPresets:
    @classmethod
    def INPUT_TYPES(cls):
        # Get the list of categories and their labels
        categories = list(NSFW_PRESETS_STRUCTURE.keys())
        labels = [CATEGORY_LABELS.get(category, category) for category in categories]

        return {
            "required": {
                "category": (labels, {"default": CATEGORY_LABELS.get(categories[0], categories[0])}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "prompt_index": ("INT", {"default": 1, "min": 0, "max": 10, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_prompt"
    CATEGORY = "custom"

    def get_prompt(self, category, seed=0, prompt_index=1):
        # Seed the random module with the provided seed for reproducible randomness
        random.seed(seed)

        # Map the selected label back to the category key
        category_key = None
        for key, label in CATEGORY_LABELS.items():
            if label == category:
                category_key = key
                break

        # Fallback to "none" if no match is found
        if category_key is None:
            category_key = "none"

        # Dynamically generate prompts for the selected category
        category_data = NSFW_PRESETS_STRUCTURE.get(category_key, {})
        profiles = category_data.get("profiles", [])
        room = category_key  # Use the category key directly, preserving spaces

        # Add random attributes to profiles
        randomized_profiles = []
        for profile in profiles:
            randomized_profiles.append({
                "hairstyle": random_hair_style(),
                "haircolour": random_hair_colour(),
                "hair_adjective": random_hair_adjective(),
                "age": random_age(),
                "attire": profile.get("attire", ""),
            })

        # Generate prompts
        prompts = generate_prompts(room, randomized_profiles)

        # Select prompt based on prompt_index
        if prompt_index == 0:
            # Random selection using the seeded random module
            prompt = random.choice(list(prompts.values()))
        else:
            # Specific selection by index, default to index 1 if invalid
            prompt = prompts.get(prompt_index, prompts.get(1, "Invalid prompt index."))

        return (prompt,)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS.update({
    "NSFWPromptPresets": NSFWPromptPresets
})

# At the end of the file, after NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = {
    "NSFWPromptPresets": "NSFW Prompt Presets"
}