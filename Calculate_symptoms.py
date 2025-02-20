


def calcualate_symptoms(symptom_list):
    
    Symptom_score={
    "Diabetes":0,
    "Dementia":0,
    "Depression":0,
    "Influenza":0,
    "Heart Disease":0,
    "Arthritis":0,
    "Pneumonia":0,
    "COPD":0,
    "Inner Infections":0,
    "Cerebrovascular Disease":0,
    "Chronic Kidney Disease":0

    }
    def add_to_symptom(symptom,x):
        Symptom_score[symptom]+=x

    for element in symptom_list:
        if element=="Fatigue":
            add_to_symptom("Diabetes",3)
            add_to_symptom("Depression",4)
            add_to_symptom("Influenza",2)
            add_to_symptom("Heart Disease",2)
            add_to_symptom("Pneumonia",1)
        
        elif element=="Frequent Urination":
            add_to_symptom("Diabetes",7)
            add_to_symptom("Chronic Kidney Disease",4)
        
        elif element=="Weight Loss":
            add_to_symptom("Diabetes",2)
        
        elif element=="Memory Problems":
            add_to_symptom("Dementia",9)
            add_to_symptom("Cerebrovascular Disease",3)
        
        elif element=="Mood Swings":
            add_to_symptom("Dementia",4)
            add_to_symptom("Depression",5)

        elif element=="Disturbed Sleep":
            add_to_symptom("Depression",5)
            add_to_symptom("Chronic Kidney Disease",3)
        
        elif element=="Low Motivation":
            add_to_symptom("Depression",5)
        
        elif element=="Coughing":
            add_to_symptom("Influenza",6)
            add_to_symptom("Heart Disease",1)
            add_to_symptom("Pneumonia",3)
            add_to_symptom("COPD",5)

        elif element=="Sore Throat":
            add_to_symptom("Influenza",5)

        elif element=="Fever":
            add_to_symptom("Influenza",2)
            add_to_symptom("Inner Infections",2)

        elif element=="Headaches":
            add_to_symptom("Dementia",1)
            add_to_symptom("Influenza",3)
            add_to_symptom("Cerebrovascular Disease",3)

        elif element=="Chest Pain":
            add_to_symptom("Heart Disease",5)
            add_to_symptom("Pneumonia",5)
        
        elif element=="Joint Stiffness":
             add_to_symptom("Arthritis",7)
             add_to_symptom("COPD",5)
             add_to_symptom("Inner Infections",3)

        elif element=="Muscle Pain":
            add_to_symptom("Influenza",2)
            add_to_symptom("Inner Infections",5)

        elif element=="Difficulty Breathing":
            add_to_symptom("Heart Disease",3)
            add_to_symptom("Pneumonia",5)
            add_to_symptom("COPD",5)
            add_to_symptom("Chronic Kidney Disease",3)
        
        elif element=="Bone Pain":
            add_to_symptom("Inner Infections",5)

        elif element=="Swelling":
            add_to_symptom("Arthritis",3)
            add_to_symptom("Inner Infections",3)
            add_to_symptom("Chronic Kidney Disease",3)

        elif element=="Sweating":
            add_to_symptom("Pneumonia",3)
            add_to_symptom("Inner Infections",2)

        elif element=="Nausea":
            add_to_symptom("Cerebrovascular Disease",5)
            add_to_symptom("Chronic Kidney Disease",5)

        elif element=="Trouble Speaking":
            add_to_symptom("Dementia",3)
            add_to_symptom("Cerebrovascular Disease",5)

        elif element=="Increased Hunger":
            add_to_symptom("Diabetes",3)
            add_to_symptom("Depression",1)
            add_to_symptom("Pneumonia",-2)
            add_to_symptom("Chronic Kidney Disease",-3)

        elif element=="Lack of Concentration":
            add_to_symptom("Dementia",4)
            add_to_symptom("Depression",4)
        
        elif element=="Unusual Heartbeat":
            add_to_symptom("Heart Disease",7)

        elif element=="Inflammed Skin":
            add_to_symptom("Arthritis",3)

        elif element=="Mucus":
            add_to_symptom("COPD",10)

    
    print(Symptom_score)
    
    return Symptom_score

def symptom_verdict(symptom_list):
    verdict=[]
    symptom_score=calcualate_symptoms(symptom_list)
    for key,value in symptom_score.items():
        if key!="COPD":
            if value>=10:
                verdict.append(key)
        elif key=="COPD":
            if value>=20:
                verdict.append(key)
    
    return verdict

def message_output(symptom_list):
    conditions=symptom_verdict(symptom_list)
    if conditions==[]:
        message="You have no conditions based on the symptoms"
        return message
    else:
        message="You may have the following conditions: "
        for condition in conditions:
            message+=condition+", "
        message=message[:-2]
        return message
    

        



          
