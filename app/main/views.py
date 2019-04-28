from .forms import Updateprofile,PitchForm,Comment
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Role,Pitch,Comment
from .. import db,photos
from . import main 
import datetime





@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  pitches = Pitch.query.all()
  title = "60sec pitch"
  return render_template('index.html', title = title, pitches = pitches)
# @main.route('/pitch/pitch/new/<int:id>') # , methods = ['GET','POST'])
# @login_required
# def new_pitch(id):


@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  pitches = Pitch.query.filter_by(username = uname).order_by(Pitch.time.desc())
  title = user.name.upper()
  if user is None:
      abort(404)

  return render_template("profile/profile.html",pitches = pitches,user = user, title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    title = "Edit Profile"
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
       

@main.route('/<uname>/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title = "New Pitch"

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        originalDate = datetime.datetime.now()
        time = str(originalDate.time())
        time =time[0:5]
        date = str(originalDate)
        date = date[0:10]
        new_pitch= Pitch(title= title, content = pitch,category= category,user = current_user, date = date, time = time)

        new_pitch.save_pitch()
        pitches = Pitch.query.all()
        return redirect(url_for("main.categories",category = category))

    return render_template("new_pitch.html",new_form = form, title = title)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.order_by(Pitch.time.desc())

    else:
        pitches = Pitch.query.filter_by(category = category).order_by(Pitch.time.desc()).all()


    return render_template("pitch.html",pitches = pitches, title = category.upper())

@main.route("/<pitch_id>/comments")
@login_required
def view_comments(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    title = "Comments"
    comments = pitch.get_pitch_comments()

    return render_template("comments.html",comments = comments, pitch = pitch, title = title)

@main.route("/<user>/pitch/<pitch_id>/new/comment", methods = ["GET","POST"])
@login_required
def comment(user,pitch_id):
    user = User.query.filter_by(id = user ).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = AddComment()
    title = "Add Comment"
    if form.validate_on_submit():
        content = form.content.data
        originalDate = datetime.datetime.now()
        time = str(originalDate.time())
        time = time[0:5]
        date = str(originalDate)
        date = date[0:10]
        new_comment = Comment(content = content, user = user, pitch = pitch)
        new_comment.save_comment()
        return redirect(url_for("main.comments", pitch_id= pitch.id))
    return render_template("comment.html,title = pitch.title,form = form, pitch = pitch ")

# @main.route('/pitch/<int:id>')
# def single_pitch(id):
#     pitch=Pitch.query.get(id)
#     if pitch is None:
#         abort(404)
#     
#     return render_template('pitch.html',pitch = pitch,format_pitch=formart_pitch)
    