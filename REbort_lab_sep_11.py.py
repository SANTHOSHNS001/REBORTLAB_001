from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch, mm
from reportlab.platypus.flowables import BalancedColumns
from reportlab.lib.styles import getSampleStyleSheet

# Define the filename for the PDF
pdf_filename = 'continuousColumn.pdf'

# Create a list to store the lines from the text file
lines = []

with open(r"enter your text note.txt", "r") as file:
    lines = file.readlines()

# Create a list to store the content of the PDF
story = []

# Create a style sheet for paragraphs
styles = getSampleStyleSheet()
style = styles["Normal"]

# Join all the lines into a single string without any spacing
text_content = "".join(lines)

# Create a paragraph with the entire text content
p = Paragraph(text_content, style)

# Create a BalancedColumns flowable with 2 columns (you can adjust the number of columns)
balanced_columns = BalancedColumns([p], nCols=4, innerPadding=1*mm)

story.append(balanced_columns)

# Create a PDF document
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Build the PDF document
doc.build(story)
