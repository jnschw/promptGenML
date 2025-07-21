import yaml
import datetime
import os
from jinja2 import Template

template = """
Runtime : {{ date }} - {{ script }}
An anime girl named {{ name }} stands on {{ scene_desc }}.
She has {{ eyes }} eyes, {{ hair }} hair with {{ haircut }},
wearing a {{ dress }} and {{ jacket }}, holding a {{ instrument }}.
She carries {{ accessories }}.
{% if mood %}Mood: {{ mood }}.{% endif %}
{% if style %}Style: {{ style }}.{% endif %}
{% if camera %}Camera: {{ camera }}.{% endif %}
"""


def load_character(yaml_file):
    try:
        with open(yaml_file, 'r') as f:
            return yaml.safe_load(f)['character']
    except Exception as e:
        print(f"error loadding character file: {e}")
        return {}


def generate_prompt_jinja(character, scene_desc, template, **kwargs):
    data = {
        "name": character['name'],
        "instrument": character['instrument'],
        "hair": character['appearance']['hair']['color'],
        "haircut": character['appearance']['hair']['style'],
        "eyes": character['appearance']['eyes'],
        "dress": character['appearance']['clothing']['stage']['dress'],
        "jacket": character['appearance']['clothing']['stage']['jacket'],
        "accessories": ', '.join(character['accessories']),
        "posture": character['appearance'].get('posture', ''),
        "emotion": character.get('emotional_context', {}).get('inner_state', ''),
        "metaphor": character.get('emotional_context', {}).get('musical_metaphor', ''),
        "scene_desc": scene_desc,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "script": os.path.basename(__file__),
    }
    data.update(kwargs)
    return template.render(**data).strip()


# example call:
if __name__ == "__main__":
    character = "" # load_character("<replace with file>")
    scene = "a dimly lit stage with fog, late evening"
    cameras = [
        "full body shot, front view, moody and cinematic atmosphere, light ink accents",
        "full body shot, side view, moody and cinematic atmosphere, light ink accents",
        "close-up, dramatic lighting, focus on face and instrument"
    ]
    template=Template(template)
    print()
    for camera in cameras:
        prompt = generate_prompt_jinja(
            character,
            scene_desc=scene,
            template=template,
            style="hand-drawn manga with soft shadows",
            camera=camera,
            mood="melancholic but calm"
        )
        print(prompt)
        print()
