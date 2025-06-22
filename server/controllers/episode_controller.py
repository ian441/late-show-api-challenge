from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from server.models.episode import Episode
from datetime import datetime


episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    try:
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes]), 200
    except Episode as e:
        return jsonify({'error': str()}), 500
    
@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    try:
        episode = Episode.query.get_or_404()
        return jsonify(episode.to_dict(include_appearances=True)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    try:
        episode = Episode.query.get_or_404(id)
        db.session.delete(episode)
        db.session.commit()
        return jsonify({'message': 'Episode deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500