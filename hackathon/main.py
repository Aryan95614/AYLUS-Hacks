import PySimpleGUI as sg
import os, sys
from hackathon.body import window, country
from playsound import playsound
import multiprocessing
import time
import keyboard

b = list()


def func1():
    playsound("images/piano-moment-9835.wav")


def func2(process1):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    join = lambda x, y: os.path.join(x, y)
    allcountries: list = ['USA', 'India', 'Brazil', 'UK', 'Russia', 'Turkey', 'France', 'Germany', 'Iran', 'Spain',
                          'Argentina', 'Italy', 'Colombia', 'Indonesia', 'Poland', 'Mexico', 'Ukraine', 'South Africa',
                          'Netherlands', 'Philippines', 'Malaysia', 'Czechia', 'Peru', 'Thailand', 'Iraq', 'Belgium',
                          'Canada',
                          'Romania', 'Chile', 'Japan', 'Bangladesh', 'Vietnam', 'Israel', 'Pakistan', 'Serbia',
                          'Sweden',
                          'Austria', 'Portugal', 'Hungary', 'Switzerland', 'Jordan', 'Greece', 'Kazakhstan', 'Cuba',
                          'Morocco', 'Georgia', 'Nepal', 'Slovakia', 'UAE', 'Bulgaria', 'Tunisia', 'Lebanon', 'Belarus',
                          'Croatia', 'Ireland', 'Guatemala', 'Azerbaijan', 'Denmark', 'Sri Lanka', 'Costa Rica',
                          'Bolivia',
                          'S. Korea', 'Saudi Arabia', 'Ecuador', 'Myanmar', 'Lithuania', 'Panama', 'Paraguay',
                          'Slovenia',
                          'Venezuela', 'Palestine', 'Kuwait', 'Dominican Republic', 'Uruguay', 'Mongolia', 'Libya',
                          'Honduras', 'Ethiopia', 'Egypt', 'Moldova', 'Norway', 'Armenia', 'Oman',
                          'Bosnia and Herzegovina',
                          'Bahrain', 'Singapore', 'Latvia', 'Kenya', 'Australia', 'Qatar', 'Estonia', 'Nigeria',
                          'North Macedonia', 'Zambia', 'Algeria', 'Finland', 'Albania', 'Botswana', 'Uzbekistan',
                          'Zimbabwe', 'Kyrgyzstan', 'Montenegro', 'Mozambique', 'Afghanistan', 'Cyprus', 'Namibia',
                          'Ghana',
                          'Uganda', 'El Salvador', 'Cambodia', 'Cameroon', 'Rwanda', 'China', 'Laos', 'Luxembourg',
                          'Maldives', 'Jamaica', 'Trinidad and Tobago', 'Senegal', 'RÃ©union', 'Angola', 'DRC',
                          'Malawi',
                          'Ivory Coast', 'Eswatini', 'Guadeloupe', 'Fiji', 'Suriname', 'Syria', 'French Guiana',
                          'Martinique', 'French Polynesia', 'Madagascar', 'Sudan', 'Malta', 'Mauritania', 'Guyana',
                          'Cabo Verde', 'Gabon', 'Papua New Guinea', 'Belize', 'Guinea', 'Barbados', 'Togo', 'Tanzania',
                          'Haiti', 'Benin', 'Lesotho', 'Seychelles', 'Somalia', 'Bahamas', 'Mauritius',
                          'Channel Islands',
                          'Burundi', 'Mayotte', 'Andorra', 'Iceland', 'Timor-Leste', 'Mali', 'Congo', 'CuraÃ§ao',
                          'Nicaragua', 'Tajikistan', 'Taiwan', 'Aruba', 'Burkina Faso', 'Brunei', 'Equatorial Guinea',
                          'Djibouti', 'New Zealand', 'South Sudan', 'Saint Lucia', 'Isle of Man', 'Hong Kong',
                          'New Caledonia', 'CAR', 'Yemen', 'Gambia', 'Cayman Islands', 'Gibraltar', 'Eritrea', 'Niger',
                          'San Marino', 'Sierra Leone', 'Guinea-Bissau', 'Dominica', 'Grenada', 'Liberia', 'Bermuda',
                          'St. Vincent Grenadines', 'Chad', 'Liechtenstein', 'Sint Maarten', 'Comoros',
                          'Faeroe Islands',
                          'Monaco', 'Antigua and Barbuda', 'Saint Martin', 'Sao Tome and Principe',
                          'Caribbean Netherlands',
                          'Turks and Caicos', 'British Virgin Islands', 'Saint Kitts and Nevis', 'Bhutan', 'Greenland',
                          'St. Barth', 'Anguilla', 'Diamond Princess', 'Wallis and Futuna', 'Saint Pierre Miquelon',
                          'Falkland Islands', 'Macao', 'Montserrat', 'Vatican City', 'Solomon Islands',
                          'Western Sahara',
                          'MS Zaandam', 'Palau', 'Vanuatu', 'Marshall Islands', 'Samoa', 'Saint Helena', 'Micronesia',
                          'Tonga']

    layout = [[sg.Text("Which Country are you from?")],
              [sg.Combo(allcountries, size=(18, 9), enable_events=True, key='-COMBO-')],
              [sg.Button('Ok')]]

    win = window("Pandemic Regulation Checker", layout=layout)

    Thing = country(str(win.runLoop(allcountries)['-COMBO-']))

    Country, totalcases, totalpop, activecases, tests, per = Thing.findInfo().returnList()
    del layout, win
    Thing.close_Window()

    layout = [[sg.Text(f"Country:\t{Country}", size=(30, 2), key='-text-')],
              [sg.Text("-------------------")],
              [sg.Text(f"The Current Infected Cases are:\t{activecases} people.")],
              [sg.Text(f"The Total Cases are:\t{totalcases} people.")],
              [sg.Text(f"The Tests the country has done with them is:\t{tests}")],
              [sg.Text(f"The Total Population is:\t{totalpop} people.")],
              [sg.Text(f"The Tests per One million people are:\t{per}")],
              [sg.Text("-------------------")],
              [sg.Text(" This is the General Graph Right Now")],
              [sg.Image(join("images", "info.png"))],
              [sg.Text("-------------------")],
              [sg.Text(" Please stay safe and don't let the Omicron hurt you! ")],
              [sg.Button("Ok")]]

    win = window("New information and Latest news", layout=layout)
    win.runloop()
    process1.terminate()




if __name__ == '__main__':
    start = time.time()
    process1 = multiprocessing.Process(target=func1, args=())
    process1.start()
    process2 = multiprocessing.Process(target=func2(process1), args=())
    process2.start()
