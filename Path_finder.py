from operator import indexOf
from z3 import *

# Let's declare all the drugs in our interaction checker
Drug = Datatype('Drug')
Drug.declare('Metformin')
Drug.declare('Paroxetine')
Drug.declare('Nateglinide')
Drug.declare('Citalopram')
Drug.declare('Donepezil')
Drug.declare('Memantine')
Drug.declare('Insulin_human')
Drug.declare('Acarbose')
Drug.declare('Miglitol')
Drug.declare('Aducanumab')
Drug.declare('Lecanemab')
Drug.declare('Brexpiprazole')
Drug.declare('Fluoxetine')
Drug.declare('Fluvoxamine')
Drug.declare('Escitalopram')
Drug.declare('Oseltamivir')
Drug.declare('Zanamivir')
Drug.declare('Peramivir')
Drug.declare('Baloxavir_marboxil')
Drug.declare('Atorvastatin')
Drug.declare('Niacin')
Drug.declare('Bumetanide')
Drug.declare('Canagliflozin')
Drug.declare('Nitroglycerin')
Drug.declare('Capsaicin')
Drug.declare('Choline_salicylate')
Drug.declare('Glucosamine')
Drug.declare('Levomenthol')
Drug.declare('Methocarbamol')
Drug.declare('Azithromycin')
Drug.declare('Clarithromycin')
Drug.declare('Doxycycline')
Drug.declare('Ramipril')
Drug.declare('Enalapril')
Drug.declare('Lisinopril')
Drug.declare('Fluticasone')
Drug.declare('Aclidinium')
Drug.declare('Arformoterol')
Drug.declare('Mepolizumab')
Drug.declare('Benralizumab')
Drug.declare('Cilastatin')
Drug.declare('Ceftriaxone')
Drug.declare('Ceftazidime')
Drug.declare('Cefotaxime')
Drug.declare('Aniracetam')
Drug.declare('Choline_alfoscerate')
Drug.declare('Cytidine')
Drug.declare('Dihydroergocristine')
Drug.declare('Galantamine')
Drug.declare('Hydroflumethiazide')
Drug.declare('Aliskiren')
Drug.declare('Cilazapril')
Drug.declare('Levamlodipine')
Drug.declare('Prazosin')
Drug = Drug.create()      

# Let's declare all the conditions in our Interaction checker
Condition = Datatype('Condition')
Condition.declare('Diabetes')
Condition.declare('Dementia')
Condition.declare('Depression')
Condition.declare('Influenza')
Condition.declare('Heart_Disease')
Condition.declare('Arthritis')
Condition.declare('Pneumonia')
Condition.declare('Chronic_Kidney_Disease')
Condition.declare('Pulmonary')
Condition.declare('Inner_Infections')
Condition.declare('Cerebrovascular')
Condition.declare('Hypertension')

Condition = Condition.create()

def hasDisease(x):
    return Or(x == Condition.Diabetes,
              x == Condition.Dementia,
              x == Condition.Depression,
              x == Condition.Influenza,
              x == Condition.Heart_Disease,
              x == Condition.Arthritis,
              x == Condition.Pneumonia,
              x == Condition.Chronic_Kidney_Disease,
              x == Condition.Pulmonary,
              x == Condition.Inner_Infections,
              x == Condition.Cerebrovascular,
              x == Condition.Hypertension)

def confl(x, y):

    return If(Or(And(x == Drug.Metformin, y == Drug.Brexpiprazole),
                    And(x == Drug.Metformin, y == Drug.Oseltamivir),
                    And(x == Drug.Metformin, y == Drug.Zanamivir),
                    And(x == Drug.Metformin, y == Drug.Doxycycline),
                    And(x == Drug.Metformin, y == Drug.Fluticasone),
                    And(x == Drug.Metformin, y == Drug.Arformoterol),
                    And(x == Drug.Metformin, y == Drug.Aclidinium),
                    And(x == Drug.Metformin, y == Drug.Ceftriaxone),
                    And(x == Drug.Metformin, y == Drug.Ceftazidime),
                    And(x == Drug.Metformin, y == Drug.Atorvastatin),
                    And(x == Drug.Metformin, y == Drug.Niacin),
                    And(x == Drug.Metformin, y == Drug.Bumetanide),
                    And(x == Drug.Aducanumab, y == Drug.Mepolizumab),
                    And(x == Drug.Aducanumab, y == Drug.Benralizumab),
                    And(x == Drug.Nateglinide, y == Drug.Memantine),
                    And(x == Drug.Nateglinide, y == Drug.Atorvastatin),
                    And(x == Drug.Nateglinide, y == Drug.Lisinopril),
                    And(x == Drug.Nateglinide, y == Drug.Aclidinium),
                    And(x == Drug.Nateglinide, y == Drug.Ceftriaxone),
                    And(x == Drug.Nateglinide, y == Drug.Ceftazidime),
                    And(x == Drug.Nateglinide, y == Drug.Arformoterol),
                    And(x == Drug.Nateglinide, y == Drug.Cefotaxime),
                    And(x == Drug.Nateglinide, y == Drug.Galantamine),
                    And(x == Drug.Lecanemab, y == Drug.Mepolizumab),
                    And(x == Drug.Lecanemab, y == Drug.Benralizumab),
                    And(x == Drug.Donepezil, y == Drug.Nateglinide),
                    And(x == Drug.Donepezil, y == Drug.Levomenthol),
                    And(x == Drug.Donepezil, y == Drug.Arformoterol),
                    And(x == Drug.Donepezil, y == Drug.Fluticasone),
                    And(x == Drug.Donepezil, y == Drug.Galantamine),
                    And(x == Drug.Memantine, y == Drug.Fluvoxamine),
                    And(x == Drug.Memantine, y == Drug.Canagliflozin),
                    And(x == Drug.Memantine, y == Drug.Doxycycline),
                    And(x == Drug.Memantine, y == Drug.Arformoterol),
                    And(x == Drug.Memantine, y == Drug.Fluticasone),
                    And(x == Drug.Memantine, y == Drug.Cefotaxime),
                    And(x == Drug.Memantine, y == Drug.Ceftriaxone),
                    And(x == Drug.Memantine, y == Drug.Ceftazidime),
                    And(x == Drug.Brexpiprazole, y == Drug.Nitroglycerin),
                    And(x == Drug.Brexpiprazole, y == Drug.Lisinopril),
                    And(x == Drug.Brexpiprazole, y == Drug.Ramipril),
                    And(x == Drug.Brexpiprazole, y == Drug.Enalapril),
                    And(x == Drug.Brexpiprazole, y == Drug.Galantamine),
                    And(x == Drug.Fluoxetine, y == Drug.Aclidinium),
                    And(x == Drug.Fluvoxamine, y == Drug.Oseltamivir),
                    And(x == Drug.Fluvoxamine, y == Drug.Zanamivir),
                    And(x == Drug.Fluvoxamine, y == Drug.Choline_salicylate),
                    And(x == Drug.Fluvoxamine, y == Drug.Doxycycline),
                    And(x == Drug.Fluvoxamine, y == Drug.Aclidinium),
                    And(x == Drug.Fluvoxamine, y == Drug.Lisinopril),
                    And(x == Drug.Fluvoxamine, y == Drug.Ceftazidime),
                    And(x == Drug.Fluvoxamine, y == Drug.Cefotaxime),
                    And(x == Drug.Fluvoxamine, y == Drug.Ceftriaxone),
                    And(x == Drug.Citalopram, y == Drug.Dihydroergocristine),
                    And(x == Drug.Oseltamivir, y == Drug.Canagliflozin),
                    And(x == Drug.Oseltamivir, y == Drug.Doxycycline),
                    And(x == Drug.Oseltamivir, y == Drug.Choline_salicylate),
                    And(x == Drug.Oseltamivir, y == Drug.Lisinopril),
                    And(x == Drug.Oseltamivir, y == Drug.Aclidinium),
                    And(x == Drug.Oseltamivir, y == Drug.Arformoterol),
                    And(x == Drug.Oseltamivir, y == Drug.Ceftazidime),
                    And(x == Drug.Zanamivir, y == Drug.Ceftazidime),
                    And(x == Drug.Zanamivir, y == Drug.Cefotaxime),
                    And(x == Drug.Zanamivir, y == Drug.Canagliflozin),
                    And(x == Drug.Zanamivir, y == Drug.Choline_salicylate),
                    And(x == Drug.Zanamivir, y == Drug.Doxycycline),
                    And(x == Drug.Zanamivir, y == Drug.Lisinopril),
                    And(x == Drug.Zanamivir, y == Drug.Aclidinium),
                    And(x == Drug.Zanamivir, y == Drug.Arformoterol),
                    And(x == Drug.Zanamivir, y == Drug.Ceftriaxone),
                    And(x == Drug.Bumetanide, y == Drug.Ramipril),
                    And(x == Drug.Bumetanide, y == Drug.Choline_salicylate),
                    And(x == Drug.Canagliflozin, y == Drug.Levomenthol),
                    And(x == Drug.Canagliflozin, y == Drug.Doxycycline),
                    And(x == Drug.Canagliflozin, y == Drug.Aclidinium),
                    And(x == Drug.Canagliflozin, y == Drug.Ceftriaxone),
                    And(x == Drug.Canagliflozin, y == Drug.Arformoterol),
                    And(x == Drug.Canagliflozin, y == Drug.Ceftazidime),
                    And(x == Drug.Canagliflozin, y == Drug.Cefotaxime),
                    And(x == Drug.Nitroglycerin, y == Drug.Ramipril),
                    And(x == Drug.Nitroglycerin, y == Drug.Enalapril),
                    And(x == Drug.Nitroglycerin, y == Drug.Lisinopril),
                    And(x == Drug.Nitroglycerin, y == Drug.Arformoterol),
                    And(x == Drug.Capsaicin, y == Drug.Fluticasone),
                    And(x == Drug.Choline_salicylate, y == Drug.Doxycycline),
                    And(x == Drug.Choline_salicylate, y == Drug.Aclidinium),
                    And(x == Drug.Choline_salicylate, y == Drug.Arformoterol),
                    And(x == Drug.Choline_salicylate, y == Drug.Ceftriaxone),
                    And(x == Drug.Choline_salicylate, y == Drug.Ceftazidime),
                    And(x == Drug.Choline_salicylate, y == Drug.Cefotaxime),
                    And(x == Drug.Levomenthol, y == Drug.Azithromycin),
                    And(x == Drug.Levomenthol, y == Drug.Ramipril),
                    And(x == Drug.Levomenthol, y == Drug.Enalapril),
                    And(x == Drug.Levomenthol, y == Drug.Lisinopril),
                    And(x == Drug.Levomenthol, y == Drug.Arformoterol),
                    And(x == Drug.Levomenthol, y == Drug.Galantamine),
                    And(x == Drug.Azithromycin, y == Drug.Arformoterol),
                    And(x == Drug.Azithromycin, y == Drug.Galantamine),
                    And(x == Drug.Clarithromycin, y == Drug.Enalapril),
                    And(x == Drug.Clarithromycin, y == Drug.Arformoterol),
                    And(x == Drug.Doxycycline, y == Drug.Cefotaxime),
                    And(x == Drug.Doxycycline, y == Drug.Arformoterol),
                    And(x == Drug.Doxycycline, y == Drug.Aclidinium),
                    And(x == Drug.Doxycycline, y == Drug.Ceftriaxone),
                    And(x == Drug.Doxycycline, y == Drug.Ceftazidime),
                    And(x == Drug.Ramipril, y == Drug.Arformoterol),
                    And(x == Drug.Ramipril, y == Drug.Dihydroergocristine),
                    And(x == Drug.Enalapril, y == Drug.Fluticasone),
                    And(x == Drug.Enalapril, y == Drug.Arformoterol),
                    And(x == Drug.Enalapril, y == Drug.Dihydroergocristine),
                    And(x == Drug.Lisinopril, y == Drug.Aclidinium),
                    And(x == Drug.Lisinopril, y == Drug.Arformoterol),
                    And(x == Drug.Lisinopril, y == Drug.Ceftriaxone),
                    And(x == Drug.Lisinopril, y == Drug.Ceftazidime),
                    And(x == Drug.Lisinopril, y == Drug.Cefotaxime),
                    And(x == Drug.Lisinopril, y == Drug.Dihydroergocristine),
                    And(x == Drug.Lisinopril, y == Drug.Galantamine),
                    And(x == Drug.Fluticasone, y == Drug.Galantamine),
                    And(x == Drug.Aclidinium, y == Drug.Cefotaxime),
                    And(x == Drug.Aclidinium, y == Drug.Ceftazidime),
                    And(x == Drug.Aclidinium, y == Drug.Ceftriaxone),
                    And(x == Drug.Arformoterol, y == Drug.Ceftriaxone),
                    And(x == Drug.Arformoterol, y == Drug.Ceftazidime),
                    And(x == Drug.Arformoterol, y == Drug.Galantamine),
                    And(x == Drug.Arformoterol, y == Drug.Cefotaxime),
                    And(x == Drug.Hydroflumethiazide, y == Drug.Brexpiprazole),
                    And(x == Drug.Aliskiren, y == Drug.Bumetanide),
                    And(x == Drug.Aliskiren, y == Drug.Nitroglycerin),
                    And(x == Drug.Aliskiren, y == Drug.Canagliflozin),
                    And(x == Drug.Aliskiren, y == Drug.Levomenthol),
                    And(x == Drug.Cilazapril, y == Drug.Brexpiprazole),
                    And(x == Drug.Cilazapril, y == Drug.Bumetanide),
                    And(x == Drug.Prazosin, y == Drug.Bumetanide),
                    And(x == Drug.Levamlodipine, y == Drug.Atorvastatin),
                    And(x == Drug.Levamlodipine, y == Drug.Bumetanide),
                    And(x == Drug.Cilazapril, y == Drug.Nitroglycerin),
                    And(x == Drug.Cilazapril, y == Drug.Arformoterol),
                    And(x == Drug.Prazosin, y == Drug.Canagliflozin),
                    And(x == Drug.Cilazapril, y == Drug.Levomenthol),
                    And(x == Drug.Levamlodipine, y == Drug.Ramipril),
                    And(x == Drug.Levamlodipine, y == Drug.Enalapril),
                    And(x == Drug.Levamlodipine, y == Drug.Lisinopril),
                    And(x == Drug.Levamlodipine, y == Drug.Arformoterol),
                    And(x == Drug.Prazosin, y == Drug.Dihydroergocristine),
                    And(x == Drug.Cilazapril, y == Drug.Dihydroergocristine),
                    And(x == Drug.Levamlodipine, y == Drug.Dihydroergocristine),
                    ),
                 50,
                If(Or(And(x == Drug.Metformin, y == Drug.Paroxetine),
                 And(x == Drug.Metformin, y == Drug.Citalopram),
                 And(x == Drug.Metformin, y == Drug.Fluoxetine),
                 And(x == Drug.Metformin, y == Drug.Fluvoxamine),
                 And(x == Drug.Metformin, y == Drug.Escitalopram),
                 And(x == Drug.Metformin, y == Drug.Ramipril),
                 And(x == Drug.Metformin, y == Drug.Enalapril),
                 And(x == Drug.Metformin, y == Drug.Lisinopril),
                 And(x == Drug.Metformin, y == Drug.Choline_salicylate),
                 And(x == Drug.Insulin_human, y == Drug.Paroxetine),
                 And(x == Drug.Insulin_human, y == Drug.Fluvoxamine),
                 And(x == Drug.Insulin_human, y == Drug.Fluoxetine),
                 And(x == Drug.Insulin_human, y == Drug.Brexpiprazole),
                 And(x == Drug.Insulin_human, y == Drug.Citalopram),
                 And(x == Drug.Insulin_human, y == Drug.Bumetanide),
                 And(x == Drug.Insulin_human, y == Drug.Escitalopram),
                 And(x == Drug.Insulin_human, y == Drug.Niacin),
                 And(x == Drug.Insulin_human, y == Drug.Canagliflozin),
                 And(x == Drug.Insulin_human, y == Drug.Choline_salicylate),
                 And(x == Drug.Insulin_human, y == Drug.Ramipril),
                 And(x == Drug.Insulin_human, y == Drug.Enalapril),
                 And(x == Drug.Insulin_human, y == Drug.Lisinopril),
                 And(x == Drug.Insulin_human, y == Drug.Fluticasone),
                 And(x == Drug.Acarbose, y == Drug.Brexpiprazole),
                 And(x == Drug.Acarbose, y == Drug.Fluoxetine),
                 And(x == Drug.Acarbose, y == Drug.Fluvoxamine),
                 And(x == Drug.Acarbose, y == Drug.Paroxetine),
                 And(x == Drug.Acarbose, y == Drug.Citalopram),
                 And(x == Drug.Acarbose, y == Drug.Escitalopram),
                 And(x == Drug.Acarbose, y == Drug.Niacin),
                 And(x == Drug.Acarbose, y == Drug.Bumetanide),
                 And(x == Drug.Acarbose, y == Drug.Canagliflozin),
                 And(x == Drug.Acarbose, y == Drug.Choline_salicylate),
                 And(x == Drug.Acarbose, y == Drug.Fluticasone),
                 And(x == Drug.Nateglinide, y == Drug.Brexpiprazole),
                 And(x == Drug.Nateglinide, y == Drug.Fluoxetine),
                 And(x == Drug.Nateglinide, y == Drug.Fluvoxamine),
                 And(x == Drug.Nateglinide, y == Drug.Escitalopram),
                 And(x == Drug.Nateglinide, y == Drug.Citalopram),
                 And(x == Drug.Nateglinide, y == Drug.Niacin),
                 And(x == Drug.Nateglinide, y == Drug.Bumetanide),
                 And(x == Drug.Nateglinide, y == Drug.Choline_salicylate),
                 And(x == Drug.Nateglinide, y == Drug.Fluticasone),
                 And(x == Drug.Miglitol, y == Drug.Brexpiprazole),
                 And(x == Drug.Miglitol, y == Drug.Fluoxetine),
                 And(x == Drug.Miglitol, y == Drug.Fluvoxamine),
                 And(x == Drug.Miglitol, y == Drug.Escitalopram),
                 And(x == Drug.Miglitol, y == Drug.Paroxetine),
                 And(x == Drug.Miglitol, y == Drug.Citalopram),
                 And(x == Drug.Miglitol, y == Drug.Niacin),
                 And(x == Drug.Miglitol, y == Drug.Bumetanide),
                 And(x == Drug.Miglitol, y == Drug.Canagliflozin),
                 And(x == Drug.Miglitol, y == Drug.Choline_salicylate),
                 And(x == Drug.Miglitol, y == Drug.Fluticasone),
                 And(x == Drug.Donepezil, y == Drug.Citalopram),
                 And(x == Drug.Donepezil, y == Drug.Paroxetine),
                 And(x == Drug.Donepezil, y == Drug.Fluvoxamine),
                 And(x == Drug.Donepezil, y == Drug.Methocarbamol),
                 And(x == Drug.Donepezil, y == Drug.Niacin),
                 And(x == Drug.Donepezil, y == Drug.Escitalopram),
                 And(x == Drug.Donepezil, y == Drug.Aclidinium),
                 And(x == Drug.Donepezil, y == Drug.Fluoxetine),
                 And(x == Drug.Memantine, y == Drug.Citalopram),
                 And(x == Drug.Memantine, y == Drug.Paroxetine),
                 And(x == Drug.Memantine, y == Drug.Bumetanide),
                 And(x == Drug.Memantine, y == Drug.Escitalopram),
                 And(x == Drug.Memantine, y == Drug.Choline_salicylate),
                 And(x == Drug.Memantine, y == Drug.Aclidinium),
                 And(x == Drug.Brexpiprazole, y == Drug.Fluvoxamine),
                 And(x == Drug.Brexpiprazole, y == Drug.Paroxetine),
                 And(x == Drug.Brexpiprazole, y == Drug.Citalopram),
                 And(x == Drug.Brexpiprazole, y == Drug.Escitalopram),
                 And(x == Drug.Brexpiprazole, y == Drug.Fluoxetine),
                 And(x == Drug.Brexpiprazole, y == Drug.Niacin),
                 And(x == Drug.Brexpiprazole, y == Drug.Canagliflozin),
                 And(x == Drug.Brexpiprazole, y == Drug.Methocarbamol),
                 And(x == Drug.Brexpiprazole, y == Drug.Arformoterol),
                 And(x == Drug.Fluoxetine, y == Drug.Niacin),
                 And(x == Drug.Fluoxetine, y == Drug.Canagliflozin),
                 And(x == Drug.Fluoxetine, y == Drug.Capsaicin),
                 And(x == Drug.Fluoxetine, y == Drug.Methocarbamol),
                 And(x == Drug.Fluoxetine, y == Drug.Arformoterol),
                 And(x == Drug.Fluoxetine, y == Drug.Clarithromycin),
                 And(x == Drug.Fluoxetine, y == Drug.Galantamine),
                 And(x == Drug.Paroxetine, y == Drug.Atorvastatin),
                 And(x == Drug.Paroxetine, y == Drug.Niacin),
                 And(x == Drug.Paroxetine, y == Drug.Canagliflozin),
                 And(x == Drug.Paroxetine, y == Drug.Capsaicin),
                 And(x == Drug.Paroxetine, y == Drug.Methocarbamol),
                 And(x == Drug.Fluvoxamine, y == Drug.Niacin),
                 And(x == Drug.Fluvoxamine, y == Drug.Bumetanide),
                 And(x == Drug.Fluvoxamine, y == Drug.Canagliflozin),
                 And(x == Drug.Fluvoxamine, y == Drug.Levomenthol),
                 And(x == Drug.Fluvoxamine, y == Drug.Methocarbamol ),
                 And(x == Drug.Fluvoxamine, y == Drug.Fluticasone),
                 And(x == Drug.Fluvoxamine, y == Drug.Arformoterol),
                 And(x == Drug.Fluvoxamine, y == Drug.Dihydroergocristine),
                 And(x == Drug.Fluvoxamine, y == Drug.Galantamine),
                 And(x == Drug.Fluvoxamine, y == Drug.Atorvastatin),
                 And(x == Drug.Citalopram, y == Drug.Atorvastatin ),
                 And(x == Drug.Citalopram, y == Drug.Niacin),
                 And(x == Drug.Citalopram, y == Drug.Canagliflozin ),
                 And(x == Drug.Citalopram, y == Drug.Capsaicin),
                 And(x == Drug.Citalopram, y == Drug.Levomenthol),
                 And(x == Drug.Citalopram, y == Drug.Methocarbamol ),
                 And(x == Drug.Citalopram, y == Drug.Clarithromycin ),
                 And(x == Drug.Citalopram, y == Drug.Arformoterol),
                 And(x == Drug.Citalopram, y == Drug.Galantamine ),
                 And(x == Drug.Escitalopram, y == Drug.Niacin),
                 And(x == Drug.Escitalopram, y == Drug.Canagliflozin),
                 And(x == Drug.Escitalopram, y == Drug.Capsaicin ),
                 And(x == Drug.Escitalopram, y == Drug.Levomenthol ),
                 And(x == Drug.Escitalopram, y == Drug.Methocarbamol ),
                 And(x == Drug.Escitalopram, y == Drug.Arformoterol ),
                 And(x == Drug.Escitalopram, y == Drug.Galantamine ),
                 And(x == Drug.Oseltamivir, y == Drug.Bumetanide),
                 And(x == Drug.Oseltamivir, y == Drug.Ceftriaxone),
                 And(x == Drug.Oseltamivir, y == Drug.Cefotaxime),
                 And(x == Drug.Zanamivir, y == Drug.Bumetanide),
                 And(x == Drug.Atorvastatin, y == Drug.Capsaicin),
                 And(x == Drug.Atorvastatin, y == Drug.Azithromycin),
                 And(x == Drug.Atorvastatin, y == Drug.Doxycycline),
                 And(x == Drug.Atorvastatin, y == Drug.Enalapril),
                 And(x == Drug.Atorvastatin, y == Drug.Fluticasone),
                 And(x == Drug.Atorvastatin, y == Drug.Dihydroergocristine),
                 And(x == Drug.Niacin, y == Drug.Azithromycin),
                 And(x == Drug.Niacin, y == Drug.Enalapril),
                 And(x == Drug.Niacin, y == Drug.Arformoterol),
                 And(x == Drug.Niacin, y == Drug.Dihydroergocristine),
                 And(x == Drug.Niacin, y == Drug.Galantamine),
                 And(x == Drug.Bumetanide, y == Drug.Enalapril),
                 And(x == Drug.Bumetanide, y == Drug.Doxycycline),
                 And(x == Drug.Bumetanide, y == Drug.Aclidinium),
                 And(x == Drug.Bumetanide, y == Drug.Lisinopril),
                 And(x == Drug.Bumetanide, y == Drug.Arformoterol),
                 And(x == Drug.Bumetanide, y == Drug.Cilastatin),
                 And(x == Drug.Bumetanide, y == Drug.Ceftriaxone),
                 And(x == Drug.Bumetanide, y == Drug.Ceftazidime),
                 And(x == Drug.Bumetanide, y == Drug.Cefotaxime),
                 And(x == Drug.Canagliflozin, y == Drug.Choline_salicylate),
                 And(x == Drug.Canagliflozin, y == Drug.Ramipril),
                 And(x == Drug.Canagliflozin, y == Drug.Enalapril),
                 And(x == Drug.Canagliflozin, y == Drug.Lisinopril),
                 And(x == Drug.Canagliflozin, y == Drug.Fluticasone),
                 And(x == Drug.Nitroglycerin, y == Drug.Dihydroergocristine),
                 And(x == Drug.Capsaicin, y == Drug.Azithromycin),
                 And(x == Drug.Capsaicin, y == Drug.Clarithromycin),
                 And(x == Drug.Capsaicin, y == Drug.Doxycycline),
                 And(x == Drug.Capsaicin, y == Drug.Aclidinium),
                 And(x == Drug.Capsaicin, y == Drug.Ceftriaxone),
                 And(x == Drug.Capsaicin, y == Drug.Ceftazidime),
                 And(x == Drug.Capsaicin, y == Drug.Cefotaxime),
                 And(x == Drug.Capsaicin, y == Drug.Dihydroergocristine),
                 And(x == Drug.Choline_salicylate, y == Drug.Ramipril),
                 And(x == Drug.Choline_salicylate, y == Drug.Enalapril),
                 And(x == Drug.Choline_salicylate, y == Drug.Lisinopril),
                 And(x == Drug.Azithromycin, y == Drug.Fluticasone),
                 And(x == Drug.Fluticasone, y == Drug.Dihydroergocristine),
                 And(x == Drug.Aclidinium, y == Drug.Galantamine),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Acarbose),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Metformin),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Nateglinide),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Insulin_human),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Miglitol),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Memantine),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Fluvoxamine),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Fluoxetine),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Paroxetine),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Escitalopram),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Citalopram),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Oseltamivir),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Zanamivir),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Bumetanide),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Nitroglycerin),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Canagliflozin),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Choline_salicylate),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Ramipril),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Doxycycline),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Enalapril),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Lisinopril),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Fluticasone),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Aclidinium),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Arformoterol),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Ceftazidime),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Ceftriaxone),
                 And(x == Drug.Hydroflumethiazide, y == Drug.Arformoterol),
                 And(x == Drug.Aliskiren, y == Drug.Fluvoxamine),
                 And(x == Drug.Levamlodipine, y == Drug.Insulin_human),
                 And(x == Drug.Levamlodipine, y == Drug.Metformin),
                 And(x == Drug.Levamlodipine, y == Drug.Nateglinide),
                 And(x == Drug.Levamlodipine, y == Drug.Acarbose),
                 And(x == Drug.Levamlodipine, y == Drug.Miglitol),
                 And(x == Drug.Cilazapril, y == Drug.Insulin_human),
                 And(x == Drug.Cilazapril, y == Drug.Metformin),
                 And(x == Drug.Cilazapril, y == Drug.Choline_salicylate),
                 And(x == Drug.Levamlodipine, y == Drug.Paroxetine),
                 And(x == Drug.Levamlodipine, y == Drug.Nitroglycerin),
                 And(x == Drug.Levamlodipine, y == Drug.Clarithromycin),
                 And(x == Drug.Prazosin, y == Drug.Nitroglycerin),
                 And(x == Drug.Prazosin, y == Drug.Choline_salicylate),
                 And(x == Drug.Cilazapril, y == Drug.Canagliflozin),
                 And(x == Drug.Levamlodipine, y == Drug.Canagliflozin),
                 And(x == Drug.Levamlodipine, y == Drug.Capsaicin),
                 And(x == Drug.Levamlodipine, y == Drug.Fluticasone),
                 And(x == Drug.Prazosin, y == Drug.Ramipril),
                 And(x == Drug.Cilazapril, y == Drug.Ramipril),
                 And(x == Drug.Prazosin, y == Drug.Enalapril),
                 And(x == Drug.Cilazapril, y == Drug.Enalapril),
                 And(x == Drug.Prazosin, y == Drug.Lisinopril),
                 And(x == Drug.Prazosin, y == Drug.Arformoterol),
                 And(x == Drug.Cilazapril, y == Drug.Lisinopril),
                 ),
              100,
                 If(Or(And(x == Drug.Nateglinide, y == Drug.Paroxetine),
                       And(x == Drug.Donepezil, y == Drug.Clarithromycin),
                       And(x == Drug.Memantine, y == Drug.Fluoxetine),
                       And(x == Drug.Brexpiprazole, y == Drug.Dihydroergocristine),
                       And(x == Drug.Paroxetine, y == Drug.Arformoterol),
                       And(x == Drug.Paroxetine, y == Drug.Aclidinium),
                       And(x == Drug.Paroxetine, y == Drug.Clarithromycin),
                       And(x == Drug.Paroxetine, y == Drug.Galantamine),
                       And(x == Drug.Fluvoxamine, y == Drug.Capsaicin),
                       And(x == Drug.Fluvoxamine, y == Drug.Clarithromycin),
                       And(x == Drug.Escitalopram, y == Drug.Clarithromycin ),
                       And(x == Drug.Escitalopram, y == Drug.Aclidinium ),
                       And(x == Drug.Canagliflozin, y == Drug.Clarithromycin),
                       And(x == Drug.Levomenthol, y == Drug.Clarithromycin),
                       And(x == Drug.Azithromycin, y == Drug.Dihydroergocristine),
                       And(x == Drug.Clarithromycin, y == Drug.Dihydroergocristine),
                       And(x == Drug.Clarithromycin, y == Drug.Fluticasone),
                       And(x == Drug.Clarithromycin, y == Drug.Galantamine),
                       And(x == Drug.Arformoterol, y == Drug.Dihydroergocristine),
                       And(x == Drug.Aliskiren, y == Drug.Clarithromycin),
                       And(x == Drug.Aliskiren, y == Drug.Ramipril),
                       And(x == Drug.Aliskiren, y == Drug.Enalapril),
                       And(x == Drug.Aliskiren, y == Drug.Lisinopril),
                       And(x == Drug.Prazosin, y == Drug.Brexpiprazole),


                       

                       ),
                    500,
                    0)))

f = Function('f', Condition, Drug)

s = Optimize()

def set_patient_conditions(conditions):
    patient_data=[]
    if "Diabetes" in conditions:
        s.add(Implies(hasDisease(Condition.Diabetes), Or(f(Condition.Diabetes) == Drug.Metformin, f(Condition.Diabetes) == Drug.Insulin_human, f(Condition.Diabetes) == Drug.Acarbose, f(Condition.Diabetes) == Drug.Nateglinide, f(Condition.Diabetes) == Drug.Miglitol)))
        patient_data.append(Condition.Diabetes)
    if "Depression" in conditions:
        patient_data.append(Condition.Depression)
        s.add(Implies(hasDisease(Condition.Depression), Or(f(Condition.Depression) == Drug.Fluoxetine, f(Condition.Depression) == Drug.Paroxetine, f(Condition.Depression) == Drug.Fluvoxamine, f(Condition.Depression) == Drug.Citalopram, f(Condition.Depression) == Drug.Escitalopram)))
    if "Dementia" in conditions:
        patient_data.append(Condition.Dementia)
        s.add(Implies(hasDisease(Condition.Dementia), Or(f(Condition.Dementia) == Drug.Aducanumab, f(Condition.Dementia) == Drug.Lecanemab, f(Condition.Dementia) == Drug.Donepezil, f(Condition.Dementia) == Drug.Memantine, f(Condition.Dementia) == Drug.Brexpiprazole)))
    if "Heart_Disease" in conditions:
        patient_data.append(Condition.Heart_Disease)
        s.add(Implies(hasDisease(Condition.Heart_Disease), Or(f(Condition.Heart_Disease) == Drug.Atorvastatin, f(Condition.Heart_Disease) == Drug.Niacin, f(Condition.Heart_Disease) == Drug.Bumetanide, f(Condition.Heart_Disease) == Drug.Canagliflozin, f(Condition.Heart_Disease) == Drug.Nitroglycerin)))
    if "Arthritis" in conditions:
        patient_data.append(Condition.Arthritis)
        s.add(Implies(hasDisease(Condition.Arthritis), Or(f(Condition.Arthritis) == Drug.Capsaicin, f(Condition.Arthritis) == Drug.Choline_salicylate, f(Condition.Arthritis) == Drug.Glucosamine, f(Condition.Arthritis) == Drug.Levomenthol, f(Condition.Arthritis) == Drug.Methocarbamol)))
    if "Pneumonia" in conditions:
        patient_data.append(Condition.Pneumonia)
        s.add(Implies(hasDisease(Condition.Pneumonia), Or(f(Condition.Pneumonia) == Drug.Azithromycin, f(Condition.Pneumonia) == Drug.Clarithromycin, f(Condition.Pneumonia) == Drug.Doxycycline)))
    if "Influenza" in conditions:
        patient_data.append(Condition.Influenza)
        s.add(Implies(hasDisease(Condition.Influenza), Or(f(Condition.Influenza) == Drug.Oseltamivir, f(Condition.Influenza) == Drug.Zanamivir, f(Condition.Influenza) == Drug.Peramivir, f(Condition.Influenza) == Drug.Baloxavir_marboxil)))
    if "Chronic_Kidney_Disease" in conditions:
        patient_data.append(Condition.Chronic_Kidney_Disease)
        s.add(Implies(hasDisease(Condition.Chronic_Kidney_Disease), Or(f(Condition.Chronic_Kidney_Disease) == Drug.Ramipril, f(Condition.Chronic_Kidney_Disease) == Drug.Enalapril, f(Condition.Chronic_Kidney_Disease) == Drug.Lisinopril)))
    if "Pulmonary" in conditions:
        patient_data.append(Condition.Pulmonary)
        s.add(Implies(hasDisease(Condition.Pulmonary), Or(f(Condition.Pulmonary) == Drug.Fluticasone, f(Condition.Pulmonary) == Drug.Aclidinium, f(Condition.Pulmonary) == Drug.Arformoterol, f(Condition.Pulmonary) == Drug.Mepolizumab, f(Condition.Pulmonary) == Drug.Benralizumab)))
    if "Inner_Infections" in conditions:
        patient_data.append(Condition.Inner_Infections)
        s.add(Implies(hasDisease(Condition.Inner_Infections), Or(f(Condition.Inner_Infections) == Drug.Cilastatin, f(Condition.Inner_Infections) == Drug.Ceftriaxone, f(Condition.Inner_Infections) == Drug.Ceftazidime, f(Condition.Inner_Infections) == Drug.Cefotaxime)))
    if "Cerebrovascular" in conditions:
        patient_data.append(Condition.Cerebrovascular)
        s.add(Implies(hasDisease(Condition.Cerebrovascular), Or(f(Condition.Cerebrovascular) == Drug.Aniracetam, f(Condition.Cerebrovascular) == Drug.Choline_alfoscerate, f(Condition.Cerebrovascular) == Drug.Cytidine, f(Condition.Cerebrovascular) == Drug.Dihydroergocristine, f(Condition.Cerebrovascular) == Drug.Galantamine)))
    if "Hypertension" in conditions:
        patient_data.append(Condition.Hypertension)
        s.add(Implies(hasDisease(Condition.Hypertension), Or(f(Condition.Hypertension) == Drug.Hydroflumethiazide, f(Condition.Hypertension) == Drug.Aliskiren, f(Condition.Hypertension) == Drug.Cilazapril, f(Condition.Hypertension) == Drug.Levamlodipine, f(Condition.Hypertension) == Drug.Prazosin)))
    return patient_data



def setup_condition_context(conditions):
    patient_data=set_patient_conditions(conditions)
    minimizer=0
    for condition1 in patient_data:
        for condition2 in patient_data:
                minimizer+=confl(f(condition1),f(condition2))
    s.minimize(minimizer)
                
                
#condition_list=["Hypertension","Pulmonary","Cerebrovascular","Dementia","Diabetes"]
#setup_condition_context(condition_list)
#s.add(Implies(hasDisease(Condition.Diabetes), Or(f(Condition.Diabetes) == Drug.Metformin, f(Condition.Diabetes) == Drug.Nateglinide)))
#s.add(Implies(hasDisease(Condition.Dementia), Or(f(Condition.Dementia) == Drug.Donepezil, f(Condition.Dementia) == Drug.Memantine)))
#s.add(Implies(hasDisease(Condition.Depression), Or(f(Condition.Depression) == Drug.Paroxetine, f(Condition.Depression) == Drug.Citalopram)))



#s.minimize(confl(f(Condition.Diabetes), f(Condition.Depression)) + confl(f(Condition.Diabetes), f(Condition.Dementia)) + confl(f(Condition.Dementia), f(Condition.Depression)))

def path_finder(condition_list):
    setup_condition_context(condition_list)
    Final_Verdict=''
    if s.check() == sat:
        model = s.model()
        drug_value=model.evaluate(f(Condition.Hypertension))
        
        if "Diabetes" in condition_list:
            drug_value=model.evaluate(f(Condition.Diabetes))
            Final_Verdict+="\n For Diabetes, you need "+str(drug_value)
        if "Depression" in condition_list:
            drug_value=model.evaluate(f(Condition.Depression))
            Final_Verdict+="\n For Depression, you need "+str(drug_value)
        if "Dementia" in condition_list:
            drug_value=model.evaluate(f(Condition.Dementia))
            Final_Verdict+="\n For Dementia, you need "+str(drug_value)
        if "Heart_Disease" in condition_list:
            drug_value=model.evaluate(f(Condition.Heart_Disease))
            Final_Verdict+="\n For Heart Diseases, you need "+str(drug_value)
        if "Arthritis" in condition_list:
            drug_value=model.evaluate(f(Condition.Arthritis))
            Final_Verdict+="\n For Arthritis, you need "+str(drug_value)
        if "Pneumonia" in condition_list:
            drug_value=model.evaluate(f(Condition.Pneumonia))
            Final_Verdict+="\n For Pneumonia, you need "+str(drug_value)
        if "Influenza" in condition_list:
            drug_value=model.evaluate(f(Condition.Influenza))
            Final_Verdict+="\n For Influenza, you need "+str(drug_value)
        if "Chronic_Kidney_Disease" in condition_list:
            drug_value=model.evaluate(f(Condition.Chronic_Kidney_Disease))
            Final_Verdict+="\n For Chronic Kidney Diseases, you need "+str(drug_value)
        if "Pulmonary" in condition_list:
            drug_value=model.evaluate(f(Condition.Pulmonary))
            Final_Verdict+="\n For Pulmonary Diseases, you need "+str(drug_value)
        if "Inner_Infections" in condition_list:
            drug_value=model.evaluate(f(Condition.Inner_Infections))
            Final_Verdict+="\n For Inner Infections, you need "+str(drug_value)
        if "Cerebrovascular" in condition_list:
            drug_value=model.evaluate(f(Condition.Cerebrovascular))
            Final_Verdict+="\n For Cerebrovascular, you need "+str(drug_value)
        if "Hypertension" in condition_list:
            drug_value=model.evaluate(f(Condition.Hypertension))
            Final_Verdict+="\n For Hypertension, you need "+str(drug_value)

        return Final_Verdict

    else:
        print("No solution found.")
        return None
