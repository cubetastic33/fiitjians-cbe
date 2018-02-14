from flask import Flask, render_template, request, send_from_directory, jsonify
import get_timetable

def get_ipaddr():
  """
  :return: the ip address for the current request (or 127.0.0.1 if none found)
    based on the X-Forwarded-For headers.
  """
  if request.access_route:
    return request.access_route[0]
  else:
    return request.remote_addr or '127.0.0.1'

app = Flask(__name__, static_url_path='/')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/index.html')
def index_html():
  return render_template('index.html')

@app.route('/classroom.html', methods=['GET'])
def classroom_html():
  return render_template('classroom.html', my_class = get_timetable.get_class(get_ipaddr()), contributor = get_timetable.get_contributor(get_ipaddr()), timetables = get_timetable.get_timetables(get_ipaddr()))

@app.route('/memes.html')
def memes_html():
  return render_template('memes.html')

@app.route('/chatDiv.html')
def chatDiv_html():
  return render_template('chatDiv.html')

@app.route('/profile.html')
def profile_html():
  return render_template('profile.html')

@app.route('/signin.html')
def signin_html():
  return render_template('signin.html')

@app.route('/signup.html')
def signup_html():
  return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/get_ip_address', methods=['POST'])
def get_ip_address():
  return get_ipaddr(), 200

@app.route('/js/<path:path>')
def send_js(path):
  return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
  return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
  return send_from_directory('images', path)

if __name__ == '__main__':
  app.run(debug = True)
 
