import json

# json 文件写入加载
class SaveDataTool():
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def save_data(self, data):
        with open(self.data_dir, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))    
    def load_data(self):
        with open(self.data_dir, 'r', encoding='utf-8') as f:
            return json.loads(f.read())        