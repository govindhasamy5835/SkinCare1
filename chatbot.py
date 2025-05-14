import datetime
import calendar
import dateutil.relativedelta
import dateutil.rrule

# Sample data (replace with a database or API calls in a real application)
skin_cancer_details = {
    "basal cell carcinoma": {
        "name": "Basal Cell Carcinoma",
        "details": "Basal cell carcinoma (BCC) is the most common type of skin cancer. It usually appears as a small, waxy bump or a scaly patch on sun-exposed areas of the skin.",
        "symptoms": ["A pearly or waxy bump", "A flat, flesh-colored or brown scar-like lesion", "A sore that bleeds or scabs over"],
        "treatment": ["Surgery (excision, Mohs surgery)", "Cryotherapy", "Topical medications", "Radiation therapy"],
    },
    "squamous cell carcinoma": {
        "name": "Squamous Cell Carcinoma",
        "details": "Squamous cell carcinoma (SCC) is the second most common type of skin cancer. It arises from the squamous cells that make up the outer layer of the skin.",
        "symptoms": ["A firm, red nodule", "A scaly patch", "A sore that doesn't heal"],
        "treatment": ["Surgery (excision, Mohs surgery)", "Radiation therapy", "Photodynamic therapy", "Topical medications"],
    },
    "melanoma": {
        "name": "Melanoma",
        "details": "Melanoma is the most serious type of skin cancer. It develops in melanocytes, the cells that produce melanin.",
        "symptoms": ["A large brownish spot with darker speckles", "A mole that changes in size, color, or feel", "A new mole that bleeds, oozes, or itches"],
        "treatment": ["Surgery", "Immunotherapy", "Targeted therapy", "Chemotherapy", "Radiation therapy"],
    },
    "merkel cell carcinoma": {
        "name": "Merkel Cell Carcinoma",
        "details": "Merkel cell carcinoma is a rare, aggressive skin cancer.",
        "symptoms": ["A firm, painless nodule on the skin", "Rapidly growing lump"],
        "treatment": ["Surgery", "Radiation therapy", "Immunotherapy", "Chemotherapy"],
    },
}

doctor_list = [
    {
        "name": "Dr. Aruna Kapoor",
        "specialization": "Dermatology",
        "hospital": "Apollo Hospitals, Chennai",
        "contact": "+91-9840012345",
    },
    {
        "name": "Dr. Vijay Kumar",
        "specialization": "Dermatology",
        "hospital": "Fortis Malar Hospital, Chennai",
        "contact": "+91-9003098765",
    },
    {
        "name": "Dr. Meera Srinivasan",
        "specialization": "Surgical Oncology",
        "hospital": "Cancer Institute (WIA), Chennai",
        "contact": "+91-9884056789",
    },
    {
        "name": "Dr. Rajesh Sharma",
        "specialization": "Radiation Oncology",
        "hospital": "MIOT International, Chennai",
        "contact": "+91-9789023456"
    },
    {
        "name": "Dr. Priya Gupta",
        "specialization": "Dermatology",
        "hospital": "Kauvery Hospital, Chennai",
        "contact": "+91-8939123456"
    },
    {
        "name": "Dr. Suresh Patel",
        "specialization": "Dermatology",
        "hospital": "Global Health City, Chennai",
        "contact": "+91-9840123457"
    },
    {
        "name": "Dr. Lakshmi Nair",
        "specialization": "Oncology",
        "hospital": "SIMS Hospital, Chennai",
        "contact": "+91-9003198766",
    },
    {
        "name": "Dr. Karthik Reddy",
        "specialization": "Surgical Oncology",
        "hospital": "Gleneagles Global Health City, Chennai",
        "contact": "+91-9884156790"
    },
    {
        "name": "Dr. Nandini Das",
        "specialization": "Radiation Oncology",
        "hospital": "Apollo Speciality Cancer Hospital, Chennai",
        "contact": "+91-9789123457"
    },
    {
        "name": "Dr. Arvind Singh",
        "specialization": "Dermatology",
        "hospital": "SRM Institutes for Medical Science (SIMS), Chennai",
        "contact": "+91-8939223457"
    },
    {
        "name": "Dr. Divya Sharma",
        "specialization": "Dermatology",
        "hospital": "Vijaya Health Centre, Chennai",
        "contact": "+91-9940012348"
    },
    {
        "name": "Dr. Ravi Kumar",
        "specialization": "Oncology",
        "hospital": "Bharathiraja Specialty Hospital, Chennai",
        "contact": "+91-9003298767"
    },
    {
        "name": "Dr. Anjali Mehta",
        "specialization": "Surgical Oncology",
        "hospital": "Be Well Hospitals, Chennai",
        "contact": "+91-9884256791"
    },
    {
        "name": "Dr. Sridhar Reddy",
        "specialization": "Radiation Oncology",
        "hospital": "VS Hospitals, Chennai",
        "contact": "+91-9789223458"
    },
    {
        "name": "Dr. Keerthi S.",
        "specialization": "Dermatology",
        "hospital": "The Madras Medical Mission, Chennai",
        "contact": "+91-8939323458"
    }
]

hospital_list = [
    {
        "name": "Apollo Hospitals, Chennai",
        "address": "21, Greams Lane, Off Greams Road, Chennai - 600006",
        "contact": "+91-44-28293333",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://www.apollohospitals.com/"
    },
    {
        "name": "Fortis Malar Hospital, Chennai",
        "address": "No. 52, 1st Main Road, Gandhi Nagar, Adyar, Chennai - 600020",
        "contact": "+91-44-42892222",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://www.fortishealthcare.com/"
    },
    {
        "name": "Cancer Institute (WIA), Chennai",
        "address": "38, Sardar Patel Road, Adyar, Chennai - 600020",
        "contact": "+91-44-22350241",
        "specialties": ["Oncology", "Radiotherapy", "Surgery"],
        "website": "https://cancerinstitutewia.org/"
    },
    {
        "name": "MIOT International, Chennai",
        "address": "4/112, Mount Poonamallee Road, Manapakkam, Chennai - 600089",
        "contact": "+91-44-22492249",
        "specialties": ["Oncology", "Radiotherapy", "Surgery"],
        "website": "https://www.miothospitals.com/"
    },
     {
        "name": "Kauvery Hospital, Chennai",
        "address": "No. 199, Luz Church Road, Mylapore, Chennai - 600004",
        "contact": "+91 44 4000 6000",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://kauveryhospital.com/"
    },
    {
        "name": "Global Health City, Chennai",
        "address": "439, Cheran Nagar, Perumbakkam, Chennai - 600100",
        "contact": "+91-44-29002900",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://www.globalhealthcity.com/"
    },
    {
        "name": "SIMS Hospital, Chennai",
        "address": "No. 1, Jawaharlal Nehru Salai, Vadapalani, Chennai - 600026",
        "contact": "+91-44-43434343",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://simshospitals.com/"
    },
    {
        "name": "Gleneagles Global Health City, Chennai",
        "address": "439, Cheran Nagar, Perumbakkam, Chennai - 600100",
        "contact": "+91 44 4477 7000",
        "specialties": ["Oncology", "Surgery"],
        "website": "https://gleneaglesglobalhealthcity.com/"
    },
    {
        "name": "Apollo Speciality Cancer Hospital, Chennai",
        "address": "Padur, Old Mahabalipuram Road, Chennai - 600096",
        "contact": "+91-44-27432233",
        "specialties": ["Oncology", "Radiotherapy", "Surgery"],
        "website": "https://chennai.apollohospitals.com/cancer-hospital/"
    },
    {
        "name": "SRM Institutes for Medical Science (SIMS), Chennai",
        "address": "No.1, Jawaharlal Nehru Salai, Vadapalani, Chennai-600026.",
        "contact": "+91 44 4343 4343",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://simshospitals.com/"
    },
    {
        "name": "Vijaya Health Centre",
        "address": "New No 434, Old No 180, N.S. Krishnan Street, Vadapalani, Chennai - 600026",
        "contact": "+91 44 2480 1601",
        "specialties": ["Dermatology", "Oncology"],
        "website": "https://www.vijayahealthcentre.org/"
    },
     {
        "name": "Bharathiraja Specialty Hospital",
        "address": "No 3 & 5, ECR Main Road, Thiruvanmiyur, Chennai - 600041",
        "contact": "+91 44 2441 4777",
        "specialties": ["Oncology", "Surgery"],
        "website": "https://www.bharathirajhospitals.com/"
    },
    {
        "name": "Be Well Hospitals",
        "address": "123, L.B. Road, Thiruvanmiyur, Chennai - 600041",
        "contact": "+91 44 7122 2333",
        "specialties": ["Oncology", "Surgery"],
        "website": "https://www.bewellhospitals.com/"
    },
    {
        "name": "VS Hospitals",
        "address": "No 2, Dr. J. Jayalalitha Nagar, Mogappair East, Chennai - 600037",
        "contact": "+91 44 4299 9999",
        "specialties": ["Oncology", "Radiotherapy"],
        "website": "https://www.vshospitals.com/"
    },
    {
        "name": "The Madras Medical Mission",
        "address": "4-A, Dr.J.Jayalalitha Nagar, Mogappair East, Chennai-600037",
        "contact": "+91 44 2656 5555",
        "specialties": ["Dermatology", "Oncology", "Surgery"],
        "website": "https://www.mmm.org.in/"
    }
]

def get_disease_details(disease_name):
    """
    Retrieves detailed information about a specific skin cancer disease.

    Args:
        disease_name (str): The name of the skin cancer disease.

    Returns:
        dict: A dictionary containing the disease details, or None if not found.
    """
    disease_name_lower = disease_name.lower()
    if disease_name_lower in skin_cancer_details:
        return skin_cancer_details[disease_name_lower]
    else:
        return None

def find_doctors(specialization=None, hospital=None):
    """
    Finds doctors based on specialization and/or hospital.

    Args:
        specialization (str, optional): The specialization of the doctor. Defaults to None.
        hospital (str, optional): The hospital where the doctor works. Defaults to None.

    Returns:
        list: A list of dictionaries, where each dictionary contains doctor details
              (name, specialization, hospital, contact).  Returns an empty list
              if no matching doctors are found.
    """
    filtered_doctors = []
    for doctor in doctor_list:
        if specialization and hospital:
            if specialization.lower() in doctor["specialization"].lower() and hospital.lower() in doctor["hospital"].lower():
                filtered_doctors.append(doctor)
        elif specialization:
            if specialization.lower() in doctor["specialization"].lower():
                filtered_doctors.append(doctor)
        elif hospital:
             if hospital.lower() in doctor["hospital"].lower():
                filtered_doctors.append(doctor)
        else:
            filtered_doctors = doctor_list # return all if no criteria provided.
            break

    return filtered_doctors

def find_hospitals(hospital_name=None,specialty=None):
    """
    Finds hospitals based on name.

    Args:
        hospital_name (str, optional): The name of the hospital. Defaults to None.

    Returns:
        list: A list of dictionaries, where each dictionary contains hospital details
              (name, address, contact, specialties). Returns an empty list if no matching
              hospitals are found.
    """
    filtered_hospitals = []
    if hospital_name:
        for hospital in hospital_list:
            if hospital_name.lower() in hospital["name"].lower():
                filtered_hospitals.append(hospital)
    elif specialty:
        for hospital in hospital_list:
            if specialty.lower() in [s.lower() for s in hospital["specialties"]]:
                filtered_hospitals.append(hospital)
    else:
        filtered_hospitals = hospital_list

    return filtered_hospitals

def get_user_input():
    """Gets user input and handles it using try...except.

       Returns:
        str: user's input
    """
    while True:
        try:
            user_input = input("User: ").strip()
            if not user_input:  # Check for empty input
                print("Chatbot: Please enter a valid query.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\nChatbot: Exiting the chat. Goodbye!")
            exit()
        except EOFError:
            print("\nChatbot: Exiting the chat. Goodbye!")
            exit()
        except Exception as e:
            print(f"Chatbot: An unexpected error occurred: {e}. Please try again.")
            # Log the error for debugging
            # logging.exception("An error occurred: ")  # Import logging


def chatbot():
    """
    Main function to run the chatbot.
    """
    print("Chatbot: Welcome! I'm here to provide information about skin cancer.")
    print("Chatbot: You can ask me about specific skin cancer diseases, doctors, and hospitals.")
    print("Chatbot: For example, you can say: 'Tell me about melanoma', 'Find doctors in Apollo Hospitals', or 'List hospitals that treat skin cancer'.")
    print("Chatbot: You can also say 'exit' to quit.")

    while True:
        user_input = get_user_input()

        if "exit" in user_input.lower():
            print("Chatbot: Thank you for using the chatbot. Goodbye!")
            break

        disease_name = None
        doctor_query = False
        hospital_query = False

        # Basic keyword matching for disease name
        for disease in skin_cancer_details:
            if disease in user_input.lower():
                disease_name = disease
                break

        if "doctor" in user_input.lower():
            doctor_query = True
        if "hospital" in user_input.lower():
            hospital_query = True

        if disease_name:
            disease_info = get_disease_details(disease_name)
            if disease_info:
                print(f"Chatbot: Here is information about {disease_info['name']}:")
                print(f"  Details: {disease_info['details']}")
                print(f"  Symptoms: {', '.join(disease_info['symptoms'])}")
                print(f"  Treatment: {', '.join(disease_info['treatment'])}")
            else:
                print("Chatbot: Sorry, I don't have information on that specific skin cancer.")

        if doctor_query:
            specialization = None
            hospital = None
            if "specialization" in user_input.lower():
                specialization = input("Chatbot: Please enter the specialization: ")
            if "hospital" in user_input.lower():
                hospital = input("Chatbot: Please enter the hospital: ")
            doctors = find_doctors(specialization, hospital)
            if doctors:
                print("Chatbot: Here are the doctors:")
                for doctor in doctors:
                    print(f"  - Name: {doctor['name']}, Specialization: {doctor['specialization']}, Hospital: {doctor['hospital']}, Contact: {doctor['contact']}")
            else:
                print("Chatbot: Sorry, I couldn't find any doctors matching your criteria.")

        if hospital_query:
            hospital_name = None
            specialty = None
            if "name" in user_input.lower():
                hospital_name = input("Chatbot: Please enter the hospital name: ")
            if "specialty" in user_input.lower() or "speciality" in user_input.lower():
                specialty = input("Chatbot: Please enter the hospital specialty: ")
            hospitals = find_hospitals(hospital_name,specialty)
            if hospitals:
                print("Chatbot: Here are the hospitals:")
                for hospital in hospitals:
                    print(f"  - Name: {hospital['name']}, Address: {hospital['address']}, Contact: {hospital['contact']}, Specialties: {', '.join(hospital['specialties'])}")
            else:
                print("Chatbot: Sorry, I couldn't find any hospitals matching your criteria.")

        if not disease_name and not doctor_query and not hospital_query:
            print("Chatbot: I'm sorry, I didn't understand your request. Please ask about a specific skin cancer disease, doctors, or hospitals.")

if __name__ == "__main__":
    chatbot()
