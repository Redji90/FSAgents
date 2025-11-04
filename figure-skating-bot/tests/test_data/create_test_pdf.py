from fpdf import FPDF

def create_test_protocol():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Добавляем тестовые данные
    test_data = """
    Competition: Test Grand Prix 2025
    Date: 04.11.2025
    Place: Moscow, Russia
    Category: Senior
    Discipline: Ladies
    
    Final Results
    
    1 ИВАНОВА Анна RUS 82.50 160.25 242.75
    2 ПЕТРОВА Мария RUS 80.15 155.30 235.45
    3 СМИРНОВА Елена RUS 78.90 150.20 229.10
    """
    
    pdf.multi_cell(0, 10, test_data)
    pdf.output("test_protocol.pdf")

if __name__ == "__main__":
    create_test_protocol()