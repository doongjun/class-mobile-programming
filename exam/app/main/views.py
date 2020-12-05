from flask import render_template
from . import main
from flask_login import login_required, current_user
from .decorators import admin_required, permission_required
from ..models import Permission, Role, User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "for administrators!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "For comment moderators!"
