from collections import deque

printer_queue = deque()
printer_queue.append("Tickets.pdf")
printer_queue.append("Marketingnotes.docx")
printer_queue.append("Proof.png")

while len(printer_queue) > 0:
  document = printer_queue.popleft()
  print(f"Printer {document}")

