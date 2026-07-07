from pathlib import Path
text = '''Ernest Anyona
Full Stack Software Engineer

Education
Murang'a University of Technology

Skills
- JavaScript / React
- Python / Django
- REST APIs
- PostgreSQL
- Git & CI/CD

Experience
- Built responsive frontends and backend services
- Developed REST APIs and deployed modern web apps

Contact
Email: ernest@example.com
LinkedIn: linkedin.com/in/ernest-anyona
'''
output = Path('public/resume.pdf')
lines = text.splitlines()
content_lines = ['BT', '/F1 14 Tf', '72 750 Td']
for i, line in enumerate(lines):
    if i > 0:
        content_lines.append('0 -18 Td')
    safe = line.replace('(', '\\(').replace(')', '\\)')
    content_lines.append(f'({safe}) Tj')
content = '\n'.join(content_lines)
objects = []
objects.append(b'1 0 obj << /Type /Catalog /Pages 2 0 R >>\nendobj\n')
objects.append(b'2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n')
objects.append(b'3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>\nendobj\n')
stream = f'4 0 obj << /Length {len(content)} >>\nstream\n{content}\nendstream\nendobj\n'.encode('utf-8')
objects.append(stream)
objects.append(b'5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n')
pdf = b'%PDF-1.4\n'
positions = []
for obj in objects:
    positions.append(len(pdf))
    pdf += obj
xref = b'xref\n0 %d\n0000000000 65535 f \n' % (len(objects) + 1)
for pos in positions:
    xref += f'{pos:010d} 00000 n \n'.encode('ascii')
trailer = b'trailer << /Size %d /Root 1 0 R >>\nstartxref %d\n%%EOF\n' % (len(objects) + 1, len(pdf))
pdf += xref + trailer
output.write_bytes(pdf)
print('Created', output)