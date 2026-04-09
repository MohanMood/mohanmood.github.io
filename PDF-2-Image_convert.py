from pdf2image import convert_from_path
from pathlib import Path

pdf_path = Path("D:/Mohan_Website/docs/assets/cover-art/circular-bioeconomy-bpj-2026.pdf")
output_dir = Path("D:/Mohan_Website/docs/assets/cover-arts")
output_dir.mkdir(exist_ok=True)

poppler_path = r"C:\poppler\Library\bin"

pages = convert_from_path(
    pdf_path,
    dpi=300,
    poppler_path=poppler_path
)

pages[0].save(output_dir / "circular-bioeconomy-bpj-2026.png", "PNG")