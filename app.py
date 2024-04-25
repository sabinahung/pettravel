import streamlit as st
import datetime
import pandas as pd

st.set_page_config(
    page_title="Reuniting with your pet", 
    page_icon='✈️', 
    layout="centered", 
    initial_sidebar_state="expanded")

df = pd.read_csv('airlines.csv')

st.write('# Reuniting with your pet! 🐶🐱')
placeholder = st.empty()
with placeholder.container():
    st.write('''
            ### Things to get done to transport your pet from Taiwan

            We understand that it is a hustle to transport your pet overseas. The information is all over the place and it is hard to keep track of what you need to do. This app is designed to help you plan your pet's travel.  
        
            
            Due to the complexity of the process, we will focus on the preparation steps for **dogs and cats to Japan, U.S., and Europe**. We are working on adding more pet types and destinations in the future.
            ''')
# started = st.button('Get started')

    
today = datetime.date.today()


with st.sidebar:
    with st.form(key='my_form', border=False):
        # st.write("#### When are you planning to leave?")
        # d = st.date_input("Select your departure date", 
        #             today)
        
        st.markdown("")
        st.title("Where are you going?")
        country = st.radio(
                "Select your destination",
                ["Japan", "U.S.", "Europe"],
                index=True, horizontal=True
            )
        
        st.markdown("")
        st.title("How would you like your pet be transported?")
        method = st.radio(
                "Select your method of preference",
                ["Carry-on", "Cargo hold"],
                index=0, horizontal=True
            )
        
        st.markdown("")
        submitted = st.form_submit_button(label='Submit')

if submitted:
    placeholder.empty()
    st.write(f'''
            #### 1. Here are some steps before your pet travels to {country}:
            ''')
    if country == "Japan":
        st.write("Please allow for **at least 6 months** to prepare for your pet's travel to Japan.")
        with st.expander('Step 1: Microchip implanting'):
                st.write('''
                        The microchip should comply with ISO 11784 and 11785 (15 digit microchip code consists only of numbers).
                         
                        Make sure the microchip number can be read by a microchip reader at veterinary hospitals.
                        In case that the microchip implanted is not ISO standards, you should contact Animal Quarantine Service at the expected port of entry.
                         ''')
                st.warning('''
                        - If our microchip reader cannot read the non-ISO microchip, you need to prepare a reader which can read it.
                         
                        - Microchip numbers starting with "900 202" are currently under investigation for their validity. Please note that for the time being, these microchips will not be accepted as a means of identification. (Apr.7, 2023)
                         '''
                           , icon="⚠️")
        with st.expander('Step 2: Twice or more rabies vaccination'):
                st.write('''
                        - First rabies vaccination
                            - At least 91 days old at the time of vaccination （the date of birth is counted as day 0）
                            - After the microchip implanting （including the same day of implanting）
                        - Second rabies vaccination
                            - More than 30 days apart from the first vaccination (the date of the first one is counted as day 0)
                            - Within the effective period of the first vaccination
                         ''')
                st.warning('''
                           - If the effective period of the rabies vaccination will expire before arrival in Japan, an additional rabies vaccination must be administered within the period.
                           - Live virus vaccine is not accepted.
                           - Rabies vaccination conducted before microchip implantation is invalid, but it may be accepted [under certain conditions](https://www.maff.go.jp/aqs/english/animal/dog/pdf/certain_conditions.pdf). 
                            '''
                           , icon="⚠️")

        with st.expander('Step 3: Rabies anitbody test'):
                st.write('''
                        Rabies antibody test must be performed at one of the [designated laboratories](https://www.maff.go.jp/aqs/animal/dog/lab.html).
                        - Antibody titer against rabies must be equal to or greater than 0.5 IU/ml. If the antibody titer is less than 0.5 IU/ml, the dog or cat must be retested.

                        - Blood sample for the test must be drawn after the second rabies vaccination and within the effective period of the rabies vaccination. The second rabies vaccination and blood sampling can be performed on the same day.

                         ''')
        with st.expander('Step 4: Waiting period (180 days or more)'):
                st.write('''
                        Dogs and cats are required to arrive in Japan after 180 days have passed from the date of blood sampling for the rabies antibody test. Dogs and cats whose waiting has passed less than 180 days will be subject to quarantine at a detention facility of Animal Quarantine Service for the period to make up the shortage.

                        In addition, the arrival date in Japan must be within the effective period of the rabies vaccine administered and within the validity period of the rabies antibody test--2 years from the date of blood sampling.
''')
                st.warning('''
                            - If unable to arrive in Japan within the validity period of the rabies antibody test, the second rabies antibody test must be carried out and the dog or cat must arrive in Japan within the validity period of the second test.
                            - If the following three conditions are all met, another 180-day waiting after the second test is not required.
                                1. The effective period from the first rabies vaccination continues until arrival in Japan with necessary additional rabies vaccinations.
                                2. The date of blood sampling for the second test is at least 180 days after the date of blood sampling for the first rabies antibody test.
                                3. The antibody titer is 0.5 IU/ml or more in all the tests.
                         ''', icon="⚠️")        
        with st.expander('Step 5: Advance notification (at least 40 days before arrival)'):
                st.write('''
                        - **Submitting Advance Notification**
                         
                            Applicants must notify Animal Quarantine Service at the expected port of entry not less than 40 days before arrival in Japan.

                            You can submit the notification form by mail, fax, or e-mail. Or notification can be made online through the [NACCS](https://www.maff.go.jp/aqs/tetuzuki/system/49.html).
                         
                            Please find the notification form below:
                            - Notification form for dogs（[PDF](https://www.maff.go.jp/aqs/english/animal/dog/pdf/notifi-dog20210721.pdf), [EXCEL](https://www.maff.go.jp/aqs/animal/dog/attach/notifi-dog20210824.xlsx))
                            - Notification form for cats（[PDF](https://www.maff.go.jp/aqs/english/animal/dog/pdf/notifi-cat20210721.pdf), [EXCEL](https://www.maff.go.jp/aqs/animal/dog/attach/notifi-cat20210824.xlsx))
''')
                st.info('''
                            For more information:                     
                            - [How to fill in the notification (dogs and cats)](https://www.maff.go.jp/aqs/english/animal/dog/pdf/notifi-dogcat-en20210721.pdf)
                            - [Contact of Animal Quarantine Service at airport or seaport](https://www.maff.go.jp/aqs/english/attach/pdf/aqs_contact_list_en.pdf)
                            - FAX transmission cover page ([PDF](https://www.maff.go.jp/aqs/english/animal/dog/attach/pdf/import-free-1.pdf), [Word](https://www.maff.go.jp/aqs/english/animal/dog/attach/doc/import-other-1.docx))

                         ''')
                st.write('''
                        - **Approval of Import Inspection of Animals**

                            Animal Quarantine Service will examine the Notification Submission and related documents to issue an Approval of Import Inspection of Animals. 
                                                    
                            For export or boarding procedures, please print or save digitally the issued form.
                                                
                        - **Modification on notification**

                            In case of any changes in the notification, you need to submit a Modification on Notification of Import of Animals([PDF](https://www.maff.go.jp/aqs/english/animal/dog/pdf/modnotifi20210721.pdf), [EXCEL](https://www.maff.go.jp/aqs/animal/dog/attach/modnotifi20210824.xlsx)) by mail, fax, or e-mail to Animal Quarantine Service.

                            In case you submitted the notification via NACCS, modification must be made through [NACCS](https://www.maff.go.jp/aqs/tetuzuki/system/49.html).
                        ''' )
                st.warning('''
                Modifications of ‘moving up arrival date after submitting the notification’, ‘increasing the number of heads’, ‘replacing with different animals’, and ‘any change after the scheduled arrival date’ are not accepted in principle.
''',icon="⚠️")
        with st.expander('Step 6: Clinical inspection before departure (pre-export inspection)'):
                st.write('''
                Before leaving the exporting country, dogs and cats must undergo a clinical inspection by a veterinarian.
                - Dogs and cats have been found to be free from any clinical signs of rabies.
                - In case of dogs, also the dogs have been found to be free from any clinical signs of leptospirosis.

                         ''')
        with st.expander('Step 7: Obtaining certificates issued by the government agency of the exporting country'):
                st.write('''
                            **Required information in the certificates**:

                            1. Individual information (including date of birth or age)
                            2. Microchip number and date of implanting 【Step 1】
                            3. Date of rabies vaccinations, effective period, kind of vaccine, product name and manufacturer of vaccine 【Step 2】
                            4. Date of blood sampling for a rabies antibody test, antibody titer, and name of designated laboratory 【Step 3】
                            5. Result and date of clinical inspection (pre-export inspection) 【Step 6】


                         ''')
                st.info('''
                        It is recommended to use Form AC ([PDF](https://www.maff.go.jp/aqs/english/animal/dog/attach/pdf/import-other-5.pdf), [EXCEL](https://www.maff.go.jp/aqs/english/animal/dog/attach/other/import-other-4.xlsm)) as the certification form to make it possible for the importer to fill in the required information without any omissions.

                        If you need more pages, fill in the ATTACH form ([PDF](https://www.maff.go.jp/aqs/english/animal/dog/attach/pdf/import-other-2.pdf), [EXCEL](https://www.maff.go.jp/aqs/english/animal/dog/attach/other/import-other-3.xlsm)) in a same manner, and attach it to Form AC.
''')
                st.warning('''
                            - Do not use pencils or erasable ink to fill in the certificates.
                            - Use of correcting fluid or correction tape is not acceptable.
                            - If there are any deficiencies in the certificates, the dog or cat will be subject to detention quarantine for up to 180 days or will be shipped back. In order to prevent any errors in the certificates, we recommend you to send copy of the certificates to us in advance so that we check them.
''',icon="⚠️")
        with st.expander('Step 8: Import inspection'):
                st.write('''
                        Dogs and cats must be inspected by Animal Quarantine Service upon arrival in Japan. Importer must apply for import inspection to Animal Quarantine Service upon arrival in Japan. 
                         
                        If no problems are found in the import inspection, we will issue an import quarantine certificate for the dog or cat. In case that the dog or cat doesn't meet import requirements, it will be subject detention quarantine for up to 180 days or will be returned.
                         
                        **Documents required**:
                         
                        - Approval of Import Inspection of Animals
                            - Application form for dogs ([PDF](https://www.maff.go.jp/aqs/animal/dog/pdf/appli-im-dog20210721.pdf), [EXCEL](https://www.maff.go.jp/aqs/animal/dog/attach/appli-im-dog20210824.xls))
                            - Application form for cats ([PDF](https://www.maff.go.jp/aqs/animal/dog/pdf/appli-im-cat20210721.pdf), [EXCEL](https://www.maff.go.jp/aqs/animal/dog/attach/appli-im-cat20210824.xls))
                        - Certificates issued by the government agency of the exporting country (original) 【Step 7】
                        - Result report of rabies antibody test 【Step 3】
                        - (For cargo transportation) A copy of Air Way Bill or Bill of lading
                        - (If the import procedure is conducted on behalf of the owner) [Letter of Authorization](https://www.maff.go.jp/aqs/english/animal/dog/pdf/power_of_attorney20210721.pdf)
                        - Other documents required by Animal Quarantine Service
                         ''')

        st.write('''         
            For more information, please visit the [Japan Animal Quarantine Service](https://www.maff.go.jp/aqs/english/animal/dog/import-other.html).
        ''')                  
    if country == "Europe":
            st.write('''
            Please allow for **at least 1 month** to prepare for your pet's travel to Europe.
                     ''')
            with st.expander('Step 1: Marking / Microchip implanting'):
                st.write('''
                The pet animal (dog, cat or ferret) must be marked by the implantation of a transponder. See technical specifications in [Annex II to Regulation (EU) No 576/2013](https://eur-lex.europa.eu/eli/reg/2013/576/oj#d1e32-21-2)
                         ''')
            with st.expander('Step 2: Vaccination against rabies'):
                st.write('''
                The pet animal (dog, cat or ferret) must be vaccinated against rabies by an authorised veterinarian in accordance with Annex III to Regulation (EU) No 576/2013, as follows:

                - The animal was at least 12 weeks old at the date the vaccine was administered
                - The date of administration of the vaccine does not precede the date of marking or reading of the transponder
                - The period of validity of the vaccination starts not less than 21 days from the completion of the vaccination protocol for the primary vaccination, and any subsequent vaccination was carried out within the period of validity of the preceding vaccination
                         ''')
            with st.expander('(Dogs only): Treatment against Echinococcus multilocularis'):
                st.write('''
                        The pet animal (dog only) must, prior to entering a Member State listed in the Annex to Commission Implementing Regulation (EU) 2018/878, or Norway, be treated against the parasite Echinococcus multilocularis in accordance with Commission Delegated Regulation (EU) 2018/772, as follows:
                        - The treatment must be administered by a veterinarian within a period of not more than 120 hours and not less than 24 hours before the time of scheduled entry
                        - The treatment must be certified by the administering veterinarian in the relevant section of the passport.
                         ''')
            with st.expander('Step 3: Health Certificate and Declaration'):
                st.write('''
                The pet animal (dog, cat or ferret) must be accompanied by:
            - [An animal health certificate](https://food.ec.europa.eu/document/download/a8648cd3-a77a-4b29-b1d4-679d584d2f0c_en?filename=pm_eu-reg_animal-health-certificate_en.doc)
            - [A written declaration](https://food.ec.europa.eu/document/download/64702643-8d8c-476b-8aa4-bb21b10c6437_en?filename=pm_eu-reg_animal-health-certificate_annex-3_en.doc) completed by the owner or an authorised person regarding the non-commercial nature of the movement and attesting, where appropriate, the carriage of the animal under the responsibility of an authorised person within up to five days of the movement of the owner.
                         ''')
            with st.expander("Step 4: Travellers' point of entry"):
                st.write('''            
            The pet animal (dog, cat or ferret) must pass through a travellers' point of entry designated by Member States. The owner must, at the time of entry, contact the competent authority present at the point of entry for the purposes of the documentary and identity checks.
                ''')
            st.write('''         
                For more information, please visit the [EU regulation of Non-commercial Movement](https://food.ec.europa.eu/animals/movement-pets/eu-legislation/non-commercial-movement-non-eu-countries_en).
            ''')         
    if country == "U.S.":
        st.write('''
                 There are not as many restrictions to transport your pet to the U.S. as to Japan or Europe. However, you will need to check the requirements of the specific state you are traveling to. 
                 
                 Below are the U.S. federal departments that regulate the importation of pets and links to the state requirements:
                 ''')
        with st.expander('Animal and Plant Health Inspection Service - Veterinary Services'):
            st.write('''
              [APHIS Veterinary Services](https://www.aphis.usda.gov/pet-travel/another-country-to-us-import/cats) does not have any animal health requirements related to bringing (importing) a pet cat into the United States from a foreign country. 
                     
                See below to view other requirements for bringing pet cats into the United States from another country.
            ''')
        with st.expander('Centers for Disease Control and Prevention'):
            st.write('''
                    - Domestic cats are subject to **inspection at ports of entry**.

                        A general certificate of health is not required by CDC for entry of domestic cats into the United States, although some airlines or states may require them. However, cats are subject to inspection at ports of entry and may be denied entry into the United States if they have evidence of an infectious disease that can be transmitted to humans. If a cat appears to be ill, further examination by a licensed veterinarian at the owner's expense might be required at the port of entry.

                    - Cats are not required to have proof of rabies vaccination for importation into the United States. However, CDC **recommends that all cats be vaccinated against rabies**, and your [US destination](https://www.nasda.org/about-nasda/state-agriculture-departments/) may have additional requirements.

                    - All pet cats arriving in the [state of Hawaii](http://hawaii.gov/hdoa/ai/aqs/info) and the [territory of Guam](http://ns.gov.gu/pets.html), even from the US mainland, are subject to locally imposed quarantine requirements.
                     ''')
            st.info('''
                    Source: [Centers for Disease Control and Prevention](https://www.cdc.gov/importation/bringing-an-animal-into-the-united-states/cats.html) 
                     ''')
        with st.expander('U.S. Fish and Wildlife Service'):
            st.write('''
                    If you are traveling abroad with a personal pet, you will probably need to obtain a permit if your pet is exotic (not a dog or cat). This is an application for one-time import, export, or re-export of any CITES-listed pet, including birds.  
 
                    If you are a resident of the United States and you will be making multiple border crossings, we recommend applying for the pet passport ([Form 3-200-64](https://www.fws.gov/service/3-200-64-certificate-ownership-personally-owned-wildlife-pet-passport-under-cites)).  
                    ''')
            st.info('''
                    Please visit the [U.S. Fish and Wildlife Service](https://www.fws.gov/service/3-200-46-importexportre-export-personal-pets-under-cites-and-or-wbca) for more information.
                     ''')
        with st.expander('U.S. State and Territory Requirements'):
            st.write('''
                    Domestic movement requirements are set by the receiving State or Territory.

                    Visit the [National Association of State Departments of Agriculture](https://www.nasda.org/about-nasda/state-agriculture-departments/) to find your destination's agriculture department and check its website for requirements.
                    ''')
            st.info('''
                    For questions or clarification on any of the requirements, contact the [State or Territorial veterinarian's office](https://www.usaha.org/saho).

                     ''')
    st.write(f'''
             #### 2. Here are some airline options to transport your pet in {method}:
                ''')
    if method == "Carry-on":
        st.write('''
                Although these airlines do allow pets travel as carry-ons, they are likely to have the specific requirements for boarding. Links to the airlines' pet policies are provided below:
                ''')
        # make each row contain three link buttons
        col1, col2, col3 = st.columns(3)


        for x in range(len(df)//3):
            with col1:
                st.link_button(f"{df['title'][x]}",f"{df['url'][x]}")
            with col2:
                st.link_button(f"{df['title'][x+1]}",f"{df['url'][x+1]}")
            with col3:
                st.link_button(f"{df['title'][x+2]}",f"{df['url'][x+2]}")
            
        # for i in range(len(df)):
        #     if df['travel_method'][i] == "cabin":
        #         st.link_button(f"{df['title'][i]}",f"{df['url'][i]}")
    if method == "Cargo hold":
        st.write('''
                If you are planning to transport your pet in the cargo hold, please check with the airline for the specific requirements. 
                ''')
        

    # if country = "Australia":

    # timeleft = d - today
    #     if timeleft.days < 0:
    #         st.write(f'''
    #             ### You are already late! You should have left {abs(timeleft.days)} days ago!
    #             ''')
    #     else:
    #         st.write(f'''
    #                 ### You have {timeleft.days} days left to plan your trip!
    #                 ''')




    
        # values = st.slider(
        #     'Please list your budget per pet in USD',
        #     0, 100, (25, 75))

# st.page_link("app.py")
# st.page_link("pages/page_1.py")
# st.page_link("pages/page_2.py")
# st.page_link("http://www.google.com")