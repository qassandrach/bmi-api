import json

def calculate_bmi(weight, height):
        result = {}

        bmi = round((weight/pow((height/100),2)),2)

        if bmi < 18.5:
            result["bmi"] = bmi
            result["label"] = "underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            result["bmi"] = bmi
            result["label"] = "healthy"
        elif bmi >= 25.0:
            result["bmi"] = bmi
            result["label"] = "overweight"
            
        return result

if __name__ == '__main__':
   bmi = calculate_bmi(50, 167)
   print(json.dumps(bmi))