# What is PromptGenML?

PromptGenML is a lightweight, human- and machine-readable format for the structured description of characters, scenes, and context elements for generative AI applications. It is designed to enable repeatable, comprehensible, and shareable prompts—particularly in areas such as image generation, comic creation, learning materials, or interactive stories.

---

## Basic Idea

PromptGenML is based on YAML ("Yet Another Markup Language") and is a semantic layer over simple prompts. It separates the description of a character or scene from the concrete request to the AI to generate an image or text.

[Learn more →](./VISION.md)

---

## Advantages

- **Reusability**: Figures and scenes can be versioned and combined
- **Consistency**: Recognizable characters across panels
- **Extensibility**: New fields and modules can be easily added
- **Readability**: Clear structure for humans and easy further processing with tools

---

## Language design: structure

```yaml
character:
  name: "Mary"
  role: "English teacher"
  version: "v1.0"
  setting:
    location: "Whitby, England, UK"
    time: "1982"
  appearance:
    hair: "blonde, tied back"
    eyes: "brown"
    clothing:
      hat: "straw hat"
      top: "beige linen blouse"
      bottom: "long skirt"
      footwear: "boots"
      accessories: ["notebook", "chalk"]
    color_palette: ["beige", "light brown", "white"]
  personality: "friendly, clear-speaking"
  tags: ["school", "northern England", "non-violent"]
  notes:
    - "Reference image: teacher_mary_v1.png"
```

---

## Example: Scene description

```yaml
scene:
  location: "classroom"
  time_of_day: "afternoon"
  weather: "sunny"
  mood: "focused but friendly"
  characters: ["Mary", "3 students"]
  action: "Mary points to a chalkboard with English words"
  camera: "medium shot"
  style: "comic, colored pencil"
```

---

## Example: Image Prompt Generation (from YAML)

A tool could automatically generate an image prompt from this data, such as:

> "A schoolteacher in 1982 stands in a sunny classroom, pointing at a chalkboard with English words. She wears a straw hat and a beige linen blouse, holding a notebook. Style: colored pencil, comic, medium shot."
 
---

## Use Cases

- **Prompt Generation**: AI-supported prompt builders that generate templates for image or text systems from YAML data
- **Storytelling**: Interactive narrative structures with semantically defined roles and locations
- **Comics**: Characters and scenes can be presented reproducibly and stylistically coherently
- **Learning Materials**: Teaching characters in thematic scenes (math, language, history)
  
---

## Responsibility

When using generative AI in conjunction with PromptGenML, copyrights and personal rights must be observed. PromptGenML supports this by:

- **Documenting the original idea** (e.g., using `notes:` and `version:`)
- **Separating description and generation**: The YAML file is declarative, not executable
- **Optional license fields** (e.g., `license: CC-BY-SA`)
- **Transparent traceability**: Who generated what, when, and how?

We recommend:
- Not using promptML for content that imitates existing brands, real people, or protected designs
- Developing characters and scenes independently – ideally with stylistic aids such as color palettes, archetypes, or prompt feedback systems
  
---

## Outlook

PromptGenML is deliberately open and modular. Possible options include:

- **Templates for roles, genres, or styles**
- **Rating grids for coherence (e.g., clothing, color codes)**
- **Versioning systems for creative development processes**
- **Bridges to tools such as Markdown, Pandoc, LaTeX, and web platforms**

---

## Conclusion

PromptGenML isn't a new data format—it's a new perspective on creative prompting: structured, modular, transparent, and sustainable. It helps humans and machines **understand complexity**, **structure creativity**, and **collaboratively design reproducible content**.

PromptGenML not only strengthens creative self-work, but can also serve as a **bridging technology** – between free prompting and structured authoring systems.

PromptGenML itself is not intended as a commercial product, but rather as a tool for structured work with AI-generated content. 
