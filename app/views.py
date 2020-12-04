from flask import Blueprint
from flask_restplus import Api, Resource
from skill_database import SkillDatabase

from app import app

blueprint = Blueprint('api', __name__, url_prefix='/api/v1/career_map')
api = Api(blueprint, doc='/documentation', version='1.0.0', title='Career Map',
          description='API to predict skill map based on the job role provided'
          )


app.register_blueprint(blueprint)


ns = api.namespace('skills', description='Operations on Soft and Hard Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class Skill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app  on skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for both hard and soft skill
        from database.

        Parameters
        ----------
        job_role : Job Role input by user.

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        job_result = SkillDatabase.get_data(
            job_role=job_role, skill_type='both skill')
        if job_result == []:
            return {'skills': 'No skill found for given input.'}, 404
        return {'skills': job_result}, 200


ns = api.namespace('soft_skills', description='Operations on Soft Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require soft skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class SoftSkill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app  on soft_skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for soft skill from database.

        Parameters
        ----------
        job_role : Job Role input by user

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        job_result = SkillDatabase.get_data(
            job_role=job_role, skill_type='soft skill')
        if job_result == []:
            return {'soft_skills': 'No soft_skill found for given input.'}, 404
        return {'soft_skills': job_result}, 200


ns = api.namespace('hard_skills', description='Operations on Hard Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require hard skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class HardSkill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app on hard_skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for hard skill from database.

        Parameters
        ----------
        job_role : Job Role input by user

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        job_result = SkillDatabase.get_data(
            job_role=job_role, skill_type='hard skill')
        if job_result == []:
            return {'hard_skills': 'No hard_skill found for given input.'}, 404
        return {'hard_skills': job_result}, 200
