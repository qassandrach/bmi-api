from flask import jsonify
from abc import ABC, abstractmethod

class Bmi(ABC):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

   
    @abstractmethod
    def calculate(self):
        label = ""
        try:
            bmi = round((self.weight/pow((self.height/100),2)),2) 
            if bmi < 18.5:
                label = "underweight"
            elif 18.5 <= bmi <= 24.9:
                label = "healthy"
            elif bmi >= 25.0:
                label = "overweight"
        except ZeroDivisionError as e:
            return jsonify(error=str(e))

        return jsonify(bmi=bmi, label=label)


class BmiStatus(Bmi):
    
    def calculate(self):
        if self.weight is None and self.height is None:
            message = "Success"
            return jsonify(message=message)

        result = super().calculate()
        return result