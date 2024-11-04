from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.user import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
def admin_dashboard():
    # Ici, vous pouvez récupérer les tables et les afficher
    # Exemple : tables = db.metadata.tables.keys()
    return render_template('admin.html', user=current_user)
