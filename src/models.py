from db_control import DBControl

class DMTarget:
    table_name="dm_targets"
    def __init__(self,id,userid,json):
        self.id=id
        self.userid=userid
        self.json=json
    
    @classmethod
    def get_by_userid(cls,userid):
        data = DBControl().select(cls.table_name,params={"userid":userid})
        if len(data)>0:
            return cls(id=data[0][0],userid=data[0][1],json=data[0][1])
        else:
            return None
    
    @classmethod
    def get(cls, id):
        data = DBControl().select(cls.table_name,params={"id":id})
        if len(data)>0:
            return cls(id=data[0][0],userid=data[0][1],json=data[0][1])
        else:
            return None
    
    def update_json(self, data):
        self.json = data
        DBControl().update(self.table_name,["json"],self.json,{"id":self.id})
    
    @classmethod
    def create(cls, userid, data):
        DBControl().insert(cls.table_name,{"userid":userid,"json":data})
        id = DBControl().select(cls.table_name,targets=["id"], params={"userid":userid})[0][0]
        return cls(id=id,userid=userid,json=data)