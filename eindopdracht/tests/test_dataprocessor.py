from loupe.data_processor import DataProcessor
import os

def test_read_json():
    # Arrange
    processor = DataProcessor()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_file_path = os.path.join(dir_path, '..', 'data', 'test_data.json')
    
    #Act
    result = processor.read_json(full_file_path)
    print(result)
    
    # Assert
    assert result == [{"test": "ok"}]
    assert result != ["sdfs"]