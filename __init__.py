"""
Prompt Presets for ComfyUI
A collection of SFW/NSFW prompt presets generation nodes for ComfyUI
"""

__version__ = "1.0.0"
__author__ = "MOVZX"
__description__ = "Simple SFW/NSFW prompt generation nodes for ComfyUI with multiple themes and styles"

from .sfw_prompts import SFWPromptPresets
from .nsfw_prompts import NSFWPromptPresets

# Node mappings
NODE_CLASS_MAPPINGS = {
    "SFWPromptPresets": SFWPromptPresets,
    "NSFWPromptPresets": NSFWPromptPresets
}

# Display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "SFWPromptPresets": "SFW Prompt Presets",
    "NSFWPromptPresets": "NSFW Prompt Presets"
}