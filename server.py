from flask import Flask, render_template, session, redirect, request
import random
import datetime
app = Flask(__name__)
app.debug = True
app.secret_key= "Very_secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutUs.html")

@app.route('/FacultyofArchitecture')
def facultyofArchitecture():
    return render_template("FacultyofArchitecture.html")

@app.route('/FacultyofCivilEngineering')
def facultyofCivilEnginering():
    return render_template("FacultyofCivilEngineering.html")

@app.route('/FacultyofComputerScienceandInformationTechnology')
def FacultyofComputerScienceandInformationTechnology():
    return render_template("FacultyofComputerScienceandInformationTechnology.html")

@app.route('/FacultyofE-LearningTechnologiesandHumanities')
def FacultyofELearningTechnologiesandHumanities():
    return render_template("FacultyofE-LearningTechnologiesandHumanities.html")

@app.route('/FacultyofElectronicsandTelecommunications')
def FacultyofElectronicsandTelecommunications():
    return render_template("FacultyofElectronicsandTelecommunications.html")

@app.route('/FacultyofEngineeringEconomicsandManagement')
def FacultyofEngineeringEconomicsandManagement():
    return render_template("FacultyofEngineeringEconomicsandManagement.html")

@app.route('/FacultyofMaterialsScienceandAppliedChemistry')
def FacultyofMaterialsScienceandAppliedChemistry():
    return render_template("FacultyofMaterialsScienceandAppliedChemistry.html")

@app.route('/FacultyofMechanicalEngineeringTransportandAeronautics')
def FacultyofMechanicalEngineeringTransportandAeronautics():
    return render_template("FacultyofMechanicalEngineeringTransportandAeronautics.html")

@app.route('/FacultyofPowerandElectricalEngineering')
def FacultyofPowerandElectricalEngineering():
    return render_template("FacultyofPowerandElectricalEngineering.html")







 

    





    return redirect('/')




