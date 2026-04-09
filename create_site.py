from pathlib import Path

site_files = {
    "mkdocs.yml": """site_name: Mohan Mood | Computational Chemistry & AI
site_url: https://yourusername.github.io/
theme:
  name: material
  palette:
    - scheme: default
      primary: blue
      accent: light blue

nav:
  - Home: index.md
  - About: about.md
  - Research: research.md
  - Publications: publications.md
  - Talks: talks.md
  - Gallery: gallery.md
  - Contact: contact.md
""",
    "docs/index.md": """# Mohan Mood
### Computational Chemistry | AI/ML | Molecular Simulation

![Profile](assets/profile.jpg)

I am an Associate R&D Staff Scientist at Oak Ridge National Laboratory (ORNL), working at the intersection of computational chemistry, artificial intelligence, and high-performance computing.
""",
    "docs/about.md": """# About

Dr. Mohan Mood is an Associate R&D Staff Scientist in the Biosciences Division at Oak Ridge National Laboratory (ORNL), working within the Center for Molecular Biophysics.
""",
    "docs/research.md": """# Research

## AI/ML for Molecular Property Prediction
## Ionic Liquids & Deep Eutectic Solvents
## Biomass Pretreatment & Lignin Valorization
## Molecular Simulation & First-Principles Modeling
## NLP & LLMs for Chemistry
""",
    "docs/publications.md": """# Publications
## 2025
## 2024
## Cover Arts
## Patents
## Book Chapters
## Books
""",
    "docs/talks.md": """# Talks
- ACS Spring Meeting 2025 — Machine Learning for Designer Solvents
""",
    "docs/gallery.md": """# Gallery
## Hobbies
- Photography
- Fitness
- DIY Projects
""",
    "docs/contact.md": """# Contact

📧 Email: your-email@ornl.gov
🔗 LinkedIn: https://linkedin.com
🔗 Google Scholar: https://scholar.google.co.in/citations?user=MCEpPbIAAAAJ&hl=en
""",
}

for filepath, content in site_files.items():
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

print("Website starter files created successfully.")