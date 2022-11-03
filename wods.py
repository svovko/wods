from random import randint, shuffle, sample
from Wendler import Wendler
from CrossFit import CrossFit

# accessory
'''
sled pushes
'''

accessory = {
    'biceps': ['DB Hammer curls', 'BB Biceps curls', 'TRX Biceps curls', 'Chinups'],

    'triceps': ['Banded triceps pulldown', 'OH DB Triceps extension', 'Skull crushers', 'TRX Triceps Extensions'],

    'shoulders': ['Sots Press', 'Seated DB press', 'Z Press', 'Strict HSPU', 'Unilateral KB Press', 'TGUs', 'Lu Flies',
                  'KB weighted BB Press', 'OH KB carry (Uni/Bi)', 'TRX Face pull', 'Y-W-T-PU-I (30s each) + Swimming'],

    'chest': ['Barbell Push ups', 'Push ups', 'Deficit pushups', 'Floor press', 'Dips', 'Floor flies (2 plates)',
              'TRX push ups', 'Ring push ups'],

    'abs': ['Single Arm Farmers carry', 'Farmers walk', 'Evil Wheels', 'GHDSU', 'Plank (alt. sides)', 'Plank',
            'Hollow rock', 'L-sit', 'Suitcase DL', 'KB Waiter Squat',
            'Russian twists', 'Front rack KB carry', 'Plank rollouts (stability ball)', 'TRX crunches', 'Pegwall hold', 
            'DBall carry'], 

    'back': ['DB/KB Row', 'Bent over row', 'Pendlay row', 'Plate fly', 'Strict Pullups', 'Back Extensions', 'TRX row',
             'Back Ext. Hold'],

    'legs': ['BB Glute Bridges', 'Goodmornings', 'Glute Ham Raises (on GHD)', 'Decline Squat', 'KB/DB Lunges',
             'Bulgarian Split Squat', 'High Box Jumps', 'Hamstring curl (stability ball)']
            }

WL_accessory =  {
                    'Snatch': ['Snatch Grip DL', 'Snatch Grip Press', 'High Pull', 'Muscle Snatch', 'Power Snatch', 'Snatch Pull', 'Snatch Ballance', 'Dip Snatch', 'Drop Snatch', 'Hang Snatch'],
                    'Clean & Jerk': ['Jerk from Rack', 'Clean pull', 'Power Clean', 'Clean Grip DL', 'Hang Clean', 'Jerk Dips']
                }

def generateWL(i, f):
    wl = WL()
    f.write('<h4>Weightlifting - ' + wl.getWorkoutName()+'</h4>')
    f.write('''
    <table class="table table-sm">
      <thead>
        <tr>
          <th>Name</th>
          <th>Warmup</th>
          <th>Main</th>
        </tr>
      </thead>
      <tbody>''')
    for user in usersWL:
        f.write('''
        <tr>
          <th>'''+user+'''</th>
        ''')
        wl.printWorkout(usersWL[user][i%2], f)
        f.write('</tr>')
        
    f.write('</tbody>')
    f.write('</table><br>')

    if (i+1) % 4 == 0: # on light clean day, perform FS - HS
        f.write('<h5> + Front Squat 3 x 3 @ 85% or HS</h5><br>')

def generateStrength1(i, f):
    w = Wendler()
    f.write('<h4>Strength - '+w.getWorkoutName()+'</h4>')
    f.write('''
    <table class="table table-sm">
      <thead>
        <tr>
          <th>Name</th>
          <th>Warmup</th>
          <th>Main</th>
          <th>BBB</th>
        </tr>
      </thead>
      <tbody>''')
    for user in users:
        f.write('''
        <tr>
          <th>'''+user+'''</th>
        ''')
        w.printWorkout(users[user][i % 4], f)
        f.write('</tr>')
    f.write('</tbody>')
    f.write('</table><br>')

def generateAccessory(f):
    types = ['biceps', 'triceps', 'shoulders', 'chest', 'abs', 'back', 'legs']
    shuffle(types)
    f.write('4 rounds: ')
    f.write('<ul>')
    for t in types:
        f.write('<li>' + sample(accessory[t], 1)[0] + '</li>')

    f.write('</ul>')

f = open('index.html', 'w', encoding='utf8')

f.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Workout schedule</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    <style> html {font-size:12px;} </style>
  </head>
  <body>
    <div class="container-fluid">
  ''')

cf = CrossFit()
w = Wendler()

days = 48 * 4
for day in range(days):
    f.write('<div id="accordion'+str(day)+'" role="tablist">')
    f.write('  <div class="card">')
    f.write('''
    <div class="card-header" role="tab" id="heading'''+str(day)+'''">
      <h5 class="mb-0">
        <a class="" data-toggle="collapse" href="#collapse'''+str(day)+'''" aria-expanded="true" aria-controls="collapse'''+str(day)+'''">
          Day '''+str(day + 1)+'''
        </a>
      </h5>
    </div>

    <div id="collapse'''+str(day)+'''" class="" role="tabpanel" aria-labelledby="heading'''+str(day)+'''" data-parent="#accordion">
      <div class="card-body">''')

    f.write('<div class="row">')

    #f.write('<div class="col">')
    #generateWL(day, f)
    #f.write('</div>')

    f.write('<div class="col">')
    f.write('<h5>Warmup</h5>')
    wu = cf.get_warmup()
    f.write('<ol>')
    for warmup in wu:
        f.write('<li>'+warmup+'</li>')
    f.write('</ol>')
    f.write('</div>')

    f.write('<div class="col">')
    f.write('<h5>Dynamic stretch</h5>')
    ds = cf.get_dynamic_stretch()
    f.write('<ol>')
    for stretch in ds:
        f.write('<li>' + stretch + '</li>')
    f.write('</ol>')
    f.write('</div>')

    f.write('<div class="col">')
    #generateStrength(day, f)
    f.write('<h5>'+w.get_workout_name()+'</h5>')
    f.write('<ol>')
    for strength in w.get_workout():
        f.write('<li>' + strength + '</li>')
    f.write('</ol>')
    f.write('</div>')

    f.write('<div class="col">')
    workout = cf.generate_workout()
    f.write('<h5>WOD Movements</h5>')
    f.write('<ul>')
    # print('\n******** Workout:********')
    for ex in workout:
        f.write('<li>' + ex + '</li>')
    f.write('</ul>')
    f.write('</div>')

    f.write('<div class="col"><h4>Accessory</h4>')
    generateAccessory(f)
    f.write('</div>')

    r = randint(1, 2)
    if r == 1:
        f.write('<div class="col"><h4>Death by ...</h4>')
        f.write(cf.get_deathby())
        f.write('</div>')
    elif r == 2:
        f.write('<div class="col"><h4>Challenge</h4>')
        f.write(cf.get_challenge())
        f.write('</div>')

    f.write('</div>')  # end of row
    
    f.write('''
         </div>
      </div>
    </div>''')
    f.write('  </div>')

f.write('''
       </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
  </body>
</html>
''')

f.close()
