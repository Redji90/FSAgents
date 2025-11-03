# Этот файл отвечает за парсинг извлеченных данных и подготовку их для анализа.

def parse_extracted_data(extracted_data):
    """
    Функция для парсинга извлеченных данных.
    
    :param extracted_data: Данные, извлеченные из PDF.
    :return: Словарь с подготовленными данными для анализа.
    """
    parsed_data = {}
    
    # Логика парсинга данных
    for entry in extracted_data:
        # Пример обработки данных
        event = entry.get('event')
        score = entry.get('score')
        
        if event not in parsed_data:
            parsed_data[event] = []
        parsed_data[event].append(score)
    
    return parsed_data