from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(30)


def main():
    name = input("name on shirt: ")
    label(name)
    
def label(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 34)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 225, f'{name} took CS50', align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

