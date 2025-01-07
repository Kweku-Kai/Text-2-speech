import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Connect to your MySQL DB
with mysql.connector.connect(
    host="localhost",
    user="root",
    password="macquena",
    database="pintoshop"
) as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Get distinct is_staff values
        cur.execute("SELECT DISTINCT is_staff FROM core_user")
        is_staff_values = [row[0] for row in cur.fetchall()]

    # Create a PDF document
    doc = SimpleDocTemplate("my_users_list.pdf", pagesize=letter)

    # Get the sample style sheet
    styles = getSampleStyleSheet()

    # Add the tables to the elements to be added to the document
    elements = []
    for is_staff in is_staff_values:
        with conn.cursor() as cur:
            # Get users with the current is_staff value
            cur.execute("SELECT username,first_name,last_name FROM core_user WHERE is_staff = %s", (is_staff,))
            data = cur.fetchall()

        # Add column headings
        data.insert(0, ('Username', 'First Name', 'Last Name'))

        # Create a Table object
        table = Table(data)

        # Create a TableStyle object and add it to the table
        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ])
        table.setStyle(style)

        # Add a title, the table, and a spacer to the elements
        elements.append(Paragraph(f'is_staff = {is_staff}', styles['Title']))
        elements.append(table)
        elements.append(Spacer(1, 0.5*inch))  # Add a spacer of 0.5 inch height

    # Build the document
    doc.build(elements)