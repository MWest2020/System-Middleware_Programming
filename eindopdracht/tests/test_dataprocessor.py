from loupe.data_processor import DataProcessor

def test_read_json():
    # Arrange
    processor = DataProcessor()
    test_file_path = 'test_data.json'
    
    #Act
    result = processor.read_json(test_file_path)
    print(result)
    
    # Assert
    assert result == [{"test": "ok"}]
    assert result != ["sdfs"]