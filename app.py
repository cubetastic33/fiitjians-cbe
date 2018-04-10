from flask import Flask, render_template, request, send_from_directory, jsonify
import get_timetable
import projects

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

@app.route('/timetable.html', methods=['GET'])
def timetable_html():
  return render_template('timetable.html', my_class = get_timetable.get_class(get_ipaddr()), timetables = get_timetable.get_timetables(get_ipaddr()))

@app.route('/projects.html')
def projects_html():
  return render_template('projects.html')

@app.route('/calculate', methods=['GET'])
def calculate_ajax():
  x, steps = projects.euclids_algorithm(int(request.args.get('number1')), int(request.args.get('number2')))
  y = projects.find_lcm(int(request.args.get('number1')), int(request.args.get('number2')))
  #z = projects.find_factors(int(request.args.get('number1')))
  print(steps)
  return jsonify({'hcf': x, 'lcm': y, 'steps': steps})

@app.route('/find_prime_factors', methods=['GET'])
def find_prime_factors_ajax():
  return jsonify({'prime_factors': projects.find_prime_factors(int(request.args.get('number1')))})

@app.route('/memes.html')
def memes_html():
  return render_template('memes.html')

@app.route('/upload.html')
def upload_html():
  return render_template('upload.html')

@app.route('/profile.html')
def profile_html():
  return render_template('profile.html')

@app.route('/legal.html')
def legal_html():
  return render_template('legal.html')

@app.route('/signin.html')
def signin_html():
  return render_template('signin.html')

@app.route('/signup.html')
def signup_html():
  return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

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
