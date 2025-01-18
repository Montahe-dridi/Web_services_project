from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import Covoiturage

# Define the Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/add_covoiturage', methods=['GET', 'POST'])
@login_required
def addCov():
    if request.method == 'POST':
        try:
            # Get form data
            departure_location = request.form.get('departure_location')
            destination = request.form.get('destination')
            seats_available = request.form.get('seats_available')
            date_string = request.form.get('date')  # Expected format: 'YYYY-MM-DD'

            # Validate and parse input
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()  # Parse date string
            seats_available = int(seats_available)  # Ensure seats_available is an integer

            # Create the new Covoiturage entry
            new_covoiturage = Covoiturage(
                departure_location=departure_location,
                destination=destination,
                date=date_object,
                seats_available=seats_available,
                user_id=current_user.id  # Logged-in user's ID
            )

            # Save to database
            db.session.add(new_covoiturage)
            db.session.commit()

            flash("Covoiturage added successfully!", "success")
            return redirect(url_for('main.get_covoiturages'))

        except ValueError as ve:
            flash("Invalid input: Ensure date is in 'YYYY-MM-DD' format and seats available is a number.", "error")
        except Exception as e:
            flash(f"An unexpected error occurred: {str(e)}", "error")

    return render_template('add_covoiturage.html')

@main.route('/covoiturages', methods=['GET'])
def get_covoiturages():
    # Query all covoiturages from the database
    covoiturages = Covoiturage.query.all()
    return render_template('covoiturages.html', covoiturages=covoiturages)

@main.route('/covoiturage/<int:cov_id>', methods=['GET'])
@login_required
def show_cov_details(cov_id):
    # Query the covoiturage by ID
    cov = Covoiturage.query.get_or_404(cov_id)
    return render_template('cov_details.html', cov=cov)


@main.route('/covoiturage/<int:cov_id>/delete', methods=['POST'])
@login_required
def delete_cov(cov_id):
    # Query the covoiturage by ID
    cov = Covoiturage.query.get_or_404(cov_id)

    # Ensure the logged-in user owns the covoiturage
    if cov.user_id != current_user.id:
        flash("You are not authorized to delete this covoiturage.", "error")
        return redirect(url_for('main.get_covoiturages'))

    # Delete the covoiturage
    db.session.delete(cov)
    db.session.commit()
    flash("Covoiturage deleted successfully!", "success")
    return redirect(url_for('main.get_covoiturages'))

