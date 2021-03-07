from flask_restful import Resource
from flask import request
from Model import db, Person, History

class History(Resource):

    #Get Data from the app from the arduino
    
    def get():
        result = []
        header = request.headers["Auth"]

        if not header:
            return {"Messege" : "No api key!"}, 400
        else:
            user = Person.query.filter_by(api_key=header).first()
            
            if user:
                histories = History.query.filter_by(person_id=person.id).all()
                for history in histories:
                    result.append(History.serialize(history))


            return {"status": 'success', 'data': result}, 201


    #Post the data from the arduino
    
    def post(self):
        header = request
        json_data = request.get_json(force = True)

        if not header: 
            return {"Message": "No api key!"}, 400

        else: 
            user = Person.query.filter_by(api_key=header).first()

            if user:
                history = History(
                    date_time = json_data['date_time'],
                    person_id = person.id,
                    systolic_pressure = json_data['systolic_pressure'],
                    diastolic_pressure = json_data['diastolic_pressure'],
                )
                db.session.add(history)
                db.session.commit()

                result = History.serialize(history)
                return {"status": 'success', 'data': result}, 201
            
            else:
                return {"Messege" : "No user with that api key"}, 402
    


