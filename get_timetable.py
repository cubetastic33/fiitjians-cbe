import bs4
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, db

#Firebase Initialization
cred = credentials.Certificate('fiitjians-cbe-firebase-adminsdk-4wll8-990da6329d.json')
default_app = firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://fiitjians-cbe.firebaseio.com'
})

table9A1 = ['''
<table id="cphMaster_clblContent2" class="CSSTableGenerator" cellspacing="10">
        <tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
          <td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
        </tr><tr>
          <td>COIF71A01</td><td>16:10-
17:30</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>09:00-
10:00</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:00-
10:45</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:55-
11:40</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>11:40-
12:25</td><td>HPT</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>14:25-
15:10</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>15:10-
15:55</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>12:50-
13:35</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>13:35-
14:10</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr>
      </table>
  ''',
  '''
<table id="cphMaster_clblContent3" class="CSSTableGenerator" cellspacing="10">
        <tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
          <td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
        </tr><tr>
          <td>COIF71A01</td><td>12:50-
13:35</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>16:10-
17:30</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>15:10-
15:55</td><td>HPT</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>09:00-
10:00</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:00-
10:45</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:55-
11:40</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>13:35-
14:10</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>11:40-
12:25</td><td>PET</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>14:25-
15:10</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr>
      </table>
  ''',
  '''
<table id="cphMaster_clblContent4" class="CSSTableGenerator" cellspacing="10">
        <tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
          <td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
        </tr><tr>
          <td>COIF71A01</td><td>12:50-
13:35</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>13:35-
14:10</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>14:25-
15:10</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>15:10-
15:55</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:55-
11:40</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>11:40-
12:25</td><td>HPT</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>09:00-
10:00</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:00-
10:45</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>16:10-
17:30</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr>
      </table>
  ''',
  '''
<table id="cphMaster_clblContent5" class="CSSTableGenerator" cellspacing="10">
        <tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
          <td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
        </tr><tr>
          <td>COIF71A01</td><td>12:50-
13:35</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>15:10-
15:55</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>16:10-
17:30</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>13:35-
14:20</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>11:40-
12:25</td><td>LAN</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>14:25-
15:10</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>09:00-
10:00</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:00-
10:45</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:55-
11:40</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr>
      </table>
  ''',
  '''
<table id="cphMaster_clblContent6" class="CSSTableGenerator" cellspacing="10">
        <tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
          <td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
        </tr><tr>
          <td>COIF71A01</td><td>09:00-
10:00</td><td>MRJ</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:00-
10:45</td><td>PCM</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>10:55-
11:40</td><td>SS</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>11:40-
12:25</td><td>HPT</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>12:50-
13:35</td><td>BSR</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>13:35-
14:20</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>14:25-
15:10</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
        </tr><tr>
          <td>COIF71A01</td><td>15:10-
15:55</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
        </tr>
      </table>
  ''']

table9B = ['''
<table id="cphMaster_clblContent1" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:00-
10:45</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>14:25-
15:10</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:55-
11:40</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>15:10-
15:55</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>11:40-
12:25</td><td>FRM</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>12:50-
14:10</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>09:00-
10:00</td><td>SS</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent2" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COSL78A01</td><td>13:35-
14:10</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>14:25-
15:10</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>09:00-
10:00</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>15:10-
15:55</td><td>FRM</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>11:40-
12:25</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:55-
11:40</td><td>PRB</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:00-
10:45</td><td>SS</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>12:50-
13:35</td><td>SS</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent3" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COSL78A01</td><td>15:10-
15:55</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>12:50-
14:10</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>11:40-
12:25</td><td>FRM</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>09:00-
10:45</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:55-
11:40</td><td>PRB</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>14:25-
15:10</td><td>PRB</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent4" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COSL78A01</td><td>09:00-
10:00</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>12:50-
13:35</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:00-
10:45</td><td>LAN</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>13:35-
14:20</td><td>PET</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>14:25-
15:55</td><td>PRB</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:55-
12:25</td><td>SS</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent5" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COSL78A01</td><td>09:00-
10:45</td><td>BMK</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>14:25-
15:10</td><td>CRA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>15:10-
15:55</td><td>EVL</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>11:40-
12:25</td><td>LAN</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>12:50-
14:20</td><td>MNS</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COSL78A01</td><td>10:55-
11:40</td><td>PRB</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''']

table11A3 = ['''
<table id="cphMaster_clblContent1" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:55-
11:40</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>15:10-
15:55</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>16:10-
17:30</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>09:00-
10:45</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>14:25-
15:10</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>11:40-
12:25</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>12:50-
14:10</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent2" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COIT79A03</td><td>15:10-
15:55</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>16:10-
17:30</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:55-
12:25</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>12:50-
13:35</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>09:00-
10:45</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>13:35-
14:10</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>14:25-
15:10</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent3" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:55-
12:25</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>14:25-
15:10</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>12:50-
14:10</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>15:10-
15:55</td><td>MJG</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>09:00-
10:45</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>16:10-
17:30</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent4" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COIT79A03</td><td>09:00-
10:00</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>12:50-
14:20</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:00-
10:45</td><td>MVCA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>14:25-
15:55</td><td>MVCA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:55-
12:25</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>16:10-
17:30</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''',
'''
<table id="cphMaster_clblContent5" class="CSSTableGenerator" cellspacing="10">
				<tr style="border-style:Solid;font-family:Calibari;font-weight:bold;">
					<td>Batch-Code</td><td>Timing</td><td>Faculty</td><td>Description</td><td>Venue</td>
				</tr><tr>
					<td>COIT79A03</td><td>13:35-
14:20</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>15:10-
15:55</td><td>CVR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>10:55-
12:25</td><td>MVCA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>12:50-
13:35</td><td>MVCA</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>09:00-
10:45</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr><tr>
					<td>COIT79A03</td><td>14:25-
15:10</td><td>PGR</td><td></td><td>SUGUNA PIP</td>
				</tr>
			</table>
''']

subject9A1 = {
  'MRJ': 'Mathematics',
  'BSR': 'Biology',
  'CRA': 'Chemistry',
  'PCM': 'Physics',
  'SS<': 'Social Studies',
  'TSM': 'Language',
  'HPT': 'Language',
  'FRM': 'Language',
  'LAN': 'Language',
  'EVL': 'English',
  'MNS': 'MAT',
  'PET': 'Games :)',
  'ART': 'Art :)',
  'YOG': 'Yoga :('
}

subject9B = {
  'MNS': 'Mathematics/MAT',
  'BMK': 'Biology',
  'CRA': 'Chemistry',
  'PRB': 'Physics',
  'PCM': 'Physics',
  'SS<': 'Social Studies',
  'TSM': 'Language',
  'HPT': 'Language',
  'FRM': 'Language',
  'LAN': 'Language',
  'EVL': 'English',
  'PET': 'Games :)',
  'ART': 'Art :)',
  'YOG': 'Yoga :('
}

subject11A3 = {
  'MJG': 'Mathematics MJG',
  'CVR': 'Chemistry',
  'PGR': 'Physics',
  'MVC': 'Mathematics MVCA',
  'EVL': 'English',
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

contributor = {
  '9 A1': 'Aravindan',
  '9 B': 'Aditya Radhakrishnan',
  '11 A3': 'Nirmal Karthikeyan'
}

def organiseTable(raw_html, subjects):
  table_rows = [
    'Unable to find 1st period',
    'Unable to find 2nd period',
    '<tr class="break"><td>10:45-10:55</td><td>Break</td></tr>',
    'Unable to find 3rd period',
    'Unable to find 4th period',
    '<tr class="break"><td>12:25-12:50</td><td>Lunch</td></tr>',
    'Unable to find 5th period',
    'Unable to find 6th period',
    '<tr class="break"><td>2:15-2:25</td><td>Break</td></tr>',
    'Unable to find 7th period',
    'Unable to find 8th period'
  ]
  pageSoup = BeautifulSoup(raw_html, 'html.parser')
  for row in pageSoup.find_all('tr'):
    if str(row).find('Timing') > -1:
      pass
    elif str(row).find('9:00-\n10:00') > -1:
      start_index = str(row).find('00</td><td>')
      print('1st')
      table_rows[0] = '<tr><td>9:00-10:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:00-\n10:45') > -1:
      start_index = str(row).find('45</td><td>')
      print('2nd')
      table_rows[1] = '<tr><td>10:00-10:45</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('9:00-\n10:45') > -1:
      start_index = str(row).find('45</td><td>')
      print('1st and 2nd')
      table_rows[0] = '<tr><td>9:00-10:00</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[1] = '<tr><td>10:00-10:45</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:55-\n11:40') > -1:
      start_index = str(row).find('40</td><td>')
      print('3rd')
      table_rows[3] = '<tr><td>10:55-11:40</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('11:40-\n12:25') > -1:
      start_index = str(row).find('25</td><td')
      print('4th')
      table_rows[4] = '<tr><td>11:40-12:25</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('10:55-\n12:25') > -1:
      start_index = str(row).find('25</td><td>')
      print('3rd and 4th')
      table_rows[3] = '<tr><td>10:55-11:40</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[4] = '<tr><td>11:40-12:25</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('12:50-\n13:35') > -1:
      start_index = str(row).find('35</td><td>')
      print('5th')
      table_rows[6] = '<tr><td>12:50-1:35</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:35-\n14:20') > -1:
      start_index = str(row).find('20</td><td')
      print('6th')
      table_rows[7] = '<tr><td>1:35-2:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('13:35-\n14:10') > -1:
      start_index = str(row).find('10</td><td')
      print('6th')
      table_rows[7] = '<tr><td>1:35-2:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('12:50-\n14:20') > -1:
      start_index = str(row).find('20</td><td>')
      print('5th and 6th')
      table_rows[6] = '<tr><td>12:50-1:35</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[7] = '<tr><td>1:35-2:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('12:50-\n14:10') > -1:
      start_index = str(row).find('10</td><td>')
      print('5th and 6th')
      table_rows[6] = '<tr><td>12:50-1:35</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[7] = '<tr><td>1:35-2:15</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('14:25-\n15:10') > -1:
      start_index = str(row).find('10</td><td>')
      print('7th')
      table_rows[9] = '<tr><td>2:25-3:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('15:10-\n15:55') > -1:
      start_index = str(row).find('55</td><td')
      print('8th')
      table_rows[10] = '<tr><td>3:10-3:55</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('14:25-\n15:55') > -1:
      start_index = str(row).find('55</td><td>')
      print('7th and 8th')
      table_rows[9] = '<tr><td>2:25-3:10</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
      table_rows[10] = '<tr><td>3:10-3:55</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>'
    elif str(row).find('16:10-\n17:30') > -1:
      start_index = str(row).find('30</td><td')
      print('9th')
      table_rows.append('<tr class="break"><td>3:55-4:10</td><td>Break</td></tr>')
      table_rows.append('<tr><td>4:10-5:30</td><td>' + subjects[str(row)[(start_index + 11):(start_index + 14)]] + '</td>')
    else:
      print('idk')
  return table_rows

timetables = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def get_timetables(ip_address):
  print('Ip Address: ', ip_address)
  for i in range(0, len(table9A1)):
    class_name = str(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())
    timetables[i] = organiseTable(all_tables[class_name][i], all_subjects[class_name])
  return timetables

def get_class(ip_address):
  print(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())
  return str(db.reference('ipAddresses/' + str(ip_address).replace('.', ' ')).get())

def get_contributor(ip_address):
  return contributor[get_class(ip_address)]
