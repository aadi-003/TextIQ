import json
class Database:
    def add_data(self,name,email,password):
        with open('db.json','r') as f:
            data = json.load(f)
            if email in data:
                return 0
            else:
                data[email] = [name,password]
                with open('db.json','w') as f:
                    json.dump(data,f)
                return 1
    def check_data(self,email,password):
        with open('db.json','r') as f:
            data = json.load(f)
            if email in data:
                if data[email][1] == password:
                    return 2
                else:
                    return 1
            else:
                return 0
