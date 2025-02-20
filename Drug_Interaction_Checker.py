import flet as ft
import Conflict_Calculation as CC
import Path_finder as PF
import Calculate_symptoms as Csymp


Conditions=["Diabetes","Depression","Dementia","Heart Disease","Arthritis","Pneumonia","Influenza","Chronic Kidney Disease","Pulmonary","Inner Infections","Cerebrovascular"]



def main(page):

    page.window_maximizable=True
    Checkbox_dictionary={
    'Diabetes':False,
    'Depression':False,
    'Dementia':False,
    'Heart_Disease':False,
    'Arthritis':False,
    'Depression':False,
    'Pneumonia':False,
    'Influenza':False,
    'Chronic_Kidney_Disease':False,
    'Pulmonary':False,
    'Inner_Infections':False,
    'Cerebrovascular':False,
    'Hypertension':False,
    }
    page.bgcolor="#01BAEF"
    page.title="Automated Drug Interaction Checker"
    page.fonts={
        "Ubuntu_Title":"/Font/Ubuntu-Title.ttf",
    }

    
    def menu_route_change(e):
        homerow2.controls[0].bgcolor="#4082ff"
        homerow2.controls[1].bgcolor="#4082ff"
        homerow2.controls[2].bgcolor="#4082ff"
        for i in range (0,len(page.controls)):
            page.remove_at(0)
        page.bgcolor="#01BAEF"
        page.appbar = ft.AppBar(
        leading_width=40,
        title= ft.Text("Main Menu", size=30, color="#4895ef",font_family="Ubuntu_Title"),
        center_title=True,
        bgcolor="#001845",)
        page.add(homerow1,homerow2)
        page.update()

    def search_path_route_change(e):
        for i in range (0,len(page.controls)):
            page.remove_at(0)
        page.appbar = ft.AppBar(
        leading_width=40,
        title= ft.Text("SELECT YOUR CONDITIONS", size=30, color="#4895ef",font_family="Ubuntu_Title"),
        center_title=True,
        bgcolor="#001845",
        actions=[
            ft.IconButton(ft.icons.HOME,icon_color="#4895ef",on_click=menu_route_change,tooltip="Return to the main menu,. ")]
        )
    
        page.add(row1,row2,row3,row4)
        page.update()
    
    def Symptoms_route_change(e):
        for i in range (0,len(page.controls)):
            page.remove_at(0)
        page.appbar = ft.AppBar(
        leading_width=40,
        title= ft.Text("SELECT YOUR SYMPTOMS", size=30, color="#4895ef",font_family="Ubuntu_Title"),
        center_title=True,
        bgcolor="#001845",
        actions=[
            ft.IconButton(ft.icons.HOME,icon_color="#4895ef",on_click=menu_route_change,tooltip="Return to the main menu,. ")]
        )
        page.add(Symptom_row1,Symptom_row2,Symptom_row3,Symptom_row4,Symptom_row5,symptom_text_row,Symptom_submit_button)
        page.update()
    
    def checkbox_changed(e):
        Checkbox_dictionary["Diabetes"]=row1.controls[0].content.value
        Checkbox_dictionary["Depression"]=row1.controls[1].content.value
        Checkbox_dictionary["Heart_Disease"]=row1.controls[2].content.value
        Checkbox_dictionary['Dementia']=row1.controls[3].content.value
        Checkbox_dictionary['Arthritis']=row1.controls[4].content.value
        Checkbox_dictionary['Hypertension']=row1.controls[5].content.value

        Checkbox_dictionary["Pneumonia"]=row2.controls[0].content.value
        Checkbox_dictionary["Influenza"]=row2.controls[1].content.value
        Checkbox_dictionary["Chronic_Kidney_Disease"]=row2.controls[2].content.value
        Checkbox_dictionary['Pulmonary']=row2.controls[3].content.value
        Checkbox_dictionary['Inner_Infections']=row2.controls[4].content.value
        Checkbox_dictionary['Cerebrovascular']=row2.controls[5].content.value
    
    def get_checked_checkbox():
        checked_elements=[]
        for elements in Checkbox_dictionary.keys():
            if Checkbox_dictionary[elements]==True:
                checked_elements.append(elements)
        if len(checked_elements)<2 or len(checked_elements)>5:
            return "Please select between 2 or 5 conditions..."
        else:
            #phrase=''
            #for elements in checked_elements:
             #   phrase+=elements+" has been selected\n"
            Verdict=PF.path_finder(checked_elements)
            return Verdict
    
    def show_submission(e):
        row3.controls[0].content=ft.Text('Please wait...',size=30,color="#001845")
        page.update()
        submission=get_checked_checkbox()
        print(submission)
        row3.controls[0].content=ft.Text(submission,size=30,color="#001845")
        page.update()

    def menu_on_hover(e):
        e.control.bgcolor = "4082ff" if e.data == "true" else "blue"
        e.control.update()

    Selection_Checkbox_dictionary={
    'Diabetes':False,
    'Depression':False,
    'Dementia':False,
    'Heart_Disease':False,
    'Arthritis':False,
    'Depression':False,
    'Pneumonia':False,
    'Influenza':False,
    'Chronic_Kidney_Disease':False,
    'Pulmonary':False,
    'Inner_Infections':False,
    'Cerebrovascular':False,
    'Hypertension':False,
    }
    def selection_checkbox_changed(e):
        Selection_Checkbox_dictionary["Diabetes"]=selection_row1.controls[0].content.value
        Selection_Checkbox_dictionary["Depression"]=selection_row1.controls[1].content.value
        Selection_Checkbox_dictionary["Heart_Disease"]=selection_row1.controls[2].content.value
        Selection_Checkbox_dictionary['Dementia']=selection_row1.controls[3].content.value
        Selection_Checkbox_dictionary['Arthritis']=selection_row1.controls[4].content.value
        Selection_Checkbox_dictionary['Hypertension']=selection_row1.controls[5].content.value

        Selection_Checkbox_dictionary["Pneumonia"]=selection_row2.controls[0].content.value
        Selection_Checkbox_dictionary["Influenza"]=selection_row2.controls[1].content.value
        Selection_Checkbox_dictionary["Chronic_Kidney_Disease"]=selection_row2.controls[2].content.value
        Selection_Checkbox_dictionary['Pulmonary']=selection_row2.controls[3].content.value
        Selection_Checkbox_dictionary['Inner_Infections']=selection_row2.controls[4].content.value
        Selection_Checkbox_dictionary['Cerebrovascular']=selection_row2.controls[5].content.value
    
    def add_options_to_next_page():
        if Selection_Checkbox_dictionary["Diabetes"]==True:
            page.add(Diabetes_title,Diabetes_row)
        if Selection_Checkbox_dictionary["Depression"]==True:
            page.add(Depression_title,Depression_row)
        if Selection_Checkbox_dictionary["Heart_Disease"]==True:
            page.add(Heart_title,Heart_Row)
        if Selection_Checkbox_dictionary["Dementia"]==True:
            page.add(Dementia_title,Dementia_row)
        if Selection_Checkbox_dictionary["Arthritis"]==True:
            page.add(Arthritis_title,Arthritis_row)
        if Selection_Checkbox_dictionary["Hypertension"]==True:
            page.add(Hypertension_title,Hypertension_Row)
        if Selection_Checkbox_dictionary["Pneumonia"]==True:
            page.add(Pneumonia_title,Pneumonia_row)
        if Selection_Checkbox_dictionary["Influenza"]==True:
            page.add(Influenza_title,Influenza_row)
        if Selection_Checkbox_dictionary["Chronic_Kidney_Disease"]==True:
            page.add(Chronic_title,Chronic_Row)
        if Selection_Checkbox_dictionary["Pulmonary"]==True:
            page.add(Pulmonary_title,Pulmonary_Row)
        if Selection_Checkbox_dictionary["Inner_Infections"]==True:
            page.add(Inner_Title,Inner_Row)
        if Selection_Checkbox_dictionary["Cerebrovascular"]==True:
            page.add(Cerebrovascular_title,Cerebrovascular_Row)

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def close_dlg2(e):
        dlg_modal2.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error!"),
        content=ft.Text("Please select between 2 and 5 conditions"),
        actions=[
            ft.TextButton("Okay", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    dlg_modal2 = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error!"),
        content=ft.Text("Please select a medication from each chosen conditions"),
        actions=[
            ft.TextButton("Okay", on_click=close_dlg2),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )


    
    def open_dlg_modal():
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def open_dlg_modal2():
        page.dialog = dlg_modal2
        dlg_modal2.open = True
        page.update()
    
    def Go_to_path_rater(e):
        checked_elements=[]
        for elements in Selection_Checkbox_dictionary.keys():
            if Selection_Checkbox_dictionary[elements]==True:
                checked_elements.append(elements)
        if len(checked_elements)<2 or len(checked_elements)>5:
            open_dlg_modal()
        else:
            for i in range (0,len(page.controls)):
                page.remove_at(0)
            page.appbar = ft.AppBar(
            leading_width=40,
            title= ft.Text("SELECT YOUR MEDICATIONS FROM THE COMBINATION", size=30, color="#4895ef",font_family="Ubuntu_Title"),
            center_title=True,
            bgcolor="#001845",
            actions=[
                ft.IconButton(ft.icons.KEYBOARD_BACKSPACE,icon_color="#4895ef",tooltip="Go back to condition selection ",on_click=go_back_to_conditions_selection),
                ft.IconButton(ft.icons.HOME,icon_color="#4895ef",tooltip="Return to the main menu ",on_click=menu_route_change)]
            )
        
            add_options_to_next_page()
            page.add(text_row)
            page.add(submit_button)
            page.update()
    
    def go_back_to_conditions_selection(e):
        for i in range (0,len(page.controls)):
                page.remove_at(0)
        text_row.controls[0].content=None
        page.appbar = ft.AppBar(
        leading_width=40,
        title= ft.Text("SELECT THE CONDITIONS OF YOUR DRUGS", size=30, color="#4895ef",font_family="Ubuntu_Title"),
        center_title=True,
        bgcolor="#001845",
        actions=[
            ft.IconButton(ft.icons.HOME,icon_color="#4895ef",tooltip="Return to the main menu,. ",on_click=menu_route_change),
            ]
        )
        page.add(selection_row1,selection_row2,selection_row3)
        page.update()
    
    def perform_drug_check(e):
        medication_list=[]
        combination_conflict_total=0
        output="The chosen drugs are "
        for i in range(1, len(page.controls)-1, 2):
            medication_list.append(page.controls[i].controls[0].content.value)
        if None in medication_list:
            open_dlg_modal2()
        else:
            for medications_x in medication_list:
                for medication_y in medication_list:
                    combination_conflict_total+=CC.calculate_conflicts(medications_x,medication_y)
            statement=CC.get_statement(combination_conflict_total)
            if statement=="Perfectly safe":
                text_row.controls[0].content=ft.Text("This combination is completely safe!The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#326400")
            elif statement=="Minor Threat":
                 text_row.controls[0].content=ft.Text("This combination threat is rated as Minor!The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#5DBA00")
            elif statement=="Mild Threat":
                 text_row.controls[0].content=ft.Text("Be careful...This combination threat is rated as Mild! The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#B28F00")
            elif statement=="Moderate Threat":
                text_row.controls[0].content=ft.Text("Be very cautious...This combination threat is rated as Moderate! The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#DC9C00")
            elif statement=="Significant Threat":
                 text_row.controls[0].content=ft.Text("Please excercise viglilance! This combination threat is rated as Significant! The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#DC6700")
            elif statement=="Major Threat":
                text_row.controls[0].content=ft.Text("Watch out! This combination threat is rated as Major! The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#EE3D00")
            elif statement=="Severe Threat":
                text_row.controls[0].content=ft.Text("WARNING, Avoid this path at all cost! This combination threat is rated as SEVERE! The conflict rating is "+str(combination_conflict_total),size=30,font_family='Ubuntu_Title',color="#B20000")
            
            page.update()
    

    def get_symptom_checkboxes():
        checked_elements=[]
        for elements in symptom_checkbox_dictionary.keys():
            if symptom_checkbox_dictionary[elements]==True:
                checked_elements.append(elements)
        
            #phrase=""
            #for elements in checked_elements:
             #   phrase+=elements+" has been selected\n"
        Verdict=Csymp.message_output(checked_elements)
        return Verdict
    
    def show_symptom_submission(e):
        submission=get_symptom_checkboxes()
        print(submission)
        symptom_text_row.controls[0].content=ft.Text(submission,size=30,color="#001845")
        page.update()

    symptom_checkbox_dictionary={
    "Fatigue":False,
    "Frequent Urination":False,
    "Weight Loss":False,
    "Memory Problems":False,
    "Mood Swings":False,
    "Disturbed Sleep":False,
    "Low Motivation":False,
    "Coughing":False,
    "Sore Throat":False,
    "Fever":False,
    "Headaches":False,
    "Chest Pain":False,
    "Joint Stiffness":False,
    "Muscle Pain":False,
    "Difficulty Breathing":False,
    "Bone Pain":False,
    "Swelling":False,
    "Nausea":False,
    "Troube Speaking":False,
    "Increased Hubger":False,
    "Lack of Concentration":False,
    "Inflammed Skin":False,
    "Mucus":False,
    }
    def symptom_checkbox_changed(e):
        symptom_checkbox_dictionary["Fatigue"]=Symptom_row1.controls[0].content.value
        symptom_checkbox_dictionary["Frequent Urination"]=Symptom_row1.controls[1].content.value
        symptom_checkbox_dictionary["Weight Loss"]=Symptom_row1.controls[2].content.value
        symptom_checkbox_dictionary["Memory Problems"]=Symptom_row1.controls[3].content.value
        symptom_checkbox_dictionary["Mood Swings"]=Symptom_row1.controls[4].content.value
        

        symptom_checkbox_dictionary["Disturbed Sleep"]=Symptom_row2.controls[0].content.value
        symptom_checkbox_dictionary["Low Motivation"]=Symptom_row2.controls[1].content.value
        symptom_checkbox_dictionary["Coughing"]=Symptom_row2.controls[2].content.value
        symptom_checkbox_dictionary["Sore Throat"]=Symptom_row2.controls[3].content.value
        symptom_checkbox_dictionary["Fever"]=Symptom_row2.controls[4].content.value
        
        symptom_checkbox_dictionary["Headaches"]=Symptom_row3.controls[0].content.value
        symptom_checkbox_dictionary["Chest Pain"]=Symptom_row3.controls[1].content.value
        symptom_checkbox_dictionary["Joint Stiffness"]=Symptom_row3.controls[2].content.value
        symptom_checkbox_dictionary["Muscle Pain"]=Symptom_row3.controls[3].content.value
        symptom_checkbox_dictionary["Difficulty Breathing"]=Symptom_row3.controls[4].content.value
    
        symptom_checkbox_dictionary["Bone Pain"]=Symptom_row4.controls[0].content.value
        symptom_checkbox_dictionary["Swelling"]=Symptom_row4.controls[1].content.value
        symptom_checkbox_dictionary["Sweating"]=Symptom_row4.controls[2].content.value
        symptom_checkbox_dictionary["Nausea"]=Symptom_row4.controls[3].content.value
        symptom_checkbox_dictionary["Trouble Speaking"]=Symptom_row4.controls[4].content.value

        symptom_checkbox_dictionary["Increased Hunger"]=Symptom_row5.controls[0].content.value
        symptom_checkbox_dictionary["Lack of Concentration"]=Symptom_row5.controls[1].content.value
        symptom_checkbox_dictionary["Unusual Heartbeat"]=Symptom_row5.controls[2].content.value
        symptom_checkbox_dictionary["Inflammed Skin"]=Symptom_row5.controls[3].content.value
        symptom_checkbox_dictionary["Mucus"]=Symptom_row5.controls[4].content.value



    

    page.appbar = ft.AppBar(
        leading_width=40,
        title= ft.Text("Main Menu", size=30, color="#4895ef",font_family="Ubuntu_Title"),
        center_title=True,
        bgcolor="#001845",)
    

    row1=ft.Row(
        [
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Diabetes",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                
                image_opacity=0.0,
                expand=True,


            ),
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Depression",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Heart Disease",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Dementia",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Arthritis",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Hypertension",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )
    


    row2=ft.Row(
        [
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Pneumonia",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Influenza",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Chronic Kidney Disease",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="COPD",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Inner Infections",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),

            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Cerebrovascular",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )

    row3=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor="#B5D0FF",
                expand=True,
                height=300,
                margin=10
            ),])

    row4=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(text="Confirm",on_click=show_submission),
                expand=True,
            ),])
    homerow1=ft.Row(
        [
            ft.Container(
                bgcolor="#001845",
                alignment=ft.alignment.center,
                
                border_radius= ft.border_radius.all(30),
                content= ft.Text(
            "Automated Drug Interaction Checker",
                size=60,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
                image_opacity=0.0,
                expand=True,)])
    homerow2=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                border = ft.border.all(10, "#001845"),
                height=500,
                ink=True,
                border_radius= ft.border_radius.all(30),
                bgcolor="#4082ff",
                content= ft.Text(
                    "Find a Safe Combination",
                font_family='Ubuntu_Title',
                size=30,
                color="#001845",
                weight=ft.FontWeight.BOLD,
        ),
                on_hover=menu_on_hover,
                on_click= search_path_route_change,
                expand=True,),

            ft.Container(
                alignment=ft.alignment.center,
                border = ft.border.all(10, "#001845"),
                height=500,
                ink=True,
                border_radius= ft.border_radius.all(30),
                bgcolor="#4082ff",
                content= ft.Text(
                    "Check Combination Safety",
                font_family='Ubuntu_Title',
                size=30,
                color="#001845",
                weight=ft.FontWeight.BOLD,
        ),
                on_hover=menu_on_hover,
                on_click=go_back_to_conditions_selection,
                expand=True,),

            ft.Container(
                alignment=ft.alignment.center,
                border = ft.border.all(10, "#001845"),
                height=500,
                ink=True,
                border_radius= ft.border_radius.all(30),
                bgcolor="#4082ff",
                content= ft.Text(
                    "Check Symptoms",
                font_family='Ubuntu_Title',
                size=40,
                color="#001845",
                weight=ft.FontWeight.BOLD,
        ),
                on_hover=menu_on_hover,
                on_click=Symptoms_route_change,
                expand=True,),
                
                
                ],
                 spacing=10,
                 alignment=ft.alignment.center,
                )

    text_row=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor="#B5D0FF",
                expand=True,
                height=100,
                margin=10
            ),])
    
    selection_row1=ft.Row(
        [
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Diabetes",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                
                image_opacity=0.0,
                expand=True,


            ),
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Depression",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Heart Disease",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Dementia",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Arthritis",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Hypertension",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )
    


    selection_row2=ft.Row(
        [
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Pneumonia",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Influenza",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Chronic Kidney Disease",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="COPD",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Inner Infections",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),

            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Cerebrovascular",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=selection_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )

    selection_row3=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(text="Next",on_click=Go_to_path_rater),
                expand=True,
            ),])
    
    submit_button=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(text="Submit",on_click=perform_drug_check),
                expand=True,
            ),])
    
    Diabetes_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Memantine", label="Metformin"),
            ft.Radio(value="Insulin human", label="Insulin Human"),
            ft.Radio(value="Acarbose", label="Acarbose"),
            ft.Radio(value="Miglitol", label="Miglitol"),
            ft.Radio(value="Nategline", label="Nateglinide"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Dementia_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Aducanumab", label="Aducanumab"),
            ft.Radio(value="Lecanemab", label="Lecanemab"),
            ft.Radio(value="Donepezil", label="Donepezil"),
            ft.Radio(value="Memantine", label="Memantine"),
            ft.Radio(value="Brexpiprazole", label="Brexpiprazole"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Depression_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Fluoxetine", label="Fluoxetine"),
            ft.Radio(value="Paroxetine", label="Paroxetine"),
            ft.Radio(value="Fluvoxamine", label="Fluvoxamine"),
            ft.Radio(value="Citalopram ", label="Citalopram"),
            ft.Radio(value="Escitalopram", label="Escitalopram"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Influenza_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Oseltamivir", label="Oseltamivir phosphate"),
            ft.Radio(value="Zanamivir ", label="Zanamivir"),
            ft.Radio(value="Peramivir", label="Peramivir"),
            ft.Radio(value="Baloxavir Marboxil", label="Baloxavir Marboxil"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Heart_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Atorvastatin", label="Atorvastatin"),
            ft.Radio(value="Niacin", label="Niacin"),
            ft.Radio(value="Bumetanide", label="Bumetanide"),
            ft.Radio(value="Canagliflozin", label="Canagliflozin"),
            ft.Radio(value="Nitroglycerin", label="Nitroglycerin"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Arthritis_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Capsaicin", label="Atorvastatin"),
            ft.Radio(value="Choline Salicylate", label="Choline salicylate"),
            ft.Radio(value="Glucosamine", label="Glucosamine"),
            ft.Radio(value="Levomenthol", label="Levomenthol"),
            ft.Radio(value="Methocarbamol", label="Methocarbamol"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Pneumonia_row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Azithromycin", label="Azithromycin"),
            ft.Radio(value="Clarithromycin", label="Clarithromycin"),
            ft.Radio(value="Doxycycline", label="Doxycycline"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Chronic_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Ramipril", label="Ramipril"),
            ft.Radio(value="Enalapril", label="Enalapril"),
            ft.Radio(value="Lisinopril", label="Lisinopril"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Pulmonary_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Fluticasone", label="Fluticasone"),
            ft.Radio(value="Aclidinium", label="Aclidinium"),
            ft.Radio(value="Arformoterol", label="Arformoterol"),
            ft.Radio(value="Mepolizumab", label="Mepolizumab"),
            ft.Radio(value="Benralizumab", label="Benralizumab"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Inner_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Cilastatin", label="Cilastatin"),
            ft.Radio(value="Ceftriaxone", label="Ceftriaxone"),
            ft.Radio(value="Ceftazidime", label="Ceftazidime"),
            ft.Radio(value="Cefotaxime", label="Cefotaxime"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Cerebrovascular_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Aniracetam", label="Aniracetam"),
            ft.Radio(value="Choline Alfoscerate", label="Choline Alfoscerate"),
            ft.Radio(value="Cytidine", label="Cytidine"),
            ft.Radio(value="Dihydroergocristine", label="Dihydroergocristine"),
            ft.Radio(value="Galantamine", label="Galantamine"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Hypertension_Row=ft.Row(
        [
            ft.Container(
            content=ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Hydroflumethiazide", label="Hydroflumethiazide"),
            ft.Radio(value="Aliskiren", label="Aliskiren"),
            ft.Radio(value="Cilazapril", label="Cilazapril"),
            ft.Radio(value="Levamlodipine", label="Levamlodipine"),
            ft.Radio(value="Prazosin", label="Prazosin"),
            ],
            tight=True
            )),
            bgcolor="#0466C8",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    Diabetes_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Diabetes",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Dementia_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Dementia and Alzheimer",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Depression_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Depression",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Influenza_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Influenza",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Heart_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Heart Disease",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Arthritis_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Arthritis",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Pneumonia_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Pneumonia",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )


    Chronic_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Chronic Kidney Disease",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Pulmonary_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Chronic Obstructive Pulmonary Disease",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Inner_Title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Bone, Joint and Bacterial Infections",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Cerebrovascular_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Cerebrovascular Diseases",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    Hypertension_title=ft.Row(
        [
            ft.Container(
            content=ft.Text(
            "Hypertension",
                size=20,
                color="#4895ef",
                weight=ft.FontWeight.BOLD,
        ),
            height=50,
            bgcolor="#002855",
            expand=True,
            alignment=ft.alignment.center,
            )
        ],
        expand=True,
        alignment=ft.CrossAxisAlignment.START,
    )

    symptom_text_row=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor="#B5D0FF",
                expand=True,
                height=100,
                margin=10
            ),])
    
    Symptom_row1=ft.Row(
        [
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Extreme Fatigue",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                image_opacity=0.0,
                expand=True,


            ),
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Frequent Urination",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Weight Loss",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Memory Loss",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Mood Swings",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )

    Symptom_row2=ft.Row(
        [
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Disturbed Sleep",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                image_opacity=0.0,
                expand=True,


            ),
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Low Motivation",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Coughing",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Sore Throat",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Fever",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )

    Symptom_row3=ft.Row(
        [
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Headaches",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                image_opacity=0.0,
                expand=True,


            ),
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Chest Pain",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Joint Stiffness",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Muscle Pain",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),

            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Difficulty Breathing",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        spacing=5,
        expand=True,
    )

    Symptom_row4=ft.Row(
        [
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Bone Pain",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Swelling",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Sweating",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Nausea",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,

            ),
            ft.Container(
                bgcolor="#002855",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Trouble Speaking",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                image_opacity=0.0,
                expand=True,


            ),
        ],
        spacing=5,
        expand=True,
    )

    Symptom_row5=ft.Row(
        [
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Increased Hunger",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Lack of Concentration",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#0466C8",
                content=ft.Checkbox(label="Unusual Heartbeat",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.Container(
                bgcolor="#002855",
                content=ft.Checkbox(label="Inflammed Skin",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                alignment=ft.alignment.center,
                expand=True,

            ),
            ft.Container(
                bgcolor="#0466C8",
                alignment=ft.alignment.center,
                content=ft.Checkbox(label="Mucus Coughs",fill_color={ft.MaterialState.SELECTED: "#08FF00",},on_change=symptom_checkbox_changed,value=False),
                image_opacity=0.0,
                expand=True,


            ),
        ],
        spacing=5,
        expand=True,
    )

    Symptom_submit_button=ft.Row(
        [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(text="Submit",on_click=show_symptom_submission),
                expand=True,
            ),])


    page.add(homerow1,homerow2)


            

ft.app(target=main)