import random
import comfy

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
                f"{profile['haircolour']} hair, stunningly beautiful, wearing "
                f"{profile['attire']}, dynamic pose, {room}, high resolution, "
                f"best quality, real human aesthetic, sfw"
            )
            prompts[index] = prompt
    return prompts

# Define the structure of SFW presets
SFW_PRESETS_STRUCTURE = {
    "none": {"label": "Tidak Ada", "profiles": []},
    "bedroom elegance": {
        "label": "Bedroom Elegance",
        "profiles": [
            {"attire": "silk emerald-green blouse and high-waisted black trousers"},
            {"attire": "cozy cream sweater and navy-blue jeans"},
            {"attire": "flowing lavender dress with lace trim"},
            {"attire": "chic white blouse and tailored gray skirt"},
            {"attire": "knitted mustard sweater and dark denim shorts"},
            {"attire": "fitted burgundy blazer and black slacks"},
            {"attire": "casual striped T-shirt and beige capris"},
            {"attire": "pastel pink cardigan and floral-print skirt"},
            {"attire": "satin navy-blue jumpsuit"},
            {"attire": "vintage-style polka-dot dress"},
        ],
    },
    "kitchen grace": {
        "label": "Kitchen Grace",
        "profiles": [
            {"attire": "crisp white chef's apron over a red blouse and denim jeans"},
            {"attire": "casual olive-green hoodie and black leggings"},
            {"attire": "classic trench coat over a knee-length navy dress"},
            {"attire": "sleeveless peach blouse and linen pants"},
            {"attire": "stylish coral wrap dress"},
            {"attire": "bohemian-patterned maxi dress"},
            {"attire": "relaxed-fit plaid shirt and cargo pants"},
            {"attire": "fitted leather jacket and dark jeans"},
            {"attire": "bold geometric-print dress"},
            {"attire": "sleek black turtleneck and charcoal-gray trousers"},
        ],
    },
    "living room serenity": {
        "label": "Living Room Serenity",
        "profiles": [
            {"attire": "pastel yellow sundress"},
            {"attire": "loose-fitting mint-green top and white shorts"},
            {"attire": "fitted navy-blue jumpsuit"},
            {"attire": "floral-print dress"},
            {"attire": "casual denim jacket and black leggings"},
            {"attire": "sporty tank top and yoga pants"},
            {"attire": "flowy teal blouse and khaki pants"},
            {"attire": "cozy oversized sweater and jeans"},
            {"attire": "chic black midi dress"},
            {"attire": "comfortable loungewear set"},
        ],
    },
    "gaming room vibe": {
        "label": "Gaming Room Vibe",
        "profiles": [
            {"attire": "graphic tee and ripped jeans"},
            {"attire": "sporty hoodie and joggers"},
            {"attire": "sleek black jumpsuit"},
            {"attire": "casual striped shirt and denim shorts"},
            {"attire": "retro-style bomber jacket and black leggings"},
            {"attire": "fitted athletic top and sweatpants"},
            {"attire": "cozy knit sweater and leggings"},
            {"attire": "casual flannel shirt and jeans"},
            {"attire": "trendy crop top and high-waisted pants"},
            {"attire": "stylish leather jacket and dark jeans"},
        ],
    },
    "streaming room glow": {
        "label": "Streaming Room Glow",
        "profiles": [
            {"attire": "casual hoodie and joggers"},
            {"attire": "chic blouse and tailored pants"},
            {"attire": "stylish dress and heels"},
            {"attire": "casual sweater and jeans"},
            {"attire": "cozy loungewear set"},
            {"attire": "sporty tank top and shorts"},
            {"attire": "casual tunic and leggings"},
            {"attire": "relaxed-fit sweater and jeans"},
            {"attire": "trendy outfit"},
            {"attire": "professional blazer and skirt"},
        ],
    },
}

# Create a mapping of category keys to labels
CATEGORY_LABELS = {
    key: value["label"] for key, value in SFW_PRESETS_STRUCTURE.items()
}

# Custom Node Class
class PromptPresets:
    @classmethod
    def INPUT_TYPES(cls):
        # Get the list of categories and their labels
        categories = list(SFW_PRESETS_STRUCTURE.keys())
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
        category_data = SFW_PRESETS_STRUCTURE.get(category_key, {})
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

# Register the Node
NODE_CLASS_MAPPINGS = {
    "PromptPresets": PromptPresets,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptPresets": "Prompt Presets",
}