from flask import Flask,redirect,url_for,render_template,request
from mgen import main
# import time

# WSGI Application
app=Flask(__name__)

#Decorator
@app.route('/')
def home():
    return render_template('index1.html')

database={'harsh@gmail.com':'123','harsha@gmail.com':'456','harshini@gmail.com':'789'}

@app.route('/Login',methods=['POST','GET'])
def login():
    print(request.form)  # Print form data to console for debugging
    name1=request.form.get('email')
    password1=request.form.get('password')
    if name1 not in database:
        return render_template('index.html')
    else:
        if database[name1]!=password1:
            return render_template('index.html')
        else:
            return render_template('index2.html')

@app.route('/Generate',methods=['POST','GET'])
def music():
    # main(num_bars=8, num_notes=4, num_steps=1, pauses=True, key="C", scale="major", root=4,
    #  population_size=10, num_mutations=2, mutation_probability=0.5, bpm=128)

    # print(request.form)
    # rating = request.form.get('rating')
    # num_bars = request.form.get('numBars')
    # notes_per_bar = request.form.get('notesPerBar')
    # scale_root = request.form.get('scaleRoot')
    # no_steps = request.form.get('nosteps')
    # pauses = request.form.get('introducePauses')
    # key = request.form.get('key')
    # scale = request.form.get('scale')

    # # Print or use the values as needed
    # print(f"Rating: {rating}, Number of Bars: {num_bars}, Notes per Bar: {notes_per_bar}, Scale Root: {scale_root},No of Steps: {no_steps},Pauses: {pauses}, Key: {key}, Scale: {scale} ")
    # return render_template('index2.html')
    

    if request.method == 'POST':
        # Getting values from the form
        rating = request.form.get('rating')
        num_bars = request.form.get('numBars')
        notes_per_bar = request.form.get('notesPerBar')
        scale_root = request.form.get('scaleRoot')
        no_steps = request.form.get('nosteps')
        pauses = request.form.get('introducePauses')
        key = request.form.get('key')
        scale = request.form.get('scale')

        duration_multiplier = 2  # Adjust this value as needed
        duration = rating * duration_multiplier

        # main(num_bars: int, num_notes: int, num_steps: int, pauses: bool, key: str, scale: str, root: int,
        #  population_size: int, num_mutations: int, mutation_probability: float, bpm: int):


        # Now, call the main function from main.py with the obtained values
        main(num_bars=int(num_bars), num_notes=int(notes_per_bar), num_steps=int(no_steps), pauses=True,
             key=key, scale=scale, root=int(scale_root), population_size=10, num_mutations=2,
             mutation_probability=0.5, bpm=128,rating=rating)


        # main(int(num_bars),int(notes_per_bar), int(no_steps),True,key,scale,(scale_root),10,2,0.5,128)

    return render_template('index2.html')



if __name__=='__main__':
    app.run(debug=True)
    
