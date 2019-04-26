from .forms import UpdateProfile
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .. import db,photos


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

  if user is None:
      abort(404)

  return render_template("profile/profile.html",user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

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
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/<,uname>/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)
    title = "New Pitch"

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data

        new_pitch= Pitch(title= title, content = pitch,category= category,user = current_user)

        new_pitch.save_pitch()
        pitches = Pitch.query.all()
        return redirect(url_for("main.categories",category = category))

return render_template("new_pitch.html",form = form, title = title)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.all()

    else:
        pitches = Pitch.query.filter_by(category = category).all()

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
        
        new_comment = Comment(content = content, user = user, pitch = pitch)
        new_comment.save_comment()
        return redirect(url_for("main.comments", pitch_id= pitch.id))
    return render_template("comment.html,title = pitch.title,form = form, pitch = pitch ")

