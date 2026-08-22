print("=========================================")
print("     MEDICAL DIAGNOSIS INTELLIGENT AGENT")
print("=========================================\n")

# PEAS Representation
print("PEAS REPRESENTATION")
print("----------------------------")
print("Performance Measure : Accurate Diagnosis, Fast Response")
print("Environment         : Hospital / Clinic")
print("Actuators           : Display Diagnosis and Suggestion")
print("Sensors             : Fever, Cough, Headache")
print("----------------------------\n")

# Taking input from user
fever = input("Does the patient have Fever? (yes/no): ").lower()
cough = input("Does the patient have Cough? (yes/no): ").lower()
headache = input("Does the patient have Headache? (yes/no): ").lower()

print("\n---------------------------------")
print("AGENT ANALYSIS")
print("---------------------------------")

# Rule-based diagnosis
if fever == "yes" and cough == "yes" and headache == "yes":
    diagnosis = "Possible Flu or Viral Infection"
    suggestion = "Consult a doctor and take adequate rest."

elif fever == "yes" and cough == "yes":
    diagnosis = "Possible Common Cold"
    suggestion = "Stay hydrated and consult a doctor if symptoms worsen."

elif fever == "yes" and headache == "yes":
    diagnosis = "Possible Viral Fever"
    suggestion = "Monitor temperature and consult a doctor."

elif cough == "yes":
    diagnosis = "Possible Throat Infection"
    suggestion = "Drink warm fluids and seek medical advice."

else:
    diagnosis = "No major illness detected"
    suggestion = "Maintain a healthy lifestyle."

print("Diagnosis :", diagnosis)
print("Suggestion:", suggestion)

print("\nAgent Decision Completed Successfully.")