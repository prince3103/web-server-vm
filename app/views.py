from app import app
from flask import Blueprint
from flask_restplus import Api, Resource, fields
from skill_database import SkillDatabase

blueprint = Blueprint('api', __name__, url_prefix = '/api/v1/career_map')
api = Api(blueprint, doc = '/documentation', version='1.0.0', title='Career Map',
    description='API to predict skill map based on the job role provided'
)


app.register_blueprint(blueprint)


ns = api.namespace('soft_skills', description='Operations on Soft Skills')
@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require soft skills'}},
responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class SoftSkill(Resource):
    def get(self, job_role):
        '''
        This function is called when a get request is made by client app  on soft_skills endpoint.

        job_role : Job Role input by user
        job_result : The skills, frequency, variants extracted from a database for a job role
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        job_result = SkillDatabase().getData(job_role=job_role, skill_type='soft skill')
        if job_result == []:
            return {'soft_skills' : 'No soft_skill found for given input.'}, 404
        return {'soft_skills' : job_result}, 200

ns = api.namespace('hard_skills', description='Operations on Hard Skills')
@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require hard skills'}},
responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class HardSkill(Resource):
    
    def get(self, job_role):
        '''
        This function is called when a get request is made by client app on hard_skills endpoint.

        job_role : Job Role input by user
        job_result : The skills, frequency, variants extracted from a database for a job role
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        job_result = SkillDatabase().getData(job_role=job_role, skill_type='hard skill')
        if job_result == []:
            return {'hard_skills' : 'No hard_skill found for given input.'}, 404
        return {'hard_skills' : job_result}, 200