# ComfyUI-PromptPresets
#### A Custom Node for ComfyUI to Dynamically Generate Prompts with Presets

This custom node for ComfyUI allows users to generate prompts dynamically using pre-defined presets. It supports both SFW _(Safe for Work)_ and NSFW (Not Safe for Work) categories, each containing at least 10 random/different prompts. The node simplifies the creative process by providing categorized prompts that can be seamlessly integrated into your workflows.

# Key Features
- Dynamic Prompt Generation: Automatically generates prompts based on pre-defined templates.
- Categorized Presets: Includes multiple categories such as Fantasy, Sci-Fi, Portraits, Landscapes, and more.
- SFW & NSFW Support: Offers both Safe-for-Work and Not-Safe-for-Work presets to cater to diverse use cases.
- Randomization: Each category contains at least 10 unique/random prompts to ensure variety.
- Customizable: Easily modify or add new presets to suit your needs.
- Seamless Integration: Works directly within ComfyUI as a custom node.

# Why Use This Custom Node?
Whether you're an artist, developer, hobbyist, or a sloth, generating creative prompts can sometimes be challenging. This custom node eliminates the need to brainstorm ideas manually by providing ready-to-use prompts that are dynamically generated. With support for both SFW and NSFW content, it caters to a wide range of creative workflows.

# Categories
The following categories are included in this custom node:
- SFW: Casual Safe-for-Work theme
- NSFW: Adult-themed prompts for mature audiences.
Each category contains at least 10 unique/random prompts.

# Installation
**Prerequisites**
- ComfyUI: Ensure you have ComfyUI installed and running.
- Python: Version 3.12 or higher.

**Steps**
1. Clone the repository into **/path/to/comfyui/custom_nodes**
    ```bash
    cd /path/to/comfyui/custom_nodes
    git clone https://github.com/MOVZX/ComfyUI-PromptPresets.git
    ```
2. Restart ComfyUI to load the custom node.

# Usage
1. Open ComfyUI and navigate to the custom nodes section.
2. Locate the **SFW Prompt Presets** _(or NSFW Prompt Presets)_ node in the interface.
3. Select a category _(e.g., Bedroom Elegance, Kitchen Grace, etc.)_ from the dropdown menu.
5. The node will dynamically generate a prompt based on the selected category and type.

Use the generated prompt in your workflow to create stunning images.

# Customisations
If you'd like to add or modify presets:
1. Edit the [sfw_prompts.py](https://github.com/MOVZX/ComfyUI-PromptPresets/blob/master/sfw_prompts.py) _(or [nsfw_prompts.py](https://github.com/MOVZX/ComfyUI-PromptPresets/blob/master/nsfw_prompts.py))_
2. Add or remove prompts as needed, ensuring they follow the same format:
    ```python
    SFW_PRESETS_STRUCTURE = {
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
    ```
3. Save the changes and restart ComfyUI to apply them.

# Preview
![image](https://github.com/user-attachments/assets/20e5c098-94be-49c6-9339-b4e09692e30a)

> [!NOTE]
> Let’s face it—sometimes, coming up with creative prompts can feel like a chore. I created this project because, honestly, I’m often too lazy to write detailed prompts myself. Whether you're stuck in a creative rut or just don’t feel like brainstorming, this custom node has got you covered.
>
> With ComfyUI-PromptPresets , you can skip the hassle of crafting prompts manually and let the node do the work for you. It provides ready-to-use, dynamically generated prompts across a variety of categories, ensuring you always have fresh ideas at your fingertips. Whether you’re working on SFW projects or exploring NSFW themes, this tool makes the process effortless and fun.

# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/MOVZX/ComfyUI-PromptPresets/blob/master/LICENSE) file for more details.
