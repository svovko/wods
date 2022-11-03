from random import randrange
from CrossFit import CrossFit
from Movement import Movement

warmup1 = Movement(['Run', 'Row', 'Bike', 'Assault bike'], True)
warmup2 = Movement(['Jump rope + burpees', 'Battle ropes + Box step ups', 'Ball salms + Mountain climbers'], True)

stretch_shoulders = Movement(['Straight Arm circles', 'Straight Arm Twists', 'Crab Walk FW + BW', 'KB Halo',
                              'Stick complex', 'Bear-Crab roll', 'Reverse Fly /w DB', 'Soulder rotation /w DB'], True)

stretch_hips = Movement(['Cossack Squat', 'Fire Hydrant Circles FW+BW',
                         'Leg Swings + Side Leg Swings', 'Side Lunges Walk', 'Kneeling split', 'Groiner'], True)

stretch_ankles = Movement(['Duck walk', 'Bunny hops', 'Goblet squat', 'Calf raises'], True)

stretch_hamstrings = Movement(['Lunge hamstring extension', 'Goodmornings /w straight arms', 'Stiff-leg DL',
                               'KB Single-leg DL', 'Russian Baby Makers', 'Glute bridge (box)', 'Leg swings'], True)

stretch_thoracic = Movement(['Spiderman + Reach', 'Page turns', 'Wall squats', 'Deep squat + Reach', 
                             'Kneeling thoracic rotations', 'V-sit Roll over', 'Cat-Cow', 'Wall-sit Wall Angels'], True)

stretch_static = Movement(['Downward Dog', 'Inchworm', 'Scorpion stretch', 'Leg Crossover', 'Pigeon pose', 'Puppy pose on box', 'Dead Hang'], True)

accessory_biceps = Movement(['DB Hammer curls', 'BB Biceps curls', 'TRX Biceps curls', 'Chinups'], True)

accessory_triceps = Movement(['Banded triceps pulldown', 'OH DB Triceps extension', 'Skull crushers', 'TRX Triceps Extensions', 'Close Grip Bench Press'], True)

accessory_shoulders = Movement(['Sots Press', 'Seated DB press', 'Z Press', 'Strict HSPU', 'Unilateral KB Press', 'TGUs', 'Lu Flies',
                                'KB weighted BB Press', 'OH KB carry (Uni/Bi)', 'TRX Face pull', 'Y-W-T-PU-I (30s each) + Swimming', 
                                'BB Press /w banded weight', 'Snatch-grip push press', 'Banded Pull-aparts'], True)

accessory_chest = Movement(['Barbell Push ups', 'Deficit pushups', 'Floor press', 'Dips', 'Floor flies (2 plates)',
                            'TRX push ups', 'Ring push ups', 'DB Incline Bench Press', 'BB Bench /w banded weight'], True)

accessory_abs = Movement(['Single Arm Farmers carry', 'Farmers walk', 'Evil Wheels', 'GHDSU', 'Plank (alt. sides)', 'Plank',
                          'Hollow rock', 'L-sit/L-hang', 'Suitcase DL', 'KB Waiter Squat',
                          'Russian twists', 'Front rack KB carry', 'Plank rollouts (stability ball)', 'TRX crunches', 
                          'Pegwall hold', 'DBall carry', 'Pallof press'], True)

accessory_back = Movement(['DB/KB Row', 'Bent over row', 'Pendlay row', 'Plate fly', 'Strict Pullups (weighted?)', 'Back Extensions', 'TRX row',
                           'Back Ext. Hold'], True)

accessory_legs = Movement(['BB Glute Bridges', 'Goodmornings', 'Glute Ham Raises (on GHD)', 'Decline Squat', 'KB/DB Lunges',
                           'Bulgarian Split Squat', 'High Box Jumps', 'Hamstring curl (stability ball)', 'Wall Sits', 'Stiff-legged DL',
                           'BB Front rack Box Step up (high elbows)'], True)

monostructural = Movement(['Assault bike', 'Run', 'Bike', 'Row'])

back_squat = Movement(['5 x 5', 'Klokov Squat (76X0)', 'Heavy Single', 'AMRAP'])
front_squat = Movement(['5 x 5', 'Tempo Squat (76X0)', 'Heavy Single', 'AMRAP', 'Hole Squat'])
clean = Movement(['EMOM 10 PC', '10-8-6-4-2', 'EMOM 10 Sq.Cl', 'Heavy Single', '3-position clean', 'Hang Squat Clean'])
clean_accessory = Movement(['Clean Pull 3 x 3', 'Clean DL'])
snatch = Movement(['EMOM 10 PS', '10-8-6-4-2', 'EMOM 10 Sq.Sn', 'Heavy Single', '3-position snatch', 'Hang Squat Snatch'])
snatch_accessory = Movement(['Snatch Pull 3 x 3', 'Snatch Grip DL', 'Snatch Ballance'])

challenges = Movement(['100m row', '1min row', '500m row', '1000m row', '2000m row', 'Prowler 6 x 50kg',
                       'Prowler for max load', 'Plank for time', '100 Pushups', '100 Burpees', 'L-sit',
                       '100 pull ups', '100 swings', '20 x DL @ Heavy Weight', 'Wall Sit', 'Bear complex',
                       'Southwood complex', 'Broad jump', 'HS hold', 'DBall hold'])

death_by = Movement(['Wall Ball Shots', 'Burpees', 'Burpee Box Jump Overs', 'DB Snatches (1,1,2,2)', 'Pull ups',
                     'Push ups', 'Mucle ups', 'Chest to Bar Pull ups', 'HSPUs', 'SHSPUs', 'GHDSU', 'Toes to Bar',
                     'Knees to Elbows', 'Situps (5-10-15...)', 'Ring dips', 'Thrusters',
                     'Power Cleans', 'Back Squats', 'Front Squats', 'Deadlifts', 'Bench Presses',
                     'Push Presses', 'OH Squats', 'KB Thrusters'])  # 'Rope Climb'

cf = CrossFit()

mono = 0
bs_fs = True

f = open('index.html', 'w', encoding='utf8')

f.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Workout schedule</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    <style> html {font-size:12px;} </style>
  </head>
  <body>
    <div class="container-fluid">
  ''')

i = 0
while i < 50:

    f.write('<div id="accordion'+str(i)+'" role="tablist">')
    f.write('  <div class="card">')
    f.write('''
                <div class="card-header" role="tab" id="heading'''+str(i)+'''">
                <h5 class="mb-0">
                    <a class="" data-toggle="collapse" href="#collapse'''+str(i)+'''" aria-expanded="false" aria-controls="collapse'''+str(i)+'''">
                    Day '''+str(i + 1)+'''
                    </a>
                </h5>
                </div>

    <div id="collapse'''+str(i)+'''" class="" role="tabpanel" aria-labelledby="heading'''+str(i)+'''" data-parent="#accordion'''+str(i)+'''">
      <div class="card-body">''')

    f.write('<div class="row">')

    if i % 4 < 3:
        # pick a warmup
        f.write('<div class="col">')
        f.write('<h5>1. Warmup <small>10"</small></h5>')
        f.write('<ul>')
        f.write('<li>' + warmup1.getMovement() + '</li>')
        f.write('<li>' + warmup2.getMovement() + '</li>')
        f.write('</ul>')
        #f.write('</div>')

        # pick stretch
        #f.write('<div class="col">')
        f.write('<h5>2. Dynamic stretch</h5>')
        f.write('<ol>')
        f.write('<li>' + stretch_shoulders.getMovement() + ', ' + stretch_shoulders.getMovement() + '</li>')
        f.write('<li>' + stretch_ankles.getMovement() + ', ' + stretch_ankles.getMovement()+ '</li>')
        f.write('<li>' + stretch_hips.getMovement() + ', ' + stretch_hips.getMovement()+ '</li>')
        f.write('<li>' + stretch_hamstrings.getMovement() + ', ' + stretch_hamstrings.getMovement()+ '</li>')
        f.write('<li>' + stretch_thoracic.getMovement() + ', ' + stretch_thoracic.getMovement()+ '</li>')
        f.write('<li>' + stretch_static.getMovement() + ', ' + stretch_static.getMovement()+ '</li>')
        f.write('</ol>')
        #f.write('</div>')

    # Squat
    if i % 4 == 0:
        #f.write('<div class="col">') 
        if bs_fs:
            f.write('<h5>3. Back Squat</h5>')
            f.write('<ul>')
            f.write('<li>' + back_squat.getMovement() + '</li>')
            f.write('</ul>')
        else:
            f.write('<h5>3. Front Squat</h5>')
            f.write('<ul>')
            f.write('<li>' + front_squat.getMovement() + '</li>')
            f.write('</ul>')
        bs_fs = not bs_fs
        #f.write('</div>')

    # Snatch
    if i % 4 == 1:
        #f.write('<div class="col">') 
        f.write('<h5>3. Snatch</h5>')
        f.write('<ul>')
        f.write('<li>' + snatch.getMovement() + '</li>')
        f.write('<li>' + snatch_accessory.getMovement() + '</li>')
        f.write('</ul>')
        #f.write('</div>') 

        #f.write('<div class="col">') 
        f.write('<h5>4. WOD (chipper)</h5>')
        f.write('<ul>')
        wods = cf.generate_workout(randrange(6, 11))
        for wod in wods:
            f.write('<li>' + wod + '</li>')
        f.write('</ul>')
        #f.write('</div>')

    
    # Clean
    if i % 4 == 2:
        # print('\t3. Clean')
        #f.write('<div class="col">') 
        f.write('<h5>3. Clean</h5>')
        f.write('<ul>')
        f.write('<li>' + clean.getMovement() + '</li>')
        f.write('<li>' + clean_accessory.getMovement() + '</li>')
        f.write('</ul>')
        f.write('<div><small>*warmup /w jerk (alt. between push and split)</small></div>')
        #f.write('</div>') 

    # WOD
    if (i % 4) % 2 == 0:
        #f.write('<div class="col">') 
        f.write('<h5>4. WOD 1</h5>')
        f.write('<ul>')
        wods = cf.generate_workout(2)
        for wod in wods:
            f.write('<li>' + wod + '</li>')
        f.write('</ul>')
        f.write('<div>5 min rest</div>')
        f.write('<h5>4. WOD 2</h5>')
        f.write('<ul>')
        wods = cf.generate_workout(2)
        for wod in wods:
            f.write('<li>' + wod + '</li>')
        f.write('</ul>')
        #f.write('</div>') 

    # Accessory
    if i % 4 < 3:
        #f.write('<div class="col">') 
        f.write('<h5>5. Accessory</h5>')
        f.write('<h6>4 rounds (aim for 40-50 quality reps)</h6>')
        if i % 4 == 0:
            f.write('<ul>')
            f.write('<li>' + accessory_biceps.getMovement() + '</li>')
            f.write('<li>' + accessory_triceps.getMovement() + '</li>')
            f.write('<li>' + accessory_abs.getMovement() + '</li>')
            f.write('</ul>')
        elif i % 4 == 1:
            f.write('<ul>')
            f.write('<li>' + accessory_back.getMovement() + '</li>')
            f.write('<li>' + accessory_legs.getMovement() + '</li>')
            f.write('<li>' + accessory_abs.getMovement() + '</li>')
            f.write('</ul>')
        elif i % 4 == 2:
            f.write('<ul>')
            f.write('<li>' + accessory_shoulders.getMovement() + '</li>')
            f.write('<li>' + accessory_chest.getMovement() + '</li>')
            f.write('<li>' + accessory_abs.getMovement()+ '</li>')
            f.write('</ul>')
        
        f.write('<div><small>*Aim for 12-15 quality reps</small></div>')

        #f.write('</div>')


    # Monostructural
    if i % 4 == 3:
        #f.write('<div class="col">') 
        f.write('<h5>1. Monostructural</h5>')
        f.write('<h6>30-60 minutes (HR 140)</h6>')
        f.write('<ul><li>' + monostructural.getMovement() + '</li></ul>')
        #f.write('</div>')

        #f.write('<div class="col">')
        f.write('<h5>2. Accessory</h5>')
        f.write('<ul>')

        if randrange(0,2) == 1:
            f.write('<li>' + accessory_biceps.getMovement() + '</li>')
        else:
            f.write('<li>' + accessory_triceps.getMovement() + '</li>')

        if randrange(0, 2) == 1:
            f.write('<li>' + accessory_back.getMovement() + '</li>')
        else:
            f.write('<li>' + accessory_legs.getMovement() + '</li>')

        if randrange(0, 2) == 1:
            f.write('<li>' + accessory_shoulders.getMovement() + '</li>')
        else:
            f.write('<li>' + accessory_chest.getMovement() + '</li>')

        f.write('<li>' + accessory_abs.getMovement() + '</li>')
        f.write('</ul>')
        #f.write('</div>')

    f.write('''
            </div>
         </div>
      </div>
    </div>
    </div>''')
    i += 1

f.write('''
       </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
  </body>
</html>
''')

f.close()