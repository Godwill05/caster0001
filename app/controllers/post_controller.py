# app/controllers/post_controller.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models.post import Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts')
def list_posts():
    posts = Post.query.all()
    return render_template('list_posts.html', posts=posts)

@post_bp.route('/posts/new', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title or not content:
            flash('Le titre et le contenu sont obligatoires.', 'danger')
            return redirect(url_for('post.create_post'))
        
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        
        flash('Article créé avec succès!', 'success')
        return redirect(url_for('post.list_posts'))
    
    return render_template('create_post.html')

@post_bp.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        
        db.session.commit()
        flash('Article mis à jour!', 'success')
        return redirect(url_for('post.list_posts'))
    
    return render_template('edit_post.html', post=post)

@post_bp.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Article supprimé avec succès.', 'success')
    return redirect(url_for('post.list_posts'))
