import bs4
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, db

#Firebase Initialization
cred = credentials.Certificate('fiitjians-cbe-firebase-adminsdk-4wll8-990da6329d.json')
default_app = firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://fiitjians-cbe.firebaseio.com'
})

table9A1 = db.reference('/timetables/9A1').get()

table9B = db.reference('/timetables/9B').get()

table11A3 = db.reference('/timetables/11A3').get()

soup_of_tables_9A1 = BeautifulSoup(str(table9A1), 'html.parser')
table9A1 = {
  'timetable1': str(soup_of_tables_9A1.find('table', {'id': 'cphMaster_clblContent1'})),
  'timetable2': str(soup_of_tables_9A1.find('table', {'id': 'cphMaster_clblContent2'})),
  'timetable3': str(soup_of_tables_9A1.find('table', {'id': 'cphMaster_clblContent3'})),
  'timetable4': str(soup_of_tables_9A1.find('table', {'id': 'cphMaster_clblContent4'})),
  'timetable5': str(soup_of_tables_9A1.find('table', {'id': 'cphMaster_clblContent5'}))
}

soup_of_tables_9B = BeautifulSoup(str(table9B), 'html.parser')
table9B = {
  'timetable1': str(soup_of_tables_9B.find('table', {'id': 'cphMaster_clblContent1'})),
  'timetable2': str(soup_of_tables_9B.find('table', {'id': 'cphMaster_clblContent2'})),
  'timetable3': str(soup_of_tables_9B.find('table', {'id': 'cphMaster_clblContent3'})),
  'timetable4': str(soup_of_tables_9B.find('table', {'id': 'cphMaster_clblContent4'})),
  'timetable5': str(soup_of_tables_9B.find('table', {'id': 'cphMaster_clblContent5'}))
}

soup_of_tables_11A3 = BeautifulSoup(str(table11A3), 'html.parser')
table11A3 = {
  'timetable1': str(soup_of_tables_11A3.find('table', {'id': 'cphMaster_clblContent1'})),
  'timetable2': str(soup_of_tables_11A3.find('table', {'id': 'cphMaster_clblContent2'})),
  'timetable3': str(soup_of_tables_11A3.find('table', {'id': 'cphMaster_clblContent3'})),
  'timetable4': str(soup_of_tables_11A3.find('table', {'id': 'cphMaster_clblContent4'})),
  'timetable5': str(soup_of_tables_11A3.find('table', {'id': 'cphMaster_clblContent5'}))
}

def exams(exam_name):
  if exam_name.find('(SC') > -1:
    return 'Science Revision Exam'
  elif exam_name.find('(S') > -1:
    return 'Social Science Revision Exam'
  elif exam_name.find('(E') > -1:
    return 'English Revision Exam'
  elif exam_name.find('(MA') > -1:
    return 'Mathematics Revision Exam'
  elif exam_name.find('(LA') > -1:
    return 'Language Revision Exam'
  else:
    return 'Error: No matching exam found. Please contact site admins.'

subject9A1 = {
  'MRJ': 'Mathematics',
  'BSA': 'Biology',
  'BJK': 'Biology',
  'CPM': 'Chemistry',
  'PCM': 'Physics',
  'SSA': 'Social Studies',
  'TSM': 'Language',
  'HPT': 'Language',
  'FRM': 'Language',
  'LAN': 'Language',
  'EPA': 'English',
  'EPK': 'English',
  'MNS': 'MAT',
  'PET': 'Games :)',
  'ART': 'Art :)',
  'YOG': 'Yoga :(',
  'OIF': 'Error: COIF71A01'
}

subject9B = {
  'BSA': 'Biology',
  'BJK': 'Biology',
  'CPM': 'Chemistry',
  'PSO': 'Physics',
  'SSA': 'Social Studies',
  'TSM': 'Language',
  'HPT': 'Language',
  'FRM': 'Language',
  'LAN': 'Language',
  'EPA': 'English',
  'EPK': 'English',
  'MNS': 'MAT',
  'PET': 'Games :)',
  'ART': 'Art :)',
  'YOG': 'Yoga :('
}

subject11A3 = {
  'MVC': 'Mathematics',
  'CVR': 'Chemistry',
  'PGR': 'Physics',
  'EVL': 'English',
  'IRN': 'Information Technology',
  'PAA': 'PAA (idk who this is)',
  'PET': 'Games :)'
}

all_tables = {
  '9 A1': table9A1,
  '9 B': table9B,
  '11 A3': table11A3
}

all_subjects = {
  '9 A1': subject9A1,
  '9 B': subject9B,
  '11 A3': subject11A3
}

exam_timetable = {
  '9 A1': [
    [
      '<tr><td>2:00-2:45</td><td>Social Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Social Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Social Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Social Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Social Exam</td></tr>'
    ],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>'],
    [
      '<tr><td>2:00-2:45</td><td>Mathematics Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Mathematics Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Mathematics Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Mathematics Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Mathematics Exam</td></tr>'
    ],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>'],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>']
  ],
  '9 B': [
    [
      '<tr><td>2:00-2:45</td><td>Social Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Social Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Social Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Social Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Social Exam</td></tr>'
    ],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>'],
    [
      '<tr><td>2:00-2:45</td><td>Mathematics Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Mathematics Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Mathematics Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Mathematics Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Mathematics Exam</td></tr>'
    ],
    ['Study holiday!'],
    ['Study holiday!']
  ],
  '11 A3': [
    [
      '<tr><td>2:00-2:45</td><td>Mathematics Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Mathematics Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Mathematics Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Mathematics Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Mathematics Exam</td></tr>'
    ],
    [
      '<tr><td>Morning</td><td>Ai<sup>2</sup>TS</td></tr>',
      '<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>'
    ],
    [
      '<tr><td>2:00-2:45</td><td>Chemistry Exam</td></tr>',
      '<tr><td>2:45-3:30</td><td>Chemistry Exam</td></tr>',
      '<tr><td>3:30-4:15</td><td>Chemistry Exam</td></tr>',
      '<tr><td>4:15-5:00</td><td>Chemistry Exam</td></tr>',
      '<tr><td>5:00-5:15</td><td>Chemistry Exam</td></tr>'
    ],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>'],
    ['<tr><td>2:00-5:15</td><td>Study holiday!</td></tr>']
  ]
}

def organiseTable(raw_html, subjects):
  print(raw_html)
  table_rows = [
    'Unable to find 1st period',
    'Unable to find 2nd period',
    '<tr class="grey darken-2 white-text"><td>10:30-10:40</td><td>Break</td></tr>',
    'Unable to find 3rd period',
    'Unable to find 4th period',
    'Unable to find 5th period',
    '<tr class="grey darken-2 white-text"><td>1:10-1:50</td><td>Lunch</td></tr>',
    'Unable to find 6th period',
    'Unable to find 7th period',
    'Unable to find 8th period'
  ]
  pageSoup = BeautifulSoup(raw_html, 'html.parser')
  for row in pageSoup.find_all('tr'):
    if str(row).find('Timing') > -1:
      pass
    elif str(row).find('STUDY LEAVE') > -1:
      table_rows = 'Study holiday!'
    elif str(row).find('9:00-\n12:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('1st, 2nd, 3rd, and 4th')
      table_rows[0] = '<tr><td>9:00-10:00</td><td>' + exams(str(row)[(start_index + 20):(start_index + 38)]) + '</td>'
      table_rows[1] = '<tr><td>10:00-10:45</td><td>' + exams(str(row)[(start_index + 20):(start_index + 38)]) + '</td>'
      table_rows[2] = '<tr><td>10:45-10:55</td><td>' + exams(str(row)[(start_index + 20):(start_index + 38)]) + '</td>'
      table_rows[3] = '<tr><td>10:55-11:40</td><td>' + exams(str(row)[(start_index + 20):(start_index + 38)]) + '</td>'
      table_rows[4] = '<tr><td>11:40-12:25</td><td>' + exams(str(row)[(start_index + 20):(start_index + 38)]) + '</td>'
    elif str(row).find('9:00-\n9:50') > -1:
      start_index = str(row).find('50</td><td>')
      print('1st')
      table_rows[0] = '<tr><td>9:00-9:50</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('9:50-\n10:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('2nd')
      table_rows[1] = '<tr><td>9:50-10:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('9:00-\n10:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('1st and 2nd')
      table_rows[0] = '<tr><td>9:00-9:50</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[1] = '<tr><td>9:50-10:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:40-\n11:20') > -1:
      start_index = str(row).find('20</td><td>')
      print('3rd')
      table_rows[3] = '<tr><td>10:40-11:20</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('11:20-\n12:00') > -1:
      start_index = str(row).find('00</td><td')
      print('4th')
      table_rows[4] = '<tr><td>11:20-12:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('12:00-\n12:40') > -1:
      start_index = str(row).find('40</td><td')
      print('5th')
      table_rows[5] = '<tr><td>12:20-12:40</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:40-\n12:00') > -1:
      start_index = str(row).find('00</td><td>')
      print('3rd and 4th')
      table_rows[3] = '<tr><td>10:40-11:20</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[4] = '<tr><td>11:20-12:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('11:20-\n12:40') > -1:
      start_index = str(row).find('00</td><td>')
      print('4th and 5th')
      table_rows[4] = '<tr><td>11:20-12:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[5] = '<tr><td>12:00-12:40</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:40-\n12:20') > -1:
      start_index = str(row).find('20</td><td>')
      print('3rd, 4th, and 5th')
      table_rows[3] = '<tr><td>10:40-11:20</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[4] = '<tr><td>11:20-12:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[5] = '<tr><td>12:00-12:20</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:10-\n13:50') > -1:
      start_index = str(row).find('50</td><td>')
      print('6th')
      table_rows[7] = '<tr><td>1:10-1:50</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:50-\n14:30') > -1:
      start_index = str(row).find('30</td><td')
      print('7th')
      table_rows[8] = '<tr><td>1:50-2:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('14:30-\n15:10') > -1:
      start_index = str(row).find('30</td><td')
      print('8th')
      table_rows[9] = '<tr><td>2:30-3:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:10-\n14:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('6th and 7th')
      table_rows[7] = '<tr><td>1:10-1:50</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[8] = '<tr><td>1:50-2:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:50-\n15:10') > -1:
      start_index = str(row).find('10</td><td>')
      print('7th and 8th')
      table_rows[8] = '<tr><td>1:50-2:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[9] = '<tr><td>2:30-3:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('12:10-\n15:10') > -1:
      start_index = str(row).find('10</td><td>')
      print('6th, 7th, and 8th')
      table_rows[7] = '<tr><td>1:10-1:50</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[8] = '<tr><td>1:50-2:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[9] = '<tr><td>2:30-3:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('15:20-\n16:10') > -1:
      start_index = str(row).find('10</td><td')
      print('9th')
      table_rows.append('<tr class="grey darken-2 white-text"><td>3:10-3:20</td><td>Break</td></tr>')
      table_rows.append('<tr><td>3:20-4:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>')
    elif str(row).find('16:10-\n17:00') > -1:
      start_index = str(row).find('00</td><td>')
      print('10th')
      table_rows.append('<tr><td>4:10-5:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>')
    elif str(row).find('15:20-\n17:00') > -1:
      start_index = str(row).find('00</td><td')
      print('9th and 10th')
      table_rows.append('<tr class="grey darken-2 white-text"><td>3:10-3:20</td><td>Break</td></tr>')
      table_rows.append('<tr><td>3:20-4:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>')
      table_rows.append('<tr><td>4:10-5:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>')
    else:
      print('idk')
  return table_rows

def newOrganiseTable(raw_html, subjects):
  print(raw_html)
  table_rows = [
    'Unable to find 1st period',
    'Unable to find 2nd period',
    'Unable to find 3rd period',
    'Unable to find 4th period'
  ]
  pageSoup = BeautifulSoup(raw_html, 'html.parser')
  for row in pageSoup.find_all('tr'):
    if str(row).find('Timing') > -1:
      pass
    elif str(row).find('STUDY') > -1:
      table_rows = 'Study holiday!'
    elif str(row).find('14:00-\n17:00') > -1:
      start_index = str(row).find('17:00</td><td></td><td>')
      print('1st, 2nd, 3rd, and 4th')
      table_rows[0] = '<tr><td>2:00-2:45</td><td>' + exams(str(row)[(start_index + 20):(start_index + 42)]) + '</td>'
      table_rows[1] = '<tr><td>2:45-3:30</td><td>' + exams(str(row)[(start_index + 20):(start_index + 42)]) + '</td>'
      table_rows[2] = '<tr><td>3:30-4:15</td><td>' + exams(str(row)[(start_index + 20):(start_index + 42)]) + '</td>'
      table_rows[3] = '<tr><td>4:15-5:00</td><td>' + exams(str(row)[(start_index + 20):(start_index + 42)]) + '</td>'
    elif str(row).find('14:00-\n14:45') > -1:
      start_index = str(row).find('45</td><td>')
      print('1st')
      table_rows[0] = '<tr><td>2:00-2:45</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('14:45-\n15:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('2nd')
      table_rows[1] = '<tr><td>2:45-3:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('14:00-\n15:30') > -1:
      start_index = str(row).find('30</td><td>')
      print('1st and 2nd')
      table_rows[0] = '<tr><td>2:00-2:45</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[1] = '<tr><td>2:45-3:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('15:30-\n16:15') > -1:
      start_index = str(row).find('15</td><td>')
      print('3rd')
      table_rows[2] = '<tr><td>3:30-4:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('16:15-\n17:00') > -1:
      start_index = str(row).find('00</td><td')
      print('4th')
      table_rows[3] = '<tr><td>4:15-5:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('15:30-\n17:00') > -1:
      start_index = str(row).find('00</td><td>')
      print('3rd and 4th')
      table_rows[2] = '<tr><td>3:30-4:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[3] = '<tr><td>4:15-5:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    else:
      print('idk')
  return table_rows


def get_timetables(ip_address):
  print('Ip Address: ', ip_address)
  timetables = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  for i in range(1, (len(table9A1) + 1)):
    class_name = str(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())
    timetables[i - 1] = organiseTable(all_tables[class_name]['timetable' + str(i)], all_subjects[class_name])
  return timetables

def get_class(ip_address):
  print(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())
  return str(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())
