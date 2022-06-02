from flask import Flask, render_template, request, redirect

app = Flask('app')

partidas = []

@app.route('/')
def index():
  return render_template(
    'index.html',
    partidas=partidas
  )
  
@app.route('/store', methods=['POST'])
def create():
  timeA = request.form.get('timeA')
  timeB = request.form.get('timeB')
  golsA = request.form.get('golsA')
  golsB = request.form.get('golsB')
  partidas.append({
    'timeA': timeA,
    'timeB': timeB,
    'golsA': golsA,
    'golsB': golsB
  })
  return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)